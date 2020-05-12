> # 一本通-1360：奇怪的电梯(lift)（BFS或dijkstra）

【题目描述】
大楼的每一层楼都可以停电梯，而且第i层楼（1≤i≤N）上有一个数字Ki(0≤=Ki≤=N）。电梯只有四个按钮：开，关，上，下。上下的层数等于当前楼层上的那个数字。当然，如果不能满足要求，相应的按钮就会失灵。例如：3 3 1 2 5代表了Ki（K1=3,K2=3,……），从一楼开始。在一楼，按“上”可以到4楼，按“下”是不起作用的，因为没有-2楼。那么，从A楼到B楼至少要按几次按钮呢？

【输入】
共有二行，第一行为三个用空格隔开的正整数，表示N,A,B(1≤N≤200, 1≤A,B≤N)，第二行为N个用空格隔开的正整数，表示Ki。

【输出】
一行，即最少按键次数,若无法到达，则输出-1。

【输入样例】
5 1 5
3 3 1 2 5

【输出样例】
3

-----

解法一：BFS搜索，从一个位置开始搜索上下所能到达的点，如果未被访问且在范围内，则入队。

```c++
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> seq(205);
vector<bool> used(205, false);
int start, tail;

struct Node
{
	int pos, step;
	Node(int pEle, int sEle) : pos(pEle), step(sEle) {}
};

int solve()
{
	queue<Node> q;
	q.push(Node(start, 0));
	used[start] = true;

	while (!q.empty()) {
		Node tmp = q.front(); q.pop();
		if (tmp.pos == tail) return tmp.step;

		int up = tmp.pos + seq[tmp.pos];
		if (up <= n && !used[up]) {
			used[up] = true;
			q.push(Node(up, tmp.step + 1));
		}

		int down = tmp.pos - seq[tmp.pos];
		if (0 <= down && !used[down]) {
			used[down] = true;
			q.push(Node(down, tmp.step + 1));
		}
	}

	return -1;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> start >> tail;
	for (int i = 1; i <= n; ++i) cin >> seq[i];

	cout << solve() << endl;

	return 0;
}
```

解法二：单源最短路。从一个点出发到达另一个点，固定起点和终点，典型的单源最短路。方法有Bellman-Ford、SPFA、Dijkstra，其中Dijkstra算法时间复杂度最优（图中无负环）







