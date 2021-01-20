> # Supervised Learning——Softmax Regression

参考资料：

* 周志华《机器学习》
* 赵志勇《Python机器学习算法》
* 《动手学习深度学习》

## Softmax 回归

Logistic Regression主要用于处理二分类问题（还有线性判别分析），Softmax Regression是逻辑回归的推广，主要用于处理多分类问题（比如手写数字识别）。

假设有`k`类，`m`个样本点，每个样本`n`个特征，那么权重矩阵的形状为$n \times k$，将偏置项合并到权重矩阵里，则可以计算对于第`i`个样本，属于某个类别的概率为：
$$
h_{\theta}\left(X^{(i)}\right)=\left[\begin{array}{c}
P\left(y^{(i)}=1 \mid X^{(i)} ; \theta\right) \\
P\left(y^{(i)}=2 \mid X^{(i)} ; \theta\right) \\
\vdots \\
P\left(y^{(i)}=k \mid X^{(i)} ; \theta\right)
\end{array}\right]=\frac{1}{\sum_{j=1}^{k} e^{\theta_{j}^{\prime} X^{(i)}}}\left[\begin{array}{c}
e^{\theta_{1}^{T} X^{(i)}} \\
e^{\theta_{2}^{\prime} X^{(i)}} \\
\vdots \\
e^{O_{k}^{T} X^{(i)}}
\end{array}\right]
$$

$$
P\left(y^{(i)}=j \mid X^{(i)} ; \theta\right)=\frac{e^{\theta_{j}^{T} X^{(i)}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} X^{(i)}}}
$$

损失函数的定义则是通过极大似然法求得,利用梯度下降（梯度提升求最大值，加了符号相当于求最小值）求更新公式：
$$
J(\theta)=-\frac{1}{m}\left[\sum_{i=1}^{m} \sum_{j=1}^{k} I\left\{y^{(i)}=j\right\} \log \frac{e^{\theta_{j}^{T} X^{(i)}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} X^{(i)}}}\right]
$$

$$
L(\theta)=-\frac{1}{m}\left[\sum_{i=1}^{m} \sum_{j=1}^{k} 1\left\{y^{(i)}=j\right\} \log \frac{e^{\theta_{j}^{T} x_{i}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}}\right]
$$

$$
\begin{aligned}
\frac{\partial L(\theta)}{\partial \theta_{j}} &=-\frac{1}{m} \frac{\partial}{\partial \theta_{j}}\left[\sum_{i=1}^{m} \sum_{j=1}^{k} 1\left\{y^{(i)} = j\right\} \log \frac{e^{\theta_{j}^{T} x_{i}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}}\right] \\
&=-\frac{1}{m} \frac{\partial}{\partial \theta_{j}}\left[\sum_{i=1}^{m} \sum_{j=1}^{k} 1\left\{y^{(i)}=j\right\}\left(\theta_{j}^{T} x_{i}-\log \sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}\right)\right] \\
&=-\frac{1}{m}\left[\sum_{i=1}^{m} 1\left\{y^{(i)}=j\right\}\left(x_{i}-\sum_{j=1}^{k} \frac{e^{\theta_{j}^{T} x_{i}} \cdot x_{i}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}}\right)\right] \\
&=-\frac{1}{m}\left[\sum_{i=1}^{m} x_{i} 1\left\{y^{(i)}=j\right\}\left(1-\sum_{j=1}^{k} \frac{e^{\theta_{j}^{T} x_{i}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}}\right)\right] \\
&=-\frac{1}{m}\left[\sum_{i=1}^{m} x_{i}\left(1\left\{y^{(i)}=j\right\}-\sum_{j=1}^{k} 1\left\{y_{i}=j\right\} \frac{e^{\theta_{j}^{T} x_{i}}}{\sum_{l=1}^{k} e^{\theta_{l}^{T} x_{i}}}\right)\right] \\
&=-\frac{1}{m}\left[\sum_{i=1}^{m} x_{i}\left(1\left\{y^{(i)}=j\right\}-\frac{e^{\theta_{j}^{T} x_{i}}}{\sum_{l=1}^{k} e^{\theta_{l} x_{i}}}\right)\right] \\
&=-\frac{1}{m}\left[\sum_{i=1}^{m} x_{i}\left(1\left\{y^{(i)}=j\right\}-p\left(y_{i}=j \mid x_{i} ; \theta\right)\right)\right]
\end{aligned}
$$

其中$1\{y_i = j\}$是示性函数，当类别属于`j`的时候为1，于是有：
$$
\theta_j = \theta_j + \alpha \nabla_{\theta_j} J(\theta)
$$

## 代码实现

```python
# coding:UTF-8

import numpy as np
import pandas as pd


def load_data(fileName):
    df = pd.read_csv(fileName, header = None, sep = '\t')
    feature = df.iloc[:, :-1].copy()
    pos = np.shape(np.array(feature))[1]
    feature.insert(value = 1, loc = pos, column = "one")
    label = df.iloc[:, [-1]].copy()
    feature = np.mat(feature)
    label = np.mat(label)
    return feature, label


def error_rate(err, label):
    m = np.shape(err)[0]
    sum_cost = 0.0
    for i in range(m):
        if err[i, label[i, 0]] / np.sum(err[i, :]) > 0:
            sum_cost -= np.log(err[i, label[i, 0]] / np.sum(err[i, :]))
        else:
            sum_cost -= 0
    return sum_cost / m


def softmax_regression(feature, label, maxCycle, alpha, k):
    m, n = feature.shape
    weight = np.mat(np.ones((n, k)))

    for i in range(maxCycle):
        err = np.exp(feature * weight)
        if i % 500 == 0:
            print("\titer = " + str(i) + " , train error rate = " + str(error_rate(err, label)))
        rowSum = -err.sum(axis = 1)
        rowSum = rowSum.repeat(k, axis = 1)
        err = err / rowSum
        for j in range(m):
            err[j, label[j, 0]] += 1
        weight = weight + alpha / m * feature.T * err
    return weight


def countNum(label):
    n = np.shape(label)[0]
    s = set()
    for i in range(n):
        s.add(label[i, 0])
    return len(s)


def save_model(fileName, weight):
    weight = pd.DataFrame(weight)
    weight.to_csv(fileName, header = None, index = None, sep = '\t')


def main():
    feature, label = load_data('./data.txt')
    weight = softmax_regression(feature, label, 10000, 0.4, countNum(label))
    save_model('./weight.txt', weight)


if __name__ == '__main__':
	main()
```

