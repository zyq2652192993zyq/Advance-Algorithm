> # 集成学习——决策树

参考

* 《python机器学习算法》
* 机器学习在-周志华 第四章
* 统计学习方法 李航 第五章

## 基础知识



## 划分选择

### 信息增益

**信息熵**（information entropy）：用来度量样本集合纯度的一种指标。假设样本集合`d`中第`k`类样本的比例为$p_k(k = 1,2, \cdots |y|)$，则information entropy定义为：
$$
Ent(D) = -\sum_{k = 1} ^{|y|} p_k \times \log_2{p_k}
$$
`Ent(D)`的值越小，则样本集合`d`的纯度越高。

假定某个特征维度`a`有`v`种可能的取值$a^1, a^2, \cdots, a^v$，使用`a`对样本集进行划分，会产生最多`v`个分支，每个分支包含的样本点在维度`a`上的取值都相同，分支包含的样本数量标记为$d^v$，从而定义信息增益：
$$
Gain(D, a) = Ent(D) - \sum_{v = 1} ^{V} \frac{|D^v|}{|D|}Ent(D^v)
$$
**信息增益**（information gain）：通过某个维度对样本划分，划分前后信息熵的减少量称为信息增益。

信息增益越大，意味着属性`a`的划分获得的纯度提升越大， ID3决策树就是选择infomation gain作为属性划分的依据。

### 增益率

information gain准则对取值数目较多的属性有偏好，从而衍生出增益率(gain  ratio)，C4.5算法所采用。

**增益率**（gain ratio）：
$$
\text{gain ratio}(D, a) = \frac{Gain(D, a)}{IV(a)} \\
IV(a) = - \sum_{v = 1} ^V \frac{|D^v|}{|D|} \log_2{\frac{|D^v|}{|D|}}
$$
其中`IV(a)`称为属性`a`的固有值，属性a的可能取值越多，固有值通常越大。

gain ratio对取值数目越少的属性有偏好，C4.5并没有直接选用，而是使用了启发式的方法：先从候选划分属性找出information gain高于平均水平的，然后选择gain ratio最大的。

### 基尼指数

基尼指数（Gini index）。CART决策树使用gini index作为划分依据。 假设有`k`个分类，样本属于第`k`个分类的概率为$p_k$，则基尼指数为：
$$
Gini(p) = \sum_{k = 1}^Kp_k \times (1 - p_k) = 1 - \sum_{k = 1}^K p_k^2 \\
Gini(D) = 1 - \sum_{k = 1}^K(\frac{|C_k|}{|D|})^2
$$
其中$|C_k|$表示数据集中，属于类别`k`的样本个数。假设现在根据特征`a`将数据集划分为两个数据集`d1`和`d2`，则基尼指数为：
$$
Gini(D, A) = \frac{|D_1|}{|D|} Gini(D_1) + \frac{|D_2|}{|D|} Gini(D_2)
$$
基尼指数越小，则划分后的数据集纯度越高。

## ID3





## C4.5



使用增益率（gain ratio）作为划分数据集的方法。



## CART决策树



利用Gini指数作为划分数据集的方法。



## 剪枝策略

剪枝（pruning）是决策树对付过拟合的主要手段，常用的策略有预剪枝(prepruning)和后剪枝（post-pruning）。





