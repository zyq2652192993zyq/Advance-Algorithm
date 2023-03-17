> # 一本通-1345：【例4-6】香甜的黄油（Dijkstra单源最短路）

# 【题目描述】

农夫John发现做出全威斯康辛州最甜的黄油的方法：糖。把糖放在一片牧场上，他知道N（1≤N≤500）只奶牛会过来舔它，这样就能做出能卖好价钱的超甜黄油。当然，他将付出额外的费用在奶牛上。

农夫John很狡猾。像以前的巴甫洛夫，他知道他可以训练这些奶牛，让它们在听到铃声时去一个特定的牧场。他打算将糖放在那里然后下午发出铃声，以至他可以在晚上挤奶。

农夫John知道每只奶牛都在各自喜欢的牧场（一个牧场不一定只有一头牛）。给出各头牛在的牧场和牧场间的路线，找出使所有牛到达的路程和最短的牧场（他将把糖放在那）。

# 【输入】

第一行: 三个数：奶牛数N，牧场数P（2≤P≤800），牧场间道路数C(1≤C≤1450)。

第二行到第N+1行: 1到N头奶牛所在的牧场号。

第N+2行到第N+C+1行：每行有三个数：相连的牧场A、B，两牧场间距（1≤D≤255），当然，连接是双向的。

# 【输出】

一行 输出奶牛必须行走的最小的距离和。

# 【输入样例】

**3 4 5
2
3
4
1 2 1
1 3 5
2 3 7
2 4 3
3 4 5**

# 【输出样例】

**8**

-----

总体思路是，依次将糖放在各个牧场，用Dijkstra计算从糖放的牧场到其他牧场的最短路，然后计算从糖到牛所在牧场的距离的总和，选取总和中最小的作为结果。另一种想法是使用全源最短路Floyed算法，但是Floyed算法的时间复杂度为$O(n^3)$，这里的`n`是牧场数，会超时。使用Dijkstra算法，时间复杂度是$O(P \times C \times \log{P})$，为$10^6$级别。

```c++
#include <bits/stdc++.h>

using namespace std;


struct Node
{
	int to, cost;

	Node(int t, int c) : to(t), cost(c) {}

	bool operator<(const Node & obj) const
	{
		return cost > obj.cost;
	}
};

int vertexNum, edgeNum, cowNum;
vector<int> cowPostion(505);
vector<vector<Node> > grid(805);
vector<int> d(805, INT_MAX);


inline void init()
{
	fill(d.begin(), d.begin() + vertexNum + 5, INT_MAX);
}


void Dijkstra(int start)
{
	init();

	d[start] = 0;
	priority_queue<Node> pq;
	pq.push(Node(start, 0));

	while (!pq.empty()) {
		Node tmp = pq.top(); pq.pop();

		int from = tmp.to;
		int len = grid[from].size();
		for (int i = 0; i < len; ++i) {
			Node & ele = grid[from][i];
			if (d[ele.to] > d[from] + ele.cost) {
				d[ele.to] = d[from] + ele.cost;
				pq.push(Node(ele.to, d[ele.to]));
			}
		}
	}
}


int calculate()
{
	int sum = 0;
	for (int i = 1; i <= cowNum; ++i) {
		sum += d[cowPostion[i]];
	}

	return sum;
}


int solve()
{
	int res = INT_MAX;
	for (int i = 1; i <= vertexNum; ++i) {
		Dijkstra(i);
		res = min(res, calculate());
	}

	return res;
}



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> cowNum >> vertexNum >> edgeNum;
	for (int i = 1; i <= cowNum; ++i) {
		cin >> cowPostion[i];
	}

	int from, to, cost;
	for (int i = 0; i < edgeNum; ++i) {
		cin >> from >> to >> cost;
		grid[from].push_back(Node(to, cost));
		grid[to].push_back(Node(from, cost));
	}

	cout << solve() << endl;

	return 0;
}
```

