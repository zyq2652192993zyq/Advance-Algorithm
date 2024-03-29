> # Optimization Algorithm

参考资料：

* AI圣经《深度学习》
* 《动手学习深度学习》
* https://zhuanlan.zhihu.com/p/25765735 （含程序例子）

对于优化算法的总结：

![optimization_Algorithm.png](https://i.loli.net/2021/01/17/etckQx7PTrvK5zg.png)



模型的训练误差远远小于在测试集上的误差，这是因为发生了过拟合，应对过拟合的常用方法有权重衰减（weight decay）。

## 权重衰减

权重衰减等价于L2范数正则化（regulation），是应对过拟合的常用手段。





## 批量梯度提升/下降算法

梯度提升算法（gradient ascent）：求函数的极大值

梯度下降算法（gradient decent）：求函数的极小值

区别在于表达式$x = x + \alpha \nabla_x f(x)$，中是`+`号还是`-`号。不变的是都需要对损失函数求导数。



## 小批量梯度下降



## 随机梯度下降



















