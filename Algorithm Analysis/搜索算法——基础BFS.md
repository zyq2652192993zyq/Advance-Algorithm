> # 搜索算法——基础BFS

# 围成面积

- [x] 一本通-1359：围成面积

这道题虽然在一本通归为队列，实际上考察的是BFS。很类似在线性代数里的加边法。

编程计算由`*`号围成的下列图形的面积。面积计算方法是统计`*`号所围成的闭合曲线中水平线和垂直线交点的数目。如下图所示，在10×10的二维数组中，有“*”围住了15个点，因此面积为15。

![img](http://ybt.ssoier.cn:8088/pic/1359.gif)

给整个矩阵外面套一圈-1，既然求被1包含的面积直接求解比较困难，那么可以把不被包含的0都变成-1，这样只需要计算最后矩阵0的个数即可。

这道题如果用类似泛洪算法的方法，算出来的结果是17，在倒数第二行的倒数第二列，在遍历到这里的时候，四方向搜索都没有-1，但是当遍历到它的后一个位置，却变成了-1，但是前面的点却无法再遍历到了。那么用BFS可以将找到的-1看成是病源，能感染周围的0，然后把感染的0加入队列作为新的病源。

```c++
#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > grid(12, vector<int>(12, -1));
int m = 10, n = 10;
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

struct Node
{
	int x, y;
	Node(int a, int b) : x(a), y(b) {}
};


int solve()
{
	queue<Node> q;
	for (int i = 0; i < 12; ++i) q.push(Node(0, i));
	for (int i = 0; i < 12; ++i) q.push(Node(11, i));
	for (int i = 0; i < 12; ++i) q.push(Node(i, 0));
	for (int i = 0; i < 12; ++i) q.push(Node(i, 11));

	while (!q.empty()) {
		Node tmp = q.front(); q.pop();
		for (int i = 0; i < 4; ++i) {
			int nextRow = tmp.x + direction[i][0];
			int nextCol = tmp.y + direction[i][1];
			if (0 <= nextRow && nextRow < 12 && 0 <= nextCol && nextCol < 12 && grid[nextRow][nextCol] == 0) {
				grid[nextRow][nextCol] = -1;
				q.push(Node(nextRow, nextCol));
			}
		}
	}

	int cnt = 0;
	for (int i = 1; i <= 10; ++i) {
		for (int j = 1; j <= 10; ++j) {
		    //cout << setw(2) << grid[i][j] << ' ';
			if (grid[i][j] == 0) ++cnt;
		}
		//cout << endl;
	}


	return cnt;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 1; i <= 10; ++i) {
		for (int j = 1; j <= 10; ++j) {
			cin >> grid[i][j];
		}
	}

	cout << solve() << endl;

	return 0;
}
```









典型题目

注意，在解决广搜问题前，需要熟悉hash的相关知识，不然完美哈希部分较难理解，也需要理解Cantor展开的方法。

<https://blog.csdn.net/u013480600/article/details/45066957>

- [x] POJ 3984 迷宫问题
- [x] 一本通-1330：【例8.3】最少步数（经典BFS）
- [x] 一本通-1359：围成面积
- [x] 一本通-1248：Dungeon Master（三维迷宫BFS）或 POJ 2251 Dungeon Master
- [x] 一本通-1251：仙岛求药（迷宫类型的BFS）
- [x] 一本通-1252：走迷宫（二维迷宫型BFS）
- [x] 一本通-1253：抓住那头牛（一维BFS）
- [x] 一本通-1254：走出迷宫（二维迷宫型BFS）
- [x] 一本通-1255：迷宫问题（二维迷宫BFS）
- [x] 一本通-1256：献给阿尔吉侬的花束（二维迷宫BFS）
- [x] POJ 1915 Knight Moves（迷宫型BFS）或一本通-1257：Knight Moves
- [ ] POJ 2049 Finding Nemo ==待深入思考==
- [ ] POJ 1077 Eight（八数码问题）
- [ ] POJ 2893 MxN Puzzle
- [ ] CODE[VS] 1004 四子连棋
- [ ] 双向BFS => 解决八数码问题
- [ ] A*算法 => 解决八数码问题

