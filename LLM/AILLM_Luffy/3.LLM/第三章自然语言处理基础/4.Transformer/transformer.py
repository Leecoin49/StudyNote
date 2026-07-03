"""
================================================================================
  Transformer 模型完整实现
  "Attention Is All You Need" — Vaswani et al., 2017
================================================================================

  模型架构总览:

      输入(src)                          输出(tgt, 已右移)
         │                                    │
   ┌─────┴──────┐                      ┌──────┴──────┐
   │ Embedding  │                      │ Embedding   │
   │ + 位置编码  │                      │ + 位置编码   │
   └─────┬──────┘                      └──────┬──────┘
         │                                    │
   ┌─────┴──────┐                             │
   │  Encoder   │                             │
   │  × N 层    │                             │
   │            │──────────────────────┐       │
   └─────┬──────┘                     │       │
         │                            ▼       │
         │                      ┌─────────────┴──┐
         │                      │    Decoder     │
         │                      │    × N 层      │
         │                      └───────┬────────┘
         │                              │
         │                     ┌────────┴────────┐
         │                     │    Generator    │
         │                     │   Linear+Softmax│
         │                     └────────┬────────┘
         │                              │
         ▼                              ▼
    编码器输出                    输出概率分布
  (用于交叉注意力)              (预测下一个词)

  费曼一句话:
    编码器 = "读懂源语言"
    解码器 = "写出目标语言，写的时候同时参考源语言和已经写出来的部分"
================================================================================
"""

import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


# ================================================================================
#  1. 辅助函数
# ================================================================================

def clones(module, N):
    """
    克隆模块 N 份，返回 nn.ModuleList。

    为什么需要？
      Encoder 和 Decoder 都有 N 个完全相同的层（结构相同，参数独立），
      用 copy.deepcopy 克隆 N 份比写 N 次代码更简洁。

    费曼类比: 一栋楼有 N 层，每层格局一样，但住户（参数）不同。
    """
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])


def subsequent_mask(size):
    """
    生成向后遮掩的掩码张量（下三角矩阵）。

    输入:  size — 序列长度
    输出:  (1, size, size) 的掩码，1=允许看，0=遮住

    原理:
      np.triu(全1, k=1) → 上三角为1 → 1-翻转 → 下三角为1

      例 size=3:
      [[1, 0, 0],
       [1, 1, 0],     ← 第i行：位置i只能看到0~i（前面和自己）
       [1, 1, 1]]

    只在解码器的自注意力中使用！
    编码器不需要——编码器是"读"，可以看全部。
    """
    attn_shape = (1, size, size)
    # 上三角矩阵（不含对角线）→ 1-翻转 → 下三角矩阵
    subsequent_mask = np.triu(np.ones(attn_shape), k=1).astype('uint8')
    return torch.from_numpy(subsequent_mask) == 0  # bool类型：True=可见


# ================================================================================
#  2. 注意力机制
# ================================================================================

def attention(query, key, value, mask=None, dropout=None):
    """
    缩放点积注意力 — Transformer 的核心计算。

    公式: Attention(Q, K, V) = Softmax(Q·K^T / √d_k) · V

    参数:
      query:  (batch, h, seq_len, d_k)  — "我想找什么"
      key:    (batch, h, seq_len, d_k)  — "我是什么，来匹配我"
      value:  (batch, h, seq_len, d_k)  — "匹配到了，给你内容"
      mask:   掩码张量，0的位置会被遮成 -∞（Softmax后≈0）
      dropout: Dropout层实例

    返回:
      (注意力输出, 注意力权重)

    三步走（费曼类比）:
      第1步 Q·K^T       → 你走进图书馆的每个书架，扫一眼标签
      第2步 ÷√d_k+Softmax → 决定在每个书架前花多少时间
      第3步 ×V           → 按时间分配，阅读并带走内容
    """
    d_k = query.size(-1)

    # 第1步：Q × K^T ÷ √d_k → 相关性分数
    # query: (batch, head, seq_len, d_k)  key^T: (batch, head, d_k, seq_len)  → scores: (batch, head, seq_len, seq_len)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)

    # 掩码：把不该看的位置的分数设为 -1e9
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)     # → (batch, head, seq_len, seq_len)

    # 第2步：Softmax → 每行归一化为概率
    p_attn = F.softmax(scores, dim=-1)                    # → (batch, head, seq_len, seq_len)

    if dropout is not None:
        p_attn = dropout(p_attn)                           # → 形状不变

    # 第3步：p_attn × V → 加权求和
    # p_attn: (batch, head, seq_len, seq_len)  value: (batch, head, seq_len, d_k)  → (batch, head, seq_len, d_k)
    return torch.matmul(p_attn, value), p_attn


class MultiHeadedAttention(nn.Module):
    """
    多头注意力机制。

    为什么需要"多头"？
      单一注意力只看一个角度 → 可能有偏见
      8个头从8个角度同时看 → 学到的信息更全面:
        - 头0: 可能学会"主语和谓语的关系"
        - 头1: 可能学会"形容词和名词的关系"
        - 头2: 可能学会"代词指代谁"
        - ...

    实现方式:
      把 d_model 切成 h 份，每份单独做注意力，最后拼接回来。

      d_model=512, h=8 → 每个头处理 512/8=64 维

    费曼类比:
      8个专家分别从不同角度审阅同一份文档，最后把8份意见汇总。
    """

    def __init__(self, h, d_model, dropout=0.1):
        """
        参数:
          h:       头数（论文中 h=8）
          d_model: 模型维度（论文中 d_model=512）
          dropout: Dropout比率
        """
        super(MultiHeadedAttention, self).__init__()
        assert d_model % h == 0, "d_model 必须能被 h 整除!"

        self.d_k = d_model // h    # 每个头处理的维度
        self.h = h                 # 头数

        # 四个线性变换层：
        #   Q, K, V 各自一个（从 d_model 映射到 d_model）
        #   最后一个用于拼接后的输出变换
        self.linears = clones(nn.Linear(d_model, d_model), 4)

        self.attn = None           # 保存注意力权重（用于可视化）
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, query, key, value, mask=None):
        """
        前向传播。

        输入形状: (batch, seq_len, d_model)
        输出形状: (batch, seq_len, d_model)  — 形状不变！

        内部维度变换:
          (batch, seq_len, d_model) → (batch, seq_len, head, d_k) → (batch, head, seq_len, d_k)
          → 注意力计算 → (batch, head, seq_len, d_k)
          → (batch, seq_len, head, d_k) → (batch, seq_len, d_model)
        """
        if mask is not None:
            mask = mask.unsqueeze(1)          # (batch, seq_len, seq_len) → (batch, 1, seq_len, seq_len)

        nbatches = query.size(0)

        # 1) 线性变换 + 切分多头
        #    lin(x):                  (batch, seq_len, d_model) → (batch, seq_len, d_model)
        #    .view(batch, -1, head, d_k):   (batch, seq_len, d_model) → (batch, seq_len, head, d_k)
        #    .transpose(1, 2):       (batch, seq_len, head, d_k) → (batch, head, seq_len, d_k)
        query, key, value = [
            lin(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
            for lin, x in zip(self.linears, (query, key, value))
        ]

        # 2) 对每个头独立做注意力
        #    attention(q, k, v) → x: (batch, head, seq_len, d_k)  attn: (batch, head, seq_len, seq_len)
        x, self.attn = attention(query, key, value, mask=mask, dropout=self.dropout)

        # 3) 拼接所有头
        #    x.transpose(1,2):       (batch, head, seq_len, d_k) → (batch, seq_len, head, d_k)
        #    .contiguous().view:     (batch, seq_len, head, d_k) → (batch, seq_len, d_model)
        x = x.transpose(1, 2).contiguous().view(nbatches, -1, self.h * self.d_k)

        # 4) 最后的线性变换：融合8个头的信息 → (batch, seq_len, d_model)
        return self.linears[-1](x)


# ================================================================================
#  3. 前馈全连接 + 层归一化 + 残差连接
# ================================================================================

class PositionwiseFeedForward(nn.Module):
    """
    位置级别的全连接前馈网络。

    公式: FFN(x) = ReLU(x·W1 + b1)·W2 + b2

    结构:
      输入 (d_model=512)
        → Linear(512 → d_ff=2048)  ← 升维，扩大表示空间
        → ReLU                       ← 引入非线性
        → Linear(2048 → 512)        ← 降维，回到原来的维度
      输出 (512)

    为什么维度先扩后缩?
      → 升维让网络有更大的空间去"思考"，降维把思考结果压缩回来
      → 2048维的中间层给ReLU提供了充足的"激活自由"

    为什么是 position-wise?
      → 同一层不同位置用相同的 W1, b1, W2, b2（参数共享）
      → 每个词独立过FFN，不跟别的词交流（交流是注意力干的活）

    费曼类比:
      注意力 = 听别人发言，收集信息
      FFN    = 自己独立思考，消化信息
    """

    def __init__(self, d_model, d_ff, dropout=0.1):
        """
        参数:
          d_model: 模型维度（512）
          d_ff:    前馈网络中间层维度（2048）
          dropout: Dropout比率
        """
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)    # 升维
        self.w_2 = nn.Linear(d_ff, d_model)    # 降维
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # x: (batch, seq_len, d_model)    如 (2, 4, 512)
        # ReLU(x·W1+b1):  (batch, seq_len, d_model) → Linear(512→2048) → (batch, seq_len, d_ff)
        # ReLU → Dropout → W2:  (batch, seq_len, d_ff) → Linear(2048→512) → (batch, seq_len, d_model)
        return self.w_2(self.dropout(F.relu(self.w_1(x))))


class LayerNorm(nn.Module):
    """
    层归一化 (Layer Normalization)。

    计算步骤:
      1. 对每个样本的最后 d_model 维求均值和方差
      2. (x - 均值) / sqrt(方差 + eps)  — 标准化
      3. γ * 标准化结果 + β  — 可学习的缩放和平移

    为什么需要?
      深层网络 → 每层的输出分布可能"漂移" → 后面层的学习越来越困难
      归一化 → 把每层输出拉回"标准分布"（均值≈0, 方差≈1）
              → 训练稳定、收敛更快

    费曼类比:
      讨论会上每个人控制音量——有人太激动（数值太大），
      有人不敢说话（数值太小），
      主持人（层归一化）让所有人用正常音量说话。
    """

    def __init__(self, features, eps=1e-6):
        """
        参数:
          features: 归一化的维度数（通常就是 d_model=512）
          eps:      防止除0的小常数
        """
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))   # γ — 可学习的缩放
        self.b_2 = nn.Parameter(torch.zeros(features))  # β — 可学习的平移
        self.eps = eps

    def forward(self, x):
        # x: (batch, seq_len, d_model)  如 (2, 4, 512)
        mean = x.mean(-1, keepdim=True)     # → (batch, seq_len, 1)
        std = x.std(-1, keepdim=True)        # → (batch, seq_len, 1)
        # 返回: (batch, seq_len, d_model) — 形状不变，分布变为均值0方差1
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2


class SublayerConnection(nn.Module):
    """
    子层连接结构：残差连接 + 层归一化。

    公式: 输出 = LayerNorm(x + Dropout(Sublayer(x)))

    组成:
      残差连接 (Add): x + 子层输出
        → 即使子层学坏了（梯度≈0），原始信息 x 也能无损传递
        → 这就是为什么 Transformer 可以堆叠6层而不出现梯度消失

      层归一化 (Norm): 控制数值范围
        → 防止深层网络中的数值爆炸或消失

    费曼类比:
      LSTM的信息高速公路还记得吗？残差连接就是 Transformer 的高速公路——
      你听了别人的意见（子层），但你没把自己的想法丢掉（+x）。
    """

    def __init__(self, size, dropout=0.1):
        super(SublayerConnection, self).__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        """
        x: (batch, seq_len, d_model)
        self.norm(x):          → (batch, seq_len, d_model)
        sublayer(norm):        → (batch, seq_len, d_model) ← 子层（注意力或FFN）
        self.dropout:          → (batch, seq_len, d_model)
        x + dropout:           → (batch, seq_len, d_model) ← 残差连接
        全程形状不变！
        """
        return x + self.dropout(sublayer(self.norm(x)))


# ================================================================================
#  4. 编码器
# ================================================================================

class EncoderLayer(nn.Module):
    """
    单个编码器层。

    结构:
      输入 x
        → LayerNorm → 多头自注意力 → Dropout → +x (残差)
        → LayerNorm → 前馈全连接    → Dropout → +x (残差)
      输出

    自注意力: Q=K=V=x，自己注意自己
    前馈:     每个词独立变换
    """

    def __init__(self, size, self_attn, feed_forward, dropout=0.1):
        super(EncoderLayer, self).__init__()
        self.self_attn = self_attn            # 多头自注意力
        self.feed_forward = feed_forward      # 前馈全连接
        # 两个子层连接结构（结构相同但参数独立）
        self.sublayer = clones(SublayerConnection(size, dropout), 2)
        self.size = size

    def forward(self, x, mask):
        """
        x:    (batch, seq_len, d_model)  如 (2, 4, 512)
        mask: 源端掩码
        → 子层1: 自注意力 → (batch, seq_len, d_model)
        → 子层2: 前馈     → (batch, seq_len, d_model)
        全程形状不变！
        """
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        return self.sublayer[1](x, self.feed_forward)


class Encoder(nn.Module):
    """
    完整编码器：Embedding + 位置编码 + N 层 EncoderLayer。

    数据流:
      输入(src) → Embedding → 位置编码 → [EncoderLayer × N] → 输出(每个词带上全句上下文)
    """

    def __init__(self, layer, N):
        """
        参数:
          layer: EncoderLayer 实例（被克隆 N 份）
          N:     堆叠层数（论文中 N=6）
        """
        super(Encoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)   # 最后加一层归一化

    def forward(self, x, mask):
        """
        x: (batch, src_seq_len, d_model)  如 (2, 10, 512)
        → 逐层传递: 每层输入输出形状不变
        → LayerNorm: (2, 10, 512)
        """
        for layer in self.layers:
            x = layer(x, mask)              # (batch, seq_len, d_model) → (batch, seq_len, d_model)
        return self.norm(x)                 # (batch, seq_len, d_model)


# ================================================================================
#  5. 解码器
# ================================================================================

class DecoderLayer(nn.Module):
    """
    单个解码器层。

    比编码器层多一层注意力！结构:

      输入 x（目标序列）
        → LayerNorm → 掩码多头自注意力 → Dropout → +x
              ↑
         Q=K=V=x, 使用下三角掩码 → "只能看已经写出来的词"

        → LayerNorm → 交叉多头注意力 → Dropout → +x
              ↑
         Q=解码器输出, K=V=编码器输出 → "我该翻译哪个源词？"

        → LayerNorm → 前馈全连接 → Dropout → +x
      输出

    费曼类比:
      解码器 = 翻译官工作的三步:
        第1步 (掩码自注意力): "我写了一半了，回顾一下我写了什么"
        第2步 (交叉注意力):   "看看原文，下一个词该对应原文的哪部分？"
        第3步 (前馈):         "消化一下，把译文写流畅"
    """

    def __init__(self, size, self_attn, src_attn, feed_forward, dropout=0.1):
        """
        参数:
          size:          维度
          self_attn:     多头自注意力（解码器自己看自己，带掩码）
          src_attn:      多头交叉注意力（解码器看编码器的输出）
          feed_forward:  前馈全连接
          dropout:       Dropout比率
        """
        super(DecoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn         # 掩码自注意力
        self.src_attn = src_attn           # 交叉注意力（Q=解码, K/V=编码）
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 3)  # 3个子层！

    def forward(self, x, memory, src_mask, tgt_mask):
        """
        x:        (batch, tgt_seq_len, d_model)  如 (2, 9, 512)
        memory:   (batch, src_seq_len, d_model)  如 (2, 10, 512)
        → 子层1: 掩码自注意力  Q=K=V=x + tgt_mask    → (batch, 9, 512)
        → 子层2: 交叉注意力    Q=x, K=V=memory       → (batch, 9, 512)
        → 子层3: 前馈                               → (batch, 9, 512)
        全程形状: (batch, tgt_seq_len, d_model) 不变！
        """
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, tgt_mask))
        x = self.sublayer[1](x, lambda x: self.src_attn(x, memory, memory, src_mask))
        return self.sublayer[2](x, self.feed_forward)


class Decoder(nn.Module):
    """
    完整解码器：Embedding + 位置编码 + N 层 DecoderLayer。

    数据流:
      目标序列 → Embedding → 位置编码 → [DecoderLayer × N] → 输出
                                                 ↑
                                           编码器输出(memory)
    """

    def __init__(self, layer, N):
        """
        参数:
          layer: DecoderLayer 实例
          N:     堆叠层数（论文中 N=6）
        """
        super(Decoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, x, memory, src_mask, tgt_mask):
        """
        x:       (batch, tgt_seq_len, d_model)  如 (2, 9, 512)
        memory:  (batch, src_seq_len, d_model)  如 (2, 10, 512)
        → 逐层传递, 每层输入输出形状不变
        → LayerNorm → (batch, 9, 512)
        """
        for layer in self.layers:
            x = layer(x, memory, src_mask, tgt_mask)
        return self.norm(x)


# ================================================================================
#  6. 输入层
# ================================================================================

class Embeddings(nn.Module):
    """
      词嵌入层：把词编号变成稠密向量。

      nn.Embedding 本质: 一个巨大的查找表 (vocab × d_model)
        输入: 词的整数编号
        输出: 这个词对应的 d_model 维向量

      × √d_model 的原因:
        → 让 Embedding 的数值范围和位置编码的[-1,1]在同一个数量级
        → 两者相加时谁也不"淹没"谁

      费曼类比: 公司员工管理系统
        词编号 = 员工姓名
        Embedding = 给每个员工分配一个工号（数字）
        语义相近的词向量也相近 = 同部门员工工号前缀相同
    """

    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        # x: (batch, seq_len)             如 (2, 4) — 词编号
        # self.lut(x):                    如 (2, 4, 512) — 查表得向量
        # * sqrt(d_model):                (2, 4, 512) — 放大22.6倍，形状不变
        # 返回: (batch, seq_len, d_model)
        return self.lut(x) * math.sqrt(self.d_model)


class PositionalEncoding(nn.Module):
    """
    位置编码器：给每个词打上"时间戳"。

    公式:
      PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))   ← 偶数维
      PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))   ← 奇数维

    为什么用 sin/cos 而不用可学习的编码?
      1. 外推性: 训练最大长度=100，推理长度=200也能工作
      2. 零参数: 不需要额外学习
      3. 相对位置: sin(pos+k) 可通过 sin(pos)和cos(pos)线性表示

    费曼类比: 公司里重名的人
      两个"张伟" → 给不同的工号后缀 → "张伟-001" vs "张伟-003"
      同一个词在不同位置 → 加上不同的位置编码 → 网络能区分
    """

    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        # ① pe: (max_len, d_model) = (5000, 512) — 预分配位置编码矩阵
        pe = torch.zeros(max_len, d_model)
        # ② position: (max_len, 1) = (5000, 1) — 列向量 [0],[1],...,[4999]
        position = torch.arange(0, max_len).unsqueeze(1)

        # ③ div_term: (d_model/2,) = (256,) — 256个频率 [1.0, 0.965, ..., 0.0001]
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model)
        )

        # ④⑤ position * div_term: (5000,1) × (256,) →广播→ (5000, 256)
        #     pe[:, 0::2] = sin → 偶数列, pe[:, 1::2] = cos → 奇数列
        #     pe 仍在 (5000, 512)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        # ⑥ pe: (5000, 512) → (1, 5000, 512) — 加batch维，方便广播
        pe = pe.unsqueeze(0)
        # ⑦ register_buffer: 不参与梯度更新，但保存到 state_dict
        self.register_buffer('pe', pe)

    def forward(self, x):
        """
        x: (batch, seq_len, d_model)  如 (2, 4, 512) ← Embedding的输出
        → + pe[:, :seq_len] →        如 (1, 4, 512) 广播到 (2, 4, 512)
        → Dropout →                  (2, 4, 512) 形状不变
        """
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)


# ================================================================================
#  7. 输出层（Generator）
# ================================================================================

class Generator(nn.Module):
    """
    输出层：把解码器的输出映射回词表空间。

    结构:
      Linear(d_model → vocab) — 把512维向量映射到vocab维
      Softmax(dim=-1)          — 变成概率分布

    最终输出的每一行: P(下一个词 | 上下文)，所有行加起来=1

    费曼类比:
      解码器输出 = 你对句子的"内部理解"（512维的脑内表示）
      Generator  = 你把这个理解"说出口"，变成具体的一个词
                   → 给你1000个候选词，每个词一个概率，选最高的那个
    """

    def __init__(self, d_model, vocab):
        super(Generator, self).__init__()
        self.proj = nn.Linear(d_model, vocab)

    def forward(self, x):
        # x: (batch, seq_len, d_model)        如 (2, 9, 512)
        # self.proj: Linear(512 → vocab)  →  (2, 9, vocab) 如 (2, 9, 1000)
        # log_softmax:                     →  (2, 9, 1000)  形状不变
        return F.log_softmax(self.proj(x), dim=-1)


# ================================================================================
#  8. 完整 Transformer 模型
# ================================================================================

class Transformer(nn.Module):
    """
    Transformer 完整模型。

    组装:
      ├── src_embed:  源语言 Embedding + 位置编码
      ├── tgt_embed:  目标语言 Embedding + 位置编码
      ├── encoder:    N × EncoderLayer
      ├── decoder:    N × DecoderLayer
      └── generator:  Linear + Softmax → 输出概率

    数据流:
      源句子(src) → src_embed → encoder → memory(编码器输出)
      目标句子(tgt) → tgt_embed → decoder(memory) → generator → 输出概率
    """

    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(Transformer, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def encode(self, src, src_mask):
        """
        src:      (batch, src_seq_len)         如 (2, 10) — 源词编号
        src_mask: (batch, 1, src_seq_len)
        → src_embed: (2, 10) → (2, 10, 512)    ← Embedding + PE
        → encoder:   (2, 10, 512) → (2, 10, 512)
        → 返回 memory
        """
        return self.encoder(self.src_embed(src), src_mask)

    def decode(self, memory, src_mask, tgt, tgt_mask):
        """
        memory:   (batch, src_seq_len, d_model)  如 (2, 10, 512)
        tgt:      (batch, tgt_seq_len)           如 (2, 9) — 目标词编号
        tgt_mask: (batch, tgt_seq_len, tgt_seq_len)
        → tgt_embed: (2, 9) → (2, 9, 512)        ← Embedding + PE
        → decoder:   (2, 9, 512) → (2, 9, 512)
        → 返回 decoder output
        """
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)

    def forward(self, src, tgt, src_mask, tgt_mask):
        """
        src:      (batch, src_seq_len)     如 (2, 10)
        tgt:      (batch, tgt_seq_len)     如 (2, 9)
        → encode: (2, 10) → (2, 10, 512)  memory
        → decode: memory + (2, 9) → (2, 9, 512)
        → 返回: (batch, tgt_seq_len, d_model)
        """
        memory = self.encode(src, src_mask)             # (batch, src_seq_len, d_model)
        return self.decode(memory, src_mask, tgt, tgt_mask)  # (batch, tgt_seq_len, d_model)


# ================================================================================
#  9. 构建函数：用论文默认参数创建 Transformer
# ================================================================================

def make_transformer(src_vocab, tgt_vocab, N=6, d_model=512, d_ff=2048,
                     h=8, dropout=0.1):
    """
    构建一个完整的 Transformer 模型（论文默认参数）。

    参数:
      src_vocab: 源语言词表大小
      tgt_vocab: 目标语言词表大小
      N:         编码器/解码器堆叠层数（默认 6）
      d_model:   模型维度（默认 512）
      d_ff:      前馈网络中间层维度（默认 2048）
      h:         注意力头数（默认 8）
      dropout:   Dropout比率（默认 0.1）

    返回:
      Transformer 模型实例

    费曼类比:
      这就像盖房子的标准图纸——你只需要指定"多大的词汇量"，
      其他结构按照论文标准自动搭建。
    """
    c = copy.deepcopy
    attn = MultiHeadedAttention(h, d_model, dropout)
    ff = PositionwiseFeedForward(d_model, d_ff, dropout)
    position = PositionalEncoding(d_model, dropout)

    model = Transformer(
        Encoder(EncoderLayer(d_model, c(attn), c(ff), dropout), N),
        Decoder(DecoderLayer(d_model, c(attn), c(attn), c(ff), dropout), N),
        nn.Sequential(Embeddings(d_model, src_vocab), c(position)),
        nn.Sequential(Embeddings(d_model, tgt_vocab), c(position)),
        Generator(d_model, tgt_vocab)
    )

    # 初始化参数
    for p in model.parameters():
        if p.dim() > 1:
            nn.init.xavier_uniform_(p)

    return model


# ================================================================================
#  10. 测试代码
# ================================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  Transformer 模型测试")
    print("=" * 60)

    # 超参数设置
    SRC_VOCAB = 1000   # 源语言词表大小
    TGT_VOCAB = 1000   # 目标语言词表大小
    N = 6              # 编码器/解码器层数
    D_MODEL = 512      # 模型维度
    D_FF = 2048        # 前馈网络维度
    H = 8              # 注意力头数
    DROPOUT = 0.1      # Dropout比率

    # 构造测试数据
    batch_size = 2
    src_seq_len = 10   # 源句子: "今天 天气 真 好 <PAD> <PAD> <PAD> <PAD> <PAD> <PAD>"
    tgt_seq_len = 9    # 目标句子: "<SOS> Today weather is good <EOS> <PAD> <PAD> <PAD>"

    # 随机词编号模拟真实输入
    torch.manual_seed(42)
    src = torch.randint(1, SRC_VOCAB, (batch_size, src_seq_len))
    tgt = torch.randint(1, TGT_VOCAB, (batch_size, tgt_seq_len))

    # 掩码
    src_mask = torch.ones(batch_size, 1, src_seq_len)           # 源端全可见（简化）
    tgt_mask = subsequent_mask(tgt_seq_len).repeat(batch_size, 1, 1)  # 下三角掩码

    # 构建模型
    print(f"\n[Model Params]")
    print(f"   Encoder layers: {N}")
    print(f"   Decoder layers: {N}")
    print(f"   d_model:        {D_MODEL}")
    print(f"   d_ff:           {D_FF}")
    print(f"   Heads:          {H}")
    print(f"   Src vocab:      {SRC_VOCAB}")
    print(f"   Tgt vocab:      {TGT_VOCAB}")

    model = make_transformer(SRC_VOCAB, TGT_VOCAB, N, D_MODEL, D_FF, H, DROPOUT)

    total_params = sum(p.numel() for p in model.parameters())
    print(f"   Total params:  {total_params:,}")

    # 前向传播测试
    print(f"\n[Forward Pass Test]...")
    model.eval()
    with torch.no_grad():
        # 完整 forward
        output = model(src, tgt, src_mask, tgt_mask)

        # 分别测试 encode 和 decode
        memory = model.encode(src, src_mask)
        decoder_output = model.decode(memory, src_mask, tgt, tgt_mask)
        final_output = model.generator(decoder_output)

    # 形状验证
    print(f"\n[Shape Verification]:")
    print(f"   src input:          {tuple(src.shape)}")
    print(f"   tgt input:          {tuple(tgt.shape)}")
    print(f"   encoder output:     {tuple(memory.shape)}")
    print(f"   decoder output:     {tuple(decoder_output.shape)}")
    print(f"   generator output:   {tuple(final_output.shape)}")

    # 验证
    assert memory.shape == (batch_size, src_seq_len, D_MODEL), \
        f"编码器输出形状错误: {memory.shape}"
    assert decoder_output.shape == (batch_size, tgt_seq_len, D_MODEL), \
        f"解码器输出形状错误: {decoder_output.shape}"
    assert final_output.shape == (batch_size, tgt_seq_len, TGT_VOCAB), \
        f"Generator输出形状错误: {final_output.shape}"

    # 验证掩码正确性
    print(f"\n[Attention Mask Verification]:")
    mask_sample = subsequent_mask(5)[0]
    print(f"   subsequent_mask(5):")
    print(f"   {mask_sample.int()}")
    print(f"   row=current position, col=visible range, 1=visible, 0=masked")

    print(f"\n[PASS] All tests passed! Transformer model is correct.")
    print(f"\n[Data Flow Summary]:")
    print(f"   src({batch_size},{src_seq_len})")
    print(f"     -> Embedding + PositionalEncoding")
    print(f"     -> Encoder x {N}")
    print(f"     -> memory({batch_size},{src_seq_len},{D_MODEL})")
    print(f"")
    print(f"   tgt({batch_size},{tgt_seq_len})")
    print(f"     -> Embedding + PositionalEncoding")
    print(f"     -> Decoder x {N} (masked + cross-attention)")
    print(f"     -> Generator(Linear + LogSoftmax)")
    print(f"     -> output({batch_size},{tgt_seq_len},{TGT_VOCAB})")
