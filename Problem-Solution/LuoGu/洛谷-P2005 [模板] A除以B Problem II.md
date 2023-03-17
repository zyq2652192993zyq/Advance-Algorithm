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

----

下面这种方法在SJTU OJ和《一本通》都能通过，但是在洛谷会有7个样例超时。

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
#include <ctime>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

int n = 4005;
vector<int> num1(n), num2(n);
vector<int> tmp(n);
vector<int> res(n);

void init(vector<int> & v, string & s)
{
	int len = s.size();
	v[0] = len;
	for (int i = 1; i <= len; ++i)
		v[i] = s[len - i] - '0';
}

void addZero(vector<int> & a, vector<int> & b, int det)
{
	for (int i = 1; i <= a[0]; ++i)
		b[i + det] = a[i];
	b[0] = a[0] + det;
}

int compare(vector<int> & a, vector<int> & b)
{
	if (a[0] < b[0]) return -1;
	else if (a[0] > b[0]) return 1;

	for (int i = a[0]; i >= 1; --i) {
		if (a[i] > b[i]) return 1;
		else if (a[i] < b[i]) return -1;
	}
	return 0;
}

void bigNumMinus(vector<int> & a, vector<int> & b)
{
	if (compare(a, b) == 0) {
		a[0] = 0;
		return;
	}

	for (int i = 1; i <= b[0]; ++i) {
		a[i] -= b[i];
		if (a[i] < 0) {
			a[i] += 10;
			--a[i + 1];
		}
	}
	//消除a的前导0
	while (a[0] > 1 && a[a[0]] == 0) --a[0];
}

void bigNumDivide(string & s1, string & s2)
{
	init(num1, s1);
	init(num2, s2);

	res[0] = num1[0] - num2[0] + 1; //商数的最大位数
	for (int i = res[0]; i >= 1; --i) {
		if (num1[0] == 0) break;

		addZero(num2, tmp, i - 1); //在num2的后面添加i-1个0
		while (compare(num1, tmp) >= 0) {
			++res[i];
			bigNumMinus(num1, tmp);
		}
	}
	//消除前导0
	while (res[0] > 1 && res[res[0]] == 0) --res[0];
	//输出商数，num1中保存的是余数
	for (int i = res[0]; i >= 1; --i)
		cout << res[i];
	cout << endl;

	//输出余数
	// if (num1[0] == 0) cout << 0 << endl;
	// else {
	// 	for (int i = num1[0]; i >= 1; --i)
	// 		cout << num1[i];
	// 	cout << endl;
	// }
}	


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string s1, s2;
	cin >> s1 >> s2;

	if (s1.size() < s2.size() || (s1.size() == s2.size() && s1 < s2))
		cout << 0 << endl;
	else 
		bigNumDivide(s1, s2);

	return 0;
}
```

