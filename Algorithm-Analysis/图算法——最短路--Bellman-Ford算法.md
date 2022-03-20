> # 图算法——最短路之Bellman-Ford算法

参考资料：

* https://www.bilibili.com/video/BV15E411v7Wx
* https://www.bilibili.com/video/BV15E411v7bE
* https://www.bilibili.com/video/BV1b7411z7PP

Bellman-Ford算法和SPFA都是用来求解单源最短路问题，还可以用来判断负环。

## Bellman-Ford算法求单源最短路

单源最短路算法（Bellman-Ford算法）是解决起点固定，求到其他所有点最短路的算法。终点也固定的问题叫做两点之间最短路问题。算法地时间复杂度$O(\text{vertexNum}\times\text{edgeNum})$。

典型题目：

- [x] 洛谷 P3371 [模板] 单源最短路径（弱化版，无负环）

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

记出发点是`s`，从出发点到顶点`i`的最短距离为`d[i]`，则以下等式成立：
$$
d[i]=\min \left\{d[j]+(从j到i的边的权值)|e=(j, i) \in E\right\}
$$
初始阶段，所有的`d[i] = INF`，令`d[s] = 0`，因为到自己的最短路一定是0。更新的过程的理解：

第一次`while`循环的时候，进入`for`循环，这时候能进行更新的只有以`s`为起点的边，然后更新`d[i]`的数值，第二轮更新的时候，将会更新上一轮新增的点作为起点的边。举个特殊的例子，比如第一轮以`s`为起点的边的终点分别为A,B,C，那么下一轮循环的时候，起点变成了A，B，C，可能存在从`s`到A的距离大于从`s`到B再到A的距离，于是产生更新。更新停止会有两种情况：一种是图本身是联通的，当所有边都遍历过了，所有点的最短距离也都更新完成，那么就可以退出循环了；或者是图最初不是连通的，可能有的点从`s`出发无法到达，那么其`d[i]`就始终为`INT_MAX`。时间复杂度是$O(|vertexNum|\times|edgeNum|)$

或者换一种写法更容易分析时间复杂度：

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

	for (int i = 0; i < vertexNum; ++i) {
		for (int j = 1; j <= edgeNum; ++j) {
			const Node & tmp = es[j];
			if (d[tmp.from] != INT_MAX && d[tmp.to] > d[tmp.from] + tmp.cost) {
				d[tmp.to] = d[tmp.from] + tmp.cost;
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
		cin >> es[i].from >> es[i].to >> es[i].cost; 
	}
	BellmanFord(s);
	cout << d;
	
    return 0;
}
```

改进后地算法很容易分析时间复杂度，但是会在三个测试用例部分超时，因为对于100%的数据，是有可能退化到$O(nm)$的，所以会被卡。

上面的方法是建立在图中没有负环的基础上，因为如果存在负环，那么从`s`出发的最短距离一定是在减小的，也可以利用这一点来判断负环，负环的判定单独总结。

## Bellman-Ford算法找负环

典型题目：

- [x] 洛谷 P3385 [模板] 负环

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

struct Node
{
    int from, to, cost;
};

int vertexNum = 2005, edgeNum = 6005;
vector<int> d(vertexNum, INT_MAX); //最短距离
vector<Node> es(edgeNum); //边

bool findNegativeCircle(int s)
{
    fill(d.begin(), d.end(), INT_MAX);
    d[s] = 0;

    for (int i = 0; i < vertexNum; ++i) {
        for (int j = 1; j <= edgeNum; ++j) {
            if (d[es[j].from] != INT_MAX && d[es[j].to] > d[es[j].from] + es[j].cost) {
                d[es[j].to] = d[es[j].from] + es[j].cost;
                if (i == vertexNum - 1) return true;
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
            cin >> es[i].from >> es[i].to >> es[i].cost;
            if (es[i].cost >= 0) {
                ++edgeNum;
                ++i;
                es[i].from = es[i - 1].to;
                es[i].to = es[i - 1].from;
                es[i].cost = es[i - 1].cost;
            }
        }
        if (findNegativeCircle(1)) cout << "YE5" << endl;
        else cout << "N0" << endl;
    }

    return 0;
}
```

注意是`YE5`的最后一个是数字5。找负环的原理在于，如果最后一轮还有点会被更新，那么意味着存在一个负环，始终让距离在减小。Dijkstra算法就是在此思想的基础上衍生的，所以无法处理存在负环的情况。

## Bellman-Ford求全源最短路

思路就是以每个点为源点，做一次单源最短路的计算，时间复杂度是$O(n^2 m)$，效率比Floyed还要慢。

## 典型题目

- [ ] POJ 3259
- [ ] POJ 180
- [ ] HDU 2145(SPFA)
- [ ] POJ 1511（SPFA）
- [x] 一本通-1342：【例4-1】最短路径问题（可以Bellman-Ford，也可以Floyed）

