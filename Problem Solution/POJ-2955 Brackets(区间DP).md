> # POJ-2955 Brackets(区间DP)

# Description

We give the following inductive definition of a “regular brackets” sequence:

- the empty sequence is a regular brackets sequence,
- if *s* is a regular brackets sequence, then (*s*) and [*s*] are regular brackets sequences, and
- if *a* and *b* are regular brackets sequences, then *ab* is a regular brackets sequence.
- no other sequence is a regular brackets sequence

For instance, all of the following character sequences are regular brackets sequences:

> `(), [], (()), ()[], ()[()]`

while the following character sequences are not:

> `(, ], )(, ([)], ([(]`

Given a brackets sequence of characters *a*1*a*2 … *an*, your goal is to find the length of the longest regular brackets sequence that is a subsequence of *s*. That is, you wish to find the largest *m* such that for indices *i*1, *i*2, …, *im* where 1 ≤ *i*1 < *i*2 < … < *im* ≤ *n*, *ai*1*ai*2 … *aim* is a regular brackets sequence.

Given the initial sequence `([([]])]`, the longest regular brackets subsequence is `[([])]`.

# Input

The input test file will contain multiple test cases. Each input test case consists of a single line containing only the characters `(`, `)`, `[`, and `]`; each input test will have length between 1 and 100, inclusive. The end-of-file is marked by a line containing the word “end” and should not be processed.

# Output

For each input case, the program should print the length of the longest possible regular brackets subsequence on a single line.

# Sample Input

```
((()))
()()()
([]])
)[)(
([][][)
end
```

# Sample Output

```
6
6
4
0
6
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 105;
vector<vector<int> > d(n, vector<int>(n));

int maxLen(string & s)
{
	int m = s.size();

	for (int j = 1; j < m; ++j) {
		for (int i = j - 1; i >= 0; --i) {
			if ((s[i] == '(' && s[j] == ')') || (s[i] == '[' && s[j] == ']'))
				d[i][j] = d[i + 1][j - 1] + 2;
			//主要针对()()()类型
			for (int k = i; k <= j; ++k) {
				d[i][j] = max(d[i][j], d[i][k] + d[k + 1][j]);
			}
		}
	}

	return d[0][m - 1];
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	while ((cin >> str) && str[0] != 'e') {
		cout << maxLen(str) << endl;
		for (int i = 0; i < n; ++i)
			fill(d[i].begin(), d[i].end(), 0);
	}
	
    return 0;
}
```

这道题要和POJ 3280联系起来，因为循环的写法是一样的，这里只需要注意一点，就是需要去检查从`i`到`j`内的区间段连接起来，比如`()()()`的情况。

上面的方法时间复杂度是$O(n^2)$，这道题目因为数据范围长度小于等于100，所以可以过掉。

另外就是注意，这道题目允许的最大长度可以不连续，如果变为子串（要求连续），那么上面的方法就需要修改，比如LeetCode 32。