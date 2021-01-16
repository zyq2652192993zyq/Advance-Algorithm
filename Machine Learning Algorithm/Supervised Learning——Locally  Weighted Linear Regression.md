> # Supervised Learning——Locally  Weighted Linear Regression

参考资料：

* https://kivy-cn.github.io/Stanford-CS-229-CN/#/Markdown/cs229-notes1
* 赵志勇《python机器学习算法》
* 《机器学习实战》预测鲍鱼年龄的数据

## 局部加权线性回归

线性回归存在的问题是欠拟合，一种改进的方案是在待预测表的点附近的点赋予一个权重，损失函数形式为：
$$
f = \sum_{i = 1}^m \omega^{(i)} \left(y^{(i)}- \bf{X}\theta\right)^2
$$
写成矩阵的形式为：
$$
f = (\bf{y - X\theta})^T \cdot W \cdot (\bf{y - X\theta})
$$
