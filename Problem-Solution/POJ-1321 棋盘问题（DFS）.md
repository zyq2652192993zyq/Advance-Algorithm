> # POJ-1321 棋盘问题（简单路径搜索）

#Description

在一个给定形状的棋盘（形状可能是不规则的）上面摆放棋子，棋子没有区别。要求摆放时任意的两个棋子不能放在棋盘中的同一行或者同一列，请编程求解对于给定形状和大小的棋盘，摆放k个棋子的所有可行的摆放方案C。

#Input

输入含有多组测试数据。
每组数据的第一行是两个正整数，n k，用一个空格隔开，表示了将在一个n*n的矩阵内描述棋盘，以及摆放棋子的数目。 n <= 8 , k <= n
当为-1 -1时表示输入结束。
随后的n行描述了棋盘的形状：每行有n个字符，其中 # 表示棋盘区域， . 表示空白区域（数据保证不出现多余的空白行或者空白列）。

#Output

对于每一组数据，给出一行输出，输出摆放的方案数目C （数据保证C<2^31）。

# Sample Input

```
2 1
#.
.#
4 4
...#
..#.
.#..
#...
-1 -1
```

# Sample Output

```
2
1
```

---

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

int n, k;
int curChess = 0;
int res = 0;
vector<vector<int> > grid(10, vector<int>(10));
vector<bool> used(10, false);
// int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};


void DFS(int row)
{
	if (curChess == k) { //已经正确摆放k个棋子
		++res; return;
	}

	if (row >= n) return; //行数超出棋盘范围
	//在第row行放置棋子
	for (int col = 0; col < n; ++col) {
		if (!used[col] && grid[row][col] == '#') {
			++curChess;
			used[col] = true;

			DFS(row + 1);

			used[col] = false;
			--curChess;
		}
	}
	//在第row行不放置棋子
	DFS(row + 1);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while ((cin >> n >> k) && n != -1 && k != -1) {
    	for (int i = 0; i < n; ++i) {
    		string line; cin >> line;
    		for (int j = 0; j < n; ++j) {
    			grid[i][j] = line[j];
    		}
    	}

    	DFS(0);
    	cout << res << endl;

    	fill(used.begin(), used.end(), false);
    	curChess = res = 0;
    }

    return 0;
}
```

类似八皇后问题，但是并不是每一行都可以放置棋子，也并不是可以放置的行数是相邻的。

84行又一次调用`dfs(k + 1)`是因为如果本行不放入任何棋子，而从下一行开始搜索。
