> # POJ-3050 Hopscotch(DFS暴力搜索)

# Description 

The cows play the child's game of hopscotch in a non-traditional way. Instead of a linear set of numbered boxes into which to hop, the cows create a 5x5 rectilinear grid of digits parallel to the x and y axes.

They then adroitly hop onto any digit in the grid and hop forward, backward, right, or left (never diagonally) to another digit in the grid. They hop again (same rules) to a digit (potentially a digit already visited).

With a total of five intra-grid hops, their hops create a six-digit integer (which might have leading zeroes like 000201).

Determine the count of the number of distinct integers that can be created in this manner.

# Input

Lines 1..5: The grid, five integers per line

# Output

Line 1: The number of distinct integers that can be constructed

# Sample Input

```
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
```

# Sample Output

```
15
```

-----

```c++
#include <iostream>
//#include <unordered_set>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> > ground(5, vector<int>(5));
//unordered_set<int> us;
set<int> us;
int direction[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void DFS(int row, int col, int step, int res)
{
    if (step == 5) {
        res = res * 10 + ground[row][col];
        us.insert(res);
        //us.emplace(res);
        return;
    }

    res = res * 10 + ground[row][col];

    for (int i = 0; i < 4; ++i) {
        int nextRow = row + direction[i][0];
        int nextCol = col + direction[i][1];
        if (0 <= nextRow && nextRow < 5 && 0 <= nextCol && nextCol < 5) {
            DFS(nextRow, nextCol, step + 1, res);
        }
    }
}

void solve()
{
    int res = 0;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            DFS(i, j, 0, res);
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            cin >> ground[i][j];
        }
    }
    solve();
    cout << us.size() << endl;
 
    return 0;
}
```

每个位置暴力搜素即可，注意POJ 不支持C++11的新特性，所以`unordered_set`，`emplace`会报CE。

另外有一个最初写的时候犯得一个错误，假如支持C++11，`us`定义成`unordered_set<vector<int>> us`是错误的，最初想到的是利用数组来保存结果，但是要注意，`unordered_set`的构造函数是被删除的，那么`vector`的构造函数自然也会被删除，所以不能这么定义。详细参见《C++ primer》