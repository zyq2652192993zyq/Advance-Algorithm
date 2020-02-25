> # POJ-3181 Dollar Dayz（划分数+高精度）

# Description

Farmer John goes to Dollar Days at The Cow Store and discovers an unlimited number of tools on sale. During his first visit, the tools are selling variously for $1, $2, and $3. Farmer John has exactly $5 to spend. He can buy 5 tools at $1 each or 1 tool at $3 and an additional 1 tool at $2. Of course, there are other combinations for a total of 5 different ways FJ can spend all his money on tools. Here they are:

```
        1 @ US$3 + 1 @ US$2

        1 @ US$3 + 2 @ US$1

        1 @ US$2 + 3 @ US$1

        2 @ US$2 + 1 @ US$1

        5 @ US$1
```

Write a program than will compute the number of ways FJ can spend N dollars (1 <= N <= 1000) at The Cow Store for tools on sale with a cost of $1..$K (1 <= K <= 100).

# Input

A single line with two space-separated integers: N and K.

# Output

A single line with a single integer that is the number of unique ways FJ can spend his money.

# Sample Input

```
5 3
```

# Sample Output

```
5
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;


int n = 105, m = 1005;
vector<vector<long long> > before(n, vector<long long>(m)); //前18位数
vector<vector<long long> > after(n, vector<long long>(m)); //后18位数
long long M = 1e18;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	after[0][0] = 1;

	int m, n;
	while (cin >> m >> n) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j <= m; ++j) {
				if (j >= i) {
					before[i][j] = before[i - 1][j] + before[i][j - i] + (after[i - 1][j] + after[i][j - i]) / M;
					after[i][j] = (after[i - 1][j] + after[i][j - i]) % M;
				}
				else {
					before[i][j] = before[i - 1][j];
					after[i][j] = after[i - 1][j];
				}
			}
		}

		if (before[n][m]) cout << before[n][m];
		cout << after[n][m] << endl;
	}

    return 0;
}
```

这道题目其实就是划分数的模板题，但是因为数据范围导致结果很大，超过了`long long`的标识范围，所以这个题目一个很巧妙的地方是可以用两个`long long`的数组合起来表示一个大整数。用数组`before`表示前18位的数字，`after`表示后18位的数字，用一个大数`M`来考察如何划分。