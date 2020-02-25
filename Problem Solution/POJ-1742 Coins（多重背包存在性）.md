> # POJ-1742 Coins（多重背包存在性）

# Description

Whuacmers use coins.They have coins of value A1,A2,A3...An Silverland dollar. One day Hibix opened purse and found there were some coins. He decided to buy a very nice watch in a nearby shop. He wanted to pay the exact price(without change) and he known the price would not more than m.But he didn't know the exact price of the watch.

You are to write a program which reads n,m,A1,A2,A3...An and C1,C2,C3...Cn corresponding to the number of Tony's coins of value A1,A2,A3...An then calculate how many prices(form 1 to m) Tony can pay use these coins.

# Input

The input contains several test cases. The first line of each test case contains two integers n(1 ≤ n ≤ 100),m(m ≤ 100000).The second line contains 2n integers, denoting A1,A2,A3...An,C1,C2,C3...Cn (1 ≤ Ai ≤ 100000,1 ≤ Ci ≤ 1000). The last test case is followed by two zeros.

# Output

For each test case output the answer on a single line.

# Sample Input

```
3 10
1 2 4 2 1 1
2 5
1 4 2 1
0 0
```

# Sample Output

```
8
4
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 105, m = 100005;
vector<int> d(m);
vector<int> value(n), num(n);

void completePack(int value)
{
	for (int i = value; i <= m; ++i) {
		d[i] = max(d[i], d[i - value] + value);
	}
}

void zeroOnePack(int value)
{
	for (int i = m; i >= value; --i) {
		d[i] = max(d[i], d[i - value] + value);
	}
}

void multiPack(int value, int num)
{
	if (value * num >= m) {
		completePack(value);
		return;
	}

	int k = 1;
	while (k < num) {
		zeroOnePack(value * k);
		num -= k;
		k = k * 2;
	}
	zeroOnePack(num * value);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while ((cin >> n >> m) && n && m) {
		for (int i = 1; i <= n; ++i) cin >> value[i];
		for (int i = 1; i <= n; ++i) cin >> num[i];
		for (int i = 1; i <= n; ++i) {
			multiPack(value[i], num[i]);
		}

		int cnt = 0;
		for (int i = 1; i <= m; ++i) {
			if (i == d[i]) ++cnt;
		}
		cout << cnt << endl;

		fill(d.begin(), d.end(), 0);
	}
	
    return 0;
}
```

其实相当于POJ 1276的变形，也就是判断在每一个容量$\leq m$时用前`i`种硬币是否能恰好表示出。但是这种方法在POJ会TLE。

利用多重背包存在性的解法可AC

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 105, m = 100005;
vector<int> f(m), g(m);
vector<int> value(n), num(n);



int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while ((cin >> n >> m) && n && m) {
		for (int i = 1; i <= n; ++i) cin >> value[i];
		for (int i = 1; i <= n; ++i) cin >> num[i];
		
		f[0] = 1;
		for (int i = 1; i <= n; ++i) {
			fill(g.begin(), g.end(), 0);
			for (int j = value[i]; j <= m; ++j) {
				if (!f[j] && f[j - value[i]] && g[j - value[i]] < num[i]) {
					f[j] = 1;
					g[j] = g[j - value[i]] + 1;
				}
			}
		}
		int cnt = 0;
		for (int i = 1; i <= m; ++i) cnt += f[i];
		cout << cnt << endl;
		fill(f.begin(), f.end(), 0);
	}
	
    return 0;
}
```

时间复杂度$O(nm)$。用数组`f[j]`表示对于金额为`i`时是否可以由这些硬币组成，能组成为1，不能就是0.数组`g[j]`表示满足当前金额`j`的时候，需要第`i`种硬币的数量。如果存在一种方法是`f[j] = 1`，那么就无需再考查究竟是由哪些硬币组成，所以无需去更新。如果`f[j]= 0`，思路是考虑如果已经能组成金额为`j - value[i]`，那么只需要增加一个面额为`value[i]`的硬币即可。所以在`f[j]= 0 `时必须`f[j - value[i]] = 1`才可以继续。但是需要考虑的是目前面额为`value[i]`的硬币数量是否还能拿出来一个。那么就用另一个数组`g[j - value[i]]`来考察当金额为`j - value[i]`时使用了多少个面额为`value[i]`的硬币，必须其数量小于硬币的数量，因为如果等于，那么到了金额`j`肯定就没法拿出一个硬币来了。因为数组`g[]`是和不同硬币挂钩的，所以它需要考察下一种面额的硬币的时候初始化。而`f[]`和一个大问题对应，所以考察下一个case的之前初始化。