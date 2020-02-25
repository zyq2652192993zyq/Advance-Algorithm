> # POJ-2392 Space Elevator（多重背包存在性）

# Description

The cows are going to space! They plan to achieve orbit by building a sort of space elevator: a giant tower of blocks. They have K (1 <= K <= 400) different types of blocks with which to build the tower. Each block of type i has height h_i (1 <= h_i <= 100) and is available in quantity c_i (1 <= c_i <= 10). Due to possible damage caused by cosmic rays, no part of a block of type i can exceed a maximum altitude a_i (1 <= a_i <= 40000).

Help the cows build the tallest space elevator possible by stacking blocks on top of each other according to the rules.

# Input

* Line 1: A single integer, K
* Lines 2..K+1: Each line contains three space-separated integers: h_i, a_i, and c_i. Line i+1 describes block type i.

# Output

Line 1: A single integer H, the maximum height of a tower that can be built

# Sample Input

```
3
7 40 3
5 23 8
2 52 6
```

# Sample Output

```
48
```

# Hint

OUTPUT DETAILS:

From the bottom: 3 blocks of type 2, below 3 of type 1, below 6 of type 3. Stacking 4 blocks of type 2 and 3 of type 1 is not legal, since the top of the last type 1 block would exceed height 40.

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
	int h, a, c;

	bool operator<(const Node & obj) const
	{
		return a < obj.a;
	}
};

vector<int> f(40005), g(40005);
vector<Node> sequence(405);
int n = 400;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	int maxHeight = 0;
	for (int i = 1; i <= n; ++i) {
		cin >> sequence[i].h >> sequence[i].a >> sequence[i].c;
		maxHeight = max(maxHeight, sequence[i].a);
	}
    sort(sequence.begin() + 1, sequence.begin() + 1 + n);
    
	f[0] = 1;
	for (int i = 1; i <= n; ++i) {
		fill(g.begin(), g.end(), 0);
		for (int j = sequence[i].h; j <= maxHeight; ++j) {
			if (!f[j] && f[j - sequence[i].h] && g[j - sequence[i].h] < sequence[i].c && j <= sequence[i].a) {
				f[j] = 1;
				g[j] = g[j - sequence[i].h] + 1;
			}
		}
	}
	for (int i = maxHeight; i >= 0; --i) {
		if (f[i]) {
			cout << i << endl;
			break;
		}
	}

    return 0;
}
```

和POJ 1742 Coins是同一类型题目，但是1742的题目不需要先排序，因为本题对于每个物品还有一个自身的高度限制。最大高度一定是所有高度里面的最大值，也就是上限，然后从上限往下寻找，如果`f[i]=1`，表明此高度可以达到，直接输出即可。