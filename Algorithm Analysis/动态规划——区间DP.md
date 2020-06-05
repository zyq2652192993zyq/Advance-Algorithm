> # 动态规划——区间动态规划

区间DP相较于线性DP，需要两个坐标（区间左端点、区间右端点）来描述每个维度，区间DP还是树型DP的基础，并且对记忆化搜索的理解很有帮助。

参考资料：https://blog.csdn.net/u011815404/category_7813197.html

# 石子合并

石子合并并不意味着最终题目会以石子作为背景，类似于背包问题，石子作为一种典型的代表，其实石子这个模型可以被项链、水果、矩阵等代替。

## 无顺序的情况

有N堆石子，现要将石子有序的合并成一堆，规定如下：每次只能移动**任意**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

- [x] 洛谷-P6033 合并果子 加强版（基数排序 + 单调队列）
- [x] 一本通-1369：合并果子(fruit)

数据量小的时候可以用优先级队列选出最小（大）的两个，相当于去构建一棵Huffman树；数据量很大的时候，需要挖掘隐含单调信息，用队列来进行优化，不可避免的要进行排序，这时候最保险通用的就是基数排序，然后利用单调队列求解即可。

## 线性排列的情况

- [x] 洛谷-P5569 [SDOI2008]石子合并（线性排列的石子合并，大数据）
- [ ] POJ-1738 An old Stone Game（楼天城男人八题之一）（https://www.cnblogs.com/acgoto/p/9642578.html）
- [x]  UVa-348 Optimal Array Multiplication Sequence(线性石子合并，路径输出)
- [x] 一本通-1274：【例9.18】合并石子（小数据）

### 朴素区间DP

有N堆石子直线排列，现要将石子有序的合并成一堆，规定如下：每次只能移动**相邻**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

设$d[i][j]$表示将区间`[i,j]`内的石子进行合并的最小代价，状态转移方程：
$$
d[i][j] = \min_{i \leq k < j} (d[i][k] + d[k + 1][j]) + \sum_{n = i}^{j} A_n
$$
通过状态转移方程可知，需要计算连续区间段的和，那么就需要计算前缀和。

初始化，当`i == j`的时候，就是单独的石子，并不需要合并，所以`d[i][i] = 0`，其余初始化为正无穷，求解的目标值是`d[1][n]`。

```c++
int solve()
{
    for (int i = 1; i <= n; ++i) d[i][i] = 0;
    for (int i = 1; i <= n; ++i) preSum[i] = preSum[i - 1] + seq[i - 1];

    for (int len = 2; len <= n; ++len) { //根据长度划分阶段
        for (int i = 1; i <= n - len + 1; ++i) { //左端点
            int j = i + len - 1; //右端点
            for (int k = i; k < j; ++k) d[i][j] = min(d[i][j], d[i][k] + d[k + 1][j]);
            d[i][j] += preSum[j] - preSum[i - 1];
        }
    }

    return d[1][n];
}
```

未经优化的情况下，时间复杂度是$O(n^3)$，空间复杂度是$O(n^2)$。

### 四边形不等式

**时间优化**

时间复杂度$O(n^3)$，比如洛谷-P5569，三次方的算法肯定会TLE的，所以需要进行优化。四边形不等式进行优化，时间复杂度优化到$O(n^2)$。主要参考了《算法竞赛进阶指南》中的证明。

**四边形不等式定义**：设$w(i, j)$是整数集合上的二元函数，对于定义域上任意整数$a \leq b \leq c \leq d$，都有
$$
w(a, d) + w(b, c) \geq w(a,c) + w(b, d)
$$
就认为函数$w(i, j)$满足四边形不等式。

**四边形不等式的等价定义**：如果对于定义域上的任意整数$a, b$，有$a < b$，都有$w(a, b + 1) + w(a + 1, b) \geq w(a, b) + w(a + 1, b + 1)$，那么称函数$w(i, j)$满足四边形不等式。

证明：

条件里是$a < b$，但是希望证明的四边形不等式是$a \leq b$，所以应该先考虑$a == b$ 的情况。当$a = b$，首先其不一定满足等价定义的形式，而是应该看四边形不等式的直接定义，则：
$$
w(a, d) + w(a, c) \geq w(a, c) + w(a, d)
$$
很显然，当$a = b$的时候满足四边形不等式。

对于$a < c$，有$w(a, c + 1) + w(a + 1, c) \geq w(a, c) + w(a+1, c+1)$

对于$a + 1 < c$，有$w(a + 1, c + 1) + w(a + 2, c) \geq w(a + 1, c) + w(a + 2, c + 1)$

上面两式相加：
$$
w(a, c+1)+w(a+2, c)\geq w(a, c) + w(a+2, c+1) \\
当a + 2< c时，有w(a,c+1)+w(a+3, c) \geq w(a, c) + w(a+3,c+1)\\
令a+3 = b\\
\therefore a \leq b \leq c, w(a, c + 1) + w(b, c) \geq w(a, c) + w(b, c + 1)
$$

上面这样构造不等式意味着b取遍`[a,c]`之间的数值，不等式仍然成立。但是上面的还缺少一个数字`d`，其实只需要将`b`视为`a`，然后继续按照`b < d`和`b +1< d, b+2<d`的思路，就可以得到：
$$
\forall a \leq b \leq c \leq d, w(a,d) + w(b, c) \geq w(a, c) + w(b, d)
$$
于是就证明了四边形不等式。

石子合并的问题里，状态转移方程：
$$
d[i][j] = \min_{i \leq k < j} (d[i][k] + d[k + 1][j]) + \sum_{n = i}^{j} A_n
$$
$d[i][i] = w(i,i) = 0$。如果满足下面条件，四边形不等式也成立：

* $w(i, j)$满足四边形不等式
* $\forall a \leq b \leq c \leq d$，有$w(a, d) +\geq w(b, c)$

在石子合并问题里，$w(i, j) = s[j] - s[i - 1]$，代表的是区间和，当$a \leq b \leq c \leq d$时，有：
$$
s[d] - s[a - 1] + s[c] - s[b - 1] \geq s[c] - s[a - 1] + s[d] - s[b - 1]
$$
实际上上式左右相等，所以$w(i, j)$满足四边形不等式，并且$\forall a \leq b \leq c \leq d$，有$w(a, d) +\geq w(b, c)$显然成立。

接下来利用成立的条件证明$d[i][j]$也满足四边形不等式。

当$i + 1 == j$时，有$d[i][j+1]+d[i+1][j]=d[i][i+2]+d[i+1][i+1]=d[i][i+2]$.

设最优决策点为$x$，则$i \leq x < j$，于是分情况讨论：

* 当$x = i + 1$时，

$$
d[i][i+2] = d[i][i+1]+d[i+2][i+2]+w(i, i+2)=w(i, i+1)+w(i, i+2) \\
\geq w(i, i+1)+w(i+1, i+2)=d[i][i+1]+d[i+1][i+2]=d[i][j]+d[i+1][j+1]\\
\therefore d[i][j+1]+d[i+1][j] \geq d[i][j] + d[i+1][j+1]
$$

* 当$x = i$时

$$
d[i][i+2] = d[i][i]+d[i+1][i+2]+w(i,i+2)=w(i+1, i+2)+w(i,i+2) \\
\geq w(i+1,i+2) + w(i, i+1) = d[i+1][i+2]+d[i][i+1]\\
\therefore d[i][j+1]+d[i+1][j] \geq d[i][j] + d[i+1][j+1]
$$

上述不等式证明的意义在于，对于长度为2的区间，都成立四边形不等式的等价形式，进而可知长度为2的区间满足四边形不等式。然后采用数学归纳法，假设长度小于$k-1$的区间满足四边形不等式，然后证明长度为$k$的区间也满足四边形不等式，从而完成证明。

假设$j - i < k$时，$d[i][j]$满足四边形不等式，现在考虑当$j = i + k$时，设$d[i][j+1]$在$x$处取得最优值，$d[i+1][j]$在$y$处取得最优值，不失一般性，现在假设$i+1 \leq x \leq y < j$ ，发现条件左边是$i+1$，那么当$x = i$会怎么样？

假设$x=i$，我们目的是为了证明当区间长度为$k$时成立$d[i][j+1]+d[i+1][j] \geq d[i][j] + d[i+1][j+1]$
$$
d[i][j+1]+d[i+1][j] = d[i][x] + d[x+1][j+1]+w(i, j+1) \\
+d[i+1][y]+d[y+1][j]+w(i+1,j)\\
=d[i][i]+d[i+1][j+1]+w(i, j+1) +d[i+1][j] \\
=d[i+1][j+1]+d[i+1][j]+w(i, j+1)
$$
考虑$d[i][j+1]$，其最优值不一定是在$x = i$处取到，所以$d[i][j+1] \leq d[i][i] + d[i+1][j+1]$，所以当$x=i$时，四边形不等式的等价形式依然成立。

然后考虑$i+1 \leq x \leq y < j$ 
$$
d[i][j+1] + d[i+1][j] = d[i][x] + d[x+1][j+1] + w(i, j+1) \\
+ d[i+1][y]+ d[y+1][j] + w(i+1, j) 
$$
但是对于$d[i][j], d[i+1][j+1]$，$x, y$并不一定是最优决策点，所以：
$$
d[i][j]+d[i+1][j+1] \leq d[i][x] + d[x+1][j] + w(i, j) \\
+d[i+1][y] + d[y+1][j+1] + w(i+1, j+1)
$$
根据条件一知$w(i, j)$满足四边形不等式，于是$w(i, j+1) + w(i+1,j) \geq w(i, j) + w(i+1, j+1)$

另外知道$i+2 \leq x+1 \leq y + 1 \leq j \leq j+1$，在长度为$k-1$的区间内，根据归纳假设，满足四边形不等式：
$$
d[x+1][j+1] + d[y+1][j] \geq d[x+1][j]+d[y+1][j+1]
$$
所以可知当$i + k = j$时，四边形不等式的等价形式也成立，所以$d[i][j]$满足四边形不等式。

**二维决策单调性**

状态转移返程$d[i][j] = \min_{i \leq k < j} (d[i][k] + d[k + 1][j]) + w(i, j)$，记$P[i,j]$为令$d[i][j]$取到最小值的$k$值，如果$d[i][j]$满足四边形不等式，$\forall i < j$，有$P[i, j-1] \leq P[i,j] \leq P[i+1, j]$。

证明：

* 记$p = P[i, j]$， $\forall i \leq i+1 \leq k \leq p$，因为$d[i]j[]$满足四边形不等式，有

$$
d[i][p] + d[i+1][k] \geq d[i][k] + d[i+1][p] \\
d[i+1][k] - d[i+1][p] \geq d[i][k] - d[i][p]
$$

因为$p$是$d[i][j]$的最优决策点，则$d[i][k] + d[k+1][j] \geq d[i][p] + d[p+1][j]$
$$
(d[i+1][k] + d[k+1][j] + w(i+1, j)) -(d[i+1][p]+d[p+1][j]+w(i+1, j)) \\
= (d[i+1][k]-d[i+1][p]) + (d[k+1][j]-d[p+1][j]) \\
\geq (d[i][k] - d[i][p]) + (d[k+1][j]-d[p+1][j]) \\
= (d[i][k] + d[k+1][j]) - (d[i][p] + d[p+1][j]) 
\geq 0
$$
上述不等式意味着对于$d[i+1][j]$，$p$比任意的$k \leq p$更优，也就意味着$d[i+1][j]$的最优决策点一定大于$p$，从而$P[i,j] \leq P[i+1, j]$。

* $\forall p < k < j$，有$p+1 \leq k+1 \leq j-1 \leq j$， 因为$d[i][j]$满足四边形不等式：

$$
d[p+1][j]+d[k+1][j-1] \geq d[p+1][j-1]+d[k+1][j] \\
d[k+1][j-1] - d[p+1][j-1] \geq d[k+1][j]  - d[p+1][j]
$$

因为$p$是$d[i][j]$的最优决策点，则$d[i][k] + d[k+1][j] \geq d[i][p] + d[p+1][j]$
$$
d[i][k] + d[k+1][j-1] + w(i, j-1) - (d[i][p]+d[p+1][j-1] + w(i, j-1)) \\
= (d[i][k] - d[i][p]) + (d[k+1][j-1] - d[p+1][j-1]) \\
\geq (d[i][k] - d[i][p]) + (d[k+1][j]  - d[p+1][j]) \\
= (d[i][k] + d[k+1][j]) - (d[i][p]+d[p+1][j]) \geq 0
$$
意味着对于$d[i][j-1]$，$p$比任意的$p < k$更优，即$d[i][j-1]$的最优决策点一定比$p$小，所以$P[i][j] \geq P[i][j-1]$.

综上可证明$P[i][j-1] \leq P[i][j] \leq P[i+1][j]$.

根据二维决策单调性的性质，可知我们不再是遍历$i \leq k < j$而是遍历$p[i, j-1] \leq k \leq p[i+1, j]$，大大缩小了遍历的范围，时间复杂度为


$$
O(\sum_{i=1}^{n-1} \sum_{j=i+1}^{n}(P[i+1][j] - P[i][j-1] + 1)) = O(\sum_{i=1}^{n-1}(P[i+1][n]-P[1][n-i] + n - i)) = O(n^2)
$$

于是我们看到，利用四边形不等式将时间复杂度从$o(n^3)$降到了$O(n^2)$，空间复杂度还是$O(n^2)$。


```c++
int solve()
{
    for (int i = 1; i <= n; ++i) { 
        d[i][i] = 0; 
        p[i][i] = i; 
        preSum[i] = preSum[i - 1] + seq[i - 1];
    }

    for (int len = 1; len < n; ++len) { //枚举区间长度
        for (int i = 1; i + len <= n; ++i) { //区间左端点
            int j = i + len; //区间右端点
            for (int k = p[i][j - 1]; k <= p[i + 1][j]; ++k) {
                if (d[i][k] + d[k + 1][j] + preSum[j] - preSum[i - 1] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k + 1][j] + preSum[j] - preSum[i - 1];
                    p[i][j] = k;
                }
            }
        }
    }

    return d[1][n];
}
```

### Garsia-Wachs算法

Garsia-Wachs算法可以将空间复杂度优化到$O(n)$，时间复杂度优化到$O(n \log n)$。该算法深刻的揭示了石子合并的本质是最优树问题，详细的证明在《计算机程序设计艺术》第三卷的6.2.2节里。

这里只写构造方法：

假定数据存储在数组`seq`里，下标从$1$ 到 $n$

1. 找到满足$\text{seq}[i]< \text{seq}[i+2]$的最小下标 $i$
2. 将$\text{seq}[i]$的数据加到$\text{seq}[i+1]$，同时代价`res`加上 $\text{seq}[i+1]$的数据
3. 从列表清除$\text{seq}[i]$的数据
4. 在列表中寻找满足$\text{seq}[j] > \text{seq}[i+1], j \leq i$的最大$j$
5. 将$\text{seq}[0] = +\infty, \text{seq}[n + 1] = +\infty$处理

如果利用数组模拟并利用`insert`和`erase`性能会比较差，我们这里选择用数组模拟列表。

```c++
//洛谷-P5569 [SDOI2008]石子合并
#include <bits/stdc++.h>

using namespace std;

vector<int> seq(40005);
int n;

int stoneMerge()
{
	int start = 1, res = 0;
	int i;
	while (start < n - 1) {
		for (i = start; i < n - 1; ++i) {
			if (seq[i] < seq[i + 2]) {
				seq[i + 1] += seq[i], res += seq[i + 1];
				for (int j = i; j > start; --j) seq[j] = seq[j - 1];
				++start;
				int j = i + 1;
				while (seq[j] > seq[j - 1] && j > start) {
					std::swap(seq[j], seq[j - 1]);
					--j;
				}
				break;
			}
		}
		if (i == n - 1) {
			seq[n - 1] += seq[n];
			res += seq[--n];
		}
	}
	res += seq[n - 1] + seq[n];

	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> seq[i];

	cout << stoneMerge() << endl;

	return 0;
}
```



## 环形排列的情况

- [x] P1880 [NOI1995]石子合并
- [x] 洛谷 1063 能量项链（环形合并）

有N堆石子环形排列，现要将石子有序的合并成一堆，规定如下：每次只能移动**相邻**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

另外环形的情况可以参考《算法竞赛进阶指南》P295“环形与后效性处理”。

环形情况，采用扩展域的方法，也就是在`n`个数据后面再补充`n`个数据，然后枚举每个数字作为开头，长度为`n`的序列，然后就转化成了线性情况的石子合并。求最小值的时候可以用四边形不等式，但是求最大值的时候是不能用四边形不等式。所以即使求最小值时间复杂度优化到$O(n^2)$，但是求最大值还是$O(n^3)$.

```c++
#include <bits/stdc++.h>

using namespace std;

const int INF = 0xffffff;

vector<int> seq(205), preSum(205);
vector<vector<int>> d(205, vector<int>(205, INF)), f(205, vector<int>(205, -INF));
int n;


void stoneMerge()
{
	for (int i = 1; i <= 2 * n; ++i) {
		d[i][i] = 0;
		f[i][i] = 0;
		preSum[i] = preSum[i - 1] + seq[i - 1];
	}

	for (int len = 2; len <= n; ++len) {
		for (int i = 1; i + len - 1 <= 2 * n; ++i) {
			int j = i + len - 1;
			for (int k = i; k < j; ++k) {
				d[i][j] = min(d[i][j], d[i][k] + d[k + 1][j] + preSum[j] - preSum[i - 1]);
				f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + preSum[j] - preSum[i - 1]);
			}
		}
	}

	int minVal = INT_MAX, maxVal = INT_MIN;
	for (int i = 1; i <= n; ++i) {
		minVal = min(minVal, d[i][i + n - 1]);
		maxVal = max(maxVal, f[i][i + n - 1]);
	}

	cout << minVal << endl << maxVal << endl;
}



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> seq[i];
		seq[i + n] = seq[i];
	}

	stoneMerge();

	return 0;
}
```

# 山区建小学

- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624

【题目描述】
政府在某山区修建了一条道路，恰好穿越总共m个村庄的每个村庄一次，没有回路或交叉，任意两个村庄只能通过这条路来往。已知任意两个相邻的村庄之间的距离为di(为正整数)，其中，0<i<m。为了提高山区的文化素质，政府又决定从m个村中选择n个村建小学(设0<n≤m<500)。请根据给定的m、n以及所有相邻村庄的距离，选择在哪些村庄建小学，才使得所有村到最近小学的距离总和最小，计算最小值。

【输入】
第1行为m和n，其间用空格间隔

2行为m−1个整数，依次表示从一端到另一端的相邻村庄的距离，整数之间以空格间隔。

例如:

    10 3

    2 4 6 5 2 4 3 1 3

表示在10个村庄建3所学校。第1个村庄与第2个村庄距离为2，第2个村庄与第3个村庄距离为4，第3个村庄与第4个村庄距离为6，...，第9个村庄到第10个村庄的距离为3。

【输出】
各村庄到最近学校的距离之和的最小值。

【输入样例】
10 2
3 1 3 1 1 1 1 1 3

【输出样例】
18

```c++
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

int school, n;
//dp[i][j]表示前i个村庄建立j个学校的最小和
//m[i][j]表示第i个村庄到第j个村庄只建立一所学校的最小和
vector<vector<int> > d(505, vector<int>(505, INT_MAX / 2)), m(505, vector<int>(505));
vector<int> pos(505); //每个村庄的绝对坐标

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> school;
    for (int i = 2; i <= n; ++i) {
        int dis; cin >> dis;
        pos[i] = pos[i - 1] + dis;
    }

    for (int i = 1; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            m[i][j] = m[i][j - 1] + pos[j] - pos[(i + j) >> 1];
        }
    }

    for (int i = 1; i <= n; ++i) d[i][1] = m[1][i];

    for (int i = 1; i <= n; ++i) {
        for (int j = 2; j <= i && j <= school; ++j) {
            for (int k = j - 1; k < i; ++k) {
                d[i][j] = min(d[i][j], d[k][j - 1] + m[k + 1][i]);
            }
        }
    }
    cout << d[n][school] << endl;

    return 0;
}
```

这道题目注意输入的是各个村庄之间的距离，需要转化一步算出绝对的坐标。

```
//dp[i][j]表示前i个村庄建立j个学校的最小和
//m[i][j]表示第i个村庄到第j个村庄只建立一所学校的最小和
//pos[i]表示第i个村庄的绝对坐标，第一个村庄在位置0
//村庄从1开始计数
```

计算`m[i][j]`：

```c++
m[i][j] = m[i][j - 1] + pos[j] - pos[(i + j) >> 1];
```

考虑三个村庄1，2，3。那么最优选择是建立在2，当多了一个村庄4，其实还是建在2，那么只是多出了4到2的距离。

如果原来是1，2，3，4。最初是建在2和3都一样，一开始肯定建在(1 + 4) / 2的位置，也就是2，现在多了一个村庄5，那么最优选择是建在3，前四个的距离是没有变化的，仍然只是多出了5到3的距离，也就是上面表达式的内容。

状态转移方程是

```c++
d[i][j] = min(d[i][j], d[k][j - 1] + m[k + 1][i]);
```

也就是在前`k`个村庄建立`j-1`个学校，后面的村庄只建立一个学校。

时间复杂度$O(n^2m)$，其中m是学校的数量。



# 括号匹配

- [x] POJ-2955 Brackets （最大括号匹配，区间动态规划）

括号匹配也是很典型的一种区间DP问题，因为括号问题的背景性很强，所以单独拿出来在《典型问题——括号相关的问题》做了总结，括号问题需要区分题目要求的条件是连续子序列还是可以不连续，方法会完全不同。

```c++
//POJ 2955
int maxLen(string & s)
{
	int m = s.size();

	for (int j = 1; j < m; ++j) {
		for (int i = j - 1; i >= 0; --i) {
			if ((s[i] == '(' && s[j] == ')') || (s[i] == '[' && s[j] == ']'))
				d[i][j] = d[i + 1][j - 1] + 2;
			//主要针对()()()类型
			for (int k = i; k <= j; ++k) {
				d[i][j] = max(d[i][j], d[i][k] + d[k + 1][j]);
			}
		}
	}

	return d[0][m - 1];
}
```



# 机器分配

- [x] 一本通-1266：【例9.10】机器分配 或 洛谷-P2066 机器分配

【题目描述】
总公司拥有高效设备M台，准备分给下属的N个分公司。各分公司若获得这些设备，可以为国家提供一定的盈利。问：如何分配这M台设备才能使国家得到的盈利最大？求出最大盈利值。其中M≤15，N≤10。分配原则：每个公司有权获得任意数目的设备，但总台数不超过设备数M.

【输入】
第一行有两个数，第一个数是分公司数N，第二个数是设备台数M；

接下来是一个N*M的矩阵，表明了第 I个公司分配 J台机器的盈利。

【输出】
第一行输出最大盈利值；

接下N行，每行有2个数，即分公司编号和该分公司获得设备台数。

【输入样例】

```
3 3           //3个分公司分3台机器
30 40 50
20 30 50
20 25 30
```

【输出样例】

```
70                                         //最大盈利值为70
1 1                                        //第一分公司分1台
2 1                                        //第二分公司分1台
3 1                                        //第三分公司分1台
```

用`d[i][j]`代表前`i`个公司分得`j`台机器所能获得最大价值，状态转移方程（state transition equation）是：
$$
d[i][j] = \max(d[i - 1][k] + \text{value}[i][j - k]), 0 \leq k \leq j
$$
思路就是前`i-1`个公司分配`k`台机器，最后一个公司分配`j-k`台，取所有价值中的最大值。注意题目条件里数据范围在20，所以$O(n^3)$是可行的。另外路径输出的技巧也很值得学习。

```c++
#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<vector<int> > d(20, vector<int>(20)), 
	value(20, vector<int>(20)), pre(20, vector<int>(20));

void PathPrint(int i, int j, int sum)
{
	if (!i) return; //递归终止条件
	for (int k = 0; k <= j; ++k) {
		if (sum == d[i - 1][k] + value[i][j - k]) {
			PathPrint(i - 1, k, d[i - 1][k]);
			cout << i << ' ' << (j - k) << endl;
			break;
		}
	}
}

void solve()
{
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			for (int k = 0; k <= j; ++k) {
				d[i][j] = max(d[i][j], d[i - 1][k] + value[i][j - k]);
			}
		}
	}
	cout << d[n][m] << endl;
	PathPrint(n, m, d[n][m]);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			cin >> value[i][j];
		}
	}

	solve();

	return 0;
}
```



# 删除回文子数组

- [x] LeetCode 1246.删除回文子数组

Given an integer array `arr`, in one move you can select a palindromic subarray `arr[i], arr[i+1], ..., arr[j]` where `i <= j`, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

**Example 1:**

```
Input: arr = [1,2]
Output: 2
```

**Example 2:**

```
Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
```

**Constraints:**

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= 20`

------

```c++
class Solution {
public:
    int minimumMoves(vector<int>& arr) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int n = arr.size();
        vector<vector<int>> d(n + 1, vector<int>(n + 1, INT_MAX - 1000));
        //每个字母单独删除需要1次
        d[0][0] = 0;
        for (int i = 1; i <= n; ++i) d[i][i] = 1; 
        for (int i = 1; i <= n; ++i) d[i][i - 1] = 0;

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i < n - len + 1; ++i) {
                int j = i + len - 1;
                //第i个字母单独删除
                d[i][j] = 1 + d[i + 1][j];
                if (arr[i] == arr[i + 1]) 
                    d[i][j] = min(d[i][j], 1 + d[i + 2][j]);

                for (int k = i + 2; k <= j; ++k) {
                    if (arr[i] == arr[k])
                        d[i][j] = min(d[i][j], d[i + 1][k - 1] + d[k + 1][j]);
                }
            }
        }

        return d[0][n - 1];
    }
};
```

数组长度小于100，意味着可能存在多重循环。

设$d[i][j]$代表删除区间$[i,j]$的字符的最少操作数。初始$d[i][i] = 1, d[i][i - 1] = 0$。其余为较大数值。

* 删除字符的方式可以单独删除，那么$d[i][j] = \min (d[i][j], 1 + d[i + 1][j])$
* 如果$arr[i] == arr[i + 1]$，意味着构成回文串，可以一起删除：$d[i][j] = \min (d[i][j], 1 + d[i + 2][j])$。
* 另外如果$k \geq i + 2, arr[i] == arr[k]$，那么意味着$arr[i], arr[k]$可以和区间$[i + 1, k - 1]$一起删除，那么$d[i][j] = \min (d[i][j], d[i + 1][k - 1] + d[k + 1][j])$。

注意一下边界条件即可。

另外这道题还是微软的笔试题，可以变化的形式比如改成字符串，方法一样，引起重视。







典型题目：

- [x] Uva 348 Optimal Array Multiplication Sequence 或 ZOJ 1276
- [x] 洛谷 1063 能量项链（环形合并）
- [x] LeetCode 1246.删除回文子数组（字符串回文背景的区间DP）
- [ ] [十个利用矩阵乘法解决的经典题目](http://www.matrix67.com/blog/archives/276)
- [ ] 洛谷 P1880 石子合并（大数据，线性排列情况）
- [ ] 洛谷 P1005 矩阵取数游戏
- [x] POJ 3280 Cheapest Palindrome
- [x] POJ-2955 Brackets （最大括号匹配，区间动态规划）
- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624
- [x] OpenJudge 162:Post Office
- [ ] POJ 1160
- [x] POJ-1651 Multiplication Puzzle（基础区间DP）