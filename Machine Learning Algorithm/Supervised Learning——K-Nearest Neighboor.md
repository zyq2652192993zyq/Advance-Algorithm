> # Supervised Learning——K-nearest neighboor

参考资料：

* 《统计学习》李航
* 《机器学习实战》

## KNN基础

KNN（K近邻算法），存在一个样本数据集合（训练样本集），并且样本集都是有标签的，输入没有标签的数据，将数据的每个特征与样本集中数据对应的特征进行比较，最后选择样本集中前`k`个最相似的数据，统计`k`个数据中出现次数最多的分类，最为新数据的分类。参数`k`是超参数，一般是不大于20的整数。

```python
import numpy as np
import operator

def KNN(inputData, trainData, label, k):
    rowNum = trainData.shape[0]
    diffMat = np.tile(inputData, (rowNum, 1)) - trainData
    squareDiffMat = diffMat ** 2
    squareDisMat = squareDiffMat.sum(axis = 1)
    disMat = squareDisMat ** 0.5
    sortedIndex = disMat.argsort() #得到升序后原数组索引下标
    classCount = {}
    for i in range(k):
        voteLabel = label[sortedIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(
        classCount.iteritems(), 
        key = operator.itemgetter(1), 
        reverse = True
    )

    return sortedClassCount[0][0]
```

上面的算法每次传入一个数据向量，依次去计算其和样本集的距离，最后统计前`k`小距离中`label`出现次数最多的`label`并返回，时间复杂度为$O(nm\log{m})$，其中`m`是样本集的数量，`n`是验证集的数量。

实际上算法还可以进行优化，既然取出前`k`个，可以用优先级队列来进行排序，这样时间复杂读可以优化到$O(nm\log{k})$。

[python优先级队列](https://geek-docs.com/python/python-examples/python-priority-queue.html)



## 优化算法

### 距离加权

https://blog.csdn.net/weixin_41770169/article/details/81560946

### K-Decision Tree

KNN的优化版本。

### BallTree

https://blog.csdn.net/weixin_41770169/article/details/81634307

### LSH

https://blog.csdn.net/weixin_41770169/article/details/81634943

