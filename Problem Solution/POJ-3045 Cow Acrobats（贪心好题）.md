> # POJ-3045 Cow Acrobats（贪心好题）

# Description

Farmer John's N (1 <= N <= 50,000) cows (numbered 1..N) are planning to run away and join the circus. Their hoofed feet prevent them from tightrope walking and swinging from the trapeze (and their last attempt at firing a cow out of a cannon met with a dismal failure). Thus, they have decided to practice performing acrobatic stunts.

The cows aren't terribly creative and have only come up with one acrobatic stunt: standing on top of each other to form a vertical stack of some height. The cows are trying to figure out the order in which they should arrange themselves ithin this stack.

Each of the N cows has an associated weight (1 <= W_i <= 10,000) and strength (1 <= S_i <= 1,000,000,000). The risk of a cow collapsing is equal to the combined weight of all cows on top of her (not including her own weight, of course) minus her strength (so that a stronger cow has a lower risk). Your task is to determine an ordering of the cows that minimizes the greatest risk of collapse for any of the cows.

# Input

* Line 1: A single line with the integer N.
* Lines 2..N+1: Line i+1 describes cow i with two space-separated integers, W_i and S_i.

# Output

Line 1: A single integer, giving the largest risk of all the cows in any optimal ordering that minimizes the risk.

# Sample Input

```
3
10 3
2 5
3 3
```

# Sample Output

```
2
```

# Hint

OUTPUT DETAILS:

Put the cow with weight 10 on the bottom. She will carry the other two cows, so the risk of her collapsing is 2+3-3=2. The other cows have lower risk of collapsing.

-----

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

struct Node
{
	int weight, strength, sum;
	bool operator<(const Node & obj) const
	{
		return sum < obj.sum;
	}
};

int n = 50005, k;
vector<Node> sequence(n);

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
   	while (cin >> n) {
   		for (int i = 1; i <= n; ++i) {
   			cin >> sequence[i].weight >> sequence[i].strength;
   			sequence[i].sum = sequence[i].weight + sequence[i].strength;
   		}
   		sort(sequence.begin() + 1, sequence.begin() + 1 + n);
   		
   		long long res = -INF;
   		long long sum = 0;
   		for (int i = 1; i <= n; ++i) {
   			res = max(res, sum - sequence[i].strength);
   			sum += sequence[i].weight;
   		}

   		cout << res << endl;
   	}
	
    return 0;
}
```

首先要想到，对于相邻的两头牛，交换它们的位置，仅仅会影响他们两个的risk值
然后，对于最优系列的相邻的两头牛
w1 s1
w2 s2
最顶上的那头的顶上的牛的质量和为sum
那么第一头牛的risk就是 sum - s1   r1
第二头的为sum + w1 - s2           r2

假如交换位置之后：
sum - s2                      r3
sum + w2 - s1                 r4

不失一般性，为了得到max(r1, r2) < max(r3, r4)，看看能推出什么结论。

首先隐藏的结论是r1 < r4，r2 > r3。

如果有max(r3, r4) = r3，那么有max(r1,r2) < r3，则等价于r1< r3和r2 < r3，产生矛盾，所以必然有

max(r1, r2) < r4。

因为r1 < r4已知，则根据r2 < r4可以得到 w1 + s1 < w2 + s2。

得到重要结论：w+s越大的放在最底下，得到的最大risk会越小。

于是一个排序就可以解决问题。