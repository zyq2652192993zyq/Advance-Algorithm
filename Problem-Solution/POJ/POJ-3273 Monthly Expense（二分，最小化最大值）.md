> # POJ-3273 Monthly Expense（二分，最小化最大值）

# Description

Farmer John is an astounding accounting wizard and has realized he might run out of money to run the farm. He has already calculated and recorded the exact amount of money (1 ≤ *moneyi* ≤ 10,000) that he will need to spend each day over the next *N* (1 ≤ *N* ≤ 100,000) days.

FJ wants to create a budget for a sequential set of exactly *M* (1 ≤ *M* ≤ *N*) fiscal periods called "fajomonths". Each of these fajomonths contains a set of 1 or more consecutive days. Every day is contained in exactly one fajomonth.

FJ's goal is to arrange the fajomonths so as to minimize the expenses of the fajomonth with the highest spending and thus determine his monthly spending limit.

# Input

Line 1: Two space-separated integers: *N* and *M*
Lines 2.. *N*+1: Line *i*+1 contains the number of dollars Farmer John spends on the *i*th day

# Output

Line 1: The smallest possible monthly limit Farmer John can afford to live with.

# Sample Input

```
7 5
100
400
300
100
500
101
400
```

# Sample Output

```
500
```

# Hint

If Farmer John schedules the months so that the first two days are a month, the third and fourth are a month, and the last three are their own months, he spends at most $500 in any month. Any other method of scheduling gives a larger minimum monthly limit.

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 100005, k;
vector<int> sequence(n);

bool check(int d)
{
	int cnt = k - 1;
	int sum = 0;
	for (int i = 0; i < n; ++i) {
		//在财务月内的和小于d
		if (sum + sequence[i] <= d) {
			sum += sequence[i];
		}
		else {
			--cnt; //开启一个新的财务月
			sum = 0;
			--i;
		}

		if (cnt < 0) break; //cnt < 0说明财务月的预算偏小
	}

	return cnt < 0;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
   	while (cin >> n >> k) {
   		for (int i = 0; i < n; ++i) cin >> sequence[i];

   		int left = 0, right = INF;
   		while (left < right) {
   			int mid = left + ((right - left) >> 1);
   			if (check(mid)) left = mid + 1;
   			else right = mid;
   		}
   		cout << left << endl;
   }
	
    return 0;
}
```

最小化最大值的思路，其实相当于最大化最小值思路逆转过来。

为了让每一个财务月的越算尽可能地小，用sum来记录连续地天数内地金额总和，超过了预算，那么就新开一个财务月。需要注意地是新开一个财务月地时候需要`--i`，这是因为判断条件是`sum + sequence[i] <= d`，如果新开一个财务月，下一轮循环计算地就是`i +1`了，所以需要`--i`来再次判断是否满足，应对的是财务月地越算小于序列里地某个日期地金额导致财务月内日期为空。