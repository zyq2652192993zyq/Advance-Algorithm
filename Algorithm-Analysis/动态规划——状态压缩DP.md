> # 动态规划-状态压缩DP

参考资料：

* <https://www.cnblogs.com/Tony-Double-Sky/p/9283254.html>
* <https://blog.csdn.net/u013480600/article/category/1916309>
* https://www.bilibili.com/video/BV1MV411d7Fz
* https://www.bilibili.com/video/BV1Z4411x7Kw
* https://blog.csdn.net/u011815404/category_7955244.html
* 《挑战程序设计竞赛》3.4 熟练掌握动态规划
* 《算法竞赛进阶指南》0x56 状态压缩DP
* 《算法竞赛入门经典》9.5 集合上的动态规划
* 《训练指南》P384 轮廓线动态规划
* [《从零开始学算法——状压DP》](http://alg.muyids.com/chapter/dp/%E7%8A%B6%E6%80%81%E5%8E%8B%E7%BC%A9dp.html)

将集合转化为整数记录在DP状态中的算法称为**状态压缩DP**。另外经常听到一种**轮廓线DP**，它是状态压缩DP的一种，应用的典型特征是棋盘类型的问题，棋盘的行数和列数比较少。状压DP经常会联系到知识点P和NP。

## 例题

### 旅行商问题

> 也是《算法竞赛进阶指南》里0x01里面二进制状态压缩的例题，两者的区别是进阶指南的是无向图并且是从0到n-1，挑战程序设计竞赛是有向图，要求从0出发，最后回到0。
>

- [x] 牛客-996D 最短Hamilton路径

给定一张 $n(n \leq 20)$ 个点的带权无向图，点从$0 \sim n-1$标号，求起点 0 到终点 n-1 的最短Hamilton路径。 Hamilton路径的定义是从 0 到 n-1 不重不漏地经过每个点恰好一次。

分析：用`d[s][i]`表示已经访问过的点的状态，目前刚好处于点`i`，最后到达`n - 1`的最短路径。状态转移方程：刚好处于点`i`的意思就是在上一个状态点`i`还没有被访问，假设处于点`j`，在上一时刻点`j`已经被访问了，恰好从点`j`转移到点`i`。

为了方便的表示一个点是否被访问，选择用位运算来表示集合状态。

```c++
#include <bits/stdc++.h>

using namespace std;

const int INF = 0x3f;

//vector<vector<int> > dis(20, vector<int>(20)), d(1 << 20, vector<int>(20, INF));
int n;
int dis[20][20], d[1 << 20][20];

int solve()
{
	memset(d, 0x3f, sizeof(d));
	d[1][0] = 0;

	for (int s = 1; s < 1 << n; ++s) {
		for (int i = 0; i < n; ++i) {
			if (s >> i & 1) { //点i刚好被访问
				for (int j = 0; j < n; ++j) {
					//点j已经被访问
					if ((s ^ 1 << i) >> j & 1) {
						d[s][i] = min(d[s][i], d[s ^ 1 << i][j] + dis[i][j]);
					}
				}
			}
		}
	}

	return d[(1 << n) - 1][n - 1];
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> dis[i][j];
		}
	}

	cout << solve() << endl;

	return 0;
}
```



### 铺砖问题

- [x] POJ 2411 Mondriaan's Dream 

这种题目很容易联想到使用分治方法的棋盘覆盖问题，注意问题背景以及核心解决思路。

题目：假设有一个`m`行`n`列的矩形，现在要用长为2，宽为1的小矩形去密铺这个大矩形，问总共可以有多少种方法？

分析：这个其实一般归类为轮廓线DP，也算是状压DP的一种，如果是采取暴力搜索的方法（DFS + 回溯），那么时间复杂度是$O(mn2^{mn})$，肯定会超时，这里的解决方案是我们对每一行的状态用一个整数来表示，接下来的问题就是每个状态表示的含义，以及上一行的状态如何传递到下一行。对于每一行用一个`n`位二进制的数字表示，但是把他转成十进制整数来表示，便于处理。用`d[i][j]`表示第`i`行的状态为`j`，每行的状态`j`的二进制某一位为1表示此处是小矩形竖着放的上半部分，**0表示其他状态**，我们最后求解的目标是`d[m][0]`，最后一行肯定不能竖着放，所以必须所有位都是0。上一行的状态传递给下一行，假设`i-1`行的状态是`k`，第`i`行的状态是`j`，则需要：

* `(k & j) == 0`，这个表示如果`i-1`行的状态是`k`，其二进制位的某一位是1，对应下一行的二进制位必须是0，表示什么都不放。
* `k | j`的二进制中连续0的个数不能是奇数。`k | j`的二进制某一位是0，表明`k`的二进制对应的位是0，`j`的二进制位也是0，如果是奇数，那么无论上一行放还是不放，第`i`行都没办法补全（横着放）。

所以需要先预处理出究竟出`k | j`的结果，注意，不能一开始就按最大位来预处理出一个结果，因为每次输入一个`m, n`都需要针对对应的`n`位来处理。

```c++
#include <bits/stdc++.h>

using namespace std;

const int N = 1 << 11;

int m, n;
vector<vector<long long> > d(12, vector<long long>(N));
vector<bool> isLegal(N);


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> n >> m) {
		if (!n && !m) break;

		for (int i = 0; i < 1 << m; ++i) {
			int cnt = 0, hasOdd = 0;
			for (int j = 0; j < m; ++j) {
				if (i >> j & 1) hasOdd |= cnt, cnt = 0;
				else cnt ^= 1;
			}
			isLegal[i] = (hasOdd | cnt) ? false : true;
		}

		d[0][0] = 1;
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j < 1 << m; ++j) {
				d[i][j] = 0;
				for (int k = 0; k < 1 << m; ++k) {
					if ((j & k) == 0 && isLegal[j | k]) d[i][j] += d[i - 1][k];
				}
			}
		}

		cout << d[n][0] << endl;
	}

	return 0;
}
```







## 典型题目

洛谷 P2622，P1879，P1896，P2704

- [ ] LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts
- [x] 牛客-996D 最短Hamilton路径
- [x] POJ 2411 Mondriaan's Dream 
- [x] LeetCode 698 划分为K个相等的子集

