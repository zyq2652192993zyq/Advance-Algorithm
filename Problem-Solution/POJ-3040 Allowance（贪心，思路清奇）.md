> # POJ-3040 Allowance（贪心，思路清奇）

# Description

As a reward for record milk production, Farmer John has decided to start paying Bessie the cow a small weekly allowance. FJ has a set of coins in N (1 <= N <= 20) different denominations, where each denomination of coin evenly divides the next-larger denomination (e.g., 1 cent coins, 5 cent coins, 10 cent coins, and 50 cent coins).Using the given set of coins, he would like to pay Bessie at least some given amount of money C (1 <= C <= 100,000,000) every week.Please help him ompute the maximum number of weeks he can pay Bessie.

# Input

* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Each line corresponds to a denomination of coin and contains two integers: the value V (1 <= V <= 100,000,000) of the denomination, and the number of coins B (1 <= B <= 1,000,000) of this denomation in Farmer John's possession.

# Output

Line 1: A single integer that is the number of weeks Farmer John can pay Bessie at least C allowance

# Sample Input

```
3 6
10 1
1 100
5 120
```

# Sample Output

```
111
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node {
	int value, num;
	bool operator<(const Node & obj) const
	{
		return value < obj.value;
	}
};

int n = 25, cash;
vector<Node> sequence(n);
vector<int> use(n); //记录每个面值的硬币使用的数量


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> cash;
	for (int i = 1; i <= n; ++i) {
		cin >> sequence[i].value >> sequence[i].num;
	}
	//根据面值从小到大排序
	sort(sequence.begin() + 1, sequence.begin() + 1 + n);

	int cnt = 0;
	while (true) {
		fill(use.begin(), use.end(), 0);
		int rest = cash;
		for (int i = n; i >= 1; --i) { //先从大到小遍历，寻找不大于剩余金额的硬币
			int tmpNum = min(rest / sequence[i].value, sequence[i].num);
			rest -= tmpNum * sequence[i].value;
			use[i] = tmpNum; //记录第i个硬币使用的数量
		}

		if (rest) { //没有凑够需要的金额
			//从价值小的开始寻找，找第一个大于剩余金额的币种
			for (int i = 1; i <= n; ++i) {
				//当前的硬币数量减去上面使用的还有剩余
				if (sequence[i].num > use[i] && sequence[i].value >= rest) {
					++use[i];
					rest = 0;
					break;
				}
			}
		}

		if (rest) break; //此时钱不够了，退出循环

		int tmpNum = INF;
		for (int i = 1; i <= n; ++i) {
			if (use[i]) { //计算出每种硬币按目前方案能维持几周
				tmpNum = min(tmpNum, sequence[i].num / use[i]);
			}
		}
		cnt += tmpNum;
		//更新剩余硬币的数量
		for (int i = 1; i <= n; ++i) {
			sequence[i].num -= use[i] * tmpNum;
		}
	}
	cout << cnt << endl;

    return 0;
}
```

这道题思路还是很少见的，但是很符合常理，先用大的面额去凑金额，但是凑出来的部分不能超过`cash`的总额，剩余的部分从小的面额开始寻找，找一个大于等于剩余金额的币种。很显然，如果都用大金额，那么到了最后肯定会造成浪费，所以用尽量小的金额来凑。

这里注意一个是从小金额开始搜寻的时候，`sequence[i].num > use[i] `不能写成`sequence[i].num > 0`，因为到这里还没有扣除`use[i]`的数值，比如一组数据：

```
1 3
2 1
```

就会造成死循环。