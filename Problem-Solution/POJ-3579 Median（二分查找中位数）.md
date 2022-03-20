> # POJ-3579 Median（二分查找中位数）

# Description

Given *N* numbers, *X*1, *X*2, ... , *XN*, let us calculate the difference of every pair of numbers: ∣*Xi* - *Xj*∣ (1 ≤ *i* ＜ *j* ≤ *N*). We can get *C(N,2)* differences through this work, and now your task is to find the median of the differences as quickly as you can!

Note in this problem, the median is defined as the *(m/2)-th*  smallest number if *m*,the amount of the differences, is even. For example, you have to find the third smallest one in the case of *m* = 6.

# Input

The input consists of several test cases.
In each test case, *N* will be given in the first line. Then *N* numbers are given, representing *X*1, *X*2, ... , *XN*, ( *Xi* ≤ 1,000,000,000  3 ≤ N ≤ 1,00,000 )

# Output

For each test case, output the median in a separate line.

# Sample Input

```
4
1 3 2 4
3
1 10 2
```

# Sample Output

```
1
8
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

int n = 100005;
vector<int> sequence(n);
int k = 0;

//检验mid为中位数时是否有大于等于k个满足 差值<=mid
bool check(int mid)
{
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		cnt += upper_bound(sequence.begin(), sequence.begin() + n, sequence[i] + mid) - sequence.begin() - i - 1;
		if (cnt >= k) return true;
	}

	return false;
}

int solve()
{
	//n * (n - 1)可能溢出，要先转为long long类型
	k = ((long long)(n - 1) * (long long)n / 2 + 1) / 2; //+1为了应对奇数的情况
	
	sort(sequence.begin(), sequence.begin() + n);
	int left = 0, right = sequence[n - 1] - sequence[0];
	while (left < right) {
		int mid = left + ((right - left) >> 1);
		if (check(mid)) right = mid;
		else left = mid + 1;
	}

	return left;
}

int main()
{
	// std::ios_base::sync_with_stdio(false);
	// cin.tie(NULL);
	// cout.tie(NULL);

	//while (cin >> n) {
	while (scanf("%d", &n) != EOF) {
		for (int i = 0; i < n; ++i) scanf("%d", &sequence[i]);
		printf("%d\n", solve());
	}

	return 0;
}
```

一般属于POJ 月赛的题目即使解除绑定也会造成TLE！！！

很明显的二分思路，但是在程序设计的时候需要考虑一些细节问题，比如题目里n的数据范围是100000，计算`n -* (n -1)`的时候可能造成数据溢出，所以要先转为`long long`的数据类型，另外在计算中位数的位置的时候，需要先对$C_n^2$加1，这是为了应对组合数为奇数的情况。

比如题目里的1，2，10的数据，差值为1，8，9，那么中位数是8，第二个数，所以应该为`(3 + 1) / 2`。

check函数是统计数据差值小于等于`mid`的个数，又用了一次二分查找。查找第一个大于目标值的数，其位置提前1个就是所有小于等于目标值的数的个数。