> # UVA-10976 Fractions Again?!（不等式缩小搜索范围）

# Description

It is easy to see that for every fraction in the form 1 k (k > 0), we can always find two positive integers x and y, x ≥ y, such that:
$$
\frac{1}{k} = \frac{1}{x} + \frac{1}{y}
$$
Now our question is: can you write a program that counts how many such pairs of x and y there are for any given k?

# Input

Input contains no more than 100 lines, each giving a value of k (0 < k ≤ 10000).

# Output

For each k, output the number of corresponding (x, y) pairs, followed by a sorted list of the values of x and y, as shown in the sample output

# Sample Input

```
2
12
```

# Sample Output

```
2
1/2 = 1/6 + 1/3
1/2 = 1/4 + 1/4
8
1/12 = 1/156 + 1/13
1/12 = 1/84 + 1/14
1/12 = 1/60 + 1/15
1/12 = 1/48 + 1/16
1/12 = 1/36 + 1/18
1/12 = 1/30 + 1/20
1/12 = 1/28 + 1/21
1/12 = 1/24 + 1/24
```

------

题目里很重要的两个限制条件，$x, y$都是正整数，$x \geq y$，从而推导范围：
$$
\frac{1}{x} + \frac{1}{y} = \frac{1}{k} \leq \frac{2}{y} \\
\therefore y \leq 2k
$$
如果我们找到一个正确的答案，则$x$的结果为：
$$
x = \frac{y \times k}{y - k}
$$
为了保证`x`是整数，所以可以利用此条件来检验结果是否正确，并且`x`是正数，所以`y - k > 0`，那么得出`y`的取值范围：
$$
k < y \leq 2k
$$
从而缩小了搜索范围。

```c++
#include <bits/stdc++.h>

using namespace std;

int k;
vector<vector<int>> res(10005, vector<int>(2));
int totalNum = 0;

ostream & operator<<(ostream & os, vector<vector<int>> & v)
{
	os << totalNum << endl;
	for (int i = 0; i < totalNum; ++i) {
		os << "1/" << k << " = 1/" << v[i][0] << " + 1/" << v[i][1] << endl;
	}

	return os;
}
 
void solve()
{
	for (int y = k + 1; y <= 2 * k; ++y) {
		int numerator = k * y, denominator = y - k;
		if (numerator % denominator == 0) {
			res[totalNum][0] = numerator / denominator, res[totalNum][1] = y;
			++totalNum;
		}
	}

	sort(res.begin(), res.begin() + totalNum, [] (vector<int> & a, vector<int> & b) {
		return a[0] > b[0];
	});

	cout << res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> k) {
		totalNum = 0;
		solve();
	}

	return 0;
}
```



