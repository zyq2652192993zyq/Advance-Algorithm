> # POJ-2411 Mondriaan's Dream（状态压缩DP）

# Description

Squares and rectangles fascinated the famous Dutch painter Piet Mondriaan. One night, after producing the drawings in his 'toilet series' (where he had to use his toilet paper to draw on, for all of his paper was filled with squares and rectangles), he dreamt of filling a large rectangle with small rectangles of width 2 and height 1 in varying ways.

![img](https://vj.z180.cn/91cd2a849209448a71d50fa577e5d5ed?v=1593177368)

Expert as he was in this material, he saw at a glance that he'll need a computer to calculate the number of ways to fill the large rectangle whose dimensions were integer values, as well. Help him, so that his dream won't turn into a nightmare!

# Input

The input contains several test cases. Each test case is made up of two integer numbers: the height h and the width w of the large rectangle. Input is terminated by h=w=0. Otherwise, 1<=h,w<=11.

# Output

For each test case, output the number of different ways the given rectangle can be filled with small rectangles of size 2 times 1. Assume the given large rectangle is oriented, i.e. count symmetrical tilings multiple times.

![img](https://vj.z180.cn/9275391b5c2fd4e3cb556e4ab10140b5?v=1593177368)

# Sample Input

```
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
```

# Sample Output

```
1
0
1
2
3
5
144
51205
```

-----

分析：这个其实一般归类为轮廓线DP，也算是状压DP的一种，如果是采取暴力搜索的方法（DFS + 回溯），那么时间复杂度是$O(mn2^{mn})$，肯定会超时，这里的解决方案是我们对每一行的状态用一个整数来表示，接下来的问题就是每个状态表示的含义，以及上一行的状态如何传递到下一行。对于每一行用一个`n`位二进制的数字表示，但是把他转成十进制整数来表示，便于处理。用`d[i][j]`表示第`i`行的状态为`j`，每行的状态`j`的二进制某一位为1表示此处是小矩形竖着放的上半部分，**0表示其他状态**，我们最后求解的目标是`d[m][0]`，最后一行肯定不能竖着放，所以必须所有位都是0。上一行的状态传递给下一行，假设`i-1`行的状态是`k`，第`i`行的状态是`j`，则需要：

* `(k & j) == 0`，这个表示如果`i-1`行的状态是`k`，其二进制位的某一位是1，对应下一行的二进制位必须是0，表示什么都不放。
* `k | j`的二进制中连续0的个数不能是奇数。`k | j`的二进制某一位是0，表明`k`的二进制对应的位是0，`j`的二进制位也是0，如果是奇数，那么无论上一行放还是不放，第`i`行都没办法补全（横着放）。

所以需要先预处理出究竟出`k | j`的结果，注意，不能一开始就按最大位来预处理出一个结果，因为每次输入一个`m, n`都需要针对对应的`n`位来处理。

```c++
#include <bits/stdc++.h>

using namespace std;

const int N = 1 << 11;

int m, n;
vector<vector<long long> > d(12, vector<long long>(N));
vector<bool> isLegal(N);


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> n >> m) {
		if (!n && !m) break;

		for (int i = 0; i < 1 << m; ++i) {
			int cnt = 0, hasOdd = 0;
			for (int j = 0; j < m; ++j) {
				if (i >> j & 1) hasOdd |= cnt, cnt = 0;
				else cnt ^= 1;
			}
			isLegal[i] = (hasOdd | cnt) ? false : true;
		}

		d[0][0] = 1;
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j < 1 << m; ++j) {
				d[i][j] = 0;
				for (int k = 0; k < 1 << m; ++k) {
					if ((j & k) == 0 && isLegal[j | k]) d[i][j] += d[i - 1][k];
				}
			}
		}

		cout << d[n][0] << endl;
	}

	return 0;
}
```

