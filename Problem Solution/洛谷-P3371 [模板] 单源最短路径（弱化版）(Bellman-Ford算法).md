> # 洛谷-P3371 [模板] 单源最短路径（弱化版）(Bellman-Ford算法)

## 题目背景

本题测试数据为随机数据，在考试中可能会出现构造数据让SPFA不通过，如有需要请移步 [P4779](https://www.luogu.org/problemnew/show/P4779)。

## 题目描述

如题，给出一个有向图，请输出从某一点出发到所有点的最短路径长度。

## 输入格式

第一行包含三个整数 n,m,sn,m,s，分别表示点的个数、有向边的个数、出发点的编号。

接下来 mm 行每行包含三个整数 u,v,wu,v,w，表示一条 u \to vu→v 的，长度为 ww 的边。

## 输出格式

输出一行 nn 个整数，第 ii 个表示 ss 到第 ii 个点的最短路径，若不能到达则输出 2^{31}-1231−1。

## 输入输出样例

**输入 #1**

```
4 6 1
1 2 2
2 3 2
2 4 1
1 3 5
3 4 3
1 4 4
```

**输出 #1**

```
0 2 4 3
```

## 说明/提示

【数据范围】
对于 20\%20% 的数据：1\le n \le 51≤n≤5，1\le m \le 151≤m≤15；
对于 40\%40% 的数据：1\le n \le 1001≤n≤100，1\le m \le 10^41≤m≤104；
对于 70\%70% 的数据：1\le n \le 10001≤n≤1000，1\le m \le 10^51≤m≤105；
对于 100\%100% 的数据：1 \le n \le 10^41≤n≤104，1\le m \le 5\times 10^51≤m≤5×105，保证数据随机。

对于真正 100\%100% 的数据，请移步 [P4779](https://www.luogu.org/problemnew/show/P4779)。请注意，该题与本题数据范围略有不同。

样例说明：

![img](https://cdn.luogu.com.cn/upload/pic/7641.png)

图片1到3和1到4的文字位置调换

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <algorithm>

using namespace std;

const int INF = 0X0ffffff;

struct Node
{
	int from, to, cost;
};

int vertexNum = 10005, edgeNum = 500005;
vector<int> d(vertexNum, INT_MAX); //最短距离
vector<Node> es(edgeNum); //边

void BellmanFord(int s)
{
	d[s] = 0;
	while (true) {
		bool update = false;
		for (int i = 1; i <= edgeNum; ++i) {
			Node tmp = es[i];
			//不为INF代表可达
			if (d[tmp.from] != INT_MAX && d[tmp.to] > d[tmp.from] + tmp.cost) {
				d[tmp.to] = d[tmp.from] + tmp.cost;
				update = true;
			}
		}
		if (!update) break;
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
		cin >> es[i].from >> es[i].to >> es[i].cost; 
	}
	BellmanFord(s);
	cout << d;
	
    return 0;
}
```

注意一下题目要求不能到达输出最大的正整数。`0x0ffffff`不等于`INT_MAX`。不然会有一个测试用例过不去（WA）。