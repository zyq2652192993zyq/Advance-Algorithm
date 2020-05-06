> # 洛谷-P1480 A除B Problem

## 题目描述

输入两个整数a,b，输出它们的商(a<=10^5000,b<=10^9)

## 输入格式

两行，第一行是被除数，第二行是除数。

## 输出格式

一行，商的整数部分

## 输入输出样例

## 输入

```
10
2
```

## 输出

```
5
```

----

```c++
#include <string>
#include <iostream>

using namespace std;

int main()
{
	string str;
	long long num;
	cin >> str >> num;

	if (str == "0") cout << 0;
    else if (num == 1) cout << str;
	else {
		string res;
		long long extra = 0;
		for (size_t i = 0; i < str.size(); ++i) {
			long long tmp = extra * 10 + (str[i] - '0');
			res += to_string(tmp / num);
			extra = tmp % num;
		}
		int pos = 0;
		while (res[pos] == '0') ++pos;
		res = res.substr(pos);
		cout << res;
	}
	
	return 0;
}
```

