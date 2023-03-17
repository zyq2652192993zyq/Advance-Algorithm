> # HDU-1525 Euclid's Game（基础博弈）

# Description

Two players, Stan and Ollie, play, starting with two natural numbers. Stan, the first player, subtracts any positive multiple of the lesser of the two numbers from the greater of the two numbers, provided that the resulting number must be nonnegative. Then Ollie, the second player, does the same with the two resulting numbers, then Stan, etc., alternately, until one player is able to subtract a multiple of the lesser number from the greater to reach 0, and thereby wins. For example, the players may start with (25,7):

25 7
11 7
4 7
4 3
1 3
1 0

an Stan wins.

# Input

The input consists of a number of lines. Each line contains two positive integers giving the starting two numbers of the game. Stan always starts.

# Output

For each line of input, output one line saying either Stan wins or Ollie wins assuming that both of them play perfectly. The last line of input contains two zeroes and should not be processed.

# Sample Input

```
34 12
15 24
0 0
```

# Sample Output

```
Stan wins
Ollie wins
```

----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <set>
#include <algorithm>

using namespace std;

bool judge(int a, int b) 
{
	int sign = 1; //1代表第一个人，0代表第二个
	if (b > a) std::swap(a, b);

	if (!a || !b) return sign;

	while (a / b < 2) {
		sign = (sign + 1) % 2;
		a -= b;

		if (!a || !b) return (sign + 1) % 2;
		if (b > a) std::swap(a, b);
	}

	return sign;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a, b;
    while ((cin >> a >> b) && a && b) {
    	if (judge(a, b)) cout << "Stan wins" << endl;
    	else cout << "Ollie wins" << endl;
    }

    return 0;
}
```

**假设石子数目为(a,b)且a >= b,如果[a/b] >= 2则先手必胜,如果[a/b]<2,那么先手只有唯一的一种取法。[a/b]表示a除以b取整后的值。**

这个规律是一本通1218取石子游戏的提示。我们来证明这个结论。

首先考虑特殊情况，其中一堆石子是0，那么胜负态确定，所以如果中间状态到了这一步，那么可以直接输出结果。

题目限定了都是正数，考虑`a == b`的情况，那么先手必输，因为只有一种取法，就是将其中一堆都取走，那么后面的人就获胜了。

因为`a,b(假设a > b)`的状态先手的人肯定有办法使这个状态变为`a%b, b`，那么先手的人是有办法去判断`a % b, b`的状态是必胜还是必败。假如`a >= 2 * b`，那么先手的人必胜，因为：

* 如果`a%b, b`的状态是必胜，那么先手的策略是取出石子，让状态变为`b + a%b, b`，那么接下来的人只能取走`b`个，那么先手的人遇到了必胜态。
* 如果`a%b, b`是必败态，那么先手就取走石子让状态变为`a%b, b`，那么下一个人就面临必败态，于是先手获胜。

所以`[a/b]>=2`先手必胜，不然先手只有一种取法，需要迭代去判断。