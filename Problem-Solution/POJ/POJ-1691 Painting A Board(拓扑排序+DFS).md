> # POJ-1691 Painting A Board(拓扑排序+DFS)

## Description

The CE digital company has built an Automatic Painting Machine (APM) to paint a flat board fully covered by adjacent non-overlapping rectangles of different sizes each with a predefined color.
![img](POJ-1691 Painting A Board(拓扑排序+DFS).assets/dd0c5a824365fae70ef9c301363ba303.jpeg)
To color the board, the APM has access to a set of brushes. Each brush has a distinct color C. The APM picks one brush with color C and paints all possible rectangles having predefined color C with the following restrictions:
To avoid leaking the paints and mixing colors, a rectangle can only be painted if all rectangles immediately above it have already been painted. For example rectangle labeled F in Figure 1 is painted only after rectangles C and D are painted. Note that each rectangle must be painted at once, i.e. partial painting of one rectangle is not allowed.
You are to write a program for APM to paint a given board so that the number of brush pick-ups is minimum. Notice that if one brush is picked up more than once, all pick-ups are counted.

## Input

The first line of the input file contains an integer M which is the number of test cases to solve (1 <= M <= 10). For each test case, the first line contains an integer N, the number of rectangles, followed by N lines describing the rectangles. Each rectangle R is specified by 5 integers in one line: the y and x coordinates of the upper left corner of R, the y and x coordinates of the lower right corner of R, followed by the color-code of R.
Note that:

1. Color-code is an integer in the range of 1 .. 20.
2. Upper left corner of the board coordinates is always (0,0).
3. Coordinates are in the range of 0 .. 99.
4. N is in the range of 1..15.

## Output

One line for each test case showing the minimum number of brush pick-ups.

## Sample

**input**

```
1
7
0 0 2 2 1
0 2 1 6 2
2 0 4 2 1
1 2 4 4 2
1 4 3 6 1
4 0 6 4 1
3 4 6 6 2
```

**output**

````
3
```

----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> pa;



struct Node
{
    pa lu, ru, ld, rd;
    int color;

    Node() {}

    Node(int x1, int y1, int x2, int y2, int c) {
        lu = make_pair(x1, y1);
        rd = make_pair(x2, y2);
        ru = make_pair(x1, y2);
        ld = make_pair(x2, y1);
        color = c;
    }

    bool operator<(const Node & obj) const {
        return lu.first < obj.lu.first;
    }
};

vector<Node> brick(20);
vector<bool> used(30, false);
vector<int> degree(20, 0);
vector<vector<bool> > grid(20, vector<bool>(20, false));
int res, n;


void DFS(int cnt, int step, int color) {
    if (step > res) return;
    if (cnt == n) {
        res = min(res, step);
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (degree[i] == 0 && ! used[i]) {
            used[i] = true;
            int currentColor = brick[i].color;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) --degree[j];
            }

            if (currentColor == color) DFS(cnt + 1, step, currentColor);
            else DFS(cnt + 1, step + 1, currentColor);

            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) ++degree[j];
            }
            used[i] = false;
        }
    }
}



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int caseNum; cin >> caseNum;
    while (caseNum--) {
        fill(used.begin(), used.end(), false);
        for (int i = 0; i < grid.size(); ++i) {
            fill(grid[i].begin(), grid[i].end(), false);
        }
        fill(degree.begin(), degree.end(), 0);
        res = 1e9 + 7;

        cin >> n;
        for (int i = 0; i < n; ++i) {
            int x1, y1, x2, y2, c;
            cin >> x1 >> y1 >> x2 >> y2 >> c;
            brick[i] = Node(x1, y1, x2, y2, c);
        }

        sort(brick.begin(), brick.begin() + n);
        for (int i = 0; i < n; ++i) {
            int xLevel = brick[i].ld.first;
            int l = brick[i].ld.second, r = brick[i].rd.second;
            for (int j = i + 1; j < n; ++j) {
                int top = brick[j].lu.first;
                int curL = brick[j].lu.second, curR = brick[j].ru.second;
                if (top == xLevel && ((l <= curL && curL <= r) || (l <= curR && curR <= r))) {
                    grid[i][j] = grid[j][i] = true;
                    ++degree[j];
                }
            }
        }
        DFS(0, 0, -1);
        cout << res << endl;
    }


    return 0;
}
```

把砖块看做一个点，上下相邻的砖块之间相当于存在一条有向边，每次做DFS的时候从入度为0的点开始进行DFS。时间复杂度为$O(2^n)$，当只有一行，一块砖放一行，相当于暴力枚举。

不支持C++11特性。