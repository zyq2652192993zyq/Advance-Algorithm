> # Deep Learning——Siamesce Network

参考资料：

* [Siamese network 孪生神经网络--一个简单神奇的结构](https://zhuanlan.zhihu.com/p/35040994)
* [孪生网络入门（上） Siamese Net](https://blog.51cto.com/u_15185176/2798001)
* [多种类型的神经网路（孪生网络](https://www.cnblogs.com/Lee-yl/p/10113386.html)）
* [SiameseNetwork孪生神经网络原理及实现](https://booleflow.com/2021/03/06/siamesenetwork-luan-sheng-shen-jing-wang-luo-yuan-li-ji-shi-xian/)
* [孪生网络入门（下） Siamese Net分类服装MNIST数据集(pytorch)](https://blog.51cto.com/u_15185176/2992591?b=totalstatistic)
* [卷积神经网络学习笔记——Siamese networks（孪生神经网络）](https://www.cnblogs.com/wj-1314/p/11556107.html)

孪生神经网络（Siamesce network）用来衡量输入的相似度，将输入映射到新的空间，形成输入在新的空间的表示。

如果两个神经网络并不相同，那么就是伪孪生神经网络（pseudo Siamese network）

当然还有三个神经网络组成的Triplet network，论文是《**Deep** **metric learning using Triplet network**》

孪生网络由于权重共享，所以一定程度上限制了network1和network2的差异不能太大，所以通常用来处理两个输入差异不是非常大的问题， 比如，对比两张图片、两个句子、两个词汇的相似度。对于输入差异很大的相似度，比如图片与相应的文字描述，文章标题与文章段落的相似度，这时候就需要使用伪孪生网络。

所以针对不同的情况，主要需要选择的是网络结构和对应的损失函数。

