> # POJ-2236 Wireless Network（基础并查集）

# Description

An earthquake takes place in Southeast Asia. The ACM (Asia Cooperated Medical team) have set up a wireless network with the lap computers, but an unexpected aftershock attacked, all computers in the network were all broken. The computers are repaired one by one, and the network gradually began to work again. Because of the hardware restricts, each computer can only directly communicate with the computers that are not farther than d meters from it. But every computer can be regarded as the intermediary of the communication between two other computers, that is to say computer A and computer B can communicate if computer A and computer B can communicate directly or there is a computer C that can communicate with both A and B.

In the process of repairing the network, workers can take two kinds of operations at every moment, repairing a computer, or testing if two computers can communicate. Your job is to answer all the testing operations.

# Input

The first line contains two integers N and d (1 <= N <= 1001, 0 <= d <= 20000). Here N is the number of computers, which are numbered from 1 to N, and D is the maximum distance two computers can communicate directly. In the next N lines, each contains two integers xi, yi (0 <= xi, yi <= 10000), which is the coordinate of N computers. From the (N+1)-th line to the end of input, there are operations, which are carried out one by one. Each line contains an operation in one of following two formats:

1. "O p" (1 <= p <= N), which means repairing computer p.
2. "S p q" (1 <= p, q <= N), which means testing whether computer p and q can communicate.

The input will not exceed 300000 lines.

# Output

For each Testing operation, print "SUCCESS" if the two computers can communicate, or "FAIL" if not.

# Sample Input

```
4 1
0 1
0 2
0 3
0 4
O 1
O 2
O 4
S 1 4
O 3
S 1 4
```

# Sample Output

```
FAIL
SUCCESS
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <algorithm>

using namespace std;

struct Node
{
	int xPos, yPos;
};

int n = 1005;
vector<int> parent(n);
vector<int> rankNum(n); //树的高度
//vector<int> rela(n);
vector<bool> isWork(n, false); //因为输入有多行，可能存在一个已经修理好后的二次修理
vector<Node> sequence(n);
int rangeNum;

//初始化
void init(int num)
{
	for (int i = 0; i <= num; ++i) {
		parent[i] = i;
	}
}

inline int find(int x)
{
	if (x == parent[x]) return x;
	
	return parent[x] = find(parent[x]);
}

void unite(int x, int y) 
{
	x = find(x);
	y = find(y);

	if (x == y) return;

	if (rankNum[x] < rankNum[y]) parent[x] = y;
	else {
		parent[y] = x;
		if (rankNum[x] == rankNum[y]) ++rankNum[x];
	}
}

inline bool isSame(int x, int y)
{
	return find(x) == find(y);
}

inline bool isConnect(int i, int p)
{
	int x = sequence[i].xPos - sequence[p].xPos;
	int y = sequence[i].yPos - sequence[p].yPos;
	
	return x * x + y * y <= rangeNum * rangeNum;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> rangeNum;
	for (int i = 1; i <= n; ++i) cin >> sequence[i].xPos >> sequence[i].yPos;
	init(n);

	char ops;
	while (cin >> ops) {
		if (ops == 'O') {
			int p;
			cin >> p;
			if (isWork) continue;

			isWork[p] = true;
			//更新目前已知的可以相连的电脑
			for (int i = 1; i <= n; ++i) {
				if (isWork[i] && isConnect(i, p)) {
					unite(i, p);
				}
			}
		}
		else {
			int p, q;
			cin >> p >> q;
			if (isSame(p, q)) cout << "SUCCESS" << endl;
			else cout << "FAIL" << endl;
		}
	}
	
    return 0;
}
```

每修复一台电脑，就要去和所有已知的修复的电脑去判断是否可以满足合并要求，满足后进行合并。