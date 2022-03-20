> # 洛谷-P1303 A*B Problem

## 题目描述

求两数的积。

## 输入格式

两行，两个数。

## 输出格式

积

## 输入输出样例

## 输入

```
1
2
```

## 输出

```
2
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

int n = 4005;
vector<int> num1(n), num2(n);
vector<int> res(n);

void init(vector<int> & v, string s)
{
	int len = s.size();
	v[0] = len;
	for (int i = 1; i <= len; ++i)
		v[i] = s[len - i] - '0';
}

void bigNumMultiply(string & s1, string & s2)
{
	init(num1, s1);
	init(num2, s2);

	for (int i = 1; i <= num1[0]; ++i) {
		int extra = 0;
		for (int j = 1; j <= num2[0]; ++j) {
			res[i + j - 1] = num1[i] * num2[j] + extra + res[i + j - 1];
			extra = res[i + j - 1] / 10;
			res[i + j - 1] %= 10;
		}
		res[i + num2[0]] = extra;
	}
	//消除前导0
	int len = num1[0] + num2[0];
	while (res[len] == 0 && len > 1) --len;
	
	for (int i = len; i >= 1; --i)
		cout << res[i];
	cout << endl;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	string s1, s2;
	cin >> s1 >> s2;
	bigNumMultiply(s1, s2);

	return 0;
}
```

这里模拟竖式乘法的时候，始终保持利用数位最小的数的每一位去乘上数位较大的数，最后统一进位。相当于OI Wiki里面“高精度——单精度”的思想，时间复杂度从$O(n^2)$优化到$O(nm)$，其中$n,m$分别是字符串的长度。

典型题目：

- [x] 洛谷-P1303 A*B Problem

需要考虑的问题：

- 其中一个数是0
- 其中一个数是1
- 考虑前导0
- 两个数中有一个负数
- 两个数中有两个负数

最后两点在题目里是不需要考虑的，因为题目默认都是给定正数。即使是负数，只需要增加变量来记录符号，影响不大。