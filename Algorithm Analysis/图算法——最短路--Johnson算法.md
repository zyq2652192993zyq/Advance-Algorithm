> # 图算法——最短路--Johnson算法

## Johnson求全源最短路

Johnson算法解决的是全源最短路问题，相比于Floyed算法的$O(n^3)$的时间复杂度，Johnson算法的时间复杂度为$O(nm\log{n} + mn)$（源自《算法导论》，其中$O(mn)$是用Bellman-Ford预处理的时间），算法既可以完成全源最短路的求解，还可以完成负环的检测。

总体思路是因为Dijkstra算法无法解决存在负权的问题，所以Johnson算法的目的是在保证正确的前提下，让边的权重为非负，然后以每个点作为源点用Dijkstra计算单源最短路，这样核心计算部分效率明显提高。

**例题**

给定一个包含 n 个结点和 m 条带权边的有向图，求所有点对间的最短路径长度，一条路径的长度定义为这条路径上所有边的权值和。

注意：

1. 边权**可能**为负，且图中**可能**存在重边和自环；
2. 部分数据卡 n 轮 SPFA 算法。

**输入格式**

第 1 行：2 个整数 n,m，表示给定有向图的结点数量和有向边数量。

接下来 m行：每行 33 个整数 u,v,w，表示有一条权值为 w 的有向边从编号为 u的结点连向编号为 v 的结点。

**输出格式**

若图中存在负环，输出仅一行 −1。

若图中不存在负环：

输出 n 行：令 $dis_{i,j}$ 为从 i 到 j的最短路，在第 i 行输出 $\sum\limits_{j=1}^n j\times dis_{i,j}$，注意这个结果可能超过 int 存储范围。

如果不存在从 i 到 j的路径，则 $dis_{i,j}=10^9$；如果 i=j，则$ dis_{i,j}=0$。

----


对于洛谷的P5905，基本上涵盖了SPFA和Dijkstra算法的全部内容，是个很好的练习。思路是先用SPFA判断是否存在负环，然后进行`n`轮的Dijkstra算法。理论上Dijkstra并不需要像SPFA一样用一个数组去记录某些点是否在优先级队列里面，但是对比后如果不用数组记录，会有两个测试用例超时。此题还是练习链式前向星的好机会。

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



## 典型题目

- [x] 洛谷-P5905 【模板】Johnson 全源最短路

