> # HDU 3496 Watch The Movie（二维01背包）

# Description

New semester is coming, and DuoDuo has to go to school tomorrow. She decides to have fun tonight and will be very busy after tonight. She like watch cartoon very much. So she wants her uncle to buy some movies and watch with her tonight. Her grandfather gave them L minutes to watch the cartoon. After that they have to go to sleep.
DuoDuo list N piece of movies from 1 to N. All of them are her favorite, and she wants her uncle buy for her. She give a value Vi (Vi > 0) of the N piece of movies. The higher value a movie gets shows that DuoDuo likes it more. Each movie has a time Ti to play over. If a movie DuoDuo choice to watch she won’t stop until it goes to end.
But there is a strange problem, the shop just sell M piece of movies (not less or more then), It is difficult for her uncle to make the decision. How to select M piece of movies from N piece of DVDs that DuoDuo want to get the highest value and the time they cost not more then L.
How clever you are! Please help DuoDuo’s uncle.

# Input

The first line of the input file contains a single integer t (1 ≤ t ≤ 10), the number of test cases, followed by input data for each test case:
The first line is: N(N <= 100),M(M<=N),L(L <= 1000)
N: the number of DVD that DuoDuo want buy.
M: the number of DVD that the shop can sale.
L: the longest time that her grandfather allowed to watch.
The second line to N+1 line, each line contain two numbers. The first number is the time of the ith DVD, and the second number is the value of ith DVD that DuoDuo rated.

# Output

Contain one number. (It is less then 2^31.)
The total value that DuoDuo can get tonight.
If DuoDuo can’t watch all of the movies that her uncle had bought for her, please output 0.

# Sample Input

```
1
3 2 10
11 100
1 2
9 1
```

# Sample Output

```
3
```

-----

```c++
//这种解法是错误的
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node
{
	int time, value;
	double ratio;
	bool operator<(const Node & obj) const
	{
		return (ratio > obj.ratio || 
			(ratio == obj.ratio && value > obj.value));
	}
};

int n = 105;
vector<Node> sequence(n);
int m, l;

int oneZeroPack()
{
	//对所有电影排列，取前m项
	sort(sequence.begin() + 1, sequence.begin() + 1 + n);

	vector<int> d(1 + l);
	for (int i = 1; i <= m; ++i) {
		for (int j = l; j >= sequence[i].time; --j) {
			d[j] = max(d[j], d[j - sequence[i].time] + sequence[i].value);
		}
	}
	return d[l];
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		cin >> n >> m >> l;
		bool flag = false;
		for (int i = 1; i <= n; ++i) {
			cin >> sequence[i].time >> sequence[i].value;
			if (sequence[i].time <= l) {
				flag = true;
				sequence[i].ratio = (sequence[i].value * 1.0) / sequence[i].time;
			} 
			else sequence[i].ratio = -1;
		}
		// for (int i = 1; i <= n; ++i) {
		// 	cout << sequence[i].time << " " << sequence[i].value << " " << sequence[i].ratio << endl;
		// }
		if (flag) cout << oneZeroPack() << endl;
		else cout << 0 << endl;
	}
	
    return 0;
}
```

二维01背包的典型问题，初次遇到这个题目，从n种电影中选出m个来组成一维的01背包，想法是考虑每个电影的价值率`ratio`，价值率越高的电影越应该被选择。也恰好可以过样例。对于不在时间允许范围内的，令价值率为-1，然后排序取前m项化为01背包问题。但是这种方法我们可以举出一个反例。

比如，从3种电影选出2个，总时间限制是8，存在三组数据

```
6 9
4 5
4 6
```

如果按照上面的思路，那么只会从`6 9`和`4 6 `两组数据来考虑01背包问题，显然最优结果是选择后面两组数据。

那么问题的正确思路是采用二维01背包来考虑，把m也看成01背包，相当于增加一个维度。

用`d[i][j][k]`代表从前`i`个物品选出`j`个且总重量不超过`k`的最大价值，利用滚动数组优化后，状态转移方程是：
$$
d[i][j] = \max(d[i][j], d[i - 1][j - w[i]] + value[i])
$$

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 105;
int m, l;
vector<int> movieTime(n), value(n);

int oneZeroPack()
{
	vector<vector<int> > d(m + 1, vector<int>(l + 1, -INF));
	fill(d[0].begin(), d[0].end(), 0);
	for (int i = 1; i <= n; ++i) {
		for (int j = m; j >= 1; --j) {
			for (int k = l; k >= movieTime[i]; --k) {
				d[j][k] = max(d[j][k], d[j - 1][k - movieTime[i]] + value[i]);
			}
		}
	}

	return d[m][l] > 0 ? d[m][l] : 0;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		cin >> n >> m >> l;
		for (int i = 1; i <= n; ++i) {
			cin >> movieTime[i] >> value[i];
		}
		cout << oneZeroPack() << endl;
	}
	
    return 0;
}
```

