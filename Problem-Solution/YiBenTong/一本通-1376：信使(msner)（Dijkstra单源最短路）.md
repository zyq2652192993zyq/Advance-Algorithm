> # 一本通-1376：信使(msner)（Dijkstra单源最短路）

# 【题目描述】

战争时期，前线有n个哨所，每个哨所可能会与其他若干个哨所之间有通信联系。信使负责在哨所之间传递信息，当然，这是要花费一定时间的（以天为单位）。指挥部设在第一个哨所。当指挥部下达一个命令后，指挥部就派出若干个信使向与指挥部相连的哨所送信。当一个哨所接到信后，这个哨所内的信使们也以同样的方式向其他哨所送信。直至所有n个哨所全部接到命令后，送信才算成功。因为准备充足，每个哨所内都安排了足够的信使（如果一个哨所与其他k个哨所有通信联系的话，这个哨所内至少会配备k个信使）。

现在总指挥请你编一个程序，计算出完成整个送信过程最短需要多少时间。

# 【输入】

第1行有两个整数n和m，中间用1个空格隔开，分别表示有n个哨所和m条通信线路,且1≤n≤100。

第2至m+1行：每行三个整数i、j、k，中间用1个空格隔开，表示第i个和第j个哨所之间存在通信线路，且这条线路要花费k天。

# 【输出】

一个整数，表示完成整个送信过程的最短时间。如果不是所有的哨所都能收到信，就输出-1。

# 【输入样例】

**4 4
1 2 4
2 3 7
2 4 1
3 4 6**

# 【输出样例】

**11**

-----

解法一：Dijkstra算法

题目很容易误导产生可以使用BFS算法的误区，因为中间过程里，哪个信使先到达，哪个信使后到达会很复杂，实际上最优情况下，让每个哨所得到消息，一定是从出发点经过最短路达到每个哨所，这样完成全部通信的时间最短。所以只需要用Dijkstra算法求出出发点到所有点的最短路，也就是`d[i]`，然后找所有`d[i]`里面的最大值即可。时间复杂度$O(m\log{n})$。

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


int vertexNum, edgeNum;
vector<int> d(105, INT_MAX);
vector<vector<Node> > grid(105);


int Dijkstra(int start)
{
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

	int res = 0;
	for (int i = 1; i <= vertexNum; ++i) res = max(res, d[i]);

	return res;
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
		grid[from].push_back(Node(to, cost));
		grid[to].push_back(Node(from, cost));
	}

	cout << Dijkstra(1) << endl;

	return 0;
}
```

解法二：Floyed算法

看到数据范围，发现完全可以用$O(n^3)$的算法，实际上可以求出全源最短路，然后依次计算从出发点到各个点最短路中的最大值即可。

```c++
#include <bits/stdc++.h>

using namespace std;

const int INF = 0x7ffffff;
int vertexNum, edgeNum;
vector<vector<int> > d(105, vector<int>(105, INF));


int Floyed()
{
	for (int k = 1; k <= vertexNum; ++k) {
		for (int i = 1; i <= vertexNum; ++i) {
			for (int j = 1; j <= vertexNum; ++j) {
				if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
			}
		}
	}

	int res = 0;
	for (int i = 1; i <= vertexNum; ++i) {
		res = max(res, d[1][i]);
	}

	return res;
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
		d[from][to] = d[to][from] = cost;
	}

	for (int i = 1; i <= vertexNum; ++i) d[i][i] = 0;

	cout << Floyed() << endl;

	return 0;
}
```

