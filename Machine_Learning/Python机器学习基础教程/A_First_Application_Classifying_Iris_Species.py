import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import mglearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# 参考：https://www.cnblogs.com/hardykay/p/10880604.html
"""
    鸢尾花(iris)数据集
    它包含在 scikit-learn 的 datasets 模块中。
    我们可以调用 load_iris 函数来加载数据。
"""
iris_dataset = load_iris()

'''
    load_iris 返回的 iris 对象是一个 Bunch 对象，与字典非常相似，里面包含键和值。
    dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
        - DESCR 键对应的值是数据集的简要说明。
        - target_names 键对应的值是一个字符串数组，里面包含我们要预测的花的品种。
        - feature_names 键对应的值是一个字符串列表，对每一个特征进行了说明。
        - 数据包含在 target 和 data 字段中。
            - data 里面是花萼长度、花萼宽度、花瓣长度、花瓣宽度的测量数据，格式为 NumPy 数组。
              data 数组的每一行对应一朵花，列代表每朵花的四个测量数据。
              机器学习中的个体叫作样本（sample），其属性叫作特征（feature）。data 数组的形状（shape）是样本数乘以特征数。
            - target 数组包含的是测量过的每朵花的品种，也是一个 NumPy 数组。
'''
print("Keys of iris_dataset:\n", iris_dataset.keys())
print(iris_dataset['DESCR'][:193] + "\n...")
print("Target names: {}".format(iris_dataset['target_names']))
print("Feature names: \n{}".format(iris_dataset['feature_names']))
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))
print("First five rows of data:\n{}".format(iris_dataset['data'][:5]))
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))
# 品种被转换成从 0 到 2 的整数、
# 0 代表 setosa，1 代表 versicolor，2 代表 virginica。
print("Target:\n{}".format(iris_dataset['target']))

"""
    一部分数据用于构建机器学习模型，叫作训练数据（training data）或训练集（training set）。
    其余的数据用来评估模型性能，叫作测试数据（test data）、测试集（test set）或留出集（hold-out set）
    scikit-learn 中的 train_test_split 函数可以打乱数据集并进行拆分。
    这个函数将 75% 的行数据及对应标签作为训练集，剩下 25% 的数据及其标签作为测试集。
    训练集与测试集的分配比例可以是随意的，但使用 25% 的数据作为测试集是很好的经验法则。
    scikit-learn 中的数据通常用大写的 X 表示，而标签用小写的 y 表示。
    random_state 参数指定了随机数生成器的种子。
"""
X_train, X_test, y_train, y_test = train_test_split(
 iris_dataset['data'], iris_dataset['target'], random_state=0)


# X_train 包含 75% 的行数据，X_test 包含剩下的 25%
print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))


# 利用X_train中的数据创建DataFrame
# 利用iris_dataset.feature_names中的字符串对数据列进行标记
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# 利用DataFrame创建散点图矩阵，按y_train着色
'''
    我们来看scatter_matrix的参数
    def scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, diagonal='hist', marker='.', density_kwds=None,hist_kwds=None, range_padding=0.05, **kwds)
    frame：pandas dataframe对象
    alpha：(float, 可选)， 图像透明度，一般取(0,1]
    figsize: ((float,float), 可选)，以英寸为单位的图像大小，一般以元组 (width, height) 形式设置
    ax：(Matplotlib axis object, 可选)，一般取None
    diagonal：({‘hist’, ‘kde’})，必须且只能在{‘hist’, ‘kde’}中选择1个，’hist’表示直方图(Histogram plot),’kde’表示核密度估计(Kernel Density Estimation)；该参数是scatter_matrix函数的关键参数，下文将做进一步介绍
    marker：(str, 可选)， Matplotlib可用的标记类型，如’.’，’,’，’o’等
    density_kwds：(other plotting keyword arguments，可选)，与kde相关的字典参数
    hist_kwds：(other plotting keyword arguments，可选)，与hist相关的字典参数
    range_padding：(float, 可选)，图像在x轴、y轴原点附近的留白(padding)，该值越大，留白距离越大，图像远离坐标原点
    kwds：(other plotting keyword arguments，可选)，与scatter_matrix函数本身相关的字典参数
'''
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
plt.show()