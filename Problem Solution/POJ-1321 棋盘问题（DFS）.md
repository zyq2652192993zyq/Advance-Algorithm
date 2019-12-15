> # POJ-1321 棋盘问题（简单路径搜索）

#Description

在一个给定形状的棋盘（形状可能是不规则的）上面摆放棋子，棋子没有区别。要求摆放时任意的两个棋子不能放在棋盘中的同一行或者同一列，请编程求解对于给定形状和大小的棋盘，摆放k个棋子的所有可行的摆放方案C。

#Input

输入含有多组测试数据。
每组数据的第一行是两个正整数，n k，用一个空格隔开，表示了将在一个n*n的矩阵内描述棋盘，以及摆放棋子的数目。 n <= 8 , k <= n
当为-1 -1时表示输入结束。
随后的n行描述了棋盘的形状：每行有n个字符，其中 # 表示棋盘区域， . 表示空白区域（数据保证不出现多余的空白行或者空白列）。

#Output

对于每一组数据，给出一行输出，输出摆放的方案数目C （数据保证C<2^31）。

# Sample Input

```
2 1
#.
.#
4 4
...#
..#.
.#..
#...
-1 -1
```

# Sample Output

```
2
1
```

---

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int boardSize, chessNum;
int sum; //方案总数
vector<int> judge(8, 0);  //记录每一列上是否放置了棋子
vector<char> line(8, ' ');
vector<vector<char>> position(8, line); //存储棋盘
int curCheess; //已经放入棋盘的棋子数

void dfs(int k)
{
    if (curCheess == chessNum){
        ++sum;
        return;
    }

    if (k >= boardSize) return;

    for (int i = 0; i < boardSize; ++i){
        if (judge[i] == 0 && position[k][i] == '#'){
            judge[i] = 1;
            ++curCheess;
            dfs(k + 1);
            judge[i] = 0;
            --curCheess;
        }
    }

    dfs(k + 1);
}

int main()
{
    while(cin >> boardSize >> chessNum){
        if (boardSize == -1 && chessNum == -1) break;
        
        fill(judge.begin(), judge.end(), 0);
        sum = 0; curCheess = 0;
        
        //记录棋盘里可以摆放棋子的列数位置
        for (int i = 0; i < boardSize; ++i){
            string line;
            cin >> line;
            for (size_t j = 0; j < line.size(); ++j)
                position[i][j] = line[j];
        }
        
        dfs(0);

        cout << sum << endl;
        
    }  

    return 0;
}
```

类似八皇后问题，但是并不是每一行都可以放置棋子，也并不是可以放置的行数是相邻的。

84行又一次调用`dfs(k + 1)`是因为如果本行不放入任何棋子，而从下一行开始搜索。

这里程序较长是因为我们增加了一个基础的`class matrix`，可以作为模板，使用起来较为方便。