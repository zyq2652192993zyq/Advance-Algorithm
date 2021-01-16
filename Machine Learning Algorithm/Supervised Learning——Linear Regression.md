> # Supervised Learning——Linear Regression

参考资料：

* https://zhuanlan.zhihu.com/p/262751195

* 周志华《机器学习》
* https://kivy-cn.github.io/Stanford-CS-229-CN/#/Markdown/cs229-notes1

## 线性回归基础知识

设样本点的个数为`m`，维度为`n`，线性回归的目的是让预测值和真实值的差距最小，为了有更好的数学性质，使其平方和差距最小，即：
$$
f = ||X\omega-y||^2
$$
预测值的表达式：
$$
y_{i}=\omega_0+\omega_1 x_i^{(1)} + \cdots + \omega_n x_i^{(n)}
$$
其中上标`(1)`表示第`i`个样本的第`1`个维度，下标`i`表示第`i`个样本点。上式中`X`的维度是$m \times (n + 1)$，因为还需要增加一个全1列在矩阵的最后一列。`w`是`n+1`维的列向量，`y`同理。

利用微分的形式求取最后的表达式：

* 求微分`df`

$$
||X\omega-y||^2 = (X\omega-y)^T(X\omega-y)
$$

$$
\begin{aligned}
df &= [d(X\omega-y)]^T(X\omega-y)+(X\omega-y)^T\cdot d(X\omega-y) \\
&=(X\cdot d\omega)^T \cdot (X\omega-y) + (X\omega-y)^T \cdot (X\cdot d\omega)
\end{aligned}
$$

* 两边同时取迹

$$
\begin{aligned}
df = \mathrm{tr}(df) &= \mathrm{tr}[(X\cdot d\omega)^T \cdot (X\omega-y)] +\mathrm{tr}[ (X\omega-y)^T \cdot (X\cdot d\omega)] \\
&=\mathrm{tr}[(X\omega-y)^T \cdot (X\cdot d\omega)] + \mathrm{tr}[(X\omega-y)^T \cdot (X\cdot d\omega)] \\
&=\mathrm{tr}[2(X\omega-y)^T \cdot (X\cdot d\omega)]
\end{aligned}
$$

这里面利用了公式$\mathrm{tr}(A) = \mathrm{tr}(A^T)$。

* 根据$df = \mathrm{tr}[(\frac{\partial f}{\partial X})^T \cdot dX]$

$$
df = \mathrm{tr}[(2X^T \cdot (X\omega-y))^T \cdot d\omega]
$$

所以可知$\frac{\partial f}{\partial X}$的结果为：
$$
\frac{\partial f}{\partial X} = 2X^T \cdot (X\omega-y)
$$
为了让损失函数最小，上式为零，所以有：
$$
\omega = (X^T \cdot X)^{-1} \cdot X^T \cdot y
$$
其中上式需要考虑$X^T \cdot X$是否可拟的问题，于是会引出广义逆相关的问题。

## 线性回归的概率解释(Probabilistic interpretation)

假设预测值和真实值之间用如下关系表示：
$$
y^{(i)} = \bf{X^{(i)}\omega} + \epsilon^{(i)}
$$
其中$y^{(i)}$表示第`i`个真实值，$\bf{X^{(i)}}$是一个`m`维的列向量，$\epsilon^{(i)}$表示残差。现在假设残差独立同分布，并且服从高斯分布（Gaussian Distribution）也叫做正态分布（Normal Distribution），均值为0，方差（variance）为$\sigma^2$，一般简写为$\epsilon^{(i)} \sim \mathrm{N}(0, \sigma^2)$，概率密度函数为：
$$
\mathrm{p}(\epsilon^{(i)}) = \frac{1}{\sqrt{2\pi}\sigma} \cdot \exp{(-\frac{(\epsilon^{(i)})^2}{2\sigma^2})}
$$
将$\epsilon^{(i)}$的表达式带入上式，为了求得$\omega$的表达式，先写出似然函数，然后采用极大似然法求解：
$$
\begin{aligned}
\mathrm{L}(\theta) &=\prod_{i=1}^{m} \mathrm{p}\left(\mathrm{y}^{(\mathrm{i})} \mid \mathrm{x}^{(\mathrm{i})} ; \theta\right) \\
&=\prod_{i=1}^{\mathrm{m}} \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(\mathrm{y}^{(\mathrm{i})}-\theta^{\mathrm{T}} \mathrm{x}^{(\mathrm{i})}\right)^{2}}{2 \sigma^{2}}\right)
\end{aligned}
$$

$$
\begin{aligned}
1(\theta) &=\log \mathrm{L}(\theta) \\
&=\log \prod_{i=1}^{\mathrm{m}} \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(\mathrm{y}^{(\mathrm{i})}-\theta^{\mathrm{T}} \mathrm{x}^{(\mathrm{i})}\right)^{2}}{2 \sigma^{2}}\right) \\
&=\sum_{i=1}^{\mathrm{m}} \log \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(\mathrm{y}^{(\mathrm{i})}-\theta^{\mathrm{T}} \mathrm{x}^{(\mathrm{i})}\right)^{2}}{2 \sigma^{2}}\right) \\
&=\mathrm{m} \log \frac{1}{\sqrt{2 \pi} \sigma}-\frac{1}{\sigma^{2}} \cdot \frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{m}}\left(\mathrm{y}^{(\mathrm{i})}-\theta^{\mathrm{T}} \mathrm{x}^{(\mathrm{i})}\right)^{2}
\end{aligned}
$$

所以为了让似然函数取到最小值，则应该让$\sum_{\mathrm{i}=1}^{\mathrm{m}}\left(\mathrm{y}^{(\mathrm{i})}-\theta^{\mathrm{T}} \mathrm{x}^{(\mathrm{i})}\right)^{2}$取到最小值，这就是损失函数的定义。

## Generalized linear regression

广义线性回归，对于对数线性回归，有$\ln{y} = \textbf{w}^T\textbf{x} + b$，更一般的，考虑单调可微函数$g(\cdot)$ $$ y = g^{-1}(\textbf{w}^T\textbf{x} + b) $$ 这样得到的模型称为“广义线性模型”（generalized linear model），其中函数$g(\cdot)$称为“联系函数”

## 程序实现

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Least_Square(feature, label):
    if np.linalg.det(feature.T * feature) == 0:
        print('singular matrix')
        return
	return (feature.T * feature).I * feature.T * label

if __name__ == "__main__":
	df = pd.read_csv("./data.txt", header = None, sep = '\t')
	feature = df.iloc[:, :-1].copy()
	feature.insert(value = 1, loc = 1, column = "one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)

	res = pd.DataFrame(Least_Square(feature, label))
	res.to_csv("result.txt", header = None, index = None)
```













