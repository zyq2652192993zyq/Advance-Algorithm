> # UVA-147 Dollars（完全背包变形）

# Description

New Zealand currency consists of $100, $50, $20, $10, and $5 notes and $2, $1, 50c, 20c, 10c and 5c
coins. Write a program that will determine, for any given amount, in how many ways that amount
may be made up. Changing the order of listing does not increase the count. Thus 20c may be made
up in 4 ways: 1×20c, 2×10c, 10c+2×5c, and 4×5c.

# Input

Input will consist of a series of real numbers no greater than $300.00 each on a separate line. Each
amount will be valid, that is will be a multiple of 5c. The file will be terminated by a line containing
zero (0.00).

#  Output

Output will consist of a line for each of the amounts in the input, each line consisting of the amount
of money (with two decimal places and right justified in a field of width 6), followed by the number of
ways in which that amount may be made up, right justified in a field of width 17.

# Sample Input

```
0.20
2.00
0.00
```

# Sample Output

```
  0.20                4
  2.00              293
```

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 11;
int moneyMax = 30005;
vector<int> value = {5,10,20,50,100,200,500,1000,2000,5000,10000};
vector<long long> d(moneyMax);

inline int getNum(double money)
{
	string s = to_string(money);
	int pos = find(s.begin(), s.end(), '.') - s.begin();

	return stoi(s.substr(0, pos)) * 100 + stoi(s.substr(pos + 1, 2));
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	d[0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = value[i]; j < moneyMax; ++j) {
			d[j] += d[j - value[i]];
		}
	}

	double money;
	while ((cin >> money) && money > 0) {
		int m = getNum(money);
		cout << setw(6) << fixed << setprecision(2) << money << setw(17) << d[m] << endl;
	}

    return 0;
}
```

用数组$d[i][j]$代表利用前`i`种货币组成`j`的方案总数，状态转移方程是：
$$
d[i][j] = sum(d[i-1][j], d[i][j-value[i]])
$$
这个方程的意思是，对于第`i`种货币，存在两种情况：

* 根本不用
* 至少用一个，转化成完全背包的问题

变成需要注意的问题，输入的数据是`double`类型，转化成`int`是存在精度损失的，所以不能简单的扩大100倍，而是先转成字符串，分别取出整数部分和小数部分的前两位，然后组成一个整数。

另外在计算过程中，方案的种数数值可能会非常大，所以应该采用`long long`的数据类型。

输出注意保留小数点后两位（针对输入的金额），以及格式化输出。

