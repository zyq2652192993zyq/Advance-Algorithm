> # 数据结构——RMQ

范围最小（大）值问题（Range Minimum/Maximum Query，RMQ）。给出一个$n$个元素的数组$A_1,A_2,\cdots, A_n$，设计一个数据结构，支持查询操作Query(L,R): 计算$min(A_L,A_{L+1},\cdots,A_R)$.

# ST表解决RMQ问题

Sparse-Table算法是Tarjan发明的，预处理时间是$O(n \log n)$，查询只需要$O(1)$，常数很小。用于解决 **可重复贡献问题** 的数据结构（倍增法）。



# 线段树解决RMQ问题

* 一种方法是利用线段树实现$O(1)$建表
* 另一种方法是使用权值线段树





# 平方割方法解决RMQ问题

来自《挑战程序设计竞赛》



# 笛卡尔树和LCA解决RMQ问题

来自洛谷模板笛卡尔树，两个点的LCA就是它们的RMQ。

* 参考资料：LCA与RMQ互化：https://www.cnblogs.com/Parsnip/p/12660750.html



# 莫队解决RMQ问题



# 数列分块解决RMQ问题





# 二维RMQ



# 环形RMQ

- [ ] CodeForces 52C Circular RMQ（线段树板子）



# RMQ with Shift

- [ ] UVA12299 RMQ with Shifts（线段树解决）



# RMQ逆问题

- [ ] 51-Nod 1336 RMQ逆问题
- [ ] TopCoder-13235 InverseRMQ（51-Nod就是此题的中文翻译）

RMQ问题是一类区间最值问题，这里给出一个特殊的RMQ问题，初始给定一个`n`长的排列`P`，注：`n`长排列是指有`1~n`这`n`个整数构成的一个序列每个整数恰好出现一次。并对这个排列`P`进行`M`次查询操作，每次查询形如`Query（L，R）`，每次查询返回排列`P`中位置在区间`L,R`上所有数中最大的那个数，其中位置的下标从1开始。例如排列`P = {3,1,4,2,5}`，那么`Query(1,2) = max{3,1}=3,Query(2,4)=max{1,4,2}=4`。由于RMQ问题对大家来说实在是太简单了，所以这题要求大家求解一个RMQ的逆问题，即给你排列的长度n，以及M次查询的问题及其结果三元组`（Li,Ri,Qi）`，即`Query（Li，Ri）=Qi`，询问符合这`M`次查询的`n`长排列是否存在。若存在输出`“Possible”`；否则输出`“Impossible”`。



# RMQ相似序列

- [ ] HDU-6305 RMQ Similar Sequence





# 典型题目

* <https://blog.csdn.net/u013480600/category_2129925.html>
* 《算法竞赛训练指南》
* [ ] POJ 3368
* [ ] P4137 Rmq Problem / mex（RMQ模板题）
* [ ] POJ 3264
* [ ] HDU 4122（RMQ，动态最值）
* [ ] HDU 2888（二维RMQ）
* [ ] POJ 1785
* [ ] HDU 3183 （贪心或RMQ）
* [ ] POJ 2019（二维RMQ）
* [ ] UVA12572 RMQ Overkill

