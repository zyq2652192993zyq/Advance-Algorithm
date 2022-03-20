> # 一本通-1375：骑马修栅栏(fence)（欧拉通路）

# 【题目描述】

农民John每年有很多栅栏要修理。他总是骑着马穿过每一个栅栏并修复它破损的地方。

John是一个与其他农民一样懒的人。他讨厌骑马，因此从来不两次经过一个一个栅栏。你必须编一个程序，读入栅栏网络的描述，并计算出一条修栅栏的路径，使每个栅栏都恰好被经过一次。John能从任何一个顶点(即两个栅栏的交点)开始骑马，在任意一个顶点结束。

每一个栅栏连接两个顶点，顶点用1到500标号(虽然有的农场并没有500个顶点)。一个顶点上可连接任意多(≥1)个栅栏。所有栅栏都是连通的(也就是你可以从任意一个栅栏到达另外的所有栅栏)。

你的程序必须输出骑马的路径(用路上依次经过的顶点号码表示)。我们如果把输出的路径看成是一个500进制的数，那么当存在多组解的情况下，输出500进制表示法中最小的一个 (也就是输出第一个数较小的，如果还有多组解，输出第二个数较小的，等等)。 输入数据保证至少有一个解。

# 【输入】

第1行:一个整数F(1≤F≤1024)，表示栅栏的数目;

第2到F+1行:每行两个整数i,j(1≤=i,j≤500)表示这条栅栏连接i与j号顶点。

# 【输出】

输出应当有F+1行，每行一个整数，依次表示路径经过的顶点号。注意数据可能有多组解，但是只有上面题目要求的那一组解是认为正确的。

# 【输入样例】

**9
1 2
2 3
3 4
4 2
4 5
2 5
5 6
5 7
4 6**

# 【输出样例】

**1
2
3
4
2
5
4
6
5
7**

------

这道题和以往的一笔画问题没什么太多区别，但是注意题目里有一句话（洛谷上P2731），两个顶点间可能存在多个栅栏，所以需要用`grid`进行计数。

```c++
#include <bits/stdc++.h>

using namespace std;

vector<int> degree(505, 0);
int n = 0, start = INT_MAX;
vector<vector<int> > grid(505, vector<int>(505, 0));
stack<int> s;


void EulerPath(int from)
{
	for (int to = start; to <= n; ++to) {
		if (grid[from][to]) {
			--grid[from][to];
			--grid[to][from];
			EulerPath(to);
		}
	}

	s.push(from);
}


void solve()
{
	int from = start;
	for (int i = start; i <= n; ++i) {
		if (degree[i] & 1) {
			from = i; break;
		}
	}

	EulerPath(from);

	while (!s.empty()) {
		cout << s.top() << endl;
		s.pop();
	}
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int edgeNum; cin >> edgeNum;
	int x, y;
	while (edgeNum--) {
		cin >> x >> y;
		n = max(n, max(x, y));
		start = min(start, min(x, y));
		++grid[x][y]; ++grid[y][x];
		++degree[x]; ++degree[y];
	}

	solve();

	return 0;
}
```

