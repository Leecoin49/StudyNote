## 创建虚拟环境

~~~powershell
# 创建虚拟环境，并安装指定的包
conda create --name data_analysis python=3.8 pandas matplotlib
conda create --name myenv python=3.8

# 方法二：使用 --prefix 选项
#在创建环境时，可以使用 --prefix 选项明确指定环境的路径：

conda create --prefix C:\Anaconda3\envs\spider python=3.8

conda activate C:\Anaconda3\envs\myenv

# 安装其他包（如果需要）
conda install scipy

# 完成操作后停用虚拟环境
conda deactivate
~~~

## 查看现有的 Conda 虚拟环境，可以使用以下命令：

```powershell
conda env list
```

```powershell
conda info --envs
```



### 删除指定环境

使用以下命令删除指定的环境，将 `myenv` 替换为你要删除的环境名称：

```powershell
conda env remove --name myenv
```

