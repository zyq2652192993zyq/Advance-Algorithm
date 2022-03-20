> # POJ-3984 迷宫问题（BFS最短路径）

# Description

定义一个二维数组：

```
int maze[5][5] = {
	0, 1, 0, 0, 0,
	0, 1, 0, 1, 0,
	0, 0, 0, 0, 0,
	0, 1, 1, 1, 0,
	0, 0, 0, 1, 0,
};
```

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。

# Input

一个5 × 5的二维数组，表示一个迷宫。数据保证有唯一解。

# Output

左上角到右下角的最短路径，格式如样例所示。

# Sample Input

```
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
```

# Sample Output

```
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(3, 4)
(4, 4)
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node{
	int x, y;
};

vector<vector<int> > ground(5, vector<int>(5)), visit(5, vector<int>(5, 0));
int startRow = 0, startCol = 0;
int endRow = 4, endCol = 4;
//vector<int> rowDirection = {1, -1, 0, 0}, colDirection = {0, 0, -1, 1};
int rowDirection[4] = {1, -1, 0, 0};
int colDirection[4] = {0, 0, -1, 1};
vector<Node> record(26);
vector<int> pre(26);

bool go(const int & nextRol, const int & nextCol)
{
	return (0 <= nextRol && nextRol < 5 && 0 <= nextCol && nextCol < 5 && 
				ground[nextRol][nextCol] != 1);
}

void print(int x)
{
	int t = pre[x];
	if (t == -1) {
		cout << "(0, 0)" << endl;
		return;
	}
	else print(t);
	cout << "(" << record[x].x << ", " << record[x].y << ")" << endl;
}

void BFS()
{
	visit[startRow][startCol] = 1;
	int cur = 0, next = 1;
	record[0].x = startRow;
	record[0].y = startCol;
	pre[0] = -1;

	while (cur < next) {
		int curRow = record[cur].x;
		int curCol = record[cur].y;
		if (curRow == endRow && curCol == endCol) {
			print(cur);
			return;
		}

		for (int i = 0; i < 4; ++i) {
			int nextRol = curRow + rowDirection[i];
			int nextCol = curCol + colDirection[i];
			if (go(nextRol, nextCol) && !visit[nextRol][nextCol]) {
				visit[nextRol][nextCol] = 1;
				record[next].x = nextRol;
				record[next].y = nextCol;
				pre[next] = cur;
				++next;
			}
		}
		++cur;
	}
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j){
			cin >> ground[i][j];
		}
	}
	BFS();
	
	return 0;
}
```

思路就是BFS，用了一个数组来记录访问顺序。

坑点：

* 用`vector`定义矩阵时两个`>>`中间加个空格，编译器是老版本，新版本就没问题。
* 编译器不支持列表初始化，所以还是用圆括号初始化吧，同时矩阵也不可以列表初始化
* 输出的`,`后面有个空格。

---

思路分析：

首先用一个5x5的数组`ground`来存储给出的迷宫，用一个5x5的二维数组来记录某个位置是否被访问过，0代表未访问，1代表访问过了。

因为要输出最短路径，这里不再和之前找最短步数一样用`queue`来存储，而是用数组`record`去模拟`queue`。`record`中的元素是自定义的`Node`，之所以没有选用`pair`，是因为`pair`的效率一般较低，可能会TLE，保险起见用`struct`来代替。用数组`pre`来记录路径，`pre`的每个位置`i`，也就是`pre[i]`，它保留的是父节点，也就是路径从`pre[i]`到`i`的。

用数组模拟队列，需要增加两个变量，一个是`cur`，一个是`next`，`cur`记录的是队列的首部位置，也就是在`record`中的位置，`next`用来记录尾部的位置，循环到终止位置则输出路径。

在向四个方向搜索的时候，注意一个细节，要先用`go`函数去判断下一个位置是否可以到达，然后才是判断下一个位置是否被访问过。因为如果位置互换，那么如果`nextRow = -1`，则会出现`segmental fault`。注意搜索完并找到了下一个位置，那么就存入`record`，记得要`++next`，更新尾部的位置。四个方向搜索完毕，则队列头部的位置要向后移动一个位置，所以`++cur`。

其实这个程序并不完善，主要是因为题意所致，因为题目限定了两点之间必然是可以到达的，实际上如果不能到达，比如不能到达输出-1，只需要增加一条语句即可。

输出路径采取的就是递归策略，采取递归就免去了使用栈来辅助输出路径。