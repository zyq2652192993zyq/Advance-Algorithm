> # POJ-2251 Dungeon Master（三维迷宫BFS）

# Description

You are trapped in a 3D dungeon and need to find the quickest way out! The dungeon is composed of unit cubes which may or may not be filled with rock. It takes one minute to move one unit north, south, east, west, up or down. You cannot move diagonally and the maze is surrounded by solid rock on all sides.

Is an escape possible? If yes, how long will it take?

# Input

The input consists of a number of dungeons. Each dungeon description starts with a line containing three integers L, R and C (all limited to 30 in size).
L is the number of levels making up the dungeon.
R and C are the number of rows and columns making up the plan of each level.
Then there will follow L blocks of R lines each containing C characters. Each character describes one cell of the dungeon. A cell full of rock is indicated by a '#' and empty cells are represented by a '.'. Your starting position is indicated by 'S' and the exit by the letter 'E'. There's a single blank line after each level. Input is terminated by three zeroes for L, R and C.

# Output

Each maze generates one line of output. If it is possible to reach the exit, print a line of the form

> Escaped in x minute(s).


where x is replaced by the shortest time it takes to escape.
If it is not possible to escape, print the line

> Trapped!

# Sample Input

```
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0
```

# Sample Output

```
Escaped in 11 minute(s).
Trapped!
```

-----

三维迷宫，运动方向变成了6个，注意点是需要把`'E'`给修改成`.`，不然在BFS的判断条件里无法到达，或者也可以修改BFS的判断条件。

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
    int x, y, z;
    Node(int x, int y, int z): x(x), y(y), z(z) {}
};

int m, n, h;
vector<vector<vector<char> > > grid(105, vector<vector<char> >(105, vector<char>(105)));
vector<vector<vector<int> > > path(105, vector<vector<int> >(105, vector<int>(105, INT_MAX)));
int startX, startY, startZ;
int endX, endY, endZ;
int directionX[6] = {1, -1, 0, 0, 0, 0};
int directionY[6] = {0, 0, 1, -1, 0, 0};
int directionZ[6] = {0, 0, 0, 0, 1, -1};

ostream & operator<<(ostream & os, vector<vector<vector<int> > > & v)
{
    for (int i = 0; i < m; ++i)  {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < h; ++k) {
                os << v[i][j][k] << ' ';
            }
            os << endl;
        }
        os << "-----------------" << endl;
    }

    return os;
}

void BFS()
{
    path[startX][startY][startZ] = 0;
    queue<Node> q;
    q.push(Node(startX, startY, startZ));

    while (!q.empty()) {
        Node tmp = q.front(); q.pop();

        if (tmp.x == endX && tmp.y == endY && tmp.z == endZ) break;

        for (int i = 0; i < 6; ++i) {
            int nextX = tmp.x + directionX[i];
            int nextY = tmp.y + directionY[i];
            int nextZ = tmp.z + directionZ[i];
            if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n && 0 <= nextZ 
                && nextZ < h && grid[nextX][nextY][nextZ] == '.') {
                path[nextX][nextY][nextZ] = path[tmp.x][tmp.y][tmp.z] + 1;
                grid[nextX][nextY][nextZ] = '#';
                q.push(Node(nextX, nextY, nextZ));
            }
        }
    }

    if (path[endX][endY][endZ] == INT_MAX) cout << "Trapped!" << endl;
    else cout << "Escaped in " << path[endX][endY][endZ] << " minute(s)." << endl;

    //cout << path;
}

void init()
{
    for (int i = 0; i < m; ++i)  {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < h; ++k) {
                path[i][j][k] = INT_MAX;
            }
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while ((cin >> m >> n >> h) && (m || n || h)) {
        for (int i = 0; i < m; ++i)  {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < h; ++k) {
                    cin >> grid[i][j][k];
                    if (grid[i][j][k] == 'S') {
                        startX = i; startY = j; startZ = k;
                    }
                    else if (grid[i][j][k] == 'E') {
                        endX = i; endY = j; endZ = k;
                        grid[i][j][k] = '.';
                    }
                }
            }
        }

        BFS();
        init();
    }

    return 0;
}
```

