> # UVA-524 Prime Ring Problem（回溯-暴力搜索）

# Description

A ring is composed of n (even number) circles as shown in diagram.Put natural numbers 1, 2, . . . , n into each circle separately, and thesum of numbers in two adjacent circles should be a prime.
**Note:** the number of first circle should always be 1.

![img](F:\Project\Advanced-Algorithm\Problem Solution\assets\20150727210833681.png)



# Input

$n(0 < n \leq 16)$

# Output

The output format is shown as sample below. Each row represents a series of circle numbers in the
ring beginning from 1 clockwisely and anticlockwisely. The order of numbers must satisfy the above
requirements.
You are to write a program that completes above process.

# Sample Input

```
6
8
```

# Sample Output

```
Case 1:
1 4 3 2 5 6
1 6 5 2 3 4

Case 2:
1 2 3 8 5 6 7 4
1 2 5 8 3 4 7 6
1 4 7 6 5 8 3 2
1 6 7 4 3 8 5 2
```

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

int n;
vector<bool> used(17, false);

ostream & operator<<(ostream & os, vector<int> & v)
{
	int len = v.size();
	for (int i = 0; i < len; ++i) {
		os << v[i];
		if (i != len - 1) cout << ' ';
	}
	os << endl;

	return os;
}

bool isPrime(int num)
{
	if (num <= 1) return false;
	if (num == 2) return true;

	if (!(num & 1)) return false; //去除偶数

	int limit = sqrt(num) + 1;
	for (int i = 3; i <= limit; i += 2) {
		if (num % i == 0) return false;
	} 
	return true;
}

void search(int k, vector<int> & v)
{
	for (int i = 2; i <= n; ++i) {
		if (isPrime(v[k - 2] + i) && !used[i]) {
			v[k - 1] = i;
			used[i] = true;

			if (k == n) {
				if (isPrime(v[n - 1] + v[0])) cout << v;
			}
			else search(k + 1, v);
			used[i] = false;
		}
	}
}



int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum = 0;
    while (cin >> n) {
    	if (caseNum++) cout << endl;
    	cout << "Case " << caseNum << ":" << endl;

    	vector<int> res(n);
    	res[0] = 1; //要求必须以1开头
    	used[1] = true;

    	search(2, res);

    	fill(used.begin(), used.end(), false);
    }
}
```

先抛开思路不说，输出细节较之以往还是比较严格的。比如每一行的末尾不能有空格，最后一个输出的末尾不能有空行。

思路上属于第一类搜索框架的写法，注意这里限定了必须第一个元素是1，而且输出的序列是字典序升序的。