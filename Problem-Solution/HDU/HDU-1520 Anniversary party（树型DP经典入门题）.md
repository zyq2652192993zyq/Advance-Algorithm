> # HDU-1520 Anniversary party（树型DP经典入门题）

# Description

There is going to be a party to celebrate the 80-th Anniversary of the Ural State University. The University has a hierarchical structure of employees. It means that the supervisor relation forms a tree rooted at the rector V. E. Tretyakov. In order to make the party funny for every one, the rector does not want both an employee and his or her immediate supervisor to be present. The personnel office has evaluated conviviality of each employee, so everyone has some number (rating) attached to him or her. Your task is to make a list of guests with the maximal possible sum of guests' conviviality ratings.

# Input

Employees are numbered from 1 to N. A first line of input contains a number N. 1 <= N <= 6 000. Each of the subsequent N lines contains the conviviality rating of the corresponding employee. Conviviality rating is an integer number in a range from -128 to 127. After that go T lines that describe a supervisor relation tree. Each line of the tree specification has the form:
L K
It means that the K-th employee is an immediate supervisor of the L-th employee. Input is ended with the line
0 0

# Output

Output should contain the maximal sum of guests' ratings.

# Sample Input

```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
0 0
```

# Sample Output

```
5
```

-----

实际上就是洛谷 1352没有上司的舞会的英文版本，但是注意存在多组输入的坑。

分析：用`d[i][0]`表示当`i`不参加时的最大快乐指数和，状态转移方程：
$$
d[i][0] = \sum_{s \in \text{son}(i)} \max (d[s][0], d[s][1])
$$
上面方程的意思是，上司`i`选择不参加，那么`i`的直接下属可以选择参加，也可以选择不参加，应该选择两者中的最大值，最后对所有下属的快乐指数求和。

用`d[i][1]`表示上司`i`参加的最大快乐指数，设上司`i`个人的快乐指数是`happiness[i]`，如果上司`i`参加，那么它们的下属都不能参加，于是状态转移方程：
$$
d[i][1] = \text{happiness}[i] + \sum_{s \in \text{son}(i)} d[s][0]
$$
可以发现`d[i][1]`应该被初始化为`happiness[i]`，所以可以直接在输入阶段就初始化`d[i][1]`，这样就省下很多空间。

那么最终的结果就是`d[i][0], d[i][1]`中的最大值了。因为只需要一次遍历，时间复杂度$O(n)$，空间复杂度$O(n)$。

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

int n;
vector<vector<int>> d(6005, vector<int>(2, 0)), son(6005);
vector<bool> haveParent(6005, false);


void solve(int start)
{
	for (int i = 0; i < son[start].size(); ++i) {
		int e = son[start][i];
		solve(e);
		d[start][0] += max(d[e][0], d[e][1]);
		d[start][1] += d[e][0];
	}
}

void init()
{
	for (int i = 1; i <= n; ++i) {
		son[i].clear();
		d[i][0] = d[i][1] = 0;
	}
	fill(haveParent.begin() + 1, haveParent.begin() + 1 + n, false);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> n) {
		for (int i = 1; i <= n; ++i) cin >> d[i][1];
		int employee, boss;
		while ((cin >> employee >> boss) && !(employee == 0 && boss == 0)) {
			haveParent[employee] = true;
			son[boss].push_back(employee);
		}

		int start = 0;
		for (int i = 1; i <= n; ++i) {
			if (!haveParent[i]) { start = i; break; }
		}

		solve(start);
		cout << max(d[start][0], d[start][1]) << endl;

		init();
	}

	return 0;
}
```

