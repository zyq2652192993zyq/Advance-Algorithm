> # AOJ-0558 Chess(BFS最短路)

> 原文是日文，这里翻译成了中文，评测在virtual judge

# 芝士

## 问题问题

同样，今年，JOI镇的一家奶酪工厂也开始生产奶酪，一只老鼠从窝里出来。JOI镇分为北，南，东和西，每个地块都是巢，奶酪工厂，障碍物或空地。鼠标从巢穴开始，并访问所有奶酪工厂，一次只能吃一种奶酪。

该镇有N个奶酪工厂，每个工厂仅生产一种奶酪。奶酪的硬度因工厂而异，并且恰好有一个奶酪工厂生产硬度为1到N的奶酪。

老鼠的初始健康状况是1，每吃一块奶酪，您的健康状况就会增加1。但是，老鼠不能吃比其体力更坚硬的奶酪。

鼠标可以在一分钟内移动到相邻的东西南北向隔间，但不能进入障碍物隔间。您甚至可以不吃奶酪就通过奶酪工厂。编写一个程序，以最短的时间完成所有奶酪的食用。但是，小鼠吃奶酪所需的时间可以忽略不计。

## 输入项

输入为H + 1行。在第一行中，三个整数H，W和N（1≤H≤1000、1≤W≤1000、1≤N≤9）以空格隔开。从第2行到第H + 1行的每一行都包含一个W字符串，由'S'，'1'，'2'，...，'9'，'X'和'。组成。它被编写，每个代表每个部分的状态。如果将北起的第i个分段和西起的第j个分段描述为（i，j）（1≤i≤H，1≤j≤W），则第i + 1行中的第j个字符为如果块（i，j）是一个嵌套，它将是'S'，如果是一个障碍，它将是'X'，如果是一个空地，它将是'。'，并且其硬度将为1，2，...，9如果是一家生产奶酪的工厂，则分别为“ 1”，“ 2”，...，“ 9”。输入有一个巢穴和一个工厂，生产的奶酪的硬度为1，2，...，N。其他牢房一定会成为障碍物或空缺。保证老鼠可以吃所有的奶酪。

## 输出量

在一行上打印一个整数，代表完成吃完所有奶酪所需的最短时间（以分钟为单位）。

## 输入/输出示例

### 输入示例1

```
3 3 1
S ..
...
..1
```

### 输出示例1

```
4
```

### 输入示例2

```
4 5 2
.X..1
.... X
.XX.S
.2.X。
```

### 输出示例2

```
12
```

### 输入例3

```
10 10 9
.X ... XSX
6..5X..X1X
... XXXX..X
X..9X ... X.
8.X2X..X3X
XX.X4 ..
XX .... 7X ..
X..X..XX ..
X ... X.XX ..
..X .......
```

### 输出示例3

```
91
```
----

```c++
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node {
    int row, col;
    Node(int x, int y) : row(x), col(y) {}
};

int m = 1000, n = 1000;
int num = 9;
vector<Node> factory(num + 1);
vector<vector<char> > ground(m, vector<char>(n));
vector<vector<int> > pathLen(m, vector<int>(n, INF));
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

inline void init()
{
    for (int i = 0; i < m; ++i) {
        fill(pathLen[i].begin(), pathLen[i].begin() + n, INF);
    }
}

inline bool canGo(int x, int y)
{
    return (0 <= x && x < m && 0 <= y && y < n 
        && ground[x][y] != 'X' && pathLen[x][y] == INF);
}

int BFS(Node start, Node end)
{
    init();
    queue<Node> q;
    q.push(start);
    pathLen[start.row][start.col] = 0;

    while (!q.empty()) {
        Node e = q.front(); q.pop();
        for (int i = 0; i < 4; ++i) {
            int nextRow = e.row + direction[i][0];
            int nextCol = e.col + direction[i][1];
            if (canGo(nextRow, nextCol)) {
                pathLen[nextRow][nextCol] = pathLen[e.row][e.col] + 1;
                if (nextRow == end.row && nextCol == end.col) {
                    return pathLen[nextRow][nextCol];
                }
                q.push(Node(nextRow, nextCol));
            }
        }
    }

}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> m >> n >> num;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> ground[i][j];
            if (ground[i][j] == 'S') {
                factory[0].row = i;
                factory[0].col = j;
            }
            else if ('1' <= ground[i][j] && ground[i][j] <= '9') {
                int number = ground[i][j] - '0';
                factory[number].row = i;
                factory[number].col = j;
            }
        }
    }
    int sum = 0;
    for (int i = 1; i <= num; ++i) {
        sum += BFS(factory[i-1], factory[i]);
    }
    cout << sum << endl;

    return 0;
}
```

这道题目本质上和《挑战程序设计竞赛》的走迷宫例题是一样的，但是给了一点迷惑的信息。最初写的很复杂，考虑的是需要一个`health`变量，然后搜索距离当前节点的所有工厂中，可以被访问的（健康值满足）的最短距离，然后用了两个`queuq`来恢复走过的路径（精确版的`init()`），但是这样就属于暴力模拟，实际上仔细分析题意，初始健康值是1，只能吃标号为1的工厂，然后健康值为2，小于等于2的只剩下2号工厂，所以转化成从1到2，2到3 ，……，8到9的最短路径，转化成了图中给定两点求最短路的问题。有一个细节，就是我们用数组`pathLen()`来记录当前节点是否被访问过，以及从起始点到当前点所走的最短路长度，但是下一轮的时候要记得把走过的路径恢复，为了简便就直接全部初始化。

