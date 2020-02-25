> # POJ-2184 Cow Exhibition（带负数的01背包）

# Description

"Fat and docile, big and dumb, they look so stupid, they aren't much
fun..."

- Cows with Guns by Dana Lyons

The cows want to prove to the public that they are both smart and fun. In order to do this, Bessie has organized an exhibition that will be put on by the cows. She has given each of the N (1 <= N <= 100) cows a thorough interview and determined two values for each cow: the smartness Si (-1000 <= Si <= 1000) of the cow and the funness Fi (-1000 <= Fi <= 1000) of the cow.

Bessie must choose which cows she wants to bring to her exhibition. She believes that the total smartness TS of the group is the sum of the Si's and, likewise, the total funness TF of the group is the sum of the Fi's. Bessie wants to maximize the sum of TS and TF, but she also wants both of these values to be non-negative (since she must also show that the cows are well-rounded; a negative TS or TF would ruin this). Help Bessie maximize the sum of TS and TF without letting either of these values become negative.

# Input

* Line 1: A single integer N, the number of cows
* Lines 2..N+1: Two space-separated integers Si and Fi, respectively the smartness and funness for each cow.

# Output

Line 1: One integer: the optimal sum of TS and TF such that both TS and TF are non-negative. If no subset of the cows has non-negative TS and non- negative TF, print 0.

# Sample Input

```
5
-5 7
8 -6
6 -3
2 1
-8 -5
```

# Sample Output

```
8
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int sum = 200010;
vector<int> d(sum + 1, -INF); 
vector<int> smart(105), funness(105);
int n = 105;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> smart[i] >> funness[i];
		if (smart[i] <= 0 && funness[i] <= 0) {
			--i;
			--n;
			continue;
		}
	}

	d[100000] = 0;
	for (int i = 1; i <= n; ++i) {
		if (smart[i] >= 0) {
			for (int j = sum; j >= smart[i]; --j)
				d[j] = max(d[j], d[j - smart[i]] + funness[i]);
		}
		else {
			for (int j = 0; j - smart[i] <= sum; ++j) {
				d[j] = max(d[j], d[j - smart[i]] + funness[i]);
			}
		}
	}
	int res = 0;
	for (int i = 100000; i <= sum; ++i) {
		if (d[i] >= 0) res = max(res, i + d[i] - 100000);
	}
	cout << res << endl;

    return 0;
}
```

这道题目分析，对于每一个物品，都是取与不取两种状态，很明显是用01背包来解决。但是这个题目很特殊的是每个物品的状态可能有一个属性是负值（全是负值的情况在输入阶段就处理掉了）。

解决的办法是将`smart`看成是重量，`funness`看成是价值，用`d[i][j]`来表示前`i`种物品在背包容量为`j`的时候所能得到的最大价值，状态转移方程是`d[i][j] =max(d[i - 1][j], d[i-1][j - w[i]] + v[i]) `，很熟悉的套路，然后用滚动数组优化存储空间。

问题出在`j - w[i]`这里，因为`w[i]`可能为负值，比如`j = 100, w[i] = -10`，那么其数值依赖的是`d[i-1][110]`，应对这种情况，不妨将背包的“零点”移位。通常状态下，价值和重量都是正数的时候，“零点”就是数值0所在的点，但是现在存在负数，仍然想利用背包的方法来求解，那么就需要把负数的部分全部变成正数，所以需要加上一个数值大于所有物品重量的绝对值之和，本题每个物品重量小于等于1000，共100个物品，所以背包容量为100000肯定可以容纳下所有物品，但是考虑到刚才`w[i] < 0`的情况，会发现可能会出现数字超过背包容量，那么我们将背包容量翻倍，“零点”就变成了100000.

负数的影响还在于对于循环遍历的顺序，重量为正数的情况，逆序遍历已经很熟悉了，但是负数的时候我们就需要注意了，不能是逆序遍历。回顾重量为正数的时候，可以认为是大容量的背包依赖小容量的背包（从状态转移方程得出），为了确保每个物品使用一次，那么需要逆序。而负数的时候，小容量的背包依赖于大容量的背包，所以此时应该顺序遍历。

最后得出结果的时候，因为要保证重量和价值都是非负数，此时零点在100000，自然是从100000开始遍历，寻找最大值。