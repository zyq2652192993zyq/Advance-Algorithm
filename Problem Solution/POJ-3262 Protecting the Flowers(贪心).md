> # POJ-3262 Protecting the Flowers(贪心)

# Description

Farmer John went to cut some wood and left *N* (2 ≤ *N* ≤ 100,000) cows eating the grass, as usual. When he returned, he found to his horror that the cluster of cows was in his garden eating his beautiful flowers. Wanting to minimize the subsequent damage, FJ decided to take immediate action and transport each cow back to its own barn.

Each cow *i* is at a location that is *Ti* minutes (1 ≤ *Ti* ≤ 2,000,000) away from its own barn. Furthermore, while waiting for transport, she destroys *Di* (1 ≤ *Di* ≤ 100) flowers per minute. No matter how hard he tries, FJ can only transport one cow at a time back to her barn. Moving cow *i* to its barn requires 2 × *Ti* minutes (*Ti* to get there and *Ti* to return). FJ starts at the flower patch, transports the cow to its barn, and then walks back to the flowers, taking no extra time to get to the next cow that needs transport.

Write a program to determine the order in which FJ should pick up the cows so that the total number of flowers destroyed is minimized.

# Input

Line 1: A single integer *N*
Lines 2.. *N*+1: Each line contains two space-separated integers, *Ti* and *Di*, that describe a single cow's characteristics

# Output

Line 1: A single integer that is the minimum number of destroyed flowers

# Sample Input

```
6
3 1
2 5
2 3
3 2
4 1
1 6
```

# Sample Output

```xml-dtd
86
```

-----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node
{
	long long transTime;
	long long destroy;
	bool operator<(const Node & obj) const
	{
		return (destroy * 1.0) / transTime > (obj.destroy * 1.0) / obj.transTime;
	}
};

int n = 100001;
vector<Node> sequence(n);

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	long long sum = 0;
	for (int i = 0; i < n; ++i) {
		cin >> sequence[i].transTime >> sequence[i].destroy;
		sum += sequence[i].destroy;
	}

	sort(sequence.begin(), sequence.begin() + n);
	long long res = 0;
	for (int i = 0; i < n; ++i) {
		sum -= sequence[i].destroy; //余下的破坏力
		long long time = 2 * sequence[i].transTime; //往返花费的时间
		res += sum * time;
	}
	cout << res << endl;

    return 0;
}
```

考虑剩下两头牛a和b的时候：

* 如果先送走a，则损耗为`2 * t_a * d_b`
* 如果先送走b，则损耗为`2 * t_b * d_a`

为了让损失最小，则比较上面两式可以做除法与1比较，那么相当于比较$\frac{d_a}{t_a} \quad \frac{d_b}{t_b}$.

由此作为排序的顺序，最开始出错是因为只考虑了损耗d，而忽略了时间的影响。