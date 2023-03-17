> # HDU-1599 find the mincost route（Floyed最小环）

## Description

杭州有N个景区，景区之间有一些双向的路来连接，现在8600想找一条旅游路线，这个路线从A点出发并且最后回到A点，假设经过的路线为V1,V2,....VK,V1,那么必须满足K>2,就是说至除了出发点以外至少要经过2个其他不同的景区，而且不能重复经过同一个景区。现在8600需要你帮他找一条这样的路线，并且花费越少越好。

## Input

第一行是2个整数N和M（N <= 100, M <= 1000)，代表景区的个数和道路的条数。
接下来的M行里，每行包括3个整数a,b,c.代表a和b之间有一条通路，并且需要花费c元(c <= 100)。

## Output

对于每个测试实例，如果能找到这样一条路线的话，输出花费的最小值。如果找不到的话，输出"It's impossible.".

## Sample Input

```
3 3
1 2 1
2 3 1
1 3 1
3 3
1 2 1
1 2 3
2 3 1
```

## Sample Output

```
3
It's impossible.
```

-----

需要注意的点在于初始化的部分，点`i`到自身的距离以及权重必须是0，另外可能存在重边，也就是两个点之间可能存在不止一条边，肯定要选择权重最小的，不然会`WA`。

```c++
#include <bits/stdc++.h>

using namespace std;


int vertexNum, edgeNum;
vector<vector<long long>> d(105, vector<long long>(105, INT_MAX)), g(105, vector<long long>(105, INT_MAX));


void init()
{
	int len = d.size();
	for (int i = 0; i < len; ++i) {
		fill(d[i].begin(), d[i].end(), INT_MAX);
		fill(g[i].begin(), g[i].end(), INT_MAX);
	}
}


void Floyed()
{
	for (int i = 1; i <= vertexNum; ++i) d[i][i] = g[i][i] = 0;

	long long res = INT_MAX;
	for (int k = 1; k <= vertexNum; ++k) {
		for (int i = 1; i < k; ++i) {
			for (int j = i + 1; j < k; ++j) {
				res = min(res, d[i][j] + g[i][k] + g[k][j]);
			}
		}

		for (int i = 1; i <= vertexNum; ++i) {
			for (int j = 1; j <= vertexNum; ++j) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}

	if (res == INT_MAX) cout << "It's impossible." << endl;
	else cout << res << endl;
}



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> vertexNum >> edgeNum) {
		int from, to, cost;
		for (int i = 0; i < edgeNum; ++i) {
			cin >> from >> to >> cost;
			d[from][to] = d[to][from] = g[from][to] = g[to][from] = min((long long)cost, d[from][to]);
		}

		Floyed();
		init();
	}

	return 0;
}
```

