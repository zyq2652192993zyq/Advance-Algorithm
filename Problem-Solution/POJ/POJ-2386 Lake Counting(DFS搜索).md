> # POJ-2386 Lake Counting(DFS搜索)

# Description

Due to recent rains, water has pooled in various places in Farmer John's field, which is represented by a rectangle of N x M (1 <= N <= 100; 1 <= M <= 100) squares. Each square contains either water ('W') or dry land ('.'). Farmer John would like to figure out how many ponds have formed in his field. A pond is a connected set of squares with water in them, where a square is considered adjacent to all eight of its neighbors.

Given a diagram of Farmer John's field, determine how many ponds he has.

# Input

* Line 1: Two space-separated integers: N and M
* Lines 2..N+1: M characters per line representing one row of Farmer John's field. Each character is either 'W' or '.'. The characters do not have spaces between them.

# Output

* Line 1: The number of ponds in Farmer John's field.

# Sample Input

```
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
```

# Sample Output

```
3
```

# Hint

OUTPUT DETAILS:

There are three ponds: one in the upper left, one in the lower left,and one along the right side.

---

```c++
#include <iostream>
#include <vector>

using namespace std;

int row = 100, col = 100;
vector<vector<char> > ground(row, vector<char>(col));


void DFS(int i, int j)
{
	ground[i][j] = '.';
	for (int rowDirection = -1; rowDirection <= 1; ++rowDirection) {
        int tmpRow = i + rowDirection;
		for (int colDirection = -1; colDirection <= 1; ++colDirection) {
			int tmpCol = j + colDirection;
			if (0 <= tmpRow && tmpRow < row && 0 <= tmpCol && tmpCol < col && ground[tmpRow][tmpCol] == 'W')
				DFS(tmpRow, tmpCol);
		}
	}
}

int solve()
{
	int cnt = 0;
	for (int i = 0; i < row; ++i) {
		for (int j = 0; j < col; ++j) {
			if (ground[i][j] == 'W'){
                DFS(i, j);
                ++cnt;
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

	cin >> row >> col;
	for (int i = 0; i < row; ++i) {
		for (int j = 0; j < col; ++j) {
			cin >> ground[i][j];
		}
	}

	cout << solve();
	
	return 0;
}
```

从任意的`W`开始，在八个方向上搜索，虽然代码是其实是九个方向（包含了原地不动的情况），但是在判断条件里已经除去了原地不动的情况，所以还是八个方向。深搜从找到一个`W`，继续搜索邻接的`w`，直到找不到了就返回，此时计数器`+1`，每个格点至多进行一次DFS，所以时间复杂度是$O(8\times m \times n) = O(mn)$。