> # 图算法——最短路--Floyed-Warshall算法

## Floyed-Warshall算法求解全源最短路

Floyed-Warshall算法是用来求解全源最短路问题。

平面上有n个点（n≤100），每个点的坐标均在-10000~10000之间。其中的一些点之间有连线。

若有连线，则表示可从一个点到达另一个点，即两点间有通路，通路的距离为两点间的直线距离。现在的任务是找出从一点到另一点之间的最短路径。

```c++
//一本通-1342：【例4-1】最短路径问题（可以Bellman-Ford，也可以Floyed）
#include <bits/stdc++.h>

using namespace std;


struct Point
{
	double x, y;
};

const double INF = 0x7ffffff;

int vertexNum, edgeNum;
vector<Point> p(105);
vector<vector<double> > dis(105, vector<double>(105, INF));


inline double calculateDistence(int from, int to)
{
	double xGap = p[from].x - p[to].x;
	double yGap = p[from].y - p[to].y;
	return sqrt(xGap * xGap + yGap * yGap);
}


void Floyed()
{
	for (int k = 1; k <= vertexNum; ++k) {
		for (int i = 1; i <= vertexNum; ++i) {
			for (int j = 1; j <= vertexNum; ++j) {
				if (dis[i][j] > dis[i][k] + dis[k][j]) 
					dis[i][j] = dis[i][k] + dis[k][j];
			}
		}
	}
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> vertexNum;
	for (int i = 1; i <= vertexNum; ++i) cin >> p[i].x >> p[i].y;
	cin >> edgeNum;
	int from, to;
	for (int i = 0; i < edgeNum; ++i) {
		cin >> from >> to;
		dis[from][to] = dis[to][from] = calculateDistence(from, to);
	} 

	int start, end;
	cin >> start >> end;
	Floyed();
	cout << fixed << setprecision(2) << dis[start][end] << endl;

	return 0;
}
```



## Floyed-Warshall算法求解负环

只需要检测`d[i][i] < 0`是否有成立的。

## Floyed-Warshall全源最短路径输出

因为用`dis[i][j]`代表从点`i`到点`j`的最短路，用`pre[i][j]`代表从点`i`到点`j`的最短路中，点`j`的前驱节点，假设这个点是`k`，那么接下来去看`pre[i][k]`。

每次更新点`dis[i][j]`的时候，就是更新`pre[i][j]`的时候。



## 典型题目

- [ ] HDU 3631
- [ ] POJ 2263
- [ ] POJ 2240
- [ ] HDU 1690
- [ ] HDU 4034
- [ ] POJ 3660
- [ ] POJ 1847
- [ ] HDU 1385
- [ ] POJ 2502
- [ ] HDU 2807
- [ ] HDU 1245
- [ ] POJ 3615
- [ ] POJ 2570
- [ ] HDU 1869
- [ ] HDU 3665
- [ ] POJ 1975
- [ ] POJ 1125
- [x] 一本通-1342：【例4-1】最短路径问题（可以Bellman-Ford，也可以Floyed）
- [x] 一本通-1343：【例4-2】牛的旅行（Floyed全源最短路）