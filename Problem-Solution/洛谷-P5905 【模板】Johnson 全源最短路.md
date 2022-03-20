> # 洛谷-P5905 【模板】Johnson 全源最短路

## 题目描述

给定一个包含 n*n* 个结点和 m*m* 条带权边的有向图，求所有点对间的最短路径长度，一条路径的长度定义为这条路径上所有边的权值和。

注意：

1. 边权**可能**为负，且图中**可能**存在重边和自环；
2. 部分数据卡 n*n* 轮 SPFA 算法。

## 输入格式

第 11 行：22 个整数 n,m*n*,*m*，表示给定有向图的结点数量和有向边数量。

接下来 m*m* 行：每行 33 个整数 u,v,w*u*,*v*,*w*，表示有一条权值为 w*w* 的有向边从编号为 u*u* 的结点连向编号为 v*v* 的结点。

## 输出格式

若图中存在负环，输出仅一行 -1−1。

若图中不存在负环：

输出 n*n* 行：令 dis_{i,j}*d**i**s**i*,*j* 为从 i*i* 到 j*j* 的最短路，在第 i*i* 行输出 \sum\limits_{j=1}^n j\times dis_{i,j}*j*=1∑*n**j*×*d**i**s**i*,*j*，注意这个结果可能超过 int 存储范围。

如果不存在从 i*i* 到 j*j* 的路径，则 dis_{i,j}=10^9*d**i**s**i*,*j*=109；如果 i=j*i*=*j*，则 dis_{i,j}=0*d**i**s**i*,*j*=0。

## 输入输出样例

**输入 #1**

```
5 7
1 2 4
1 4 10
2 3 7
4 5 3
4 2 -2
3 4 -3
5 3 4
```

**输出 #1**

```
128
1000000072
999999978
1000000026
1000000014
```

**输入 #2**

```
5 5
1 2 4
3 4 9
3 4 -3
4 5 3
5 3 -2
```

**输出 #2**

```
-1
```

## 说明/提示

【样例解释】

左图为样例 11 给出的有向图，最短路构成的答案矩阵为：

```
0 4 11 8 11 
1000000000 0 7 4 7 
1000000000 -5 0 -3 0 
1000000000 -2 5 0 3 
1000000000 -1 4 1 0 
```

右图为样例 22 给出的有向图，红色标注的边构成了负环，注意给出的图不一定连通。

![img](https://cdn.luogu.com.cn/upload/image_hosting/7lb35u4u.png)

【数据范围】

对于 100\%100% 的数据，1\leq n\leq 3\times 10^3,\ \ 1\leq m\leq 6\times 10^3,\ \ 1\leq u,v\leq n,\ \ -3\times 10^5\leq w\leq 3\times 10^51≤*n*≤3×103, 1≤*m*≤6×103, 1≤*u*,*v*≤*n*, −3×105≤*w*≤3×105。

对于 20\%20% 的数据，1\leq n\leq 1001≤*n*≤100，不存在负环（可用于验证 Floyd 正确性）

对于另外 20\%20% 的数据，w\ge 0*w*≥0（可用于验证 Dijkstra 正确性）

upd. 添加一组 Hack 数据：针对 SPFA 的 SLF 优化

------

思路是先用SPFA判断是否存在负环，然后进行`n`轮的Dijkstra算法。理论上Dijkstra并不需要像SPFA一样用一个数组去记录某些点是否在优先级队列里面，但是对比后如果不用数组记录，会有两个测试用例超时。此题还是练习链式前向星的好机会。时间复杂度是$O(mn \log{n} + mn)$，其中后一项是SPFA预处理的时间。

```c++
#include <bits/stdc++.h>

using namespace std;


struct Edge
{
	int to, cost, next;
};

struct Node
{
	int to, cost;

	Node(int t, int c) : to(t), cost(c) {}

	bool operator<(const Node & obj) const
	{
		return cost > obj.cost;
	}
};


const int MAXVERTEX = 3005;
const int MAXEDGE = 6005;
const long long INF = 1e9;

int vertexNum, edgeNum, cnt = 0;
vector<Edge> es(MAXEDGE + MAXVERTEX);
vector<bool> inQueue(MAXVERTEX);
vector<long long> d(MAXVERTEX, INF), h(MAXVERTEX, INF), head(MAXVERTEX), countNum(MAXVERTEX, 0);
// Edge es[MAXVERTEX + MAXEDGE];
// bool inQueue[MAXVERTEX];
// long long d[MAXVERTEX], h[MAXVERTEX], head[MAXVERTEX], countNum[MAXVERTEX];


void addEdge(int from, int to, int cost)
{
	es[++cnt].to = to;
	es[cnt].cost = cost;
	es[cnt].next = head[from];
	head[from] = cnt;
}


bool findNegativeCircle(int start)
{
	h[start] = 0;
	queue<int> q;
	q.push(start);
	inQueue[start] = true;

	while (!q.empty()) {
		int from = q.front(); q.pop();
		inQueue[from] = false;

		for (int i = head[from]; i; i = es[i].next) {
			int to = es[i].to, cost = es[i].cost;
			if (h[to] > h[from] + cost) {
				h[to] = h[from] + cost;
				if (!inQueue[to]) {
					q.push(to);
					inQueue[to] = true;
					++countNum[to];
					if (countNum[to] > vertexNum) return true;
				}
			}
		}
	}

	return false;
}


long long Dijkstra(int start)
{
	fill(d.begin() + 1, d.begin() + 1 + vertexNum, INF);
	fill(inQueue.begin(), inQueue.end(), false);
	// memset(d, INF, sizeof(d));

	d[start] = 0;
	priority_queue<Node> pq;
	pq.push(Node(start, 0));

	while (!pq.empty()) {
		int from = pq.top().to; pq.pop();
		if (inQueue[from]) continue;
		inQueue[from] = true;
		for (int i = head[from]; i; i = es[i].next) {
			int to = es[i].to;
			if (d[to] > d[from] + es[i].cost) {
				d[to] = d[from] + es[i].cost;
				if (!inQueue[to]) pq.push(Node(to, d[to]));
			}
		}
	}

	long long res = 0;
	for (int i = 1; i <= vertexNum; ++i) {
		if (d[i] == INF) res += i * INF;
		else res += i * (d[i] + h[i] - h[start]);
	}

	return res;
}


void solve()
{
	for (int from = 1; from <= vertexNum; ++from) {
		for (int i = head[from]; i; i = es[i].next) {
			int to = es[i].to;
			es[i].cost += h[from] - h[to];
		}
	}

	for (int i = 1; i <= vertexNum; ++i) {
		cout << Dijkstra(i) << endl;
	}
}



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> vertexNum >> edgeNum;
	int from, to, cost;
	for (int i = 0; i < edgeNum; ++i) {
		cin >> from >> to >> cost;
		addEdge(from, to, cost);
	}

	for (int i = 1; i <= vertexNum; ++i) {
		addEdge(0, i, 0);
	}

	if (findNegativeCircle(0)) cout << (-1) << endl;
	else solve();

	// check SPFA result
	// for (int i = 1; i <= vertexNum; ++i) cout << h[i] << ' ';
	// cout << endl;

	return 0;
}
```

