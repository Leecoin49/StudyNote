import numpy as np
from mpl_toolkits.mplot3d import Axes3D, axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs

X, y = make_blobs(centers=4, random_state=8)
y = y % 2
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# plt.xlabel("Feature 0")
# plt.ylabel("Feature 1")

# 假设 X 是已经生成的样本数据集，并且有一个名为 y 的标签数组
# 添加第二个特征的平方，作为一个新特征
X_new = np.hstack([X, X[:, 1:] ** 2])

# 创建一个新的 figure 对象
figure = plt.figure()

# 创建一个 3D 坐标轴
ax = Axes3D(figure, elev=-152, azim=-26)

# 根据 y 的值画出不同颜色的点
# 注意：这里假设 y 是一个与 X_new 行数相同的一维数组
ax.scatter(X_new[y == 0, 0], X_new[y == 0, 1], X_new[y == 0, 2], c='b', s=60)
ax.scatter(X_new[y == 1, 0], X_new[y == 1, 1], X_new[y == 1, 2], c='r', marker='^', s=60)

# 设置坐标轴标签
ax.set_xlabel("feature0")
ax.set_ylabel("feature1")
ax.set_zlabel("feature1 squared")

# 显示图表
plt.show()