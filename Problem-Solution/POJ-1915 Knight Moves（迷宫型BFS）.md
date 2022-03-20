> # POJ-1915 Knight Moves（迷宫型BFS）

# Description

**Background**
Mr Somurolov, fabulous chess-gamer indeed, asserts that no one else but him can move knights from one position to another so fast. Can you beat him?
**The Problem**
Your task is to write a program to calculate the minimum number of moves needed for a knight to reach one point from another, so that you have the chance to be faster than Somurolov.
For people not familiar with chess, the possible knight moves are shown in Figure 1.

![img](https://vj.z180.cn/d2b26809455ce72d961db3fab309bf1a?v=1590069365)

# Input

The input begins with the number n of scenarios on a single line by itself.
Next follow n scenarios. Each scenario consists of three lines containing integer numbers. The first line specifies the length l of a side of the chess board (4 <= l <= 300). The entire board has size l * l. The second and third line contain pair of integers {0, ..., l-1}*{0, ..., l-1} specifying the starting and ending position of the knight on the board. The integers are separated by a single blank. You can assume that the positions are valid positions on the chess board of that scenario.

# Output

For each scenario of the input you have to calculate the minimal amount of knight moves which are necessary to move from the starting point to the ending point. If starting point and ending point are equal,distance is zero. The distance must be written on a single line.

# Sample Input

```
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
```

# Sample Output

```
5
28
0
```

------

```c++
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

struct Node
{
    int x, y;
    Node(int a, int b): x(a), y(b) {}   
};
int n;
int startX, startY, endX, endY;
vector<vector<int> > path(305, vector<int>(305, INT_MAX));
int direction[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, 
                        {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

int BFS()
{
    path[startX][startY] = 0;
    queue<Node> q;
    q.push(Node(startX, startY));

    while (!q.empty()) {
        Node tmp = q.front(); q.pop();

        if (tmp.x == endX && tmp.y == endY) break;

        for (int i = 0; i < 8; ++i) {
            int nextRow = tmp.x + direction[i][0];
            int nextCol = tmp.y + direction[i][1];
            if (0 <= nextRow && nextRow < n && 0 <= nextCol && nextCol < n 
                && path[nextRow][nextCol] > path[tmp.x][tmp.y] + 1) {
                path[nextRow][nextCol] = path[tmp.x][tmp.y] + 1;
                q.push(Node(nextRow, nextCol));
            }
        }
    }

    return path[endX][endY];
}



void init()
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            path[i][j] = INT_MAX;
        }
    }
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        cin >> n;
        cin >> startX >> startY >> endX >> endY;
        
        cout << BFS() << endl;

        init();
    }

    return 0;
}
```



