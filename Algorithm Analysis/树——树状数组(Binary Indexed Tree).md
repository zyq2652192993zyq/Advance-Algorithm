> # 树状数组（Binary Indexed Tree）

参考资料：

* [【SDU-ACM】 树状数组与倍增算法](https://www.bilibili.com/video/BV1e7411s7gy)

* [树状数组与倍增](https://www.bilibili.com/video/BV1e7411s7gy)
* [【算法讲堂】【电子科技大学】【ACM】树状数组与ST表](https://www.bilibili.com/video/BV1LW411e7jo/?spm_id_from=333.788.videocard.1)

* [树状数组算法](https://www.bilibili.com/video/BV1E4411H7RY/?spm_id_from=333.788.videocard.7)
* [HRBU ACM 莫队 线段树 树状数组](https://www.bilibili.com/video/BV1PW411v77R/?spm_id_from=333.788.videocard.8)

* [oiClass树状数组](https://www.bilibili.com/video/BV1Yp4y1v7mP/?spm_id_from=333.788.videocard.11)



## 基础知识

> 此部分参考《算法竞赛进阶指南》

一个数字根据其二进制表示可以写成：
$$
x = 2^{i_1} + 2^{i_2} + \cdots + 2^{i_m}
$$
设$i_1 > i_2 > \cdots > i_m$，这样可以把区间$[1,x]$分成$\log {m}$个小区间：

* 长度为$2^{i_1}$的区间$[1,2^{i_1}]$
* 长度为$2^{i_2}$的区间$[2^{i_1} + 1, 2^{i_1} + 2^{i_2}]$

* $\cdots$

* 长度为$2^{i_m}$的区间$[x - 2^{i_m} + 1, x]$

这里需要了解`lowbit`运算，`lowbit`运算在状态压缩里面也有涉及，或者可以参考《算法竞赛进阶指南那》里的位运算部分，实际上`lowbit`运算得到的是一个数字$x$最低位的1及其后面所有的0构成的数字。每次需要将区间分割，那么找出最低位的1是较为简便的，首先将数字`x`按位取反，这样最低位的1变成了0，最低位的1及以后的都变成了1，那么将取反后的数字加上1，那么从最低位的1的高一位到最高位，都二进制位与原数字相反，两者位与运算，则提取出最低位的1及其后面所有的0构成的数字。又因为`~n = -n - 1`，所以`lowbit`可以写成：

```c++
inline int lowbit(int x)
{
    return x & (-x);
}
```

书中提到用数组`c[x]`表示`[x - lowbit(x) + 1, x]`区间的数字总和，这个很好理解。满足的四条性质：

* 每个内部节点`c[x]`保存以它为根的子树所有叶节点的和
* 每个内部节点`c[x]`的子节点个数等于`lowbit(x)`的位数
* 除了根节点，每个内部子节点`c[x]`的父节点是`c[x + lowbit(x)]`
* 树的深度是$O(\log{N})$，其中`N`为数字的个数

这几条结论虽然从书中的图可以比较直观的印证，但是需要比较严谨的证明来加深理解，参考了[树状数组正确性证明](https://zhuanlan.zhihu.com/p/297885717)

* 设数字`x >= 1`，则区间`c[x]`的左端点`L(x) = x - lowbit(x) + 1`。
* 对于任意$x, y \geq 1$，如果$x \in [L(y), y]$，则称`y`覆盖`x`。
* 数字`x`可以表示为$x = a \times 2^{i + 1} + 2^i, a \geq 0, i \geq 0$

**命题1：**对于树状数组的任意三个下标$1 \leq x \leq y \leq z$，若`y`覆盖`x`，`z`覆盖`y`，则`z`覆盖`x`，即覆盖性质具有传递性

思路：`y`覆盖`x`，`z`覆盖`y`，意味着$x \in [L(y), y], y \in [L(z), z]$，如果$[L(y), y] \subset [L(z), z]$，那么就有$x \in [L(z), z]$，也就证明了`z`覆盖`x`。
$$
z = a \times 2^{i + 1} + 2^i, L(z) = 2^{i + 1} + 1, \text{lowbit}(z) = 2^i
$$
因为`z`覆盖`y`，则：
$$
y \geq L(z) = a \times 2^{i + 1} + 1, y \leq a \times 2^{i + 1} + 2^i
$$
所以`y`可以写成：
$$
y = a \times 2^{i + 1} + b, b \in [1, 2^i] \\
\therefore \text{lowbit}(y) = \text{lowbit}(b)
$$
显然$b \geq \text{lowbit}(b)$，则
$$
L(y) = y - \text{lowbit}(y) + 1 = a \times 2^{i + 1} + b - \text{lowbit}(b) + 1 \\
\geq a \times 2^{i + 1} + 1 = L(z) \\
\therefore [L(y), y] \subset [L(z), z]
$$
同理可证$[L(x), x] \subset [L(y), y]$，所以有$[L(x), x] \subset [L(z), z]$，所以$x \in [L(z), z]$，所以`z`覆盖`x`

**命题2：**，对于任意树状数组的下标`x, y`，如果`y = x + lowbit(x)`， 则`y`覆盖`x`（即反向覆盖性）

思路：证明`y`覆盖`x`，因为已知`y > x`，只需要证明$L(y) \leq x$

设$x=a\times 2^{i+1}+2^i$，则$y = a\times 2^{i+1}+2^i + 2^i = (a + 1)\times 2^{i + 1}$，显然有$\text{lowbit}(y) \geq 2^{i + 1}$，则
$$
x - L(y) = a \times 2^{i+1}+2^i-(y-\text{lowbit}(y)+1) \\
=a \times 2^{i+1}+2^i -((a + 1)\times 2^{i + 1} - \text{lowbit}(y) + 1) \\
= 2^i - 1 + \text{lowbit}(y) - 2^{i + 1} \geq 2^i - 1 \geq 0
$$
所以有`y`覆盖`x`。

**命题3：**（反向覆盖的排他性）对于树状数组的下标`x, y`，如果`y = x + lowbit(x)`，则对于任意`x < z < y`，`z`都**不覆盖**`x`，并且`L(z) > x`

根据`y = x + lowbit(x)`，设$x = a \times 2^{i + 1} + 2^i$，则$y = x + 2^i$，因为`x < z < y`，则`z = x + b`， $b \in [1, 2^i - 1]$。

显然$\text{lowbit}(z) = \text{lowbit}(b), b \geq \text{lowbit}(b)$，则
$$
L(z) = z - \text{lowbit}(z) + 1=x + b - \text{lowbit}(b) + 1 \geq x + 1 > x
$$
**命题4：**（连续反向覆盖性质）对于任意树状数组下标`x`，覆盖`x`的所有下标有且仅有$x + \text{lowbit}(x), x+\text{lowbit}(x)+\text{lowbit}(x + \text{lowbit}(x)), \cdots$，即设$p(0) = x$，当`i >0`，有$p(i) = p(i - 1) + \text{lowbit}(p(i - 1))$

命题可以拆分成两部分

* 序列`p`中任意数字都覆盖`x`，根据反向覆盖性和传递性，显然成立
* 在区间`[1, p(0)), (p(0), p(1)), ...`区间内的任何数字不会覆盖`x`，根据反向覆盖的排他性，设$y \in (p(i), p(i + 1))$，则$p(i) < L(y)$，又因为$p(i) > x$，所以`x < L(y)`

上述的证明并不是没有意义，它们会影响后面程序的设计。

初始化有两种方法：

* 数组全部初始化为0，然后相当于单线修改，这样初始化的时间复杂度为$O(n \log {n})$
* 根据连续反向覆盖性质，可以实现$O(n)$初始化

```c++
int n;
vector<int> seq(1e5 + 5), tree(1e5 + 5);

inline int lowbit(int x)
{
	return x & (-x);
}

void build()
{
	for (int i = 1; i <= n; ++i) {
		tree[i] += seq[i];
		int parent = i + lowbit(i);
		if (j <= n) tree[j] += tree[i];
	}
}
```

令函数`query(x)`表示查询区间`[1, x]`的前缀和，则想查询区间`[l, r]`的区间和，则`query(r) - query(l - 1)`

```c++
int query(int x)
{
    int res = 0;
    while (x) {
        res += tree[x];
        x -= lowbit(x);
    }
}
```

单点修改，对于下标为`pos`的增加了`val`，这里就用到了连续反向覆盖性，注意涉及累加的时候要小心溢出。

```c++
void add(int pos, int val)
{
    while (pos <= n) {
        tree[pos] += val;
        pos += lowbit(pos);
    }
}
```





## 单点修改，区间查询

- [ ] LOJ 130
- [x] 洛谷-P3374 【模板】树状数组 1

```c++
// 洛谷-P3374 【模板】树状数组 1
#include <bits/stdc++.h>

using namespace std;

vector<int> tree(5e5 + 5);
int n, m;

inline int lowbit(int x) { return x & (-x); }

void init()
{
	int val;
	for (int i = 1; i <= n; ++i) {
		cin >> val;
		tree[i] += val;
		int j = i + lowbit(i);
		if (j <= n) tree[j] += tree[i];
	}
}


int query(int pos)
{
	int res = 0;
	while (pos) {
		res += tree[pos];
		pos -= lowbit(pos);
	}

	return res;
}

void add(int pos, int val)
{
	while (pos <= n) {
		tree[pos] += val;
		pos += lowbit(pos);
	}
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	init();

	int pos, val, l, r;
	int ops;
	while (m--) {
		cin >> ops;
		if (ops & 1) {
			cin >> pos >> val;
			add(pos, val);
		}
		else {
			cin >> l >> r;
			cout << (query(r) - query(l - 1)) << endl;
		}
	}

	return 0;
}
```





### 二维形式

- [ ] loj 133



## 单点修改，单点查询

- [ ] loj 131



### 二维形式

- [ ] loj 134



## 区间修改，区间查询

- [ ] loj 132



### 二维形式

- [ ] loj 135 





## 第`k`大问题



## 逆序对问题

- [x] 洛谷-P1908 逆序对
- [x] LeetCode 493.Reverse Pairs
- [x] 牛客-1032A 楼兰图腾（逆序对变形）



```c++
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 5e5 + 5;
int n, len;
vector<int> seq(MAXN), help(MAXN), tree(MAXN);

int getID(int target)
{
	return lower_bound(help.begin(), help.begin() + len, target) - help.begin() + 1;
}


void discrete()
{
	sort(help.begin(), help.begin() + n);
	len = unique(help.begin(), help.begin() + n) - help.begin();
}

inline int lowbit(int x) { return x & (-x); }

void add(int pos, int val)
{
	while (pos <= len) {
		tree[pos] += val;
		pos += lowbit(pos);
	}
}

long long query(int pos)
{
	long long res = 0;
	while (pos) {
		res += tree[pos];
		pos -= lowbit(pos);
	}

	return res;
}

long long inversionPairNum()
{
	long long res = 0;
	for (int i = n - 1; i >= 0; --i) {
		int id = getID(seq[i]);
		res += query(id - 1);
		add(id, 1); 
	}

	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> seq[i];
		help[i] = seq[i];
	}

	discrete();

	cout << inversionPairNum() << endl;

	return 0;
}
```





## 典型题目

POJ 2182	3378 	

HDU 1556	1394 	2838 	3450

POJ 3067

HDU3743    1166

UVA 1428

POJ 2352

POJ 2299

<https://blog.csdn.net/u013480600/article/category/2094525>










