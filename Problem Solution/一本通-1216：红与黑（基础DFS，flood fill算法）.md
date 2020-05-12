> # 一本通-1216：红与黑（基础DFS，flood fill算法）

【题目描述】
有一间长方形的房子，地上铺了红色、黑色两种颜色的正方形瓷砖。你站在其中一块黑色的瓷砖上，只能向相邻的黑色瓷砖移动。请写一个程序，计算你总共能够到达多少块黑色的瓷砖。

【输入】
包括多个数据集合。每个数据集合的第一行是两个整数W和H，分别表示x方向和y方向瓷砖的数量。W和H都不超过20。在接下来的H行中，每行包括W个字符。每个字符表示一块瓷砖的颜色，规则如下:

1）‘.’：黑色的瓷砖；

2）‘#’：白色的瓷砖；

3）‘@’：黑色的瓷砖，并且你站在这块瓷砖上。该字符在每个数据集合中唯一出现一次。

当在一行中读入的是两个零时，表示输入结束。

【输出】
对每个数据集合，分别输出一行，显示你从初始位置出发能到达的瓷砖数(记数时包括初始位置的瓷砖)。

【输入样例】

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
0 0
```

【输出样例】

**45**

----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <set>
#include <algorithm>

using namespace std;

int m,n;
vector<vector<char> > grid(25, vector<char>(25));
// vector<vector<bool> > used(105, vector<bool>(105, false));
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void DFS(int row, int col, int &cnt)
{
	++cnt;
	grid[row][col] = '#';

	for (int i = 0; i < 4; ++i) {
		int nextRow = row + direction[i][0];
		int nextCol = col + direction[i][1];
		if (0 <= nextRow && nextRow < m && 0 <= nextCol && nextCol < n && grid[nextRow][nextCol] == '.') {
			DFS(nextRow, nextCol, cnt);
		}
	}
}

int solve()
{
	int cnt = 0;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (grid[i][j] == '@') {
				DFS(i, j, cnt);
				break;
			}
		}
	}

	return cnt;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while ((cin >> n >> m) && n && m) {
    	for (int i = 0; i < m; ++i) {
    		string line; cin >> line;
    		for (int j = 0; j < n; ++j) {
    			grid[i][j] = line[j];
    		}
    	}

    	cout << solve() << endl;
    }

    return 0;
}
```

