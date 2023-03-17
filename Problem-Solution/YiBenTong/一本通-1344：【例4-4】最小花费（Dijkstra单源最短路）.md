> # 一本通-1344：【例4-4】最小花费（Dijkstra单源最短路）

# 【题目描述】

在n个人中，某些人的银行账号之间可以互相转账。这些人之间转账的手续费各不相同。给定这些人之间转账时需要从转账金额里扣除百分之几的手续费，请问A最少需要多少钱使得转账后B收到100元。

# 【输入】

第一行输入两个正整数n,m，分别表示总人数和可以互相转账的人的对数

以下m行每行输入三个正整数x,y,z，表示标号为x的人和标号为y的人之间互相转账需要扣除z%的手续费 (z<100)。

最后一行输入两个正整数A,B。数据保证A与B之间可以直接或间接地转账。

# 【输出】

输出A使得B到账100元最少需要的总费用。精确到小数点后8位。

# 【输入样例】

**3 3
1 2 1
2 3 2
1 3 3
1 3**

# 【输出样例】

**103.07153164**

-----

题目的意思，假设手续费率是`z`，现在A有100元，假设一次转给B，那么B只能拿到$100 \times(1 - z\%)$，那么将问题转成最短路可以认为是B拥有100元，反过来求A，那么为了让A的数额最小，需要让手续费尽可能地低。用`d[i]`代表从出发点到`i`地最短距离。

```c++
#include <bits/stdc++.h>

using namespace std;

const double DNF = 0x7ffffff;
const int MAXN = 2005;

struct P
{
	int to;
	double ratio;

	P(int t, double r): to(t), ratio(r) {}
};

struct Element
{
	int to;
	double cost;

	Element(int t, double c) : to(t), cost(c) {}

	bool operator<(const Element & obj) const
	{
		return cost > obj.cost;
	}
};

int vertexNum, edgeNum;
vector<double> d(MAXN, DNF);
vector<vector<P> > grid(MAXN);


void Dijkstra(int start)
{
	d[start] = 100;
	priority_queue<Element> pq;
	pq.push(Element(start, 100));

	while (!pq.empty()) {
		Element tmp = pq.top(); pq.pop();
		int from = tmp.to;
		double money = tmp.cost;

		int len = grid[from].size();
		for (int i = 0; i < len; ++i) {
			int to = grid[from][i].to;
			if (d[to] > d[from] / (1 - grid[from][i].ratio)) {
				d[to] = d[from] / (1 - grid[from][i].ratio);
				pq.push(Element(to, d[to]));
			}
		}
	}
}



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> vertexNum >> edgeNum;
	int from, to;
	double ratio;
	for (int i = 0; i < edgeNum; ++i) {
		cin >> from >> to >> ratio;
		ratio /= 100;
		grid[from].push_back(P(to, ratio));
		grid[to].push_back(P(from, ratio));
	}

	int start, end;
	cin >> start >> end;

	Dijkstra(start);

	cout << fixed << setprecision(8) << d[end] << endl;

	return 0;
}
```

