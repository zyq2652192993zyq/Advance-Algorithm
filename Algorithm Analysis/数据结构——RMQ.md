> # 数据结构——RMQ

范围最小值问题（Range Minimum Query，RMQ）。给出一个$n$个元素的数组$A_1,A_2,\cdots, A_n$，设计一个数据结构，支持查询操作Query(L,R): 计算$min(A_L,A_{L+1},\cdots,A_R)$.

# 利用ST表解决RMQ问题

Sparse-Table算法是Tarjan发明的，预处理时间是$O(n \log n)$，查询只需要$O(1)$，常数很小。用于解决 **可重复贡献问题** 的数据结构。







# 利用线段树解决RMQ问题



# 二维RMQ





# 典型题目

* <https://blog.csdn.net/u013480600/category_2129925.html>
* 《算法竞赛训练指南》
* [ ] POJ 3368
* [ ] POJ 3264
* [ ] HDU 4122（RMQ，动态最值）
* [ ] HDU 2888（二维RMQ）
* [ ] POJ 1785
* [ ] HDU 3183 （贪心或RMQ）
* [ ] POJ 2019（二维RMQ）

