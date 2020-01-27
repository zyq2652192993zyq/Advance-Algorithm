> # POJ-2393 Yogurt factory（贪心）

# Description

The cows have purchased a yogurt factory that makes world-famous Yucky Yogurt. Over the next N (1 <= N <= 10,000) weeks, the price of milk and labor will fluctuate weekly such that it will cost the company C_i (1 <= C_i <= 5,000) cents to produce one unit of yogurt in week i. Yucky's factory, being well-designed, can produce arbitrarily many units of yogurt each week.

Yucky Yogurt owns a warehouse that can store unused yogurt at a constant fee of S (1 <= S <= 100) cents per unit of yogurt per week. Fortuitously, yogurt does not spoil. Yucky Yogurt's warehouse is enormous, so it can hold arbitrarily many units of yogurt.

Yucky wants to find a way to make weekly deliveries of Y_i (0 <= Y_i <= 10,000) units of yogurt to its clientele (Y_i is the delivery quantity in week i). Help Yucky minimize its costs over the entire N-week period. Yogurt produced in week i, as well as any yogurt already in storage, can be used to meet Yucky's demand for that week.

# Input

* Line 1: Two space-separated integers, N and S.
* Lines 2..N+1: Line i+1 contains two space-separated integers: C_i and Y_i.

# Output

Line 1: Line 1 contains a single integer: the minimum total cost to satisfy the yogurt schedule. Note that the total might be too large for a 32-bit integer.

# Sample Input

```
4 5
88 200
89 400
97 300
91 500
```

# Sample Output

```
126900
```

# Hint

OUTPUT DETAILS:
In week 1, produce 200 units of yogurt and deliver all of it. In week 2, produce 700 units: deliver 400 units while storing 300 units. In week 3, deliver the 300 units that were stored. In week 4, produce and deliver 500 units.

----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, s;
	cin >> n >> s;
	vector<int> cost(n), require(n);
	for (int i = 0; i < n; ++i) cin >> cost[i] >> require[i];
	for (int i = 1; i < n; ++i) cost[i] = min(cost[i - 1] + s, cost[i]);
	long long res = 0;
	for (int i = 0; i < n; ++i) res += cost[i] * require[i];
	cout << res << endl;

    return 0;
}
```

这道题目其实非常巧妙，特殊点是存储的费用是固定的，如果每周存储的费用不是固定的，此方法也同样适用。思路是将存储费用也视为生产费用。