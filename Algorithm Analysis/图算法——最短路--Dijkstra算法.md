> # 图算法——最短路之单源最短路Dijkstra算法

和Bellman-Ford算法一样，解决的是单源最短路问题，并且都要求图中不能出现负环，考虑Bellman-Ford算法，每一次循环都要检查所有的边，如果有些点的最短距离已经可以确定，那么下一次就可以不用再检测了。

使用优先级队列进行优化以后，时间复杂度为$O|edgeNum|\times log|vertexNum|$。因为SPFA的最坏情况时间复杂度可以是$O(|vertexNum| \times |edgeNum|)$，是可能构造数据卡掉的，所以最保险的是选用Dijkstra算法。

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

# 典型题目

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