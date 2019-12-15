> # 洛谷-P1601 A+B Problem（高精）

## 题目背景

无

## 题目描述

高精度加法,相当于a+b problem，**不用考虑负数**.

## 输入格式

分两行输入。a,b<=10^{500}a,b<=10500

## 输出格式

输出只有一行，代表a+ba+b的值

## 输入输出样例

## 输入

```
1
1
```

## 输出

```
2
```

---

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> bigNumPlus(vector<char> & num1, vector<char> & num2)
{
	int extra = 0;
	for (size_t i = 0; i < num1.size(); ++i) {
		int sum = (num1[i] - '0') + (num2[i] - '0') + extra;
		extra = sum / 10;
		num1[i] = '0' + sum % 10;
	}
	if (extra & 1) num1[num1.size() - 1] = '1';
	reverse(num1.begin(), num1.end());

	return num1;
}

template <typename T>
ostream & operator<<(ostream & os, const vector<T> & v)
{
	size_t i = 0;
	if (v[0] == '0') i = 1; 
	for ( ; i < v.size(); ++i) {
		os << v[i];
	}

	return os;
}

int main()
{
	string str1, str2;
	cin >> str1 >> str2;
	int length = max(str1.size(), str2.size()) + 1; //可能存在进位，所以多留出一位

	vector<char> num1(length, '0'), num2(length, '0');
	for (size_t i = 0; i < str1.size(); ++i) {
		num1[str1.size() - 1 - i] = str1[i];
	}

	for (size_t i = 0; i < str2.size(); ++i)
		num2[str2.size() - 1 - i] = str2[i];

	cout << bigNumPlus(num1, num2) << endl;

	return 0;
}
```

