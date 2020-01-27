> # HDU-3732 Ahui Writes Word(01背包转型多重背包)

# Description

We all know that English is very important, so Ahui strive for this in order to learn more English words. To know that word has its value and complexity of writing (the length of each word does not exceed 10 by only lowercase letters), Ahui wrote the complexity of the total is less than or equal to C.
Question: the maximum value Ahui can get.
Note: input words will not be the same.

# Input

The first line of each test case are two integer N , C, representing the number of Ahui’s words and the total complexity of written words. (1 ≤ N ≤ 100000, 1 ≤ C ≤ 10000)
Each of the next N line are a string and two integer, representing the word, the value(Vi ) and the complexity(Ci ). (0 ≤ Vi , Ci ≤ 10)

# Output

Output the maximum value in a single line for each test case.

# Sample Input

```
5 20
go 5 8
think 3 7
big 7 4
read 2 6
write 3 5
```

# Sample Output

```
15
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

map<pair<int, int>, int> m;

int n = 10005, c;
vector<int> d(10005, 0);

void completePack(int complexity, int value)
{
	for (int i = complexity; i <= c; ++i) {
		d[i] = max(d[i], d[i - complexity] + value);
	}
}

void zeroOnePack(int complexity, int value)
{
	for (int i = c; i >= complexity; --i) {
		d[i] = max(d[i], d[i - complexity] + value);
	}
}

void multiPack(int complexity, int value, int num)
{
	if (complexity * num >= c) {
		completePack(complexity, value);
		return;
	}

	int k = 1;
	while (k < num) {
		zeroOnePack(k * complexity, k * value);
		num -= k;
		k *= 2;
	}
	zeroOnePack(num * complexity, num * value);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> n >> c) {
		for (int i = 1; i <= n; ++i) {
			string str;
			int value, complexity;
			cin >> str >> value >> complexity;
			++m[make_pair(value, complexity)];
		}
		for (auto e : m) multiPack(e.first.second, e.first.first, e.second);

		cout << d[c] << endl;

		m.clear();
		fill(d.begin(), d.end(), 0);
	}
	

    return 0;
}
```

此题初看是01背包，但是因为时间复杂度是$O(n*c)$，很明显会超时，注意到因为`complexity`和`value`都小于10，而单词究竟是哪个其实影响不大，那么在大数据量的情况下，一定存在很多`comlexity`和`value`都相同的数据，那么相当于对应的数据是有限个数，相当于是多重背包，于是开始采用`map`来记录各个数据值，用`multiPack()`来处理，于是就从01背包转成了多重背包。因为`map`的大小最大不会超过100，其实就是一个常数项，最后时间复杂度是$O(c*logn)$。另外记得每次要对数组`d`初始化。

