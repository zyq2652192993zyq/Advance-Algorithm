> # 集成学习——基本策略

参考资料：

* [Regression Tree 回归树](https://mp.weixin.qq.com/s/HWvlxtnvXE9-Z9VNWDGOgg)
* [梯度提升（Gradient Boosting）算法](https://zhuanlan.zhihu.com/p/86354141)
* [深入理解提升树（Boosting Tree）算法](https://mp.weixin.qq.com/s/UepQi5Qezdi27MvbUSyLCA)
* [集成学习算法(Ensemble Method)浅析](https://zhuanlan.zhihu.com/p/32798104)
* [机器学习：sklearn、XGBoost、LightGBM](https://www.jianshu.com/p/fe321e478cb4)
* 《机器学习实战》第七章 AdaBoost

回归树可以利用集成学习中的Boosting框架改良升级得到提升树，提升树再经过梯度提升算法改造就可以得到GBDT算法，GBDT再进一步可以升级为XGBoost、LightGBM或者CatBoost。

## General Knowledge

参考：

* 《机器学习》周志华，第八章 集成学习

根据个体学习器的生成方式，分为：

* Boosting：个体学习器之间存在强依赖关系，必须串行生成的序列化方法。
* Bagging：个体学习器之间不存在强依赖关系，可以同时生成的并行化方法。

## Boosting方法

代表方法：

* AdaBoost 
  * 《统计学习》李航，第八章 提升方法（数学推导很详细）
  * 《机器学习实战》第七章，利用AdaBoost元算法提高分类性能
  * 《机器学习实战：基于scikit-learn和tensorflow》第七章，集成学习和随机森林，提升法（含`sklearn`的例子）



## Bagging方法





## Stacking方法



