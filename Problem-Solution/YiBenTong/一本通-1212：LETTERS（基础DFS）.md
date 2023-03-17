> # 一本通-1212：LETTERS（基础DFS）

【题目描述】
给出一个roe×col的大写字母矩阵，一开始的位置为左上角，你可以向上下左右四个方向移动，并且不能移向曾经经过的字母。问最多可以经过几个字母。

【输入】
第一行，输入字母矩阵行数R和列数S，1≤R,S≤20。

接着输出R行S列字母矩阵。

【输出】
最多能走过的不同字母的个数。

【输入样例】
3 6
HFDFFB
AJHGDH
DGAGEH

【输出样例】
6

-----

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
vector<vector<bool> > used(25, vector<bool>(25, false));
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
vector<bool> letter(26, false);
int res = 1;

void DFS(int row, int col, int cnt)
{
	++cnt; res = max(res, cnt);
	used[row][col] = true; letter[grid[row][col] - 'A'] = true;

	for (int i = 0; i < 4; ++i) {
		int nextRow = row + direction[i][0];
		int nextCol = col + direction[i][1];
		if (0 <= nextRow && nextRow < m && 0 <= nextCol && nextCol < n 
			&& !used[nextRow][nextCol] && !letter[grid[nextRow][nextCol] - 'A']) {
			DFS(nextRow, nextCol, cnt);
			used[nextRow][nextCol] = false;
			letter[grid[nextRow][nextCol] - 'A'] = false;
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
    	string line; cin >> line;
    	for (int j = 0; j < n; ++j) {
    		grid[i][j] = line[j];
    	}
    }

    DFS(0, 0, 0);
    cout << res << endl;

    return 0;
}
```

走过不同的letter，因为只有大写字母，所以可以用一个长度为26的数组来记录哪些字母被使用了。设定一个全局变量`res`来存储最长路径，用`cnt`记录当前的路径长度，来更新`res`。另外需要一个矩阵来记录哪些位置被使用了。

```c++
#include <bits/stdc++.h>

using namespace std;

int m, n;
vector<vector<char> > grid(25, vector<char>(25));
vector<vector<bool> > used(25, vector<bool>(25, false));
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
vector<bool> letter(26, false);
int res = 1;

void DFS(int row, int col, int cnt)
{
	res = max(res, cnt);

	for (int i = 0; i < 4; ++i) {
		int nextRow = row + direction[i][0];
		int nextCol = col + direction[i][1];
		if (0 <= nextRow && nextRow < m && 0 <= nextCol && nextCol < n 
			&& !used[nextRow][nextCol] && !letter[grid[nextRow][nextCol] - 'A']) {
			used[nextRow][nextCol] = true;
			letter[grid[nextRow][nextCol] - 'A'] = true;

			DFS(nextRow, nextCol, cnt + 1);

			used[nextRow][nextCol] = false;
			letter[grid[nextRow][nextCol] - 'A'] = false;
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
    	string line; cin >> line;
    	for (int j = 0; j < n; ++j) {
    		grid[i][j] = line[j];
    	}
    }

    used[0][0] = true; 
    letter[grid[0][0] - 'A'] = true;
    DFS(0, 0, 1);
    cout << res << endl;

    return 0;
}
```

