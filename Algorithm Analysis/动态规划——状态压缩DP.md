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

将集合转化为整数记录在DP状态中的算法称为**状态压缩DP**。

## 旅行商问题

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









典型题目：

洛谷 P2622，P1879，P1896，P2704

- [ ] LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts
- [x] 牛客-996D 最短Hamilton路径