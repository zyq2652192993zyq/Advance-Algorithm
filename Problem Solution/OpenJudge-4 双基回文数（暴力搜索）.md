> # OpenJudge-0004 双基回文数（暴力搜索）

Links: http://nnsznoi.openjudge.cn/directlycalculatin/0004/

**描述**

如果一个正整数n至少在两个不同的进位制b1和b2下都是回文数（2<=b1,b2<=10< span="">），则称n是双基回文数（注意，回文数不能包含前导零）。输入十进制的正整数S<106，输出比S大的最小双基回文数（十进制）

**输入**

一个十进制整数

**输出**

一个十进制整数

**样例输入**

```
1600000
```

**样例输出**

```
1632995
```

----

从`n+1`开始枚举进制2-10的所有表示，逐个检验就好了。

```c++
#include <bits/stdc++.h>

using namespace std;

int n;

void transfer(int number, int base, string & res)
{
	while (true) {
		res.push_back(char('0' + number % base));
		number /= base;
		if (!number) break;
	} 
}

bool check(const string & res)
{
	int len = res.size();
	int start = 0, end = len - 1;
	while (start <= end) {
		if (res[start++] != res[end--]) return false;
	}

	return true;
}

bool isPalindrome(int number, int base)
{
	string res;
	transfer(number, base, res);

	return check(res);
}

int solve()
{
	for (int i = n + 1; i <= INT_MAX; ++i) {
		int cnt = 0;
		for (int j = 2; j <= 10; ++j) {
			if (isPalindrome(i, j)) ++cnt;
			if (cnt == 2) return i;
		}
	}

	return INT_MAX;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	cout << solve() << endl;

	return 0;
}
```



