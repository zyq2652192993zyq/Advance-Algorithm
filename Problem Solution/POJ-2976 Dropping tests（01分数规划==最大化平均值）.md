> # POJ-2976 Dropping tests（01分数规划==最大化平均值）

# Description

In a certain course, you take *n* tests. If you get *ai* out of *bi* questions correct on test *i*, your cumulative average is defined to be

![img](F:\Project\ACM-Algorithm\Problem Solution\assets\3b276ec6cce278e02c8588ea450bbd22).

Given your test scores and a positive integer *k*, determine how high you can make your cumulative average if you are allowed to drop any *k* of your test scores.

Suppose you take 3 tests with scores of 5/5, 0/1, and 2/6. Without dropping any tests, your cumulative average is ![img](F:\Project\ACM-Algorithm\Problem Solution\assets\1d5abb1f890636d0a47bac88f3b1436b). However, if you drop the third test, your cumulative average becomes ![img](F:\Project\ACM-Algorithm\Problem Solution\assets\f70df6d58de94d28226a4ac887bd9425).

# Input

The input test file will contain multiple test cases, each containing exactly three lines. The first line contains two integers, 1 ≤ *n* ≤ 1000 and 0 ≤ *k* < *n*. The second line contains *n* integers indicating *ai* for all *i*. The third line contains *n* positive integers indicating *bi* for all *i*. It is guaranteed that 0 ≤ *ai* ≤ *bi* ≤ 1, 000, 000, 000. The end-of-file is marked by a test case with *n* = *k* = 0 and should not be processed.

# Output

For each test case, write a single line with the highest cumulative average possible after dropping *k* of the given test scores. The average should be rounded to the nearest integer.

# Sample Input

```
3 1
5 0 2
5 1 6
4 2
1 2 7 9
5 6 7 9
0 0
```

# Sample Output

```
83
100
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

int n = 1005, k;
vector<int> A(n), B(n);
vector<double> num(n);

bool check(double x)
{
	for (int i = 0; i < n; ++i) {
		num[i] = A[i] - x * B[i];
	}
	sort(num.begin(), num.begin() + n);

	double sum = 0;
	for (int i = 0; i < k; ++i) sum += num[n - i - 1];

	return sum >= 0;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
    while ((cin >> n >> k) && (n || k)) {
    	k = n - k; //这里k的含义变成了选择k个成绩
    	for (int i = 0; i < n; ++i) cin >> A[i];
    	for (int i = 0; i < n; ++i) cin >> B[i];

    	double left = 0, right = INF;
    	for (int i = 0; i < 100; ++i) {
    		double mid = (left + right) / 2;
    		if (check(mid)) left = mid;
    		else right = mid;
    	}
    	cout << (int)(left * 100 + 0.5) << endl;
    }
   	
	
    return 0;
}
```

注意结果是四舍五入，所以需要`(int)(res + 0.5)`。方法在《挑战程序设计竞赛》里“最大化平均值”已经分析的很清楚了