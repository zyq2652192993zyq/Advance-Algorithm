> # Loss Function

参考资料：

* 《统计学习》1.3.2 策略
* 《动手学习深度学习》多层感知机

## 0-1损失函数（0-1 loss function）





## 平方损失函数（quadratic loss function）





## 绝对损失函数（absolute loss function）





## 对数损失函数（logarithmic loss function）





## 交叉熵损失函数（Cross Entropy Loss Function）

https://zhuanlan.zhihu.com/p/35709485

交叉熵损失函数通常应用于分类问题。
$$
L = -\frac{1}{N} \sum_i \hat{y_m} \ln{p_m}
$$
其中$N$代表样本的数量，$\hat{y_m}$代表属于第`m`个类别为1，不属于其他类别则为0，$p_m$是算出当前样本属于第`m`个类别的概率。







