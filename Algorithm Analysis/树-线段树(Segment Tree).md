> # 树-线段树(Segment Tree)


#1 线段树的背景

```
题目一：
10000个正整数，编号1到10000，用A[1],A[2],A[10000]表示。
修改：无
统计：1.编号从L到R的所有数之和为多少？ 其中1<= L <= R <= 10000.
```

* 方法一：对于统计$L,R$ ，需要求下标从$L$到$R$的所有数的和，从$L$到$R$的所有下标记做$[L..R]$,问题就是对$A[L..R]$进行求和。这样求和，对于每个询问，需要将$(R-L+1)$个数相加。
* 方法二：更快的方法是求前缀和,令 $S[0]=0, S[k]=A[1..k]$ ，那么，$A[L..R]$的和就等于$S[R]-S[L-1]$，这样，对于每个询问，就只需要做一次减法，大大提高效率。

```
题目二：
10000个正整数，编号从1到10000，用A[1],A[2],A[10000]表示。
修改：1.将第L个数增加C （1 <= L <= 10000）
统计：1.编号从L到R的所有数之和为多少？ 其中1<= L <= R <= 10000.
```

* 再使用方法二的话，假如$A[L] += C$之后，$S[L],S[L+1],,S[R]$都需要增加$C$,全部都要修改，见下表。

|             | 方法一              | 方法二           |
| ----------- | ------------------- | ---------------- |
| $A[L] += C$ | 修改1个元素         | 修改$R-L+1$个元素  |
| 求和$A[L..R]$ | 计算$R-L+1$个元素之和 | 计算两个元素之差 |

从上表可以看出，方法一修改快，求和慢。 方法二求和快，修改慢。线段树的出现就是设法使修改和求和都比较快。

线段树的出现是为了解决具有“**区间加法**”特性的一类问题，本质其实是**分治**的思想。比如：

* 区间加法：左区间和 + 右区间和
* 最大公因数（GCD）：左区间GCD，右区间GCD
* 区间最值：左区间最值，右区间最值

# 2 线段树的实现

![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/segmentTreeree.png)

## 线段树的存储

线段树一般采取**堆式储存法**，构建方法既可以采用标准的二叉树存储，也可以采用数组来模拟。用数组模拟在解决编程问题时较为合适，可以根据题目的数据范围直接开一个大数组。

线段树从上图可以看出其不一定是完全二叉树，但是其节点编号的性质和完全二叉树相同。编号为$k$的节点的左儿子（如果有）的节点编号就是$2k$，右儿子（如果有）的编号就是$2k+1$，父节点（如果有）的编号是$k / 2$，这里可以通过位运算优化以下。分别写成 `k << 1` `k << 1 | 1` `k >> 1`，解释一下$k << 1 | 1 = 2k + 1$，因为$k$左移一位，那么二进制的最低位一定是0，与$1$或运算最后一位就成了$1$，那么相当于总体加一了。

每个节点存储的数据应该包括：区间左边界$left$，区间右边界$right$，区间和$sum$，懒惰标记$lazy$：

```c++
struct Node {
	int left, right;
	long long  sum;
	long long lazy;

	//Node():left(0), right(0), sum(0), lazy(0) {}
};

int N = 1000001; //叶节点的个数，设区间为[l, r]，则N = r - l + 1
vector<Node> v(N << 2);
vector<int> num(N); //用来存储节点原始数据
```

这里需要关注一个细节，就是为什么要开4倍的数组空间，其实是和线段树的定义方式有关，线段树可以按下面两种方式定义：

* 方式一：左子树：$[left, \frac{left + right}{2}]$，右子树：$[\frac{left + right}{2} + 1, r]$


![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/segmentTreeree1.png)

* 方式二：左子树：$[left, \frac{left + right + 1}{2} - 1]$，右子树：$[\frac{left + right + 1}{2}, right]$


![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/segmentTreeree2.png)

最坏情况应该是从第二种情况分析得出，因为此时最后一行除了两个叶节点以外，其他全是空节点。设倒数第二层的高度是$h$，那么倒数第二层的叶节点个数是$2^h-1$，因为全部叶节点个数是$n$，那么就有
$$
2^h-1+2=n\\
2^h = n -1
$$
因为要让线段树的下标属性和完全二叉树相同，那么就需要开辟$\sum_{i = 0}^{h+1} 2^i=2^{h+2}-1$大小的空间，把上面结果带入，那么就是$4n-5$大小的空间，也就是最坏需要开辟4倍节点数的空间。

## 线段树的初始化

这里我们选择递归的方式来构建线段树，需要注意一个细节，就是求取中点的程序，我们看两种写法：

* `int mid = (left + right) 2;`
* `int mid = left + ((right - left) >> 1);`

虽然这两种表达式形式上一样，但是**第一种情况可能存在溢出**。不妨设想`right = INT_MAX - 1, left = 0`，第一次求`mid`没问题，但是第二次求`mid`的时候，`left`已经更新成`right / 2`了，这时候`left + right`就会溢出，所以第二种方式可以保证不会出错。同时在二分查找以及各种变形应用的时候，都应该关注这个细节。

这里`update`函数我们没有去检查需要更新的节点是否是叶节点，我们把这份工作交给其他函数去做，也就是说比如`build, query`等函数，都是先检查是否是叶节点。

```c++
inline void update(int k)
{
	v[k].sum = v[k << 1].sum + v[k << 1 | 1].sum;
}

void build(int k, int leftPos, int rightPos)
{
	v[k].left = leftPos;
	v[k].right = rightPos;

	//递归到了叶节点可以停止了
	if (leftPos == rightPos) {
		 v[k].sum = num[leftPos];
		 return;
	}

	int mid = leftPos + ((rightPos - leftPos) >> 1);
	build(k << 1, leftPos, mid);
	build(k << 1 | 1, mid + 1, rightPos);
	update(k); //构建完成要更新当前节点的sum值
}
```

## 单点修改

设当前节点编号是$k$，需要修改的节点编号是$target$，需要将节点的值修改为$value$，方法就类似于二叉查找树，修改的点肯定是叶节点，需要注意的是修改之后要更新包含此节点的区间所在的节点。

```c++
void change(int k, int target, int value)
{
	//如果当前节点就是叶节点，直接修改，停止下滤
	if (v[k].left == v.right) {
		v.sum = value;
		return;
	}

	int mid = v[k].left + ((v[k].right - v[k].left) >> 1);

	if (target <= mid) change(k << 1, target, value);
	else change(k << 1 | 1, target, value);
	update(k);
}
```

## 区间修改与懒惰标记

如果区间修改采取的策略是遍历区间的所有点，然后一一修改，那么线段树也就没什么存在意义了。比如在下面这种图，我要把区间$[1, 4]$内的元素都加上$1$（如果赋值同理，只要自己明白$lazy$最后的含义并且要全局统一），那么就更新区间$[1,3]$和区间$[4, 4]$，更新区间的$sum$值，令$lazy$记录为此区间统一都需要修改的$1$，而区间内的节点先不修改，$lazy$的作用相当于一个标记。

需要考虑的有三种情形：

* 需要更改的区间在中点的左边
* 需要修改的区间在中点的右边
* 需要修改的区间跨越中点

![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/segmentTreeree1.png)

```c++
void intervalChange(int k, int leftPos, int rightPos, int value)
{
	//恰好找到了一个完整的区间
	if (v[k].left == leftPos && v[k].right == rightPos) {
		v[k].sum += (rightPos - leftPos + 1) * value;
		v[k].lazy += value;
		return;
	}

	pushDown(k);

	int mid = v[k].left + ((v[k].right - v[k].left) >> 1);
	if (rightPos <= mid) intervalChange(k << 1, leftPos, rightPos, value);
	else if (leftPos > mid) intervalChange(k << 1 | 1, leftPos, rightPos, value);
	else {
		intervalChange(k << 1, leftPos, mid, value);
		intervalChange(k << 1 | 1, mid + 1, rightPos, value);
	}
	update(k);
}
```

## 区间查询与标记下传

采用懒惰标记的一般针对只是想求取区间修改后的结果问题，比如对某个区间增加某一数值后的区间和，但是如果是区间查询，那么就必须要先标记下传再进行区间查询。

对于标记下传的理解可以想象过年发红包的情景，比如孩子A，B收到相同数额的红包，它们的父亲怕他们乱花钱，就统一在父亲那里保管，如果两个孩子需要用到这个红包（也就是线段树里的查询），就把红包再发下去。所以区间修改和区间查询都需要先标记下传，然后在执行其他操作。

```c++
//标记下传
void pushDown(int k) 
{
	if (v[k].lazy) {
		v[k << 1].lazy += v[k].lazy;
		v[k << 1 | 1].lazy += v[k].lazy;
		v[k << 1].sum += v[k].lazy * (v[k << 1].right - v[k << 1].left + 1);
		v[k << 1 | 1].sum += v[k].lazy * (v[k << 1 | 1].right - v[k << 1 | 1].left + 1);
		v[k].lazy = 0;
	}
}
```

```c++
//区间查询
long long query(int k, int leftPos, int rightPos)
{
	if (v[k].left == leftPos && v[k].right == rightPos) 
		return v[k].sum;

	pushDown(k);

	int mid = v[k].left + ((v[k].right - v[k].left) >> 1);
	if (rightPos <= mid) return query(k << 1, leftPos, rightPos);
	else if (leftPos > mid) return query(k << 1 | 1, leftPos, rightPos);

	return query(k << 1, leftPos, mid) + query(k << 1 | 1, mid + 1, rightPos);
}
```

# 权值线段树

权值线段树维护**数的个数，**数组下标代表**整个值域**（如果值域太大，可以**离散化**）

权值线段树可以解决的问题：

* 寻找第K大（整个区间，即左边界为1，右边界为n）
* 逆序对（归并排序也可以求解）

<u>标准练习：洛谷-P1801 黑匣子</u>

询问整体第k大（query），在线段树上进行二分（即**整体二分**）：

先看左子树数的个数，设其个数为f.

* 如果f>=t递归进入左子树寻找
* 如果f<k递归进入右子树寻找第f-k大



#3 线段树在一些经典问题中的应用

* 洛谷P1908 逆序对
* codeforces 540 E. Infinite Inversions (分类思想+线段树)求逆序对
* HDU 1394                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

   5.3.2 矩形覆盖问题 

5.4 线段树的扩展

 	5.4.1 用线段树优化动态规划 

​	5.4.2 将线段树扩展到高维 

​	5.4.3 线段树与平衡树的结合

5.5 线段树与其他数据结构的比较 

5.6 线段树的应用举例 



在OI wiki的链接：<https://oi-wiki.org/ds/seg/>

主要应用：<http://immortalco.blog.uoj.ac/blog/2102>

线段树的主要类型：

* 李超线段树
* `jiry`线段树
* `zkw`线段树（`zkw`是张昆玮拼音的所写，源自其论文《统计的力量》实际上是线段树的非递归写法）
* 线段树合并
* 可持久化线段树 / 函数式线段树
* 线段树套线段树（树套树）
* 扫描线算法
* 权值线段树

国家集训队论文：

* 2004 林涛 《线段树的应用》
* 2017 沈睿 《被操纵的线段树》（较难，知识点很综合）

入门的部分写的不错：<https://blog.csdn.net/zearot/article/details/52280189>

代码实现的参考（递归的方法，涉及懒惰修改）<https://blog.csdn.net/huangzihaoal/article/details/81813454#_30>

（最综合）很好的知识点和题目的结合：<https://blog.csdn.net/zearot/article/details/48299459>

作为参考的博客：<https://www.cnblogs.com/Xing-Ling/p/10886957.html>





# 典型题目

- [x] POJ-3264 Balanced Lineup(线段树区间最大值，最小值查询)
- [x] 洛谷-P3374 【模板】树状数组1（可以用线段树，单点修改，区间查询）
- [x] 洛谷-P3372 【模板】线段树1（区间修改 + 区间查询）
- [x] 洛谷-P1801 黑匣子（权值线段树，也可以Spaly Tree, AVL或者堆）
- [ ] 完美正方形 蓝桥杯


- [ ] HDU 3642
- [ ] POJ 1436
- [ ] HDU 1540
- [ ] HDU 1754
- [ ] HDU 3265
- [ ] HDU 1166
- [ ] HDU 1394 1698 1828 2795 3308 3397 
- [ ] HOJ 1119 / POJ 1151 / HDU 1542
- [ ] POJ 2991
- [ ] POJ 3225 3667 2528 3468

学好线段树才可以学好可持久化，比如入门的可持久化数组（等价可持久化线段树/平衡树），由此衍生很多可持久化的数据结构

<https://blog.csdn.net/u013480600/article/category/2138267>

