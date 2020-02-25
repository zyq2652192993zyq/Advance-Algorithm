> # POJ-3046 Ant Counting（多重集合组合数，计数类DP）

# Description

Bessie was poking around the ant hill one day watching the ants march to and fro while gathering food. She realized that many of the ants were siblings, indistinguishable from one another. She also realized the sometimes only one ant would go for food, sometimes a few, and sometimes all of them. This made for a large number of different sets of ants!

Being a bit mathematical, Bessie started wondering. Bessie noted that the hive has T (1 <= T <= 1,000) families of ants which she labeled 1..T (A ants altogether). Each family had some number Ni (1 <= Ni <= 100) of ants.

How many groups of sizes S, S+1, ..., B (1 <= S <= B <= A) can be formed?

While observing one group, the set of three ant families was seen as {1, 1, 2, 2, 3}, though rarely in that order. The possible sets of marching ants were:

3 sets with 1 ant: {1} {2} {3}
5 sets with 2 ants: {1,1} {1,2} {1,3} {2,2} {2,3}
5 sets with 3 ants: {1,1,2} {1,1,3} {1,2,2} {1,2,3} {2,2,3}
3 sets with 4 ants: {1,2,2,3} {1,1,2,2} {1,1,2,3}
1 set with 5 ants: {1,1,2,2,3}

Your job is to count the number of possible sets of ants given the data above.

# Input

* Line 1: 4 space-separated integers: T, A, S, and B
* Lines 2..A+1: Each line contains a single integer that is an ant type present in the hive

# Output

Line 1: The number of sets of size S..B (inclusive) that can be created. A set like {1,2} is the same as the set {2,1} and should not be double-counted. Print only the LAST SIX DIGITS of this number, with no leading zeroes or spaces.

# Sample Input

```
3 5 2 3
1
2
2
1
3
```

# Sample Output

```
10
```

# Hint

INPUT DETAILS:

Three types of ants (1..3); 5 ants altogether. How many sets of size 2 or size 3 can be made?


OUTPUT DETAILS:

5 sets of ants with two members; 5 more sets of ants with three members

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int M = 1000000;
int t = 1005, a = 1005;
int s, b;
//vector<vector<int>> d(t, vector<int>(10005));
//vector<int> sequence(t);
int d[1005][10005];
int sequence[1005];

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> t >> a >> s >> b;
	for (int i = 1; i <= a; ++i) {
		int val;
		cin >> val;
		++sequence[val];
	}

	//从前i种物品一个都不取的方案只有一种
	for (int i = 0; i <= t; ++i) d[i][0] = 1;

	//计算多重集和组合数
	for (int i = 1; i <= t; ++i) {
		for (int j = 1; j <= b; ++j) {
			if (j > sequence[i])
				d[i][j] = (d[i - 1][j] + d[i][j - 1] - d[i - 1][j - sequence[i] - 1] + M) % M;
			else
				d[i][j] = (d[i - 1][j] + d[i][j - 1]) % M;
		}
	}
	//统计组成s和b的方案数
	int cnt = 0;
	for (int i = s; i <= b; ++i) cnt = (cnt + d[t][i]) % M;

	cout << cnt << endl;
	
    return 0;
}
```

如果使用模板`vector`，会TLE，但是仅仅是简单的换成数组就通过了。本题就是《挑战程序设计竞赛》多重集合组合数的模板题。

用$d[i][j]$表示从前$i$种物品中取出$j$个的组合数，可以先从前$i-1$种物品取出$j-k$个，再从第$i$种物品取出$k$个添加进来，则状态转移方程是：
$$
d[i][j] = \sum_{k =0}^{\min(j, a[i])} d[i-1][j - k] \\
if : j \leq a_i \\
d[i][j] = \sum_{k=0}^{j} d[i-1][j - k] = d[i-1][0] +d[i-1][1]+\cdots +d[i-1][j] \\
= d[i-1][j] + \sum_{k = 0} ^{j - 1} d[i-1][j - 1 - k] \\
= d[i - 1][j] + d[i][j - 1] \\
if: j > a_i \\
d[i][j] = \sum_{k=0}^{a_i} d[i-1][j - k] \\
= d[i-1][j] + d[i-1][j - 1] + \cdots + d[i-1][j -a_i]  + d[i-1][j-1-a_i] - d[i-1][j-1-a_i]\\
= d[i-1][j]- d[i-1][j-1-a_i] + \sum_{k = 0}^{a_i} d[i-1][j - 1 -k]\\
= d[i-1][j]- d[i-1][j-1-a_i] + d[i][j-1]
$$
