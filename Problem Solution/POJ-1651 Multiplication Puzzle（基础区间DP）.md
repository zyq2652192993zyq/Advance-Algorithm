> # POJ-1651 Multiplication Puzzle（基础区间DP）

# Description

The multiplication puzzle is played with a row of cards, each containing a single positive integer. During the move player takes one card out of the row and scores the number of points equal to the product of the number on the card taken and the numbers on the cards on the left and on the right of it. It is not allowed to take out the first and the last card in the row. After the final move, only two cards are left in the row.

The goal is to take cards in such order as to minimize the total number of scored points.

For example, if cards in the row contain numbers 10 1 50 20 5, player might take a card with 1, then 20 and 50, scoring
10*1*50 + 50*20*5 + 10*50*5 = 500+5000+2500 = 8000
If he would take the cards in the opposite order, i.e. 50, then 20, then 1, the score would be
1*50*20 + 1*20*5 + 10*1*5 = 1000+100+50 = 1150.

# Input

The first line of the input contains the number of cards N (3 <= N <= 100). The second line contains N integers in the range from 1 to 100, separated by spaces.

# Output

Output must contain a single integer - the minimal score.

# Sample Input

```
6
10 1 50 50 20 5
```

# Sample Output

```
3650
```

------

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

const int INF = 0x0ffffff;

int n;
vector<int> seq(105);
vector<vector<int> > d(105, vector<int>(105, INF));

int solve()
{
	for (int i = 0; i < n - 1; ++i) d[i][i + 1] = 0;

	for (int len = 3; len <= n; ++len) {
		for (int i = 0; i + len - 1 < n; ++i) {
			int j = i + len - 1;
			for (int k = i + 1; k < j; ++k) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j] + seq[i] * seq[k] * seq[j]);
			}
		}
	}

	return d[0][n - 1];
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> seq[i];

	cout << solve() << endl;

	return 0;
}
```

用`d[i][j]`表示将下标从`i`到`j`区间内的数字提取只剩下两个数字时候的最小代价，状态转移方程：
$$
d[i][j] = \min(d[i][j], d[i][k] + d[k][j] + \text{seq}[i] * \text{seq}[k] * \text{seq}[j])
$$
最终结果为$d[0][n- 1 ]$。时间复杂度$O(n^2)$。