> # POJ-3276 Face The Right Way（开关问题）

# Description

Farmer John has arranged his *N* (1 ≤ *N* ≤ 5,000) cows in a row and many of them are facing forward, like good cows. Some of them are facing backward, though, and he needs them all to face forward to make his life perfect.

Fortunately, FJ recently bought an automatic cow turning machine. Since he purchased the discount model, it must be irrevocably preset to turn *K* (1 ≤ *K* ≤ *N*) cows at once, and it can only turn cows that are all standing next to each other in line. Each time the machine is used, it reverses the facing direction of a contiguous group of *K* cows in the line (one cannot use it on fewer than *K* cows, e.g., at the either end of the line of cows). Each cow remains in the same **location** as before, but ends up facing the **opposite direction**. A cow that starts out facing forward will be turned backward by the machine and vice-versa.

Because FJ must pick a single, never-changing value of *K*, please help him determine the minimum value of *K* that minimizes the number of operations required by the machine to make all the cows face forward. Also determine *M*, the minimum number of machine operations required to get all the cows facing forward using that value of *K*.

# Input

Line 1: A single integer: *N*
Lines 2.. *N*+1: Line *i*+1 contains a single character, *F* or *B*, indicating whether cow *i* is facing forward or backward.

# Output

Line 1: Two space-separated integers: *K* and *M*

# Sample Input

```
7
B
B
F
B
F
B
B
```

# Sample Output

```
3 3
```

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>

using namespace std;

const int INF = 0x0ffffff;

int n = 5005;
vector<int> sequence(n); //0代表前面，1代表后面
vector<int> f(n); //记录哪个位置需要反转

int calculate(int k)
{
	fill(f.begin(), f.end(), 0); //每次计算前需要将反转记录清零

	int sum = 0; //记录对当前i有影响的前面反转次数总和
	int cnt = 0; //记录反转次数
	for (int i = 0; i + k - 1 < n; ++i) { //保证每次一定能反转k头牛
		if ((sequence[i] + sum) & 1) { //和为奇数一定是朝向后面
			f[i] = 1;
			++cnt;
		}
		sum += f[i];
		if (i - k + 1 >= 0) sum -= f[i - k + 1];
	}
	//检验剩余不足长度k的部分是否都是正面
	for (int i = n - k + 1; i < n; ++i) {
		if ((sequence[i] + sum) & 1) {
			return -1;
		}
		if (i - k + 1 >= 0) sum -= f[i - k + 1];
	}

	return cnt;
}

void solve()
{
	int k = 0, cnt = n;
	for (int i = 1; i <= n; ++i) {
		int times = calculate(i); //记录需要反转的次数
		if (0 <= times && times < cnt) {
			cnt = times;
			k = i;
		}
	}

	cout << k << " " << cnt << endl;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
    while (cin >> n) {
    	for (int i = 0; i < n; ++i) {
    		char ch;
    		cin >> ch;
    		if (ch == 'B') sequence[i] = 1;
    		else sequence[i] = 0;
    	}
    	solve();
    }
    
    return 0;
}
```

问题的分析有几个关键点：

* 最终结果和反转次序无关，从第一头牛开始的K头牛先反转，从第二头牛开始的k头牛反转和顺序反过来得到的结果是一样的。
* 问题分析的目标是让反转次数最少，在此基础上的最小长度k。因为每头牛只有两个状态，所以反转次数为偶数不改变方向，只有奇数改变方向。为了让次数最少，如果反转1次和3次都能改变状态，那么肯定选1次。
* 对于长度k的处理。用`f[i]`代表从第`i`头牛到`i + k - 1`头牛是否反转，那么访问`i+1`的时候，`f[i]`是否反转会对当前是否反转产生影响，于是如何处理影响成为了重点。

假如考虑中间一个位置`i`，当前`f[i]`是否反转取决于前面能够影响当前状态的`f[i-k+1]...f[i-1]`，如果这些的累积影响（其实就是求和）不改变状态，那么取决于`i`自身的状态。所以求$\sum_{j = i - k + 1}^{i-1} f[j]$成了关键，记为`sum`，最终`f[i]`的状态取决于`sum+sequence[i]`。

由于每次`i`的位置向前移动一个位置，那么前面的`f[i-k+1]`就对当前没有影响了，所以就需要从`sum`里减去，这样其实`sum`就像一个滑动窗口一样，每次去掉一个就会增加一个。

但是当`i =n - k + 1`的时候，剩余的牛的头数肯定少于`k`了，这时需要去检验后面的是否都是朝向前面，如果不满足，那么返回`-1`，所以增加了`times >= 0`来过滤掉不符合的结果。

