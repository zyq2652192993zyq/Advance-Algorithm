> # 洛谷-P4779 [模板] 单源最短路径（标准版）(Dijkstra算法)

## 题目背景

2018 年 7 月 19 日，某位同学在 [NOI Day 1 T1 归程](https://www.luogu.org/problemnew/show/P4768) 一题里非常熟练地使用了一个广为人知的算法求最短路。

然后呢？
$$
100 \rightarrow 60\\
\text{Ag} \rightarrow \text{Cu}\\
$$
最终，他因此没能与理想的大学达成契约。

小 F 衷心祝愿大家不再重蹈覆辙。

## 题目描述

给定一个 nn 个点，mm 条有向边的带非负权图，请你计算从 ss 出发，到每个点的距离。

数据保证你能从 ss 出发到任意点。

## 输入格式

第一行为三个正整数 n, m, sn,m,s。 第二行起 mm 行，每行三个非负整数 u_i, v_i, w_iui,vi,wi，表示从 u_iui 到 v_ivi 有一条权值为 w_iwi 的有向边。

## 输出格式

输出一行 nn 个空格分隔的非负整数，表示 ss 到每个点的距离。

## 输入输出样例

**输入 #1**

```
4 6 1
1 2 2
2 3 2
2 4 1
1 3 5
3 4 3
1 4 4
```

**输出 #1**

```
0 2 4 3
```

## 说明/提示

样例解释请参考 [数据随机的模板题](https://www.luogu.org/problemnew/show/P3371)。

1 \leq n \leq 10^51≤n≤105；

1 \leq m \leq 2\times 10^51≤m≤2×105；

s = 1s=1；

1 \leq u_i, v_i\leq n1≤ui,vi≤n；

0 \leq w_i \leq 10 ^ 90≤wi≤109,

0 \leq \sum w_i \leq 10 ^ 90≤∑wi≤109。

本题数据可能会持续更新，但不会重测，望周知。

2018.09.04 数据更新 from @zzq

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0X0ffffff;

struct edge
{
	int to, cost;
	edge(int toValue, int costValue) : to(toValue), cost(costValue) {}
};

using P = pair<int, int>; //first是最短距离，second是顶点编号

int vertexNum = 100005, edgeNum = 200005;
vector<int> d(vertexNum, INT_MAX); //最短距离
vector<vector<edge>> adj(vertexNum, vector<edge>()); //边的邻接表表示法

void Dijkstra(int s)
{
	priority_queue<P, vector<P>, greater<P>> pq;
	d[s] = 0;
	pq.push(P(0, s));

	while (!pq.empty()) {
		auto p = pq.top(); pq.pop();
		int v = p.second;
		if (d[v] < p.first) continue;

		for (size_t i = 0; i < adj[v].size(); ++i) {
			edge e = adj[v][i];
			if (d[e.to] > d[v] + e.cost) {
				d[e.to] = d[v] + e.cost;
				pq.push(P(d[e.to], e.to));
			}
		}
	}
}

ostream & operator<<(ostream & os, vector<int> & d)
{
	for (int i = 1; i <= vertexNum; ++i)
		os << d[i] << " ";
	os << endl;

	return os;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
	int s;
	cin >> vertexNum >> edgeNum >> s;
	for (int i = 1; i <= edgeNum; ++i) {
		int from, to, cost;
		cin >> from	>> to >> cost;
		adj[from].push_back(edge(to, cost));
	}
	Dijkstra(s);
	cout << d;

    return 0;
}
```

和Bellman-Ford算法一样，都要求图中不能出现负环，考虑Bellman-Ford算法，每一次循环都要检查所有的边，如果有些点的最短距离已经可以确定，那么下一次就可以不用再检测了。

使用优先级队列进行优化以后，时间复杂度为$O|edgeNum|\times log|vertexNum|$。因为SPFA的最坏情况时间复杂度可以是$O(|vertexNum| \times |edgeNum|)$，是可能构造数据卡掉的，所以最保险的是选用Dijkstra算法。

这道题目用Bellman-Ford或SPFA都会超时。