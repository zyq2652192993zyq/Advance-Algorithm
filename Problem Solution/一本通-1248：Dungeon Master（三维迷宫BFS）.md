> # 一本通-1248：Dungeon Master（三维迷宫BFS）

【题目描述】
这题是一个三维的迷宫题目，其中用‘.’表示空地，‘#’表示障碍物，‘S’表示起点，‘E’表示终点，求从起点到终点的最小移动次数，解法和二维的类似，只是在行动时除了东南西北移动外还多了上下。可以上下左右前后移动，每次都只能移到相邻的空位，每次需要花费一分钟，求从起点到终点最少要多久。

【输入】
多组测试数据。

一组测试测试数据表示一个三维迷宫：

前三个数，分别表示层数、一个面的长和宽，后面是每层的平面图。前三个数据为三个零表示结束。

【输出】
最小移动次数。

【输入样例】
3 4 5
S....
.###.
.##..
###.#
#####
#####
##.##
##...
#####
#####
#.###
####E
1 3 3
S##
#E#
###
0 0 0

【输出样例】
Escaped in 11 minute(s).
Trapped!

------

三维迷宫，运动方向变成了6个，注意点是需要把`'E'`给修改成`.`，不然在BFS的判断条件里无法到达，或者也可以修改BFS的判断条件。

```c++
#include <bits/stdc++.h>

using namespace std;

struct Node
{
	int x, y, z;
	Node(int x, int y, int z): x(x), y(y), z(z) {}
};

int m, n, h;
vector<vector<vector<char> > > grid(105, vector<vector<char> >(105, vector<char>(105)));
vector<vector<vector<int> > > path(105, vector<vector<int> >(105, vector<int>(105, INT_MAX)));
int startX, startY, startZ;
int endX, endY, endZ;
int directionX[6] = {1, -1, 0, 0, 0, 0};
int directionY[6] = {0, 0, 1, -1, 0, 0};
int directionZ[6] = {0, 0, 0, 0, 1, -1};

ostream & operator<<(ostream & os, vector<vector<vector<int> > > & v)
{
	for (int i = 0; i < m; ++i)  {
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < h; ++k) {
				os << v[i][j][k] << ' ';
			}
			os << endl;
		}
		os << "-----------------" << endl;
	}

	return os;
}

void BFS()
{
	path[startX][startY][startZ] = 0;
	queue<Node> q;
	q.push(Node(startX, startY, startZ));

	while (!q.empty()) {
		Node tmp = q.front(); q.pop();

		if (tmp.x == endX && tmp.y == endY && tmp.z == endZ) break;

		for (int i = 0; i < 6; ++i) {
			int nextX = tmp.x + directionX[i];
			int nextY = tmp.y + directionY[i];
			int nextZ = tmp.z + directionZ[i];
			if (0 <= nextX && nextX < m && 0 <= nextY && nextY < n && 0 <= nextZ 
				&& nextZ < h && grid[nextX][nextY][nextZ] == '.') {
				path[nextX][nextY][nextZ] = path[tmp.x][tmp.y][tmp.z] + 1;
				grid[nextX][nextY][nextZ] = '#';
				q.push(Node(nextX, nextY, nextZ));
			}
		}
	}

	if (path[endX][endY][endZ] == INT_MAX) cout << "Trapped!" << endl;
	else cout << "Escaped in " << path[endX][endY][endZ] << " minute(s)." << endl;

	//cout << path;
}

void init()
{
	for (int i = 0; i < m; ++i)  {
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < h; ++k) {
				path[i][j][k] = INT_MAX;
			}
		}
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while ((cin >> m >> n >> h) && (m || n || h)) {
		for (int i = 0; i < m; ++i)  {
			for (int j = 0; j < n; ++j) {
				for (int k = 0; k < h; ++k) {
					cin >> grid[i][j][k];
					if (grid[i][j][k] == 'S') {
						startX = i; startY = j; startZ = k;
					}
					else if (grid[i][j][k] == 'E') {
						endX = i; endY = j; endZ = k;
						grid[i][j][k] = '.';
					}
				}
			}
		}

		BFS();
		init();
	}

	return 0;
}
```

