> # POJ-3009 Curling 2.0(DFS搜索所有路径)

# Description

On Planet MM-21, after their Olympic games this year, curling is getting popular. But the rules are somewhat different from ours. The game is played on an ice game board on which a square mesh is marked. They use only a single stone. The purpose of the game is to lead the stone from the start to the goal with the minimum number of moves.

Fig. 1 shows an example of a game board. Some squares may be occupied with blocks. There are two special squares namely the start and the goal, which are not occupied with blocks. (These two squares are distinct.) Once the stone begins to move, it will proceed until it hits a block. In order to bring the stone to the goal, you may have to stop the stone by hitting it against a block, and throw again.

![img](https://vj.z180.cn/dfcadffc211686655c382e9ad94bdbfe?v=1578109369)
Fig. 1: Example of board (S: start, G: goal)

The movement of the stone obeys the following rules:

- At the beginning, the stone stands still at the start square.
- The movements of the stone are restricted to x and y directions. Diagonal moves are prohibited.
- When the stone stands still, you can make it moving by throwing it. You may throw it to any direction unless it is blocked immediately(Fig. 2(a)).
- Once thrown, the stone keeps moving to the same direction until one of the following occurs:
  - The stone hits a block (Fig. 2(b), (c)).
    - The stone stops at the square next to the block it hit.
    - The block disappears.
  - The stone gets out of the board.
    - The game ends in failure.
  - The stone reaches the goal square.
    - The stone stops there and the game ends in success.
- You cannot throw the stone more than 10 times in a game. If the stone does not reach the goal in 10 moves, the game ends in failure.

![img](https://vj.z180.cn/725189cee19b86e1cd2410490b0dadc2?v=1578109369)
Fig. 2: Stone movements

Under the rules, we would like to know whether the stone at the start can reach the goal and, if yes, the minimum number of moves required.

With the initial configuration shown in Fig. 1, 4 moves are required to bring the stone from the start to the goal. The route is shown in Fig. 3(a). Notice when the stone reaches the goal, the board configuration has changed as in Fig. 3(b).

![img](https://vj.z180.cn/c657651fda754a877e0c3a2ce3a06fd7?v=1578109369)
Fig. 3: The solution for Fig. D-1 and the final board configuration

# Input

The input is a sequence of datasets. The end of the input is indicated by a line containing two zeros separated by a space. The number of datasets never exceeds 100.

Each dataset is formatted as follows.

> *the width(=w) and the height(=h) of the board*
> *First row of the board*
> ...
> *h-th row of the board*

The width and the height of the board satisfy: 2 <= *w* <= 20, 1 <= *h* <= 20.

Each line consists of *w* decimal numbers delimited by a space. The number describes the status of the corresponding square.

> | 0    | vacant square  |
> | ---- | -------------- |
> | 1    | block          |
> | 2    | start position |
> | 3    | goal position  |

The dataset for Fig. D-1 is as follows:

> 6 6
> 1 0 0 2 1 0
> 1 1 0 0 0 0
> 0 0 0 0 0 3
> 0 0 0 0 0 0
> 1 0 0 0 0 1
> 0 1 1 1 1 1

# Output

For each dataset, print a line having a decimal integer indicating the minimum number of moves along a route from the start to the goal. If there are no such routes, print -1 instead. Each line should not have any character other than this number.

# Sample Input

```
2 1
3 2
6 6
1 0 0 2 1 0
1 1 0 0 0 0
0 0 0 0 0 3
0 0 0 0 0 0
1 0 0 0 0 1
0 1 1 1 1 1
6 1
1 1 2 1 1 3
6 1
1 0 2 1 1 3
12 1
2 0 1 1 1 1 1 1 1 1 1 3
13 1
2 0 1 1 1 1 1 1 1 1 1 1 3
0 0
```

# Sample Output

```
1
4
-1
4
10
-1
```

---

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int m = 20, n = 20;
vector<vector<int> > ground(m, vector<int>(n));
int startRow, stratCol;
int endRow, endCol;
int res = INF;
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

inline bool go(int tmpRow, int tmpCol)
{
    return (0 <= tmpRow && tmpRow < m && 0 <= tmpCol 
        && tmpCol < n && ground[tmpRow][tmpCol] == 0);
}

inline bool isError(int tmpRow, int tmpCol)
{
    return (tmpRow < 0 || tmpRow >= m || tmpCol < 0 || tmpCol >= n);
}

inline bool noMove(int tmpRow, int tmpCol, int row, int col, int i)
{
    return (tmpRow == row + direction[i][0] && tmpCol == col + direction[i][1]);
}

void DFS(int row, int col, int step)
{
    if (step > 10) {
        return;
    }

    for (int i = 0; i < 4; ++i) {
        int tmpRow = row + direction[i][0];
        int tmpCol = col + direction[i][1];
        while (go(tmpRow, tmpCol)) {
            //恰好移动到了终点
            if (tmpRow == endRow && tmpCol == endCol) {
                ++step;
                if (step < res) res = step;
                return;
            }
            tmpRow += direction[i][0];
            tmpCol += direction[i][1];
        }
        if (isError(tmpRow, tmpCol) || noMove(tmpRow, tmpCol, row, col, i)) continue; //非法的移动
        //现在位置是在block
        ++step; 
        ground[tmpRow][tmpCol] = 0; //block disappear
        DFS(tmpRow - direction[i][0], tmpCol - direction[i][1], step);
        --step;
        ground[tmpRow][tmpCol] = 1; //回溯寻找下一条路径
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while ((cin >> n >> m) && m && n) {
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> ground[i][j];
                if (ground[i][j] == 2) {
                    startRow = i;
                    stratCol = j;
                    ground[i][j] = 0;
                }
                else if (ground[i][j] == 3) {
                    endRow = i;
                    endCol = j;
                    ground[i][j] = 0;
                }
            }
        }
        DFS(startRow, stratCol, 0);
        if (res > 10) cout << -1 << endl;
        else cout << res << endl;
        res = INF;
    }

    return 0;
}
```

为数不多的需要在输入的时候对原始数据进行修改。看virtual judge上题目是日本的一道比赛题目，注意行和列的顺序是反着来的。

最初没有在75行和80行的改动，就会报错，因为格点数字是2和3的情况根本就没有处理。所以需要转化为0然后记录位置。

解题的思路：

如何移动？只能上下左右四个方向移动。

什么是合法的移动？不超出区域范围，不是原地不动。

什么情况下移动终止？移动到了终点，或者移动的步数超过了10.

如果上面的情况都考虑到了，那么接下来的问题是如何去解决题目里所说的”最短路径“，因为移动的规律不是每次走一个格子，而是走一整行或一整列可行的距离，所以应该用DFS去遍历所有的路径。

四个方向移动直到遇到block停止，用一个`while`循环来描述，因为导致不能继续移动的情况有很多，超出范围，或者遇到了block，分别来处理。超出范围用`isError`函数来处理，有两种情况会遇到block，和block紧挨着，这种情况是非法的；正常的移动碰到了block。

达到终点一定是在单方向移动过程中出现的，因为每次的移动都是整行或整列的，遇到block就停留在上一个位置，所以就免去了一开始就检查`ground[row][col]`是否是终点的情况。

`step`是记录走过的步数，不能是一个全局变量，因为step是跟随每一个DFS分支的，如果是全局变量，则相当于是累加所有路径的和了。

最后注意一下`res`要初始化为`inf`。