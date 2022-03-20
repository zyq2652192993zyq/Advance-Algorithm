> # CODE[VS] - 1116 四色问题（DFS）

# Description

给定N（小于等于8）个点的地图，以及地图上各点的相邻关系，请输出用4种颜色将地图涂色的所有方案数（要求相邻两点不能涂成相同的颜色）数据中0代表不相邻，1代表相邻

# Input Description

第一行一个整数n，代表地图上有n个点

接下来`n`行，每行`n`个整数，每个整数是0或者1。第`i`行第`j`列的值代表了第`i`个点和第`j`个点之间是相邻的还是不相邻，相邻就是1，不相邻就是0.我们保证`a[i][j] = a[j][i] （a[i,j] = a[j,i]）`

# Output Description

染色的方案数

# Sample Input

```
8
0 0 0 1 0 0 1 0
0 0 0 0 0 1 0 1
0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0
```

# Sample Output

```
15552
```

---

```c++
#include <iostream>
#include <vector>

using namespace std;

vector<int> line(8, -1);
vector<vector<int> > denseGraph(8,line);
vector<int> history(8, 0);
int cnt = 0, pointNum;

void DFS(int p)
{
    if (p == pointNum){
        ++cnt;
        return;
    }

    for (int c = 1; c <= 4; ++c){
        bool flag = true;
        for (int i = 0; i < p; ++i){
            if (denseGraph[i][p] && c == history[i]){
                flag = false;
                break;
            }
        }
        if (flag){
            history[p] = c;
            DFS(p + 1);
        }
    }
}

int main()
{
    cin >> pointNum;

    for (int i = 0; i < pointNum; ++i){
        for (int j = 0; j < pointNum; ++j){
            cin >> denseGraph[i][j];
        }
    }

    DFS(0);
    cout << cnt << endl;

    return 0;
}
```

此OJ使用的仍然是老版本编译器，所以在需要在`>>`中间加一个空格。

思路和二部图染色差不多，但是因为涉及颜色的种类增加，代码也会有所调整。

代码13-17行的思路和“哈密顿回路”思路类似，通过验证遍历的点的个数作为终止条件。所以不用考虑连通性问题。

之所以把矩阵等变量设计为全局变量，是考虑如果有多组测试用例的情况，面对多种测试用例，还需要一个重置清空的操作。