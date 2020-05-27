> # POJ-1164 The Castle（稍加思考的DFS泛洪）

# Description

这里还是借用一本通-1250：The Castle的题目描述，更清晰一些。

一座城堡被分成ｍ*ｎ个方块（m≤50，n≤50），每个方块可有0～4堵墙（0表示无墙）。下面示出了建筑平面图：

![img](http://ybt.ssoier.cn:8088/pic/1250.gif)

 图中的加粗黑线代表墙。几个连通的方块组成房间，房间与房间之间一定是用黑线（墙）隔开的。

现在要求你编一个程序，解决以下2个问题：

  1、该城堡中有多少个房间?

  2、最大的房间有多大?

# Input

Your program is to read from standard input. The first line contains the number of modules in the north-south direction and the number of modules in the east-west direction. In the following lines each module is described by a number (0 <= p <= 15). This number is the sum of: 1 (= wall to the west), 2 (= wall to the north), 4 (= wall to the east), 8 (= wall to the south). Inner walls are defined twice; a wall to the south in module 1,1 is also indicated as a wall to the north in module 2,1. The castle always has at least two rooms.

平面图用一个数字表示一个方块(第1个房间用二进制1011表示，0表示无东墙，用十进制11表示)。

第一行一个整数m（m≤50），表示房子南北方向的长度。

第二行一个整数n（n≤50），表示房子东西方向的长度。

后面的m行，每行有n个整数，每个整数都表示平面图对应位置的方块的特征。每个方块中墙的特征由数字P来描述（0≤P≤15）。数字P是下面的可能取的数字之和：

1（西墙 west）

2（北墙 north）

4（东墙 east）

8（南墙 south）

室内的墙被定义两次： 例如方块（1，1）中的南墙也被位于其南面的方块（2，1）定义了一次。

建筑中至少有两个房间。

# Output

Your program is to write to standard output: First the number of rooms, then the area of the largest room (counted in modules).

# Sample Input

```
4
7
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
```

# Sample Output

```
5
9
```

------

这道题目最重要的是理解题意。对于墙的描述采取二进制的方法，所以在东南西北四个方向移动之前，需要先用位运算检验一下对应的位是否为0，然后才可以移动，剩下的问题就变成了Lake Counting的泛洪算法了。

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

int m, n;
vector<vector<int> > grid(55, vector<int>(55));
vector<vector<bool> > used(55, vector<bool>(55));
int maxVal = 0, tmp;
int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int checkSign[4] = {8, 2, 4, 1};

void DFS(int row, int col)
{
    maxVal = max(maxVal, tmp);
    for (int i = 0; i < 4; ++i) {
        if ((grid[row][col] & checkSign[i]) == 0) {
            int nextRow = row + direction[i][0];
            int nextCol = col + direction[i][1];
            if (0 <= nextRow && nextRow < m && 0 <= nextCol && nextCol < n && !used[nextRow][nextCol] > 0) {
                used[nextRow][nextCol] = true;
                ++tmp;
                DFS(nextRow, nextCol);
            }
        }
    }
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> m >> n;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> grid[i][j];
        }
    }

    int cnt = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (!used[i][j]) {
                ++cnt;
                used[i][j] = true;
                tmp = 1;
                DFS(i, j);
            }
        }
    }

    cout << cnt << endl;
    cout << maxVal << endl;

    return 0;
}
```

