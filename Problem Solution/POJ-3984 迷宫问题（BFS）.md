> # POJ-3984 迷宫问题（BFS）

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
#include <vector>
#include <iostream>

using namespace std;

struct Node{
    int x, y;
    int pre;

    Node(int xElement, int yElement, int preElement): 
    x(xElement), y(yElement), pre(preElement) {}

    Node(): x(0), y(0), pre(-1) {}
};

vector<int> line(5, 0);
vector<vector<int> > ground(5, line); //存放地图
vector<vector<int> > visit(5, line); //记录地图中的点是否被访问过
int front = 0, rear = 0; 
vector<Node> queue(50);  //数组模拟队列
int movementDirection[4][2] = { {-1,0}, {1,0}, {0,-1}, {0,1} }; //四个移动方向

void BFS(int beginX, int beginY, int endX, int endY)
{
    queue[0].x = beginX; queue[0].y = beginY; queue[0].pre = -1;
    ++rear;
    visit[beginX][beginY] = 1; //标记起始点被访问

    while (front < rear){
        for (int i = 0; i < 4; ++i){
            int newX = queue[front].x + movementDirection[i][0];
            int newY = queue[front].y + movementDirection[i][1];

            if (newX < 0 || newX > 4 || newY < 0 || newY > 4 
                || visit[newX][newY] == 1 || ground[newX][newY] == 1)
                continue;

            visit[newX][newY] = 1; //新探索的点标记被访问过
            queue[rear].x = newX; queue[rear].y = newY; queue[rear].pre = front;

            if (newX == endX && newY == endY) return; //探索到终点了

            ++rear;

        }
        ++front;
    }
}

void printNode(Node current)
{
    if (current.pre == -1) cout << "(" << current.x << ", " << current.y << ")" << endl;
    else{
        printNode(queue[current.pre]);
        cout << "(" << current.x << ", " << current.y << ")" << endl;
    } 
}

int main()
{
    for (int i = 0; i < 5; ++i){
        for (int j = 0; j < 5; ++j){
            cin >> ground[i][j];
        }
    }

    BFS(0, 0, 4, 4);
    printNode(queue[rear]);

    return 0;
}
```

思路就是BFS，用了一个数组来记录访问顺序。

坑点：

* 用`vector`定义矩阵时两个`>>`中间加个空格，编译器是老版本，新版本就没问题。
* 编译器不支持列表初始化，所以还是用圆括号初始化吧，同时矩阵也不可以列表初始化
* 输出的`,`后面有个空格。