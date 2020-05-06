> # OpenJudge-162 Post Office（区间DP）

描述

There is a straight highway with villages alongside the highway. The highway is represented as an integer axis, and the position of each village is identified with a single integer coordinate. There are no two villages in the same position. The distance between two positions is the absolute value of the difference of their integer coordinates.
Post offices will be built in some, but not necessarily all of the villages. A village and the post office in it have the same position. For building the post offices, their positions should be chosen so that the total sum of all distances between each village and its nearest post office is minimum.
You are to write a program which, given the positions of the villages and the number of post offices, computes the least possible sum of all distances between each village and its nearest post office.

输入

Your program is to read from standard input. The first line contains two integers: the first is the number of villages V, 1 <= V <= 300, and the second is the number of post offices P, 1 <= P <= 30, P <= V. The second line contains V integers in increasing order. These V integers are the positions of the villages. For each position X it holds that 1 <= X <= 10000.

输出

The first line contains one integer S, which is the sum of all distances between each village and its nearest post office.

样例输入

```
10 5
1 2 3 6 7 9 11 22 44 50
```

样例输出

```
9
```

来源

IOI 2000

------

```c++
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

int school, n;
//dp[i][j]表示前i个村庄建立j个学校的最小和
//m[i][j]表示第i个村庄到第i个村庄到第j个村庄只建立一所学校的最小和
vector<vector<int> > d(505, vector<int>(505, INT_MAX / 2)), m(505, vector<int>(505));
vector<int> pos(505); //每个村庄的绝对坐标

int main()
{
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
    
    cin >> n >> school;
    for (int i = 1; i <= n; ++i) {
        cin >> pos[i];        
    }

    for (int i = 1; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            m[i][j] = m[i][j - 1] + pos[j] - pos[(i + j) >> 1];
        }
    }

    for (int i = 1; i <= n; ++i) d[i][1] = m[1][i];

    for (int i = 1; i <= n; ++i) {
        for (int j = 2; j <= i && j <= school; ++j) {
            for (int k = j - 1; k < i; ++k) {
                d[i][j] = min(d[i][j], d[k][j - 1] + m[k + 1][i]);
            }
        }
    }
    cout << d[n][school] << endl;

    return 0;
}
```

这道题一本通-1197：山区建小学（区间DP）基本就是一个题，只不过这里输入的是绝对坐标。