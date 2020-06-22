> # HDU-2609 How many（字符串哈希 + 最小表示法）

# Description

Give you n ( n < 10000) necklaces ,the length of necklace will not large than 100,tell me
How many kinds of necklaces total have.(if two necklaces can equal by rotating ,we say the two necklaces are some).
For example 0110 express a necklace, you can rotate it. 0110 -> 1100 -> 1001 -> 0011->0110.

# Input

The input contains multiple test cases.
Each test case include: first one integers n. (2<=n<=10000)
Next n lines follow. Each line has a equal length character string. (string only include '0','1').

# Output

For each test case output a integer , how many different necklaces.

# Sample Input

```
4
0110
1100
1001
0011
4
1010
0101
1000
0001
```

# Sample Output

```
1
2
```

----

描述部分讲述的意思起始就是字符串同构，那么很自然的联想到最小表示法。所有字符串都是最小表示法后，假如直接排序，比较不同的字符串，因为每个字符串都是最大长度100，很可能出现大部分是`bbba`这种情况，比较的代价很大。于是想到可以利用字符串哈希，采用自然溢出法，使用`unsigned long long`类型，这样直接排序再统计不同的数值，代价就很小了。`n <= 1e4`，每个字符串最小表示法处理是$O(n)$，排序是$O(n \log n)$。

```c++
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

typedef unsigned long long ull;

const ull base = 13331;

vector<ull> seq(10005);
vector<ull> p(105);
int totalNum;

void init()
{
	p[0] = 1;
	for (int i = 1; i <= 100; ++i) p[i] = p[i - 1] * base;
}

//字符串的最小表示
int minRepresentation(const string & s)
{
	int n = s.size();
	int i = 0, j = 1, k = 0;

	while (i < n && j < n && k < n) {
		int gap = s[(i + k) % n] - s[(j + k) % n];
		if (gap == 0) ++k;
		else if (gap > 0) {
			i += k + 1;
			if (i == j) ++i;
			k = 0;
		}
		else {
			j += k + 1;
			if (i == j) ++j;
			k = 0;
		}
	}

	return min(i, j);
}

//字符串哈希
ull stringHash(const string & s)
{
	int n = s.size();
	ull res = 0;
	for (int i = 0; i < n; ++i) {
		res = res * base + s[i];
	}

	return res;
}


int solve()
{
	sort(seq.begin(), seq.begin() + totalNum); //排序统计不同的数值
	int cnt = 1;
	for (int i = 1; i < totalNum; ++i) if (seq[i] != seq[i - 1]) ++cnt;
	return cnt;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	init(); //初始化数组p，作为字符串哈希的准备

	string word;
	while (cin >> totalNum) {
		for (int i = 0; i < totalNum; ++i) {
			cin >> word;
			int pos = minRepresentation(word); //求出最小表示法在符串中的起始位置
			word = word.substr(pos) + word.substr(0, pos); 
			seq[i] = stringHash(word); //字符串哈希，便于去重
		}

		cout << solve() << endl;
	}

	return 0;
}
```

