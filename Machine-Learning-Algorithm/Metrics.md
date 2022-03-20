> # Metrics

参考资料：

* 《机器学习》周志华 2.3.2
* https://zhuanlan.zhihu.com/p/51423854
* https://zhuanlan.zhihu.com/p/347800635
* https://zhuanlan.zhihu.com/p/36305931

## Confusion Matrix

|           | 预测值 正 | 预测值 负 |
| --------- | --------- | --------- |
| 真实值 正 | TP        | FN        |
| 真实值 负 | FP        | TN        |

混淆矩阵。

## Accuracy

指预测正确的样本数占总体的比值：
$$
\text{acc} = \frac{TP + TN}{TP + TN + FP + FN}
$$
也叫做准确率。

## Precision

也叫做查准率，假设样例总数为`N`，设true positive, false positive, true negative, false negative分别为TP, FP, TN, FN，则$TP + FP + TN + FN = N$。
$$
\text{Precision} = \frac{TP}{TP + FP}
$$

1. TP（True Positive）：实际是正类，预测为正类。
2. FN（False Negative)：实际是正类，预测为负类（漏）。
3. FP（False Positive）：实际为负类，预测为正类（误）。
4. TN（True Negative）：实际为负类，预测为负类。

也就是指所有预测为positive里面和实际相符的比例。

## Recall

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

也叫做查全率，recall和precision两个目标通常来说是矛盾的。因为FN是指遗漏的真实数据，也就是指全部为正样本里被预测对的比例。

综合考虑precision和recall，出现了平衡点（break-event-point, BEP），它是PR图中`precision = recall`时的取值。

但是BEP还是过于简单，从而出现了F1 score。

## F1 Score

F1是基于precision和recall的调和平均，即：
$$
\frac{1}{F_1} = \frac{1}{2}\left( \frac{1}{P} + \frac{1}{R} \right)
$$

$$
F_1 = \frac{2 \times P \times R}{P + R} = \frac{2 \times TP}{N + TP - TN}
$$

## ROC

ROC = Receiver Operating Characteristic，受试者工作特征。

ROC曲线的纵轴为TPR，横轴为FPR，
$$
TPR = \frac{TP}{TP + FN} \\
FPR = \frac{FP}{FP + TN}
$$
对角线对应于随机猜测。点`(0, 1)`则是把所有正例排在所有反例前面的“理想模型”。



## AUC

AUC是一种模型分类指标，且仅仅是二分类模型的评价指标，是Area Under Curve的简称。这个curve就是ROC曲线。



## Kolmogorov-Smirnov

KS值是在模型中用于区分预测正负样本分隔程度的评价指标，一般应用于金融风控领域。













