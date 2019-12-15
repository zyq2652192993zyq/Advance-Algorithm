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
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> multiply(const vector<int> & num1, const vector<int> & num2, int cnt)
{
	int length = num1.size();
	vector<int> res(length, 0);

	for (int i = 0; i < cnt; ++i) {
		for (size_t j = 0; j < num1.size(); ++j) {
			res[i + j] += num2[i] * num1[j];
		}
	}

	for (size_t i = 0; i < res.size() - 1; ++i) {
		if (res[i] >= 10) {
			res[i + 1] += res[i] / 10;
			res[i] = res[i] % 10;
		}
	}
	reverse(res.begin(), res.end());

	return res;
}

template <typename T>
ostream & operator<<(ostream & os, const vector<T> & v)
{
	size_t i = 0;
    
	while (v[i] == 0) ++i; //处理前导0
	for ( ; i < v.size(); ++i)
		os << v[i];

	return os;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	string str1, str2;
	cin >> str1 >> str2;

	if (str1 == "0" || str2 == "0") cout << 0;
	else if (str1 == "1") cout << str2;
	else if (str2 == "1") cout << str1;
	else {
		if (str1.size() < str2.size()) std::swap(str1, str2);
		int length = 2 * max(str1.size(), str2.size());
		vector<int> num1(length, 0), num2(length, 0);
		int cnt = str2.size();

		for (size_t i = 0; i < str1.size(); ++i) num1[str1.size() - 1 - i] = str1[i] - '0';
		for (size_t i = 0; i < str2.size(); ++i) num2[str2.size() - 1 - i] = str2[i] - '0';
		cout << multiply(num1, num2, cnt);
	}	

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