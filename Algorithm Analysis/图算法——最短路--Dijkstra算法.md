> # 图算法——最短路之单源最短路Dijkstra算法

## Dijkstra求单源最短路

和Bellman-Ford算法一样，解决的是单源最短路问题，并且都要求图中不能出现负环，考虑Bellman-Ford算法，每一次循环都要检查所有的边，如果有些点的最短距离已经可以确定，那么下一次就可以不用再检测了。

使用优先级队列进行优化以后，时间复杂度为$O|edgeNum|\times log|vertexNum|$。因为SPFA的最坏情况时间复杂度可以是$O(|vertexNum| \times |edgeNum|)$，是可能构造数据卡掉的，所以最保险的是选用Dijkstra算法。

算法的思想是对于从起始点到终点的最短路，假设经过中间点，那么中间点一定比终点提前确定下来，于是类似于BFS的思路，每次从已经确定当前是最短路上的中间点开始，遍历所有与其相连的点，并查看这些点是否会被更新，如果发生了更新，那么被更新的点进入到优先级队列里，**在没有负环的情况下**，肯定可以保证循环的结束，并且终点会在最后一轮被更新。堆需要是小根堆。

在使用Dijkstra算法的时候，需要事先计算一下时间复杂度，因为稠密图，比如LeetCode 1345,用Dijkstra就需要仔细考虑，不能暴力建图。

核心算法代码：

```c++
priority_queue<P, vector<P>, greater<P>> pq;
d[s] = 0;
pq.push(P(0, s));

while (!pq.empty()) {
    auto p = pq.top(); pq.pop();
    int v = p.second;

    for (size_t i = 0; i < adj[v].size(); ++i) {
        edge e = adj[v][i];
        if (d[e.to] > d[v] + e.cost) {
            d[e.to] = d[v] + e.cost;
            pq.push(P(d[e.to], e.to));
        }
    }
}
```



典型题目：

- [x] P4779 [模板] 单源最短路径（标准版）

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

## Dijkstra求全源最短路

实际上就是以每个点为源点，都做一次单源最短路的计算，时间复杂度为$O(mn\log{n})$。

## 典型题目

- [ ] POJ 3037 skiing
- [ ] HDU 3499 Flight
- [ ] HDU 1548 A Strange Lift
- [ ] HDU 3986
- [ ] poj 1062
- [ ] hdu 2680
- [ ] POJ 1502
- [ ] POJ 2387
- [ ] HDU 2544
- [ ] HDU 2112
- [ ] HDU 1595
- [ ] HDU 1874
- [ ] HDU 3790
- [ ] HDU 1535
- [ ] HDU 1546
- [ ] POJ 3268
- [ ] POJ 3013
- [ ] HDU 4849
- [ ] HDU 1596
- [ ] HDU 2066
- [ ] HDU 2962
- [x] 一本通-1344：【例4-4】最小花费（Dijkstra单源最短路）
- [x] 一本通-1345：【例4-6】香甜的黄油（Dijkstra单源最短路）
- [x] 一本通-1376：信使(msner)（Dijkstra单源最短路）