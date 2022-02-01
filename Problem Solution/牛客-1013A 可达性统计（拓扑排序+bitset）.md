> # 牛客-1013A 可达性统计（拓扑排序+bitset）

链接：https://ac.nowcoder.com/acm/contest/1013/A

## 题目描述

给定一张N个点M条边的有向无环图，分别统计从每个点出发能够到达的点的数量。N,M≤30000N,M \leq 30000N,M≤30000。

## 输入描述:

```
第一行两个整数N,M，接下来M行每行两个整数x,y，表示从x到y的一条有向边。
```

## 输出描述:

```
共N行，表示每个点能够到达的点的数量。
```

示例1

## 输入

```
10 10
3 8
2 3
2 5
5 9
5 9
2 3
3 9
4 8
2 10
4 9
```

## 输出

```
1
6
3
3
2
1
1
1
1
1
```

------

假设从点`x`可以到达的点用`f(x)`来表示，则表达式为：
$$
f(x) = {x} \cup_{\text{存在有向边x, y}} f(y)
$$
为了快速的计算交集，可以考虑用bitset来实现。

先用拓扑排序对所有的点进行排序，然后从后向前一次得到每个点可达的点的数量。

```c++
#include <bits/stdc++.h>

using namespace std;
   
   
const int vNum = 3e4 + 5;
const int eNum = 3e4 + 5;
vector<vector<int>> grid(vNum);
vector<int> inDegree(vNum, 0);
vector<bitset<vNum>> cap(eNum);
int m, n;
vector<int> topo;

void addEdge(int x, int y) {
    ++inDegree[y];
    grid[x].push_back(y);
}
   
void TopologicSort() {
    queue<int> q;
    for (int i = 1; i <= m; ++i) {
        if (inDegree[i] == 0) q.push(i);
    }

    while (! q.empty()) {
        int x = q.front(); q.pop();
        topo.push_back(x);
        for (auto & e : grid[x]) {
            if (--inDegree[e] == 0) q.push(e);
        }
    }
}
   
   
int main() {
   std::ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   
   cin >> m >> n;
   int x, y;
   for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        addEdge(x, y);
   }

   TopologicSort();

   for (int i = topo.size() - 1; i >= 0; --i) {
        int x = topo[i];
        cap[x].reset();
        cap[x][x] = 1;
        for (auto & e : grid[x]) {
            cap[x] |= cap[e];
        }
   }

   for (int i = 1; i <= m; ++i) {
        cout << cap[i].count() << endl;
   }

   return 0;
}   
```













