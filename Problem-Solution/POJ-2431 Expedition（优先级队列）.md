> # POJ 2431 Expedition（优先级队列）

# Description

A group of cows grabbed a truck and ventured on an expedition deep into the jungle. Being rather poor drivers, the cows unfortunately managed to run over a rock and puncture the truck's fuel tank. The truck now leaks one unit of fuel every unit of distance it travels.

To repair the truck, the cows need to drive to the nearest town (no more than 1,000,000 units distant) down a long, winding road. On this road, between the town and the current location of the truck, there are N (1 <= N <= 10,000) fuel stops where the cows can stop to acquire additional fuel (1..100 units at each stop).

The jungle is a dangerous place for humans and is especially dangerous for cows. Therefore, the cows want to make the minimum possible number of stops for fuel on the way to the town. Fortunately, the capacity of the fuel tank on their truck is so large that there is effectively no limit to the amount of fuel it can hold. The truck is currently L units away from the town and has P units of fuel (1 <= P <= 1,000,000).

Determine the minimum number of stops needed to reach the town, or if the cows cannot reach the town at all.

# Input

* Line 1: A single integer, N
* Lines 2..N+1: Each line contains two space-separated integers describing a fuel stop: The first integer is the distance from the town to the stop; the second is the amount of fuel available at that stop.
* Line N+2: Two space-separated integers, L and P

# Output

Line 1: A single integer giving the minimum number of fuel stops necessary to reach the town. If it is not possible to reach the town, output -1.

# Sample Input

```
4
4 4
5 2
11 5
15 10
25 10
```

# Sample Output

```
2
```

-----

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

struct Node
{
	int posToTown, fuel;
};

int len, oil;
vector<int> dis(1000000);

int expedition()
{
	priority_queue<int> pq;
	int pos = 0, cnt = 0; //pos记录目前的位置，cnt记录加油的次数
	while (true) {
		if (pos + oil >= len) return cnt; //可以到达终点

		if (dis[pos]) pq.push(dis[pos]); //如果是加油站

		//没有达到终点继续走
		if (oil == 0 && pq.empty()) break;
		else if (oil == 0) { //没油了就加油
			oil += pq.top(); pq.pop(); 
			++cnt;
		}

		++pos; --oil;
	}

	return -1;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	vector<Node> sequence(n);
	for (int i = 0; i < n; ++i) cin >> sequence[i].posToTown >> sequence[i].fuel;
	cin >> len >> oil;
	for (int i = 0; i < n; ++i) {
		dis[len - sequence[i].posToTown] = sequence[i].fuel;
	}
	cout << expedition() << endl;

    return 0;
}
```

题目里给出的距离是加油站距离终点的距离，为了便于处理，转化成距离出发点的距离。开一个数组，大小和距离`len`相同，然后让下标为加油站距离出发点数值的部分存储加油站可以提供的油量。

整体的思路是，一路经过的加油点，把相应的油量放入一个优先级队列，当油量为0时，从队列里取出最大的油量加上继续前进。

程序的设计是对于在位置`pos`的时候的状态进行相应的处理，保证不重不漏。最先判断时候依靠目前的油量是否可以到达终点。

不可以达到终点，那么需要继续前进，如果当前所在的位置有加油站，那么把油量放入优先级队列。然后按照正常的逻辑是先检查油箱里是否还有油，如果没有了，那么判断是否可以加油。如果无法加油，那么就需要退出返回-1，如果可以加油，那么加油次数+1.