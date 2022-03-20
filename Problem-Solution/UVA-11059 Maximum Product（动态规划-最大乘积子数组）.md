> # UVA-11059 Maximum Product（动态规划-最大乘积子数组）

# Description

Given a sequence of integers S = {S1, S2, . . . , Sn}, you should determine what is the value of the maximum positive product involving consecutive terms of S. If you cannot find a positive sequence, you should consider 0 as the value of the maximum product.

# Input

Each test case starts with 1 ≤ N ≤ 18, the number of elements in a sequence. Each element Si is an integer such that −10 ≤ Si ≤ 10. Next line will have N integers, representing the value of each element in the sequence. There is a blank line after each test case. The input is terminated by end of file (EOF).

# Output

For each test case you must print the message: ‘Case #M: The maximum product is P.’, where M is the number of the test case, starting from 1, and P is the value of the maximum product. After each test case you must print a blank line.

# Sample Input

```
3
2 4 -3

5
2 5 -1 2 -1
```

# Sample Output

```
Case #1: The maximum product is 8.

Case #2: The maximum product is 20.
```

-----

```c++
#include <bits/stdc++.h>

using namespace std;

vector<long long> seq(20);
int n;

long long solve()
{
	long long res = seq[0], large = seq[0], small = seq[0];

	for (int i = 1; i < n; ++i) {
		long long tmpMax = large, tmpMin = small;
		large = max(max(tmpMax * seq[i], tmpMin * seq[i]), seq[i]);
		small = min(min(tmpMax * seq[i], tmpMin * seq[i]), seq[i]);
		res = max(res, large);
	}

	return res < 0 ? 0 : res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum = 0;
	while (cin >> n) {
		++caseNum;

		for (int i = 0; i < n; ++i) cin >> seq[i];

		cout << "Case #" << caseNum << ": " << "The maximum product is " << solve() << '.' << endl;
		cout << endl;
	}

	return 0;
}
```

