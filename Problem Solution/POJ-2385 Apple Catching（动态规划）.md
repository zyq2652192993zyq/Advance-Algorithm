> # POJ-2385 Apple Catching（动态规划）

# Description

It is a little known fact that cows love apples. Farmer John has two apple trees (which are conveniently numbered 1 and 2) in his field, each full of apples. Bessie cannot reach the apples when they are on the tree, so she must wait for them to fall. However, she must catch them in the air since the apples bruise when they hit the ground (and no one wants to eat bruised apples). Bessie is a quick eater, so an apple she does catch is eaten in just a few seconds.

Each minute, one of the two apple trees drops an apple. Bessie, having much practice, can catch an apple if she is standing under a tree from which one falls. While Bessie can walk between the two trees quickly (in much less than a minute), she can stand under only one tree at any time. Moreover, cows do not get a lot of exercise, so she is not willing to walk back and forth between the trees endlessly (and thus misses some apples).

Apples fall (one each minute) for T (1 <= T <= 1,000) minutes. Bessie is willing to walk back and forth at most W (1 <= W <= 30) times. Given which tree will drop an apple each minute, determine the maximum number of apples which Bessie can catch. Bessie starts at tree 1.

# Input

* Line 1: Two space separated integers: T and W
* Lines 2..T+1: 1 or 2: the tree that will drop an apple each minute.

# Output

Line 1: The maximum number of apples Bessie can catch without walking more than W times.

# Sample Input

```
7 2
2
1
1
2
2
1
1
```

# Sample Output

```
6
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 1001, w = 31;
vector<int> apple(n);
vector<int> d(w);

int catchNum()
{
	for (int i = 1; i <= n; ++i) {
		for (int j = 0; j <= w; ++j) {
			if ((apple[i] == 1 && !(j & 1)) || (apple[i] == 2 && (j & 1))) {
				d[j] = d[j] + 1;
				if (j > 0) d[j] = max(d[j], d[j - 1] + 1);
			}
		}
	}

	return d[w];
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> w;
	for (int i = 1; i <= n; ++i) cin >> apple[i];

	cout << catchNum() << endl;

    return 0;
}
```

写出状态转移方程即可写对正确代码。用$d[i][j]$表示前`i`分钟转移次数为`j`时能够得到的最大苹果数量。对于$d[i][j]$，每次都需要分析从一棵树转移过来与不转移的比较。也就是到了第`i`分钟，此时苹果`apple[i]`落下，那么如果转移次数还没有超过限制时，肯定是要过来接的，那么就存在不动，恰好对应的树落下苹果，需要移动过来接两种情况。因为最初在`1`号树下，移动次数为奇数的时候都是在`1`号树下，偶数的时候在`2`号树下，代码里利用位运算进行加速。另外还需要考虑的是，当第一颗苹果落下的时候，是没法移动的，所以需要增加一个判断条件。
$$
d[i][j] = \max(d[i-1][j], d[i-1][j-1]) + 1, \quad j \leq w
$$
然后发现其实和01背包的情形很接近，所以想到用滚动数组来优化存储空间。

