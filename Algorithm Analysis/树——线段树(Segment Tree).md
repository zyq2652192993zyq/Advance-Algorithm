> # 树——线段树(Segment Tree)

参考资料：

* <https://vjudge.net/article/467>
* <https://vjudge.net/article/1385>
* <https://www.cnblogs.com/flashhu/p/9651161.html>
* https://www.bilibili.com/video/BV1Ct411H76z/?spm_id_from=333.788.videocard.1
* [noip线段树与树状数组](https://www.bilibili.com/video/BV1Tk4y1m7VM/?spm_id_from=333.788.videocard.5) 较为全面

## 线段树的背景

```
题目一：
10000个正整数，编号1到10000，用A[1],A[2],……，A[10000]表示。
修改：无
统计：1.编号从L到R的所有数之和为多少？ 其中1<= L <= R <= 10000.
```

* 方法一：对于统计$L,R$ ，需要求下标从$L$到$R$的所有数的和，从$L$到$R$的所有下标记做$[L..R]$,问题就是对$A[L..R]$进行求和。这样求和，对于每个询问，需要将$(R-L+1)$个数相加。
* 方法二：更快的方法是求前缀和,令 $S[0]=0, S[k]=A[1..k]$ ，那么，$A[L..R]$的和就等于$S[R]-S[L-1]$，这样，对于每个询问，就只需要做一次减法，大大提高效率。

```
题目二：
10000个正整数，编号从1到10000，用A[1],A[2],……，A[10000]表示。
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

## 线段树的基本实现

### 线段树的存储

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


参考资料：https://blog.csdn.net/litble/article/details/72486558

最坏情况应该是从第二种情况分析得出，因为此时最后一行除了两个叶节点以外，其他全是空节点。设倒数第二层的高度是$h$，那么倒数第二层的叶节点个数是$2^h-1$，因为全部叶节点个数是$n$，那么就有
$$
2^h-1+2=n\\
2^h = n -1
$$
因为要让线段树的下标属性和完全二叉树相同，那么就需要开辟$\sum_{i = 0}^{h+1} 2^i=2^{h+2}-1$大小的空间，把上面结果带入，那么就是$4n-5$大小的空间，也就是最坏需要开辟4倍节点数的空间。

### 线段树的初始化

这里我们选择递归的方式来构建线段树，需要注意一个细节，就是求取中点的程序，我们看两种写法：

* `int mid = (left + right) / 2;`
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

### 单点修改

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

### 区间修改与懒惰标记

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

	pushDown(k); //标记下传

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

### 区间查询与标记下传

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



### 线段树分裂

参考链接：https://www.luogu.com.cn/training/2971

线段树分裂通常用于节选序列中的区间或可重集中的值域等，可以解决一些此类的问题。

* P5494 【模板】线段树分裂（练习线段树分裂和合并的模板题）

* P2824 [HEOI2016/TJOI2016] 排序（线段树分裂解决区间排序的问题，也可以用二分+线段树解决）

* P5298 [PKUWC2018] Minimax（树上问题的线段树合并，这题的标记处理比较特殊）

* P4770 [NOI2018] 你的名字（线段树合并维护 SAM 上 endpos 的套路）

* P3224 [HNOI2012] 永无乡（线段树合并维护连通块信息，也可以练习离散化映射后线段树直接维护的套路）



### 线段树合并



## 不同问题下的线段树实现

### 单点修改，区间加法，查询区间和

* 将指定位置的元素`a`替换成`b`
* 将区间`x`到`y`内的元素都增加一个数`k`
* 查询区间`x`到`y`内的总和

- [x] 洛谷-P3373 【模板】线段树 2

```c++
#include <bits/stdc++.h>

using namespace std;


struct Node {
	int left, right;
	long long  sum;
	long long lazy; //lazy: 延迟标记

	//Node():left(0), right(0), sum(0), lazy(0) {}
};

int n = 100005; //叶节点的个数
vector<Node> tree(n * 4);
vector<int> seq(n);

#define left(x)  tree[x].left
#define right(x) tree[x].right
#define sum(x)   tree[x].sum
#define lazy(x)  tree[x].lazy

inline int leftChild(int x) { return x << 1; } //根节点的左子节点的下标
inline int rightChild(int x) { return x << 1 | 1; } //根节点的右子节点的下标
inline int length(int x) { return right(x) - left(x) + 1; } //根节点覆盖的区间长度

inline void update(int root)
{
	sum(root) = sum(leftChild(root)) + sum(rightChild(root));
}

void build(int root, int l, int r)
{
	left(root) = l;
	right(root) = r;

	//递归到了叶节点可以停止了
	if (l == r) { sum(root) = seq[l]; return; }

	//递归构建左右子树
	int mid = l + ((r - l) >> 1);
	build(leftChild(root), l, mid);
	build(rightChild(root), mid + 1, r);

	update(root); //构建完成要更新当前节点的sum值
}

void pushDown(int root) 
{
	if (lazy(root)) {
		sum(leftChild(root)) += lazy(root) * length(leftChild(root));
		sum(rightChild(root)) += lazy(root) * length(rightChild(root));

		lazy(leftChild(root)) += lazy(root); //左子节点延迟标记
		lazy(rightChild(root)) += lazy(root); //右子节点延迟标记
		lazy(root) = 0; //清除根节点标记
	}
}

//单点修改
void change(int root, int pos, int val)
{
	//如果当前节点就是叶节点，直接修改，停止下滤
	if (left(root) == right(root)) { sum(root) = val; return; }

	int mid = left(root) + ((right(root) - left(root)) >> 1);

	if (pos <= mid) change(leftChild(root), pos, val);
	else change(rightChild(root), pos, val);

	update(root);
}

//区间修改
void intervalChange(int root, int l, int r, long long value)
{
	//恰好找到了一个完整的区间
	if (left(root) == l && right(root) == r) {
		sum(root) += length(root) * value;
		lazy(root) += value;
		return;
	}

	pushDown(root); //延迟标记下传

	int mid = left(root) + ((right(root) - left(root)) >> 1);

	if (r <= mid) intervalChange(leftChild(root), l, r, value);
	else if (l > mid) intervalChange(rightChild(root), l, r, value);
	else {
		intervalChange(leftChild(root), l, mid, value);
		intervalChange(rightChild(root), mid + 1, r, value);
	}

	update(root);
}

long long query(int root, int l, int r)
{
	if (left(root) == l && right(root) == r) return sum(root);

	pushDown(root); //延迟标记下传

	int mid = left(root) + ((right(root) - left(root)) >> 1);
	if (r <= mid) return query(leftChild(root), l, r);
	else if (l > mid) return query(rightChild(root), l, r);

	return query(leftChild(root), l, mid) + query(rightChild(root), mid + 1, r);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	
	int q;
	cin >> n >> q;

	for (int i = 1; i <= n; ++i) cin >> seq[i];

	build(1, 1, n);

	while (q--) {
		int ops; cin >> ops;
		if (ops & 1) { //ops == 1
			int l, r;
			long long value;
			cin >> l >> r >> value;
			intervalChange(1, l, r, value);
		}
		else { //ops == 2
			int l, r;
			cin >> l >> r;
			cout << query(1, l, r) << endl;
		}
	}

	return 0;
}
```



### 区间乘法，区间加法，查询区间和（多标记线段树）

参考资料：https://blog.csdn.net/litble/article/details/70902462

- [x] 洛谷-P3373 【模板】线段树 2

* 将区间`x`到`y`内的元素都增加一个数`k`
* 将区间`x`到`y`内的元素都乘上一个数`k`
* 查询区间`x`到`y`内的总和（或总和对某个数取模）



### 区间修改，查询区间和

- [ ] HihoCoder - 1078 线段树的区间修改



### jiry 线段树（小清新线段树）

jiry 线段树用于维护区间取min,max 的操作，支持区间修改。

参考链接：

* https://www.cnblogs.com/White-star/p/11508170.html
* https://www.cnblogs.com/fengzhiyuan/p/8848060.html
* https://blog.csdn.net/g21wcr/article/details/83032224
* https://www.cnblogs.com/frankchenfu/p/7132445.html
* http://wyfcyx.logdown.com/posts/201802-summary-data-structures-zkw-segment-tree-details



- [ ] HDU 5306 Gorgeous Sequence



### zkw 线段树

zkw（张琨玮） 线段树

参考资料：

* https://blog.csdn.net/keshuqi/article/details/52205884
* https://www.cnblogs.com/Judge/p/9514862.html
* https://zhuanlan.zhihu.com/p/29876526
* https://www.sohu.com/a/252683843_100201031
* https://blog.csdn.net/unicornt_/article/details/52078337



### 李超线段树

用标记永久化维护平面内线段覆盖情况的线段树

参考资料：

* https://ac.nowcoder.com/discuss/180365
* https://www.cnblogs.com/JHSeng/p/10896570.html
* https://blog.csdn.net/litble/article/details/81234303
* https://www.bilibili.com/video/av710077552/



### 权值线段树

权值线段树是主席树的前置技能。权值线段树维护**数的个数，**数组下标代表**整个值域**（如果值域太大，可以**离散化**）

权值线段树可以解决的问题：

* 寻找第K大（整个区间，即左边界为1，右边界为n）
* 逆序对（归并排序也可以求解）

<u>标准练习：洛谷-P1801 黑匣子</u>

询问整体第k大（query），在线段树上进行二分（即**整体二分**）：

先看左子树数的个数，设其个数为f.

* 如果f>=t递归进入左子树寻找
* 如果f<k递归进入右子树寻找第f-k大

参考资料：https://www.luogu.com.cn/training/1010

https://blog.csdn.net/Code92007/article/details/86761820

P2574 XOR的艺术
P2894 [USACO08FEB]酒店Hotel
P4145 上帝造题的七分钟2 / 花神游历各国
P4513 小白逛公园
P2572 [SCOI2010]序列操作
P5889 跳树
P6186 [NOI Online 提高组]冒泡排序



但权值树真的有很多的作用呢！

P3369 【模板】普通平衡树
P1972 [SDOI2009]HH的项链
P4113 [HEOI2012]采花





### 线段树实现RMQ









## 线段树分治

参考资料：https://www.luogu.com.cn/training/2971

线段树分治是一类非常重要的离线算法，修改的对象一般需要增删，而线段树分治可以通过离线转化为只有增而没有删，代价是多一个 log 的复杂度。

离线动态图就是它非常重要的应用。

P5787 二分图 /【模板】线段树分治（线段树分治的最常见题目之一）

P3733 [HAOI2017] 八纵八横（线段树分治和线性基的结合）

P3206 [HNOI2010] 城市建设（线段树分治与 LCT 维护动态 MST 结合，可以支持增删的套路）

补充题：LOJ 121 [离线可过] 动态图连通性（真正的线段树分治模板题，与可撤销并查集结合）

补充题：LOJ 6515 [雅礼集训 2018 Day10] 贪玩蓝月（线段树分治和背包 DP 结合的好题，化删为增）







## 扫描线算法

参考资料：

* https://www.bilibili.com/video/BV144411Z7tx

* https://www.luogu.com.cn/training/1010
* https://www.bilibili.com/video/BV1Po4y1Z7sm?from=search&seid=4237805124879648201&spm_id_from=333.337.0.0



### Number of Airplanes in the Sky

给出每个飞机的起落时间，如果同一时刻有飞机降落，也有飞机起飞，则先降落再起飞。

如果碰到飞机起飞，则飞机数+1，否则减1。

```c++
/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
	struct Node
	{
		int pos;
		int flag;

		Node(int p, int f): pos(p), flag(f) {}

		bool operator<(const Node & obj) const {
			return pos < obj.pos || (pos == obj.pos && flag > obj.flag);
		}
	};
public:
    /**
     * @param airplanes: An interval array
     * @return: Count of airplanes are in the sky.
     */
    int countOfAirplanes(vector<Interval> &airplanes) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        vector<Node> store;
        for (auto & e : airplanes) {
        	store.push_back(Node(e.start, -1));
        	store.push_back(Node(e.end, 1));
        }

        sort(store.begin(), store.end());

        int res = 0;
        int tmp = 0;
        for (auto & e : store) {
        	if (e.flag < 0) ++tmp;
        	else --tmp;
        	res = max(res, tmp);
        }

        return res;
    }
};
```









最典型的题目

- [x] LintCode 391.Number of Airplanes in the Sky (也可以用区间贪心中的区间选点来解决)

- [ ] P1904 天际线
- [ ] P5490 【模板】扫描线（矩形覆盖问题）
- [ ] P1856 [USACO5.5]矩形周长Picture















## 二维偏序

参考资料：https://www.luogu.com.cn/training/1010

P1502 窗口的星星
P5816 [CQOI2010]内部白点
P3431 [POI2005]AUT-The Bus







## 线段树优化动态规划









## 高维线段树





## 线段树与平衡树的结合

解决动态区间第K大问题。

- [x] ZOJ 2112 Dynamic Rankings



## 线段树的典型应用

线段树可以与约瑟夫环问题结合，具体查看《典型问题——约瑟夫环问题》







在OI wiki的链接：<https://oi-wiki.org/ds/seg/>

主要应用：<http://immortalco.blog.uoj.ac/blog/2102>

线段树的主要类型：

* 李超线段树
* `jiry`线段树
* `zkw`线段树（`zkw`是张昆玮拼音的所写，源自其论文《统计的力量》实际上是线段树的非递归写法）
* 线段树合并
* 主席树/可持久化线段树 / 函数式线段树
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





## 典型题目

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
- [ ] UVA11983——线段树求矩形覆盖K次以上面积

学好线段树才可以学好可持久化，比如入门的可持久化数组（进而学习可持久化线段树/平衡树），由此衍生很多可持久化的数据结构

<https://blog.csdn.net/u013480600/article/category/2138267>

