> # 洛谷-P2005 A/B Problem II

## 题目背景

为了让大家紧张的心情放松一下，这一题题是一道非常简单的题目。

## 题目描述

给出正整数N和M，请你计算N div M（N/M的下取整）。

## 输入格式

两行，两个正整数，N和M。

## 输出格式

一行，一个整数，表示N div M。

## 输入输出样例

## 输入

```
1000
333
```

## 输出

```
3
```

----

```c++
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct bigNum {
	vector<int> num;
	int len;

	bigNum(int n): len(n) {num.assign(n, 0);}
};

bool compare(const bigNum & a, const bigNum & b)
{
	if (a.len < b.len) return false;
	if (a.len > b.len) return true;
	for (int i = a.len - 1; i >= 0; --i) {
		if (a.num[i] < b.num[i]) return false;
		else if (a.num[i] > b.num[i]) return true;
	}

	return true; //两个数完全一致
}

void subtraction(bigNum & a, const bigNum & minus)
{
	for (int i = 0; i < minus.len; ++i) {
		a.num[i] -= minus.num[i];
		if (a.num[i] < 0) {
			--a.num[i + 1];
			a.num[i] += 10;
		}
	}

	for (int i = a.len - 1; i >= 0; --i) {
		if (a.num[i] != 0) {
			a.len = i + 1; //更新被减数的长度
			return;
		}
	}
	a.len = 0; //恰好整除，a所有位都是0
}

vector<int> divide(bigNum & a, const bigNum & b)
{
	vector<int> res(a.len - b.len + 1, 0);
	for (int i = res.size() - 1; i >= 0; --i) {
		if (a.len == 0) break;
		bigNum minus(b.len + i); //构造被减数
		for (int j = b.len - 1; j >= 0; --j) minus.num[j + i] = b.num[j];
		
		while (compare(a, minus)) {
			subtraction(a, minus);
			++res[i];
		}
	}
	reverse(res.begin(), res.end());


	return res;
}

ostream & operator<<(ostream & os, const vector<int> & v)
{
	size_t i = 0;
	while (v[i] == 0) ++i;
	for ( ; i < v.size(); ++i) os << v[i];

	return os;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	string str1, str2;
	cin >> str1 >> str2;
	
	if (str1 == "0") cout << 0;
	else if (str2 == "1") cout << str1;
	else if (str1.size() < str2.size() || (str1.size() == str2.size() && str1 < str2)) cout << 0;
	else if (str1 == str2) cout << 1;
	else {
		int length = max(str1.size(), str2.size());
		bigNum a(length), b(length);
		b.len = str2.size();
		//倒序处理，便于后续大数减法的运算
		for (size_t i = 0; i < str1.size(); ++i) a.num[str1.size() - 1 - i] = str1[i] - '0';
		for (size_t i = 0; i < str2.size(); ++i) b.num[str2.size() - 1 - i] = str2[i] - '0';

		cout << divide(a, b);
	}
	
	return 0;
}
```

