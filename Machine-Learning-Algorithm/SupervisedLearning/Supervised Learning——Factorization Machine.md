> # Supervised Learning——Factorization Machine

参考资料：

* 赵志勇《python机器学习算法》
* https://blog.csdn.net/ddydavie/article/details/82667890
* [简单易学的机器学习算法——因子分解机(Factorization Machine)](https://blog.csdn.net/kunlong0909/article/details/52496221?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-11&spm=1001.2101.3001.4242) 
* [Factorization Machine笔记及Pytorch 实现](http://shomy.top/2018/12/31/factorization-machine/)

## 因子分解机

逻辑回归模型使用的是特征的线性组合，只能处理线性可分的二分类问题，对于非线性可分问题则无法处理。解决方案有：

* 对特征进行处理，如核函数，将非线性可分问题转化为近似线性可分问题
* 对逻辑回归进行扩展，如Steffen Rendle提出的基于矩阵分解的Factorization Machine算法

FM可以解决三类问题：

* 回归问题（Regression）
* 二分类问题（Binary Classification）

* 排序（Ranking）

度为`k`的FM表达式
$$
\hat{y}=w_{0}+\sum_{i=1}^{n} w_{i} x_{i}+\sum_{i=1}^{n-1} \sum_{j=i+1}^{n}\left\langle V_{i}, V_{j}\right\rangle x_{i} x_{j}
$$
$\left\langle V_{i}, V_{j}\right\rangle$表示两个大小为`k`的向量的点积。
$$
\left\langle V_{i}, V_{j}\right\rangle = \sum_{f = 1}^k v_{i, f} \cdot v_{j, f}
$$
`k`的大小称为因子分解机FM的度。很显然上式可以解决回归问题。

使用Logit Loss作为损失函数（等价于最大熵模型），对于回归问题
$$
\text{loss}^R(\hat{y}, y) = \frac{1}{2} \sum_{i = 1} ^m \left(\hat{y}^{(i)} - y^{(i)} \right)^2
$$
对于分类问题，损失函数为：
$$
\text{loss}^R(\hat{y}, y) = \ln{\sigma(\hat{y}\cdot y)}
$$
对于交叉项的处理
$$
\hat{y}=w_{0}+\sum_{i=1}^{n} w_{i} x_{i}+\sum_{i=1}^{n-1} \sum_{j=i+1}^{n}\omega_{i, j} x_{i} x_{j}
$$
对于$\omega_{i, j}$的处理，定义矩阵：
$$
V=\left(\begin{array}{cccc}
v_{11} & v_{12} & \cdots & v_{1 k} \\
v_{21} & v_{22} & \cdots & v_{2 k} \\
\vdots & \vdots & & \vdots \\
v_{n 1} & v_{n 2} & \cdots & v_{n k}
\end{array}\right)_{n \times k}=\left(\begin{array}{c}
V_{1} \\
V_{2} \\
\vdots \\
V_{n}
\end{array}\right)
$$
于是
$$
\hat{\omega}_{i,j} = V_i V_j^T
$$
上式中，交叉项是计算量最大的一项，另$\mu_i = V_i \cdot x_i$，则：
$$
\sum_{i=1}^{n-1} \sum_{j=i+1}^{n}\omega_{i, j} x_{i} x_{j} = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \mu_i \cdot \mu_j^T
$$

$$
\sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \mu_i \cdot \mu_j^T = \sum_{p = 1}^k \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \mu_{i,p} \cdot \mu_{j, p}
$$

上式的时间复杂度为$O(kn^2)$，现在考虑来降低时间复杂度：
$$
\begin{aligned}
\sum_{p = 1}^k \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \mu_{i,p} \cdot \mu_{j, p} &= \frac{1}{2}\sum_{p = 1}^k  \left(\sum_{i=1}^{n} \sum_{j=1}^{n} \mu_{i,p} \cdot \mu_{j, p} - \sum_{i = 1}^n \mu_{i, p}^2 \right) \\
&= \frac{1}{2}\sum_{p = 1}^k  \left( \left( \sum_{i = 1}^n \mu_{i, p}\right)^2 -  \sum_{i = 1}^n \mu_{i, p}^2 \right) \\
&=w_{0}+X W+\frac{1}{2} \sum_{f=1}^{k}\left\{\left[\left(x_{1}, x_{2}, \ldots x_{n}\right)\left(\begin{array}{c}
v_{1 f} \\
v_{2 f} \\
\vdots \\
v_{n f}
\end{array}\right)\right]^{2}-\left(x_{1}^{2}, x_{2}^{2}, \ldots x_{n}^{2}\right)\left(\begin{array}{c}
v_{1 f}^{2} \\
v_{2 f}^{2} \\
\vdots \\
v_{n f}^{2}
\end{array}\right)\right\} \\
&=w_{0}+X W+\frac{1}{2} \operatorname{sum}((X V) \circ(X V)-(X \circ X)(V \circ V), a x i s=1)
\end{aligned}
$$
这样时间复杂度就将为了$O(kn)$。其中$\circ$表示哈达玛积，即两个同阶矩阵对应元素相乘。

对于上式的化简，可以参考更[**直观的表格解释**](https://zhuanlan.zhihu.com/p/145436595)。

对于$\sum_{i=1}^{n} \sum_{j=1}^{n} \mu_{i,p} \cdot \mu_{j, p}$可以认为是一个$n \times n$的矩阵，而$\sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \mu_{i,p} \cdot \mu_{j, p}$ 可以认为是这个矩阵对角线右上部分的综合，就等于矩阵全部的数字相加后，减去对角线上的数字和，然后除以2得到。

---

对于参数的求解，采用梯度下降算法计算，如果是采用批量梯度下降，则一次迭代会采用全部样本来进行参数学习，如果数据量很大，则计算会很耗时，所以需要采用随机梯度下降算法（stochastic gradient descent），在每次迭代中，只采用一个样本进行调整。

这里$\sigma(y) = \frac{1}{1 + \exp^{-y}}$，其中$y$就是FM模型的结果。
$$
\begin{aligned}
\frac{\partial{\text{loss}^R(\hat{y}, y)}}{\partial{\theta}} &= -\frac{1}{\sigma(\hat{y}\cdot y)}  \sigma(\hat{y}\cdot y) [1 - \sigma(\hat{y}\cdot y)] \cdot y \cdot \frac{\partial{\hat{y}}}{\partial{\theta}} \\
&=[\sigma(\hat{y}\cdot y) - 1] \cdot y \cdot \frac{\partial{\hat{y}}}{\partial{\theta}}
\end{aligned}
$$
则对于参数的更新：
$$
\omega_0 = \omega_0 + \alpha \cdot [\sigma(\hat{y}\cdot y) - 1] \cdot y
$$

$$
\omega_i = \omega_i + \alpha \cdot [\sigma(\hat{y}\cdot y) - 1] \cdot y \cdot x_i^{(i)}
$$

$$
v_{i, p} = v_{i, p} + \alpha \cdot [\sigma(\hat{y}\cdot y) - 1] \cdot y \cdot [x_i (\sum_{j = 1}^n \mu_{j, p}) - u_{i, p}]
$$

## 程序实现

```python
# coding:UTF-8

import pandas as pd
import numpy as np



def load_data(fileName):
	df = pd.read_scv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1]
	label = df.iloc[:, [-1]]
	return np.mat(feature), np.mat(label)


def sigmoid(x):
	return 1.0 / (1 + np.exp(-x))


def FM(feature, label, k, maxCycle, alpha):
	m, n = np.shape(feature)
	w0 = 1
	weight = np.zeros((n, 1))
	V = np.random.normal(size=(n, k))

	for it in range(maxCycle):
		for x in range(m):
			colSum = feature[x] * V
			eleSquare = np.multiply(feature[x], feature[x]) * np.multiply(V, V)
			interaction = np.sum(np.multiply(colSum, colSum) - eleSquare) / 2.0
			yHat = w0 + feature[x] * weight + interaction
			loss = sigmoid(label[x] * yHat[0, 0]) - 1
			# update parameter
			w0 = w0 + alpha * loss * label[x]
			weight = weight + alpha * loss * label[x] * feature[x].T
			for i in range(n):
				for j in range(k):
					V[i, j] = V[i, j] - alpha * loss * label[x] * (feature[x, i] * (colSum[0, j] - V[i, j] * feature[x, i]))

	return w0, weight, V



def main():
	feature, label = load_data('./data.txt')
	w0, weight, V = FM(feature, label, 3, 10000, 0.01)


if __name__ == '__main__':
	main()
```



PyTorch:

*  https://blog.csdn.net/qq_38237214/article/details/121338159 (考虑了稀疏型和稠密型特征)
* http://shomy.top/2018/12/31/factorization-machine/

对于稠密型特征：

```python
import torch
import torch.nn as nn


class FactorizationMachine(nn.Module):
    def __init__(self, n, k):
        super(FactorizationMachine, self).__init__()
        self.n = n
        self.k = k
        self.linear = nn.Linear(self.n, 1, bias=True)
        self.v = nn.Parameter(torch.Tensor(self.k, self.n))  # 注：权重矩阵是(k,n)的，与公式里的相反，目的是下一步能在n的维度上分布初始化
        nn.init.xavier_uniform_(self.v)

    def forward(self, x):
        """
        :param x: Long tensor of size ``(b, n)``
        :return: Long tensor of size ``(b, 1)``
        """
        x1 = self.linear(x)
        square_of_sum = torch.mm(x, self.v.T) * torch.mm(x, self.v.T)
        sum_of_square = torch.mm(x * x, self.v.T * self.v.T)
        x2 = 0.5 * torch.sum((square_of_sum - sum_of_square), dim=-1, keepdim=True)
        x = x1 + x2
        return x
```

`torch.mm`是线性代数里的矩阵相乘，比如一个矩阵是$1 \times 2$，另一个矩阵是$2 \times 3$，则结果的维度是$1 \times 3$。`*`则是矩阵对应位置的元素相乘，要求矩阵的维度相同。

对于稀疏型特征，会采用embedding方法进行转化再计算。

