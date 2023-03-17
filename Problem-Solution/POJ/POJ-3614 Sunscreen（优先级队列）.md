> # POJ-3614 Sunscreen（优先级队列）

# Description

To avoid unsightly burns while tanning, each of the *C* (1 ≤ *C* ≤ 2500) cows must cover her hide with sunscreen when they're at the beach. Cow *i* has a minimum and maximum *SPF* rating (1 ≤ *minSPFi* ≤ 1,000; *minSPFi* ≤ *maxSPFi* ≤ 1,000) that will work. If the *SPF* rating is too low, the cow suffers sunburn; if the *SPF* rating is too high, the cow doesn't tan at all........

The cows have a picnic basket with *L* (1 ≤ *L* ≤ 2500) bottles of sunscreen lotion, each bottle *i* with an *SPF* rating *SPFi* (1 ≤ *SPFi* ≤ 1,000). Lotion bottle *i* can cover *coveri* cows with lotion. A cow may lotion from only one bottle.

What is the maximum number of cows that can protect themselves while tanning given the available lotions?

# Input

* Line 1: Two space-separated integers: *C* and *L*
* Lines 2..*C*+1: Line *i* describes cow *i*'s lotion requires with two integers: *minSPFi* and *maxSPFi*
* Lines *C*+2..*C*+*L*+1: Line *i*+*C*+1 describes a sunscreen lotion bottle *i* with space-separated integers: *SPFi* and *coveri*

# Output

A single line with an integer that is the maximum number of cows that can be protected while tanning

# Sample Input

```
3 2
3 10
2 5
1 5
6 2
4 1
```

# Sample Output

```
2
```

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct SPF
{
	int minSPF, maxSPF;
	bool operator<(const SPF & obj) const
	{
		return (minSPF < obj.minSPF || 
			(minSPF == obj.minSPF && maxSPF < obj.maxSPF))
	}
};

struct Node
{
	int value, num;
	bool operator<(const Node & obj) const
	{
		return value < obj.value;
	}
};

int C = 2505, L = 2505;
vector<SPF> cow(C);
vector<Node> bottle(L);

int sunScreen()
{
	sort(cow.begin() + 1, cow.begin() + 1 + C);
	sort(bottle.begin() + 1, bottle.begin() + 1 + L);

	int pos = 1;
	int cnt = 0;
	priority_queue<int, vector<int>, greater<int> > pq;

	for (int i = 1; i <= L; ++i) {
		//所有满足minSPF<=value的牛进入队列
		while (pos <= C && bottle[i].value >= cow[pos].minSPF) {
			pq.push(cow[pos++].maxSPF);
		}

		while (!pq.empty() && bottle[i].num) {
			int tmp = pq.top(); pq.pop();
			if (bottle[i].value > tmp) continue;
			++cnt;
			--bottle[i].num;
		}
	}

	return cnt;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> C >> L;
	for (int i = 1; i <= C; ++i) cin >> cow[i].minSPF >> cow[i].maxSPF;
	for (int i = 1; i <= L; ++i) cin >> bottle[i].value >> bottle[i].num;
	cout << sunScreen() << endl;
	
    return 0;
}
```

每个牛的SPF按左端点（`minSPF`）排序，防晒霜按照从小到大排序，思路是首先防晒霜的防护范围应该不小于`minSPF`，然后选择最小的`maxSPF`，这样后面防晒霜的防护范围增大的时候，后面可选择的范围也就相应增大了。