> # POJ-2229 Sumsets(完全背包变形)

# Description

Farmer John commanded his cows to search for different sets of numbers that sum to a given number. The cows use only numbers that are an integer power of 2. Here are the possible sets of numbers that sum to 7:

1) 1+1+1+1+1+1+1
2) 1+1+1+1+1+2
3) 1+1+1+2+2
4) 1+1+1+4
5) 1+2+2+2
6) 1+2+4

Help FJ count all possible representations for a given integer N (1 <= N <= 1,000,000).

# Input

A single line with a single integer, N.

# Output

The number of ways to represent N as the indicated sum. Due to the potential huge size of this number, print only last 9 digits (in base 10 representation).

# Sample Input

```
7
```

# Sample Output

```
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

int n = 1000005;
vector<int> d(n);
vector<int> sequence(n);

long long completePack()
{
	int cnt = 0;
	for (int i = 0; (1 << i) <= n; ++i) {
		sequence[cnt++] = (1 << i);
	}

	d[0] = 1;
	for (int i = 0; i < cnt; ++i) {
		for (int j = sequence[i]; j <= n; ++j) {
			d[j] = (d[j] + d[j - sequence[i]]) % 1000000000;
		}
	}
	return d[n];
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	cout << completePack() << endl;	

    return 0;
}
```

完全背包的变形，二维情形时，$d[i][j]$代表利用前`i`个数拼成数字`j`的方案数，但是最开始提交超时，因为将幂运算的部分用`pow(2, i)`来代替。
$$
d[i][j] = d[i-1][j] + d[i-1][j-w[i]];
$$
也就是第`i`个物品不选凑出`j`和选了第`i`个物品凑出`j`，然后完全背包，滚动数组优化。

首先这会出现`compiler error`，因为`pow`的第一个参数是`float`或者`double`类型，这样会造成类型转换时选择的歧义，另外这样计算指数，尤其是2的指数幂，显然位运算更好。

另外注意的一点是结果只需要取保留最后的9位数字，每一步运算的时候需要进行模运算。