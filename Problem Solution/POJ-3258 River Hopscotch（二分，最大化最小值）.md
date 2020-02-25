> # POJ-3258 River Hopscotch（二分，最大化最小值）

# Description

Every year the cows hold an event featuring a peculiar version of hopscotch that involves carefully jumping from rock to rock in a river. The excitement takes place on a long, straight river with a rock at the start and another rock at the end, *L* units away from the start (1 ≤ *L* ≤ 1,000,000,000). Along the river between the starting and ending rocks, *N* (0 ≤ *N* ≤ 50,000) more rocks appear, each at an integral distance *Di* from the start (0 < *Di* < *L*).

To play the game, each cow in turn starts at the starting rock and tries to reach the finish at the ending rock, jumping only from rock to rock. Of course, less agile cows never make it to the final rock, ending up instead in the river.

Farmer John is proud of his cows and watches this event each year. But as time goes by, he tires of watching the timid cows of the other farmers limp across the short distances between rocks placed too closely together. He plans to remove several rocks in order to increase the shortest distance a cow will have to jump to reach the end. He knows he cannot remove the starting and ending rocks, but he calculates that he has enough resources to remove up to *M* rocks (0 ≤ *M* ≤ *N*).

FJ wants to know exactly how much he can increase the shortest distance **before\** he starts removing the rocks. Help Farmer John determine the greatest possible shortest distance a cow has to jump after removing the optimal set of *M* rocks.

# Input

Line 1: Three space-separated integers: *L*, *N*, and *M*
Lines 2.. *N*+1: Each line contains a single integer indicating how far some rock is away from the starting rock. No two rocks share the same position.

# Output

Line 1: A single integer that is the maximum of the shortest distance a cow has to jump after removing *M* rocks

# Sample Input

```
25 5 2
2
14
11
21
17
```

# Sample Output

```
4
```

# Hint

Before removing any rocks, the shortest jump was a jump of 2 from 0 (the start) to 2. After removing the rocks at 2 and 14, the shortest required jump is a jump of 4 (from 17 to 21 or from 21 to 25).

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
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 50005, k, len;
vector<int> sequence(n);

bool check(int d)
{
	int cnt = k, pre = 0;
	int pos = 0; //用来识别是否移动了最后一个石块
	for (int i = 1; i <= n + 1; ++i) {
		//如果距离差小于d就移走一个
		if (sequence[i] - sequence[pre] < d) {
			--cnt;
			pos = i;
		} 
		else pre = i;
		//能够移动的次数用完了
		if (cnt < 0) break;
	}
	//需要移动最后一块石头
	if (pos == n + 1) return false;

	return cnt >= 0;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
   	while (cin >> len >> n >> k) {
   		sequence[n + 1] = len;
   		for (int i = 1; i <= n; ++i) cin >> sequence[i];
   		//首尾无需变动
   		sort(sequence.begin() + 1, sequence.begin() + 1 + n);

   		int left = 0, right = sequence[n + 1] - sequence[0];
   		while (left < right) {
   			int mid = left + ((right - left + 1) >> 1);
   			if (check(mid)) left = mid;
   			else right = mid - 1;
   		}
   		cout << left << endl;
   }
	
    return 0;
}
```

最大化最小值的思路。不过题目有一些变形，第一块石头和最后一块石头不能动，所以用了一个变量`pos`来记录每次移走的石块的位置，只要`pos = n + 1`，说明需要移动最后一块石头，那么肯定无法实现。用变量`cnt`去记录还能够移走石块的次数，不是在`cnt = 0`的时候退出循环，而是小于0的时候退出，是因为可能存在恰好用完次数且满足条件的情况。至于`mid`的求法和POJ 2456基本是一直的思路，注意细节即可。