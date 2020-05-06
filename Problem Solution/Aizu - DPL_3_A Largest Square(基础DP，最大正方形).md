> # Aizu - DPL_3_A Largest Square(基础DP，最大正方形)

Given a matrix (H × W) which contains only 1 and 0, find the area of the largest square matrix which only contains 0s.

## Input

```
H W
c1,1 c1,2 ... c1,W
c2,1 c2,2 ... c2,W
:
cH,1 cH,2 ... cH,W
```

In the first line, two integers H and W separated by a space character are given. In the following H lines, ci,j, elements of the H × W matrix, are given.

## Output

Print the area (the number of 0s) of the largest square.

## Constraints

- 1 ≤ H, W ≤ 1,400

## Sample Input

```
4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0
```

## Sample Output

```
4
```

----

```c++
#include <bits/stdc++.h>

using namespace std;

int m, n;
vector<vector<int> > grid(1405, vector<int>(1405)), d(1405, vector<int>(1405));

int largestSquare()
{
	int maxLen = 0;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (grid[i][j] == 0) d[i][j] = 1;
			maxLen |= d[i][j];
		}
	}

	for (int i = 1; i < m; ++i) {
		for (int j = 1; j < n; ++j) {
			if (grid[i][j] == 0) {
				d[i][j] = min(d[i][j - 1], min(d[i - 1][j], d[i - 1][j - 1])) + 1;
				maxLen = max(maxLen, d[i][j]);
			}
		}
	}

	return maxLen * maxLen;
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

	cout << largestSquare() << endl;

	return 0;
}
```

用`d[i][j]`代表从`(i, j)`向左上角所能扩展的最大正方形的边长。状态转移方程是：
$$
d[i][j] = min(d[i - 1][j], min(d[i - 1][j - 1], d[i][j - 1])) + 1;
$$
也就是其左上、上方、左侧元素中最小的值加1。

这道题和LeetCode 221.最大正方形是一个题目。