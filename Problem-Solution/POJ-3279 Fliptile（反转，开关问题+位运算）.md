> # POJ-3279 Fliptile（反转，开关问题+位运算）

# Description

Farmer John knows that an intellectually satisfied cow is a happy cow who will give more milk. He has arranged a brainy activity for cows in which they manipulate an *M* × *N* grid (1 ≤ *M* ≤ 15; 1 ≤ *N* ≤ 15) of square tiles, each of which is colored black on one side and white on the other side.

As one would guess, when a single white tile is flipped, it changes to black; when a single black tile is flipped, it changes to white. The cows are rewarded when they flip the tiles so that each tile has the white side face up. However, the cows have rather large hooves and when they try to flip a certain tile, they also flip all the adjacent tiles (tiles that share a full edge with the flipped tile). Since the flips are tiring, the cows want to minimize the number of flips they have to make.

Help the cows determine the minimum number of flips required, and the locations to flip to achieve that minimum. If there are multiple ways to achieve the task with the minimum amount of flips, return the one with the least lexicographical ordering in the output when considered as a string. If the task is impossible, print one line with the word "IMPOSSIBLE".

# Input

Line 1: Two space-separated integers: *M* and *N*
Lines 2.. *M*+1: Line *i*+1 describes the colors (left to right) of row i of the grid with *N* space-separated integers which are 1 for black and 0 for white

# Output

Lines 1.. *M*: Each line contains *N* space-separated integers, each specifying how many times to flip that particular location.

# Sample Input

```
4 4
1 0 0 1
0 1 1 0
0 1 1 0
1 0 0 1
```

# Sample Output

```
0 0 0 0
1 0 0 1
1 0 0 1
0 0 0 0
```

------

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>

using namespace std;

const int INF = 0x0ffffff;

int m = 16, n = 16;
vector<vector<int> > ground(m, vector<int>(n)); //记录初始数据输入
vector<vector<int> > flip(m, vector<int>(n)); //记录每个位置是否反转
vector<vector<int> > optionRes(m, vector<int>(n)); //保存当前最优的反转方案

int direction[5][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}, {0,0}};

//查询在所有影响下位于(row, col)位置的最终颜色
bool getColor(int row, int col)
{
	int num = ground[row][col]; //首先去记录初始状态，为偶数才满足要求
	for (int i = 0; i < 5; ++i) {
		int nextRow = row + direction[i][0];
		int nextCol = col + direction[i][1];
		if (0 <= nextRow && nextRow < m && 0 <= nextCol && nextCol < n) {
			num += flip[nextRow][nextCol];
		}
	}

	return (num & 1); //为奇数则需要再来一次反转
}

inline void init()
{
	for (int i = 0; i < m; ++i)
		fill(flip[i].begin(), flip[i].end(), 0);
}

int calculate()
{
	//从第二行开始依次确定反转方案
	for (int i = 1; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			//检验当前列的上一行，如果为1就需要反转
			if (getColor(i - 1, j)) {
				flip[i][j] = 1;
			}
		}
	}
	int cnt = 0; //记录反转次数
	//检验最后一行是否全是0
	for (int i = 0; i < n; ++i) {
		//只要最后一行有一个不是0，就返回-1
		if (getColor(m - 1, i)) return -1;
	}

	//如果通过检验，那么就统计反转次数
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (flip[i][j]) ++cnt;
		}
	}

	return cnt;
}

ostream & operator<<(ostream & os, vector<vector<int> > & v)
{
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			os << v[i][j] << " ";
		}
		os << endl;
	}

	return os;
}

void solve()
{
	int res = -1; //初始化为无解的情况，记录最少的反转次数
	//枚举第一行的所有状态
	for (int i = 0; i < (1 << n); ++i) {
		init(); //每次计算开始前要初始化flip
		for (int j = 0; j < n; ++j) {
			//相当于判断第j个元素是否在集合i中
			flip[0][n - 1 - j] = (i >> j) & 1;
		}
		int cnt = calculate(); //记录总共的反转次数
		//cnt = -1的时候代表无解
		if (cnt >= 0 && (res < 0 || cnt < res)) {
			res = cnt; //更新当前的最少反转次数
			optionRes = flip; //更新具体的反转方案
		}
	}

	if (res < 0) 
		cout << "IMPOSSIBLE" << endl;
	else
		cout << optionRes;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> m >> n;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> ground[i][j];
		}
	}

	solve();

    return 0;
}
```

这道题目具体看注释基本就能理解思路，技巧部分需要参考《基础算法——位运算》