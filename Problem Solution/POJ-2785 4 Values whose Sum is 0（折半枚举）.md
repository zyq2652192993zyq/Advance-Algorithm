> # POJ-2785 4 Values whose Sum is 0（折半枚举）

# Description

The SUM problem can be formulated as follows: given four lists A, B, C, D of integer values, compute how many quadruplet (a, b, c, d ) ∈ A x B x C x D are such that a + b + c + d = 0 . In the following, we assume that all lists have the same size n .

# Input

The first line of the input file contains the size of the lists n (this value can be as large as 4000). We then have n lines containing four integer values (with absolute value as large as 2 28 ) that belong respectively to A, B, C and D .

# Output

For each input file, your program has to write the number quadruplets whose sum is zero.

# Sample Input

```
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
```

# Sample Output

```
5
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

int n = 4005;
vector<int> A(n), B(n), C(n), D(n);
vector<int> num(n * n);

int solve()
{
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			num[i * n + j] = C[i] + D[j];
		}
	}
	sort(num.begin(), num.begin() + n*n);

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			int target = 0 - (A[i] + B[j]);
			cnt += upper_bound(num.begin(), num.begin() + n * n, target) - lower_bound(num.begin(), num.begin() + n * n, target);
		}
	}

	return cnt;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> A[i] >> B[i] >> C[i] >> D[i];
	}
	cout << solve() << endl;

    return 0;
}
```

