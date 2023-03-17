> # POJ-1979 Red and Black(DFS 最大连通区域类问题)

# Description

There is a rectangular room, covered with square tiles. Each tile is colored either red or black. A man is standing on a black tile. From a tile, he can move to one of four adjacent tiles. But he can't move on red tiles, he can move only on black tiles.

Write a program to count the number of black tiles which he can reach by repeating the moves described above.

# Input

The input consists of multiple data sets. A data set starts with a line containing two positive integers W and H; W and H are the numbers of tiles in the x- and y- directions, respectively. W and H are not more than 20.

There are H more lines in the data set, each of which includes W characters. Each character represents the color of a tile as follows.

'.' - a black tile
'#' - a red tile
'@' - a man on a black tile(appears exactly once in a data set)
The end of the input is indicated by a line consisting of two zeros.

# Output

For each data set, your program should output a line which contains the number of tiles he can reach from the initial tile (including itself).

# Sample Input

```
6 9
....#.
.....#
......
......
......
......
......
#@...#
.#..#.
11 9
.#.........
.#.#######.
.#.#.....#.
.#.#.###.#.
.#.#..@#.#.
.#.#####.#.
.#.......#.
.#########.
...........
11 6
..#..#..#..
..#..#..#..
..#..#..###
..#..#..#@.
..#..#..#..
..#..#..#..
7 7
..#.#..
..#.#..
###.###
...@...
###.###
..#.#..
..#.#..
0 0
```

# Sample Output

```
45
59
6
13
```

----

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int m = 100, n = 100;
vector<vector<char> > ground(m, vector<char>(n));
int startRow, startCol;
int res = 0;
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0, -1}};

void DFS(int row, int col) 
{
    ++res;
    ground[row][col] = '#';
    for (int i = 0; i < 4; ++i) {
        int tmpRow = row + direction[i][0];
        int tmpCol = col + direction[i][1];
        if (0 <= tmpRow && tmpRow < m && 0 <= tmpCol && tmpCol < n && ground[tmpRow][tmpCol] == '.'){
            DFS(tmpRow, tmpCol);
        }
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
                if (ground[i][j] == '@'){
                    startRow = i;
                    startCol = j;
                }
            }
        }
        DFS(startRow, startCol);
        cout << res << endl;
        res = 0;
    }

    return 0;
}
```

思路和lake counting基本一致，注意两个细节，一个是最初`@`送在的位置也是black，另外，因为把res作为了全局变量，每个算例结束后要`res`清零。