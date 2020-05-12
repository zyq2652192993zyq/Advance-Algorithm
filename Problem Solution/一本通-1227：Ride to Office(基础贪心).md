> # 一本通-1227：Ride to Office(基础贪心)

【题目描述】
起点与终点相隔4500米。现Charley 需要从起点骑车到终点。但是，他有个习惯，沿途需要有人陪伴，即以相同的速度， 与另外一个人一起骑。而当他遇到以更快的速度骑车的人时，他会以相应的速度跟上这个更快的人。先给定所有与Charley 同路的人各自的速度与出发时间，问Charley 以这种方式跟人，骑完4500米需要多少时间。得出的结果若是小数，则向上取整。

【输入】
输入若干组数据，每组数据第一行n(1≤n≤10000),n为0，表示输入结束，接着输入n行数据，每行2个数据，表示速度v和出发时间t，如果t<0，表示陪伴人提早出发了。

【输出】
输出对应若干行数据，每行输出1个数，表示最快到达的时间。

【输入样例】
4
20 0
25 -155
27 190
30 240
2
21 0
22 34
0

【输出样例】
780
771

-----

```c++
#include <bits/stdc++.h>

using namespace std;

const double length = 4.5;
const double EPS = 1e-6;

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

 	int n;
 	double velocity, startTime; 
 	while ((cin >> n) && n){
 		int res = INT_MAX;
 		for (int i = 0; i < n; ++i) {
 			cin >> velocity >> startTime;
 			if (startTime < -EPS) continue;
 			int cost = ceil(startTime + length / velocity * 3600);
 			res = min(res, cost);
 		}
 		cout << res << endl;
 	}

    return 0;
}
```

如果`t < 0`，那么这个数据是无用的，因为如果后续这个人的速度大于了先出发的这个人的速度，即使后面相遇，速度也不会减慢，如果后续速度小于先出发的人的速度，后续也不会相遇，所以小于0的数据是无效的。

虽然Charley的速度一直在改变，但是与他相遇的没个人的速度是不会改变的，并且每个人都会达到终点，所以在所有到达终点的人里面，时间最少的就是Charley所需要的时间。

