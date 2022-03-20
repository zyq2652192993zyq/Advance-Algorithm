> # POJ-3061 Subsequence（前缀和+二分搜索+尺取法）

# Description

A sequence of N positive integers (10 < N < 100 000), each of them less than or equal 10000, and a positive integer S (S < 100 000 000) are given. Write a program to find the minimal length of the subsequence of consecutive elements of the sequence, the sum of which is greater than or equal to S.

# Input

The first line is the number of test cases. For each test case the program has to read the numbers N and S, separated by an interval, from the first line. The numbers of the sequence are given in the second line of the test case, separated by intervals. The input will finish with the end of file.

# Output

For each the case the program has to print the result on separate line of the output file.if no answer, print 0.

# Sample Input

```
2
10 15
5 1 3 5 10 7 4 9 2 8
5 11
1 2 3 4 5
```

# Sample Output

```
2
3
```

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

int n = 100005, s;
vector<int> sequence(n);
vector<int> prefixSum(n); //从1开始计数，计算包含第i个数的前缀和

int binarySearch(int target)
{
	int left = 1, right = n + 1;
	while (left < right) {
		int mid = left + ((right - left) >> 1);
		if (prefixSum[mid] < target) left = mid + 1;
		else right = mid;
	}

	return left;
}

int solve()
{
	for (int i = 1; i <= n; ++i)
		prefixSum[i] = sequence[i] + prefixSum[i - 1];
	if (prefixSum[n] < s) return 0;

	int len = INF;
	for (int i = 1; i <= n; ++i) {
		int target = s + prefixSum[i - 1];
		int endPos = binarySearch(target);
		if (endPos == n + 1) break;

		len = min(len, endPos - i + 1);
	}
	return len;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		cin >> n >> s;
		for (int i = 1; i <= n; ++i) cin >> sequence[i];
		cout << solve() << endl;
	}
    
    return 0;
}
```

先计算出前缀和，序列下标从1开始计数。

假设目前在位置`i`，满足连续的区间段和不小于`s`的第一个位置是`k`，那么这个区间段的和就是`prefixSum[k] - prefixSum[i - 1]>= s`，因为序列里的数非负，所以前缀和是单增的，那么搜索位置的过程只需要用二分搜索里的`lower_bound`，即查找第一个不小于目标值的数。

需要注意的是这里`right`设为了`n+1`，就是为了判断是否搜索的位置超过了范围，意味着无需再判断了，因为位置继续增加区间段的和必然是缩小的，目前都不满足，区间段减小肯定不会满足了，所以直接退出循环即可。