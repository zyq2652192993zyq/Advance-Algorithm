> # POJ-1041 John's trip(欧拉回路)

# Description

Little Johnny has got a new car. He decided to drive around the town to visit his friends. Johnny wanted to visit all his friends, but there was many of them. In each street he had one friend. He started thinking how to make his trip as short as possible. Very soon he realized that the best way to do it was to travel through each street of town only once. Naturally, he wanted to finish his trip at the same place he started, at his parents' house.

The streets in Johnny's town were named by integer numbers from 1 to n, n < 1995. The junctions were independently named by integer numbers from 1 to m, m <= 44. No junction connects more than 44 streets. All junctions in the town had different numbers. Each street was connecting exactly two junctions. No two streets in the town had the same number. He immediately started to plan his round trip. If there was more than one such round trip, he would have chosen the one which, when written down as a sequence of street numbers is lexicographically the smallest. But Johnny was not able to find even one such round trip.

Help Johnny and write a program which finds the desired shortest round trip. If the round trip does not exist the program should write a message. Assume that Johnny lives at the junction ending the street appears first in the input with smaller number. All streets in the town are two way. There exists a way from each street to another street in the town. The streets in the town are very narrow and there is no possibility to turn back the car once he is in the street

# Input

Input file consists of several blocks. Each block describes one town. Each line in the block contains three integers x; y; z, where x > 0 and y > 0 are the numbers of junctions which are connected by the street number z. The end of the block is marked by the line containing x = y = 0. At the end of the input file there is an empty block, x = y = 0.

# Output

Output one line of each block contains the sequence of street numbers (single members of the sequence are separated by space) describing Johnny's round trip. If the round trip cannot be found the corresponding output block contains the message "Round trip does not exist."

# Sample Input

```
1 2 1
2 3 2
3 1 6
1 2 5
2 3 3
3 1 4
0 0
1 2 1
2 3 2
1 3 3
2 4 4
0 0
0 0
```

# Sample Output

```
1 2 3 5 4 6 
Round trip does not exist.
```

---

```c++
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

int vertexNum, edgeNum, start;
vector<vector<int> > grid(50, vector<int>(2000, 0));
vector<bool> edgeUsed(2000, false);
vector<int> degree(50, 0);
stack<int> s;

void init()
{
	for (int i = 1; i <= vertexNum; ++i) 
		fill(grid[i].begin() + 1, grid[i].begin() + 1 + edgeNum, 0);

	fill(edgeUsed.begin() + 1, edgeUsed.begin() + 1 + edgeNum, false);
	fill(degree.begin() + 1, degree.begin() + 1 + vertexNum, 0);
}

bool degree_check()
{
	for (int i = 1; i <= vertexNum; ++i) {
		if (degree[i] & 1) return false;
	}
	return true;
}

void EulerCircuit(int from)
{
	for (int i = 1; i <= edgeNum; ++i) {
		if (!edgeUsed[i] && grid[from][i]) {
			edgeUsed[i] = true;
			int to = grid[from][i];
			EulerCircuit(to);
			s.push(i);
		}
	}
}

void printPath()
{
	while (!s.empty()) {
		cout << s.top() << ' ';
		s.pop();
	}
	cout << endl;
}


void solve()
{
	if (!degree_check()) cout << "Round trip does not exist." << endl;
	else EulerCircuit(start), printPath();

	init();
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int from, to, street;
	bool startFind = false;
	while (cin >> from >> to) {
		if (from == 0 && to == 0) {
			if (vertexNum) solve();
			else break;
		}
		else {
			cin >> street;
			vertexNum = max(vertexNum, max(from, to));
			edgeNum = max(edgeNum, street);

			if (!startFind) { start = min(from, to); startFind = true; } //寻找起始点

			grid[from][street] = to;
			grid[to][street] = from;
			++degree[from], ++degree[to];
		}
	}

	return 0;
}
```

题目有点长，简单翻译一下，需要走遍所有的`street`，回到起点，每条边只能走一次。输入的部分前两个数是顶点号，第三个数是边的号码，每组输入以两个0结尾，最后以两个0终止输入。如果存在欧拉回路，起始点以第一个输入的两个顶点里较小的号码组成，访问边的时候，尽可能从序号小的开始访问。如果存在回路，按顺序输出依次走过的边，否则输出`Round trip does not exist.`，注意末尾有个`.`。

很明显的欧拉回路题，不过有一点比较意外，以往的题目都是两个顶点之间只会有一条边，但是本题两个顶点间可能存在多条边，所以用矩阵`grid[from][i] = to`来表示从顶点`from`经过标号为`i`的边可以到达顶点`to`，否则为0。题目在最后一段指出图是连通的，所以就不要进行连通性检验，只需要检查节点度数是否为偶数，然后输出欧拉路径即可。

> 一个小插曲，看到来源是`Central Europe 1995`，结合题目的数据，这道题很有可能出于1995年4月4日，或者比赛当天是1995年4月4日，不影响做题的。