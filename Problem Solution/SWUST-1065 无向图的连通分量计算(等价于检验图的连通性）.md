> # SWUST-1065 无向图的连通分量计算(等价于检验图的连通性）

## 题目描述

假设无向图G采用邻接矩阵存储，编写一个算法求连通分量的个数。

## 输入

```
第一行为一个整数n，表示顶点的个数（顶点编号为0到n-1），接下来是为一个n*n大小的整数矩阵，表示图的邻接关系。数字为0表示不邻接，1表示不邻接。
```

## 输出

```
连通分量的个数。
```

## 样例输入复制

```
5
0 1 0 1 1
1 0 1 1 0
0 1 0 1 1
1 1 1 0 1
1 0 1 1 0
```

## 样例输出

```
1
```

---

```c++
#include <iostream>
#include <vector>

using namespace std;

int num;

void DFS(int s, vector<bool> &vertexVisited, vector<vector<int> > &denseGraph)
{
    for (int i = 0; i < num; ++i){
        if (!vertexVisited[i] && denseGraph[s][i]){
            vertexVisited[i] = true;
            DFS(i, vertexVisited, denseGraph);
        }
    }
}

int connectCheck(vector<bool> &vertexVisited, vector<vector<int> > &denseGraph)
{
    int count = 0;

    for (int i = 0; i < num; ++i){
        if (!vertexVisited[i]){
            DFS(i, vertexVisited, denseGraph);
            ++count;
        }
    }

    return count;
}

int main()
{
    cin >> num;

    vector<int> line(num, 0);
    vector<vector<int> > denseGraph(num, line);
    vector<bool> vertexVisited(num, false);

    for (int i = 0; i < num; ++i){
        for (int j = 0; j < num; ++j){
            cin >> denseGraph[i][j];
        }
    }

    int result = connectCheck(vertexVisited, denseGraph);
    cout << result;

    return 0;
}
```

唯一值得注意的是由于其编译器比较老，所以在定义矩阵的时候，`vector<vector<int> > `，两个`>`之间要有一个空格。

如果是检验图的连通性，则不必计算出count的数值，只需要检验count是否为1，否则就是不连通。