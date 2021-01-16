> # 基础算法——Linear Regression

参考资料：

* https://zhuanlan.zhihu.com/p/262751195

* 周志华《机器学习》

a设样本点的个数为`m`，维度为`n`，线性回归的目的是让预测值和真实值的差距最小，为了有更好的数学性质，使其平方和差距最小，即：
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
df = [d(X\omega-y)]^T(X\omega-y)+(X\omega-y)^T\cdot d(X\omega-y) \\
=(X\cdot d\omega)^T \cdot (X\omega-y) + (X\omega-y)^T \cdot (X\cdot d\omega)
$$

* 两边同时取迹

$$
df = \mathrm{tr}(df) = \mathrm{tr}[(X\cdot d\omega)^T \cdot (X\omega-y)] +\mathrm{tr}[ (X\omega-y)^T \cdot (X\cdot d\omega)] \\
=\mathrm{tr}[(X\omega-y)^T \cdot (X\cdot d\omega)] + \mathrm{tr}[(X\omega-y)^T \cdot (X\cdot d\omega)] \\
=\mathrm{tr}[2(X\omega-y)^T \cdot (X\cdot d\omega)]
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





