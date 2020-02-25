# 图算法——最短路--SPFA算法

SPFA算法是Shortest Path Faster Algorithm的缩写。是在Bellman-Ford算法基础进行的优化改进，可以用来检测负环。

# SPFA算法解决单源最短路问题

典型问题：

- [x]  P3371 [模板] 单源最短路径（弱化版）

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

int vertexNum = 10005, edgeNum = 500005;
vector<int> d(vertexNum, INT_MAX); //最短距离
vector<vector<pair<int, int>>> adj(vertexNum, vector<pair<int, int>>()); //边的邻接表表示法
//vector<int> countNum(vertexNum);
vector<bool> inQueue(vertexNum, false);

void SPFA(int s)
{
	d[s] = 0;
	queue<int> q;
	q.push(s);
	inQueue[s] = true;
	while (!q.empty()) {
		int tmp = q.front(); q.pop();
		inQueue[tmp] = false;

		//遍历以tmp为起点的边
		for (auto edge : adj[tmp]) {
			int to = edge.first; //tmp为起点的边的终点
			int len = edge.second; //边的权值
			if (d[tmp] + len < d[to]) {
				d[to] = d[tmp] + len;
				if (!inQueue[to]) {
					q.push(to);
					inQueue[to] = true;
					// ++countNum[to];
					// if (countNum[to] > vertexNum) return true;
				}
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
		adj[from].push_back(make_pair(to, cost));
	}
	SPFA(s);
	cout << d;

    return 0;
}
```

正如题目里写的，如果数据和时间卡的比较严格，可能会存在TLE，SPFA更是可能，尤其是面对P4779时候。

# SPFA算法找负环

```c++
//洛谷 P3385 【模板】负环
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

int vertexNum = 2005, edgeNum = 3005;
vector<int> d(vertexNum, INT_MAX); //最短距离
vector<vector<pair<int, int>>> adj(vertexNum, vector<pair<int, int>>()); //边的邻接表表示法
vector<int> countNum(vertexNum);
vector<bool> inQueue(vertexNum, false);

bool findNegativeCircle(int s)
{
	fill(d.begin(), d.end(), INT_MAX);
	fill(countNum.begin(), countNum.end(), 0);
	fill(inQueue.begin(), inQueue.end(), false);

	d[s] = 0;
	queue<int> q;
	q.push(s);
	inQueue[s] = true;
	while (!q.empty()) {
		int tmp = q.front(); q.pop();
		inQueue[tmp] = false;

		//遍历以tmp为起点的边
		for (auto edge : adj[tmp]) {
			int to = edge.first; //tmp为起点的边的终点
			int len = edge.second; //边的权值
			if (d[tmp] + len < d[to]) {
				d[to] = d[tmp] + len;
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

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		cin >> vertexNum >> edgeNum;
		for (int i = 1; i <= edgeNum; ++i) {
			int from, to, cost;
			cin >> from	>> to >> cost;
			adj[from].push_back(make_pair(to, cost));
			if (cost >= 0) {
				++edgeNum;
				++i;
				adj[to].push_back(make_pair(from, cost));
			}
		}
		if (findNegativeCircle(1)) cout << "YE5" << endl;
		else cout << "N0" << endl;

		for (size_t i = 0; i < adj.size(); ++i)
			adj[i].clear();
	}

    return 0;
}
```

