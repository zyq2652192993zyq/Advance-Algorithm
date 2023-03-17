> # POJ-1753 Flip Game（反转，开关问题+位运算）

# Description

Flip game is played on a rectangular 4x4 field with two-sided pieces placed on each of its 16 squares. One side of each piece is white and the other one is black and each piece is lying either it's black or white side up. Each round you flip 3 to 5 pieces, thus changing the color of their upper side from black to white and vice versa. The pieces to be flipped are chosen every round according to the following rules:

1. Choose any one of the 16 pieces.
2. Flip the chosen piece and also all adjacent pieces to the left, to the right, to the top, and to the bottom of the chosen piece (if there are any).

Consider the following position as an example:

![img](https://vj.z180.cn/14b4b3ec0b5261bea3a5ad9f1313252c?v=1581702264)

bwbw

wwww

bbwb

bwwb

Here "b" denotes pieces lying their black side up and "w" denotes pieces lying their white side up. If we choose to flip the 1st piece from the 3rd row (this choice is shown at the picture), then the field will become:

bwbw

bwww

wwwb

wwwb

The goal of the game is to flip either all pieces white side up or all pieces black side up. You are to write a program that will search for the minimum number of rounds needed to achieve this goal.

# Input

The input consists of 4 lines with 4 characters "w" or "b" each that denote game field position.

# Output

Write to the output file a single integer number - the minimum number of rounds needed to achieve the goal of the game from the given position. If the goal is initially achieved, then write 0. If it's impossible to achieve the goal, then write the word "Impossible" (without quotes).

# Sample Input

```
bwwb
bbwb
bwwb
bwww
```

# Sample Output

```
4
```

-----

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

int m = 4, n = 4;
vector<vector<int> > ground(m, vector<int>(n)); //记录初始数据输入
vector<vector<int> > flip(m, vector<int>(n)); //记录每个位置是否反转

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

int calculate1()
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

int calculate2()
{
	//从第二行开始依次确定反转方案
	for (int i = 1; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			//检验当前列的上一行，如果为0就需要反转
			if (!getColor(i - 1, j)) {
				flip[i][j] = 1;
			}
		}
	}
	int cnt = 0; //记录反转次数
	//检验最后一行是否全是0
	for (int i = 0; i < n; ++i) {
		//只要最后一行有一个不是1，就返回-1
		if (!getColor(m - 1, i)) return -1;
	}

	//如果通过检验，那么就统计反转次数
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (flip[i][j]) ++cnt;
		}
	}

	return cnt;
}

void solve()
{
	int res = -1; //初始化为无解的情况，记录最少的反转次数
	//枚举第一行的所有状态(为了让0朝上)
	for (int i = 0; i < (1 << n); ++i) {
		init(); //每次计算开始前要初始化flip
		for (int j = 0; j < n; ++j) {
			//相当于判断第j个元素是否在集合i中
			flip[0][n - 1 - j] = (i >> j) & 1;
		}
		int cnt = calculate1(); //记录总共的反转次数
		//cnt = -1的时候代表无解
		if (cnt >= 0 && (res < 0 || cnt < res)) {
			res = cnt; //更新当前的最少反转次数
		}
	}

	//枚举第一行的所有状态(为了让1朝上)
	for (int i = 0; i < (1 << n); ++i) {
		init(); //每次计算开始前要初始化flip
		for (int j = 0; j < n; ++j) {
			//相当于判断第j个元素是否在集合i中
			flip[0][n - 1 - j] = (i >> j) & 1;
		}
		int cnt = calculate2(); //记录总共的反转次数
		//cnt = -1的时候代表无解
		if (cnt >= 0 && (res < 0 || cnt < res)) {
			res = cnt; //更新当前的最少反转次数
		}
	}

	if (res < 0) 
		cout << "Impossible" << endl;
	else
		cout << res << endl;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// cin >> m >> n;
	for (int i = 0; i < 4; ++i) {
		string line;
		cin >> line;
		for (int j = 0; j < 4; ++j) {
			//黑色为1
			if (line[j] == 'b') ground[i][j] = 1;
			else ground[i][j] = 0;
		}
	}

	solve();

    return 0;
}
```

基本上就是POJ 3279的变形问题，因为输入是很规矩的4x4，所以更好处理了。

需要注意的就是要检验全是1和全是0两种反转情况，需要修改相应的计算函数，不存在方案的时候记得输出形式的问题。