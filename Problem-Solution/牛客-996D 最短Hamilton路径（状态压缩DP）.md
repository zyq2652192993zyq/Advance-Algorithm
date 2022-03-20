> # 牛客-996D 最短Hamilton路径（状态压缩DP）

链接：https://ac.nowcoder.com/acm/contest/996/D

## 题目描述

给定一张 $n(n \leq 20)$ 个点的带权无向图，点从$0 \sim n-1$标号，求起点 0 到终点 n-1 的最短Hamilton路径。 Hamilton路径的定义是从 0 到 n-1 不重不漏地经过每个点恰好一次。

## 输入描述:

第一行一个整数n。
接下来n行每行n个整数，其中第i行第j个整数表示点i到j的距离（一个不超过$10^7$的正整数，记为a[i,j]）。
对于任意的x,y,z，数据保证 a[x,x]=0，a[x,y]=a[y,x] 并且a[x,y]+a[y,z]≥a[x,z]。

## 输出描述:

```
一个整数，表示最短Hamilton路径的长度。
```

## 示例1

### 输入

```
4
0 2 1 3
2 0 2 1
1 2 0 1
3 1 1 0
```

### 输出

```
4
```

------

分析：用`d[s][i]`表示已经访问过的点的状态，目前刚好处于点`i`，最后到达`n - 1`的最短路径。状态转移方程：刚好处于点`i`的意思就是在上一个状态点`i`还没有被访问，假设处于点`j`，在上一时刻点`j`已经被访问了，恰好从点`j`转移到点`i`。

为了方便的表示一个点是否被访问，选择用位运算来表示集合状态。

```
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

