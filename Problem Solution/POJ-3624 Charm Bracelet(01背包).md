> # POJ-3624 Charm Bracelet(01背包)

# Description

Bessie has gone to the mall's jewelry store and spies a charm bracelet. Of course, she'd like to fill it with the best charms possible from the *N* (1 ≤ *N* ≤ 3,402) available charms. Each charm *i* in the supplied list has a weight *Wi* (1 ≤ *Wi* ≤ 400), a 'desirability' factor *Di* (1 ≤ *Di* ≤ 100), and can be used at most once. Bessie can only support a charm bracelet whose weight is no more than *M* (1 ≤ *M* ≤ 12,880).

Given that weight limit as a constraint and a list of the charms with their weights and desirability rating, deduce the maximum possible sum of ratings.

# Input

* Line 1: Two space-separated integers: *N* and *M*
* Lines 2..*N*+1: Line *i*+1 describes charm *i* with two space-separated integers: *Wi* and *Di*

# Output

Line 1: A single integer that is the greatest sum of charm desirabilities that can be achieved given the weight constraints

# Sample Input

```
4 6
1 4
2 6
3 12
2 7
```

# Sample Output

```
23
```

-----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n = 3402, totalWeight = 12880;
vector<int> w(n + 1), v(n + 1);

int zeroOnePack()
{
	vector<int> d(totalWeight + 1, 0);
	for (int i = 1; i <= n; ++i) {
		for (int j = totalWeight; j >= w[i]; --j) {
			d[j] = max(d[j], d[j - w[i]] + v[i]);
		}
	}
	return d[totalWeight];
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> totalWeight;
	
	for (int i = 1; i <= n; ++i) cin >> w[i] >> v[i];
	cout << zeroOnePack() << endl;
}
```

