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

当模型和损失函数形式较为简单时，上面的误差最小化问题的解可以直接用公式表达出来。这类解叫作解析解（analytical solution）。本节使用的线性回归和平方误差刚好属于这个范畴。然而，大多数深度学习模型并没有解析解，只能通过优化算法有限次迭代模型参数来尽可能降低损失函数的值。这类解叫作数值解（numerical solution）。

在求数值解的优化算法中，小批量随机梯度下降（mini-batch stochastic gradient descent）在深度学习中被广泛使用。它的算法很简单：先选取一组模型参数的初始值，如随机选取；接下来对参数进行多次迭代，使每次迭代都可能降低损失函数的值。在每次迭代中，先随机均匀采样一个由固定数目训练数据样本所组成的小批量（mini-batch）\mathcal{B}B，然后求小批量中数据样本的平均损失有关模型参数的导数（梯度），最后用此结果与预先设定的一个正数的乘积作为模型参数在本次迭代的减小量。
$$
\begin{aligned}
w_{1} & \leftarrow w_{1}-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \frac{\partial \ell^{(i)}\left(w_{1}, w_{2}, b\right)}{\partial w_{1}}=w_{1}-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} x_{1}^{(i)}\left(x_{1}^{(i)} w_{1}+x_{2}^{(i)} w_{2}+b-y^{(i)}\right) \\
w_{2} & \leftarrow w_{2}-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \frac{\partial \ell^{(i)}\left(w_{1}, w_{2}, b\right)}{\partial w_{2}}=w_{2}-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} x_{2}^{(i)}\left(x_{1}^{(i)} w_{1}+x_{2}^{(i)} w_{2}+b-y^{(i)}\right) \\
b & \leftarrow b-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \frac{\partial \ell^{(i)}\left(w_{1}, w_{2}, b\right)}{\partial b}=b-\frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}}\left(x_{1}^{(i)} w_{1}+x_{2}^{(i)} w_{2}+b-y^{(i)}\right)
\end{aligned}
$$
其中$|\mathcal{B}|$是`batch size`，$\eta$是学习率（`learning rate`）。

## Generalized linear regression

广义线性回归，对于对数线性回归，有$\ln{y} = \textbf{w}^T\textbf{x} + b$，更一般的，考虑单调可微函数$g(\cdot)$ $$ y = g^{-1}(\textbf{w}^T\textbf{x} + b) $$ 这样得到的模型称为“广义线性模型”（generalized linear model），其中函数$g(\cdot)$称为“联系函数”

## 程序实现

### 不借助框架的实现

具体的数据在`src`目录下。

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

### 借助TensorFlow的基础实现

```python
# %matplotlib inline
import tensorflow as tf
print(tf.__version__)
from matplotlib import pyplot as plt
import random

# generate data
feature_num = 2
sample_num = 1000
true_w = tf.constant([2.0, -3.4])
true_w = tf.reshape(true_w, (2, 1))
true_b = tf.constant([4.2])
features = tf.random.normal((sample_num, feature_num), stddev=1)
labels = tf.matmul(features, true_w) + true_b + tf.random.normal((sample_num, 1), stddev=0.01)

# read data
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        j = indices[i: min(i+batch_size, num_examples)]
        yield tf.gather(features, axis=0, indices=j), tf.gather(labels, axis=0, indices=j)

# initialize parameters        
batch_size = 10
predict_w = tf.Variable(tf.random.normal((feature_num, 1), stddev=0.01))
predict_b = tf.Variable(tf.zeros((1,)))

# define model
def linreg(X, w, b):
    return tf.matmul(X, w) + b

# define loss function
def squared_loss(y_hat, y):
    return (y_hat - tf.reshape(y, y_hat.shape)) ** 2 / 2

# define optimizer
def sgd(params, lr, batch_size, grads):
    """Mini-batch stochastic gradient descent."""
    for i, param in enumerate(params):
#         print(grads[0])
        param.assign_sub(lr * grads[i] / batch_size)

# train model
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        with tf.GradientTape() as t:
            t.watch([predict_w, predict_b])
            l = tf.reduce_sum(loss(net(X, predict_w, predict_b), y))
        grads = t.gradient(l, [predict_w, predict_b])
        sgd([predict_w, predict_b], lr, batch_size, grads)
    train_l = loss(net(features, predict_w, predict_b), labels)
    print('epoch %d, loss %f' % (epoch + 1, tf.reduce_mean(train_l)))

    
# validation
print(predict_w, true_w)
print(predict_b, true_b)
```



### 借助TensorFlow的简洁实现

```python
import tensorflow as tf
from tensorflow import data
from tensorflow import keras
from tensorflow import losses
from tensorflow.keras import optimizers
from tensorflow.keras import layers
from tensorflow import initializers as init

config = {
    "feature_num": 2,
    "sample_num": 1000,
    "batch_size": 10,
    "num_epochs": 3
}


def get_dataset():
    true_w = tf.reshape(tf.constant([2.0, -3.4]), (2, 1))
    true_b = tf.constant([4.2])
    features = tf.random.normal((config['sample_num'], config['feature_num']), stddev=1)
    labels = tf.matmul(features, true_w) + true_b + tf.random.normal((config['sample_num'], 1), stddev=0.01)
    dataset = data.Dataset.from_tensor_slices((features, labels)) \
        .shuffle(buffer_size=config['sample_num']).batch(config['batch_size'])

    return dataset, features, labels, true_w, true_b


def get_model():
    model = keras.Sequential(
        layers.Dense(1, kernel_initializer=init.RandomNormal(stddev=0.01))
    )
    return model


def get_loss():
    return losses.MeanSquaredError()


def get_optimizer():
    return optimizers.SGD(learning_rate=0.03)


def train(dataset, features, labels, model, optimizer, loss):
    for epoch in range(1, config['num_epochs'] + 1):
        for (batch, (X, y)) in enumerate(dataset):
            with tf.GradientTape() as tape:
                l = loss(model(X, training=True), y)

            grads = tape.gradient(l, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))
        l = loss(model(features), labels)
        print(f'epoch {epoch}, loss: {l}')


def main():
    dataset, features, labels, true_w, true_b = get_dataset()
    model = get_model()
    train(
        dataset=dataset,
        features=features,
        labels=labels,
        model=model,
        optimizer=get_optimizer(),
        loss=get_loss()
    )

    print(true_w, model.get_weights()[0])
    print(true_b, model.get_weights()[1])


if __name__ == '__main__':
    main()
```

### Pytorch实现

```python
import torch
import numpy as np
import torch.utils.data as Data
from torch import nn, optim
from torch.nn import init


class LinearNet(nn.Module):
    def __init__(self, num_inputs):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(num_inputs, 1)

    def forward(self, x):
        y = self.linear(x)
        return y


def main():
    # y = x_1 * w_1 + x_2 * w_2 + b
    num_inputs = 2
    num_examples = 1000
    true_w = [2, -3.4]
    true_b = 4.2
    features = torch.tensor(
        np.random.normal(0, 1, (num_examples, num_inputs)),
        dtype=torch.float
    )
    labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b + torch.tensor(
        np.random.normal(0, 0.01, size=(num_examples,)),
        dtype=torch.float
    )
    print(labels.shape)

    batch_size = 10
    dataset = Data.TensorDataset(features, labels)
    date_iter = Data.DataLoader(dataset, batch_size, shuffle=True)
    for X, y in date_iter:
        print(X, y)
        print(X.shape)
        print(y.shape)
        break

    # net = LinearNet(num_inputs)
    net = nn.Sequential(
        nn.Linear(num_inputs, 1)
    )
    print(net)
    for param in net.parameters():
        print(param)

    # model parameters initialize
    init.normal_(net[0].weight, mean=0, std=0.01)
    init.constant_(net[0].bias, val=0)

    loss = nn.MSELoss()

    optimizer = optim.SGD(net.parameters(), lr=0.03)
    print(optimizer)

    num_epochs = 3
    for epoch in range(num_epochs):
        for X, y in date_iter:
            output = net(X)
            l = loss(output, y.view(-1, 1))
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        print(f'epoch {epoch + 1}, loss: {l.item()}')

    dense = net[0]
    print(true_w, dense.weight)
    print(true_b, dense.bias)


if __name__ == '__main__':
    main()
```







































