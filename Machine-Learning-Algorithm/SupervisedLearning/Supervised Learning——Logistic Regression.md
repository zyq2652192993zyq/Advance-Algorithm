> # Supervised Learning——Logistic Regression

 参考资料：

* [【机器学习】逻辑回归（非常详细](https://zhuanlan.zhihu.com/p/74874291)
* 赵志勇《python机器学习》
* 《机器学习实战》
* 周志华《机器学习》
* https://kivy-cn.github.io/Stanford-CS-229-CN/#/Markdown/cs229-notes1
* [LR逻辑回归模型的原理、公式推导、Python实现和应用](https://zhuanlan.zhihu.com/p/151036015)

优点：计算代价小，易于理解和实现

缺点：容易欠拟合，分类精度可能不高

## 原理

适用数据类型：数值型和标称型数据

$$
 h_\theta(x) = g(\theta^T x) = \frac 1{1+e^{-\theta^Tx}} 
$$

其中有：

$$
g(z)= \frac 1 {1+e^{-z}}
$$
这个函数叫做**逻辑函数 （Logistic function）** ，或者也叫**双弯曲S型函数（sigmoid function**）

首先假设：

$$
\begin{aligned} P(y=1|x;\theta)&=h_{\theta}(x)\ P(y=0|x;\theta) \\
&=1- h_{\theta}(x)\ \end{aligned}
$$

更简洁的写法是：

$$
p(y|x;\theta)=(h_\theta (x))^y(1- h_\theta (x))^{1-y} 
$$

假设 $m$ 个训练样本都是各自独立生成的，那么就可以按如下的方式来写参数的似然函数：

$$
\begin{aligned}
L(\theta) &= p(\vec{y}| X; \theta)\\
&= \prod^m_{i=1} p(y^{(i)}| x^{(i)}; \theta)\\
&= \prod^m_{i=1} (h_\theta (x^{(i)}))^{y^{(i)}}(1-h_\theta (x^{(i)}))^{1-y^{(i)}} \\
\end{aligned}
$$

然后还是跟之前一样，取个对数就更容易计算最大值：

$$
\begin{aligned} 
l(\theta) &=\log L(\theta) \\
&= \sum^m_{i=1} y^{(i)} \log h(x^{(i)})+(1-y^{(i)})\log (1-h(x^{(i)})) 
\end{aligned}
$$
为了让函数取到最大值，选择梯度提升算法，先假设只有一个样本

$$
\begin{aligned} 
\frac {\partial}{\partial \theta_j} l(\theta) &=(y\frac 1 {g(\theta ^T x)} - (1-y)\frac 1 {1- g(\theta ^T x)} )\frac {\partial}{\partial \theta_j}g(\theta ^Tx) \\
&= (y\frac 1 {g(\theta ^T x)} - (1-y)\frac 1 {1- g(\theta ^T x)} ) g(\theta^Tx)(1-g(\theta^Tx)) \frac {\partial}{\partial \theta_j}\theta ^Tx \\
&= (y(1-g(\theta^Tx) ) -(1-y) g(\theta^Tx)) x_j\\
&= (y-h_\theta(x))x_j 
\end{aligned}
$$

对于所有样本，也就是批量梯度下降算法：
$$
\frac{\partial f}{\partial\theta_j}=\frac{1}{m} \sum_{i = 1}^m (y^{(i)} - h_{\theta}(x^{(i)}))x_j^{(i)}
$$

$$
\theta_j = \theta_j + \frac{1}{m} \sum_{i = 1}^m (y^{(i)} - h_{\theta}(x^{(i)}))x_j^{(i)}
$$

写成矩阵的形式：
$$
\bf{\theta = \theta - \alpha X^T (X\theta-Y)}
$$


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def error_rate(predict, label):
    m = np.shape(predict)[0]
    sum_err = 0.0
    for i in range(m):
        if predict[i, 0] > 0 and (1 - predict[i, 0]) > 0:
            sum_err -= (label[i,0] * np.log(predict[i,0]) + (1-label[i,0]) * np.log(1-predict[i,0]))
        else:
            sum_err -= 0
    return sum_err / m


def save_model(fileName, weight):
	weight = pd.DataFrame(weight)
	weight.to_csv(fileName, header = None, index = None)


def LR(feature, label, maxCycle, alpha):
    n = np.shape(feature)[1]
    weight = np.mat(np.ones((n, 1)))

    for i in range(maxCycle):
        predict = sigmoid(feature * weight)
        err = label - predict
        if (i + 1) % 100 == 0:
            print("\titer = " + str(i + 1) + " , train error rate = " + str(error_rate(predict, label)))
        weight = weight + alpha * feature.T * err
    return weight


def main():
	fileName = './data.txt'
	df = pd.read_csv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1].copy()
	pos = np.shape(np.array(feature))[1]
	feature.insert(value = 1, loc = pos, column = "one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)
	weight = LR(feature, label, 1000, 0.01)
	save_model('weight.txt', weight)


if __name__ == '__main__':
	main()
```

求似然函数最大值的方法不止梯度提升一种方法，还可以采用牛顿法，用牛顿法来在逻辑回归中求似然函数$l(\theta)$ 的最大值的时候，得到这一结果的方法也叫做**Fisher评分（Fisher scoring）。**

```python
class LogisticRegression(nn.Module):
    def __init__(self):
        super(LogisticRegression,self).__init__()
        self.lr=nn.Linear(2,1)   #相当于通过线性变换y=x*T(A)+b可以得到对应的各个系数
        self.sm=nn.Sigmoid()   #相当于通过激活函数的变换

    def forward(self, x):
        x=self.lr(x)
        x=self.sm(x)
        return x
```



## LR正则化

* [CTR预估[三]: Algorithm-LR and Regularization](https://zhuanlan.zhihu.com/p/31504720)





## LR的Bias及其应用





## LR的扩展MLR





