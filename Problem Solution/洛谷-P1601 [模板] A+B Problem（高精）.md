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
//洛谷P1601 A+B Problem
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

int n = 205;
vector<int> num1(n), num2(n);
vector<int> res(n);

void init(vector<int> & v, string s)
{
	int len = s.size();
	v[0] = len;
	for (int i = 1; i <= len; ++i)
		v[i] = s[len - i] - '0';
}

void bigNumPlus(string & s1, string & s2)
{
	init(num1, s1);
	init(num2, s2);

	int pos = 1;
	int extra = 0;
	while (pos <= num1[0] || pos <= num2[0]) {
		res[pos] = num1[pos] + num2[pos] + extra;
		extra = res[pos] / 10;
		res[pos] %= 10;
		++pos;
	}
	res[pos] = extra;
	//去除前导0
	while (res[pos] == 0 && pos > 1) --pos;

	for (int i = pos; i >= 1; --i)
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
	bigNumPlus(s1, s2);

	return 0;
}
```

