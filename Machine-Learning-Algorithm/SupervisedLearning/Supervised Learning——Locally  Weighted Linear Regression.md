> # Supervised Learning——Locally  Weighted Linear Regression

参考资料：

* https://kivy-cn.github.io/Stanford-CS-229-CN/#/Markdown/cs229-notes1
* 赵志勇《python机器学习算法》
* 《机器学习实战》预测鲍鱼年龄的数据

## 局部加权线性回归

线性回归存在的问题是欠拟合，局部加权线性回归为每一个待预测点构建一个加权的线性模型，加权方式为根据预测点与数据集里的点的距离来为点赋予权重，离预测点近的点权重大，反之则权重小，效果是产生一种局部分段拟合的效果。定义损失函数形式为：
$$
f = \sum_{i = 1}^m \omega^{(i)} \left(y^{(i)}- \bf{X}\theta\right)^2
$$
写成矩阵的形式为：
$$
f = (\bf{y - X\theta})^T \cdot W \cdot (\bf{y - X\theta})
$$

其中$\bf{X}$的维度是$m \times n$， $\bf{y}$的维度是$m \times 1$。局部加权回归使用高斯核来为待预测点附近的点赋予权重， $\bf{W}$的维度是$m \times m$，是一个对角矩阵，主对角线上$w(i, i) = \exp{\left(-\frac{x^{(i) - x}}{2k^2}\right)}$。

## 程序实现

数据选取《python机器学习算法》中的数据，其中`k`依次选择`1.0, 0.01, 0.002`来展示欠拟合，效果较好的你和，过拟合的现象。

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter


# style setting
GOLD_RATIO = 1.618
MINIMAL_WIDTH = 3.54
SHORT_HEIGHT = MINIMAL_WIDTH / GOLD_RATIO
plt.rcParams['figure.figsize'] = MINIMAL_WIDTH, SHORT_HEIGHT
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['legend.loc'] = 'best'
plt.rcParams['legend.fontsize'] = 'medium'
plt.rcParams['font.size'] = 8


def lwlr(feature, label, k):
    m = np.shape(feature)[0]
    predict = np.zeros(m)
    weight = np.mat(np.eye(m))
    for i in range(m):
        for j in range(m):
            diff = feature[i, ] - feature[j, ]
            weight[j, j] = np.exp(diff * diff.T / (-2 * k ** 2))
        xTWx = feature.T * (weight * feature)
        theta = xTWx.I * (feature.T * (weight * label))
        predict[i] = feature[i, ] * theta
    return predict


def sortXY(feature, predict):
    L = sorted(zip(feature, predict), key = itemgetter(0))
    sort_feature, sort_predict = zip(*L)
    return sort_feature, sort_predict


def plotFigure(feature, predict, label, k):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	sort_feature, sort_predict = sortXY(np.array(feature[: , 0]), predict)
	plt.scatter(np.array(feature[: , 0]), np.array(label), s = 5)
	plt.plot(sort_feature, sort_predict, color='r', linewidth=1.5)
	plt.legend(labels = ['predict', 'data'])
	plt.title('k = ' + str(k))
	plt.xlabel('feature')
	plt.ylabel('label')
	plt.show()
	plt.savefig('./k=' + str(k) + '.png', bbox_inches = 'tight')


def main():
	fileName = './data.txt'
	df = pd.read_csv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1].copy()
	feature.insert(value = 1, loc = 1, column = "one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)

	kVal = [1.0, 0.01, 0.002]
	for k in kVal:
		predict = lwlr(feature, label, k)
		plotFigure(feature, predict, label, k)


if __name__ == '__main__':
	main()
```

效果如下：

![k_1.0.png](https://i.loli.net/2021/01/17/VWUE9c6r3dA4zop.png)

![k_0.01.png](https://i.loli.net/2021/01/17/GxnhKZeyQjzJM1g.png)

![k_0.002.png](https://i.loli.net/2021/01/17/gZesVOqEcPHj4F3.png)

