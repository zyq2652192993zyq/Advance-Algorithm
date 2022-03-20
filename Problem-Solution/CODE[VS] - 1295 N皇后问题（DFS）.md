> #CODE[VS] - 1295 N皇后问题（DFS） 

# Description

在n×n格的棋盘上放置彼此不受攻击的n个皇后。按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。n后问题等价于再n×n的棋盘上放置n个皇后，任何2个皇后不妨在同一行或同一列或同一斜线上。

# Input

给定棋盘的大小n (n ≤ 13)

# Output

输出整数表示有多少种放置方法。

# Sample Input

```
8
```

# Sample Output

```
92
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> position(13, 0);
int sum = 0, queensNum;

bool place(int k, int i)
{
    for (int j = 0; j < k; ++j){
        if (position[j] == i ||
            abs(j - k) == abs(position[j] - i))
            return false;
    }

    return true;
}

void nQueens(int k, int num)
{
    for (int i = 0; i < queensNum; ++i){
        if (place(k, i)){ //在第k行，第i列是否可以放置
            position[k] = i;
            if (k == queensNum - 1){
                ++sum;
                return;
            }
            else nQueens(k+1, queensNum);
        }
    }
}

int main()
{
    cin >> queensNum;

    nQueens(0, queensNum);

    cout << sum << endl;

    return 0;
}
```

和上面程序的主要区别在于，我们不用去考虑棋盘如何表示（即是否选用二维数组），考虑是否在同一对角线上，则或者“行数-列数”的值相同（主对角线平行方向），或者“行数 + 列数”的值相同（副对角线平行方向）。