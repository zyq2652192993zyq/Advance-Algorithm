> # POJ-3616 Milking Time（基础动态规划）

# Description

Bessie is such a hard-working cow. In fact, she is so focused on maximizing her productivity that she decides to schedule her next *N* (1 ≤ *N* ≤ 1,000,000) hours (conveniently labeled 0..*N*-1) so that she produces as much milk as possible.

Farmer John has a list of *M* (1 ≤ *M* ≤ 1,000) possibly overlapping intervals in which he is available for milking. Each interval *i* has a starting hour (0 ≤ *starting_houri* ≤ *N*), an ending hour (*starting_houri* < *ending_houri* ≤ *N*), and a corresponding efficiency (1 ≤ *efficiencyi* ≤ 1,000,000) which indicates how many gallons of milk that he can get out of Bessie in that interval. Farmer John starts and stops milking at the beginning of the starting hour and ending hour, respectively. When being milked, Bessie must be milked through an entire interval.

Even Bessie has her limitations, though. After being milked during any interval, she must rest *R* (1 ≤ *R* ≤ *N*) hours before she can start milking again. Given Farmer Johns list of intervals, determine the maximum amount of milk that Bessie can produce in the *N* hours.

# Input

* Line 1: Three space-separated integers: *N*, *M*, and *R*
* Lines 2..$M+$1: Line$ i+1$ describes FJ's i th milking interval with three space-separated integers: $starting_hour_i$ , $ending_hour_i$ , and$ efficiency_i$

# Output

Line 1: The maximum number of gallons of milk that Bessie can product in the *N* hours

# Sample Input

```
12 4 2
1 2 8
10 12 19
3 6 24
7 10 31
```

# Sample Output

```
43
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

struct Node
{
	int start, end;
	long long efficiency;
	bool operator<(const Node & obj) const
	{
		return (start < obj.start || (start == obj.start && end < obj.end));
	}
};

int n = 1000005, m = 1005, r;
vector<Node> sequence(m);
vector<long long> d(m);

long long milkNum()
{
	sort(sequence.begin() + 1, sequence.begin() + 1 + m);

	long long res = 0;
	for (int i = 1; i <= m; ++i) d[i] = sequence[i].efficiency;

	for (int i = 1; i <= m; ++i) {
		for (int j = i + 1; j <= m; ++j) {
			if (sequence[j].start >= sequence[i].end) {
				d[j] = max(d[j], d[i] + sequence[j].efficiency);
			}
		}
		res = max(res, d[i]);
	}

	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m >> r;
	for (int i = 1; i <= m; ++i) {
		cin >> sequence[i].start >> sequence[i].end >> sequence[i].efficiency;
		sequence[i].end += r;
	}

	cout << milkNum() << endl;

    return 0;
}
```

用$d[i]$表示前$i$小时所能得到的最大牛奶量，休息时间其实影响的是结束时间。因为所有奶牛的结束时间都在时间范围内，所以不需要考虑可能某头牛开始时间在范围内，但是结束时间不在范围内。另外注意的是并不一定是在最后一头奶牛取到极值。