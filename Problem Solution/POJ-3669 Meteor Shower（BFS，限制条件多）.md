> # POJ-3669 Meteor Shower（BFS，限制条件多）

# Description

Bessie hears that an extraordinary meteor shower is coming; reports say that these meteors will crash into earth and destroy anything they hit. Anxious for her safety, she vows to find her way to a safe location (one that is never destroyed by a meteor) . She is currently grazing at the origin in the coordinate plane and wants to move to a new, safer location while avoiding being destroyed by meteors along her way.

The reports say that *M* meteors (1 ≤ *M* ≤ 50,000) will strike, with meteor *i* will striking point (*Xi*, *Yi*) (0 ≤ *Xi* ≤ 300; 0 ≤ *Yi* ≤ 300) at time *Ti* (0 ≤ *Ti*  ≤ 1,000). Each meteor destroys the point that it strikes and also the four rectilinearly adjacent lattice points.

Bessie leaves the origin at time 0 and can travel in the first quadrant and parallel to the axes at the rate of one distance unit per second to any of the (often 4) adjacent rectilinear points that are not yet destroyed by a meteor. She cannot be located on a point at any time greater than or equal to the time it is destroyed).

Determine the minimum time it takes Bessie to get to a safe place.

# Input

* Line 1: A single integer: *M*
* Lines 2..*M*+1: Line *i*+1 contains three space-separated integers: *Xi*, *Yi*, and *Ti*

# Output

Line 1: The minimum time it takes Bessie to get to a safe place or -1 if it is impossible.

# Sample Input

```
4
0 0 2
2 1 2
1 1 2
0 3 5
```

# Sample Output

```
5
```

----

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 
int M;

struct Node{
	int x, y, t;
};

Node curNode, nextNode;

vector<vector<int> > ground(310, vector<int>(310, -1));
int direction[5][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}, {0,0}};

int BFS()
{
	if (ground[0][0] == -1) return 0; //原点(出发点)始终没有被轰炸
	if (ground[0][0] == 0) return -1; //原点最开始就被轰炸，无路可去

	curNode.x = curNode.y = curNode.t = 0;
	queue<Node> q;
	q.push(curNode);

	while (!q.empty()) {
		curNode = q.front(); q.pop();
		for (int i = 0; i < 4; ++i) {
			nextNode.x = curNode.x + direction[i][0];
			nextNode.y = curNode.y + direction[i][1];
			nextNode.t = curNode.t + 1;
			if (nextNode.x >= 0 && nextNode.y >= 0) {
				//下一个可行点始终没有被轰炸过
				if (ground[nextNode.x][nextNode.y] == -1) return nextNode.t;
				if (nextNode.t < ground[nextNode.x][nextNode.y]) {
					ground[nextNode.x][nextNode.y] = nextNode.t; //这个后面会被轰炸的点暂时可以走
					q.push(nextNode);
				}
			}
		}
	}

	return -1;
} 



int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> M;
    for (int i = 0; i < M; ++i) {
    	int pointX, pointY, time;
    	cin >> pointX >> pointY >> time;
    	for (int j = 0; j < 5; ++j) {
    		int tmpX = pointX + direction[j][0];
    		int tmpY = pointY + direction[j][1];
    		if (0 <= tmpX && tmpX <= 300 && 0 <= tmpY && tmpY <= 300) {
    			if (ground[tmpX][tmpY] == -1) ground[tmpX][tmpY] = time;
    			else ground[tmpX][tmpY] = min(ground[tmpX][tmpY], time);
    		}
    	}
    }
    cout << BFS() << endl;

    return 0;
}
```

这道题目初看感觉限制条件很复杂，不如先采用朴素的分析方法，然后逐步优化思路。

题意是流星会袭击在时间$t_i$袭击坐标$(x_i, y_I)$以及它上下左右相邻四个点，并且规定被袭击的点是不能作为安全地点的。到了这里其实应该对问题有以下想法：

首先一个永远不被轰炸的点肯定可以作为安全的地点，但是要考虑时间的限制，也就是比如现在的时间是$curTime$，它在这个时间点能够停留的位置有一系列备选点，离$curTime$最近的时间点是$t_i$，那么在这个时间差$t_i-curTime$里，可以继续取搜索可以停留的位置，然后扩大备选范围，但是到了时间点$t_i$，发现可选的点都在轰炸范围内，则不会存在安全的点。

按照上面的思路，有一个很暴力的思路，可以把输入的轰炸坐标和时间点，按照时间点排序，搜索的时候动态去加上轰炸的点。那么这种思路其实就是模拟的方法，会发现存在很多难点，比如如何存储备选点，备选点被否决后如何从存储的可选点里面删掉，所以需要考虑是否可以一次性把轰炸点都提前进行描述，也就是站在“上帝视角”去寻找路径，按照以往的方法，可以考虑用一个矩阵去描述。

因为被轰炸的区域有一个很重要的影响因素——时间，所以不如用矩阵去存储时间，下标与被轰炸的做表对应，在考虑如何搜索的时候，考虑BFS和DFS，题目里问最短用时，那么基本上就暗示了用BFS，于是选定方法。

确定了采用BFS来解题，那么根据以往BFS的套路，一个队列存储可行的点，用矩阵来存储走过的路的长度，恰好本题是1秒走一个格子，所以两者是等价的，联系之前的分析，会发现思路不谋而合，才会坚定用BFS来解题的想法。

问题的矛盾来到了什么样的点是可以停留的点（安全的地点），在BFS里面，都会对访问过的点进行标记，那么当访问一个会被轰炸的点可能存在两种情况，第一种，t小于被轰炸的时间点，说明这个点是在t时可以被访问的，加入到队列里，大于等于显然就不能访问了。

综上所述，进行一下思路整理：

首先处理输入，对于被轰炸的点进行标记，标记的是当前点最早被轰炸的时间。

核心处理，采用BFS求解，用队列存储可行的点，点的坐标要符合范围要求。如果访问到一个值为-1的点，说明永远不被轰炸，则直接返回即可。如果这个点已经有数值，存在两种情况，一种是之前访问过的点，那么必然$curTime>=t$，另一种是被轰炸的点，又存在两种情况，一种是$curTime < t$，被轰炸的时间点较晚，暂时是可以停留的，那么加入队列，修改标记的时间值，如果$curTime >= t$，显然已经被轰炸过了，不可访问。

代码就是把上述整理的思路转化成代码，核心代码套路仍然是BFS的。