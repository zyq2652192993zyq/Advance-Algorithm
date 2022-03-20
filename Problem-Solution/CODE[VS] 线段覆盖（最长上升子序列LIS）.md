> # CODE[VS] 线段覆盖（最长上升子序列LIS）

# 描述

数轴上有n(n <= 1000) 条线段，线段的两端都是整数坐标，坐标范围在0 ~1000000，每条线段有一个价值，请从n 条线段中挑出若干条线段，使得这些线段两两不覆盖（端点可以重合）且线段价值之和最大。

# 输入

第一行一个整数n，表示有多少条线段。
接下来n行每行三个整数，ai，bi，ci，分别代表第i条线段的左端点ai，右端点bi（保证左端点<右端点）和价值ci。

# 输出

输出能获得的最大价值

# 样例输入

```
3
1 2 1
2 3 2
1 3 4
```

# 样例输出

```
4
```

----

```c++
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define maxNum 1000
vector<int> d(maxNum, 0);

void LIS(vector<int> & leftPoint, vector<int> & rightPoint, vector<int> & value) //longest increasing subsequence
{
    d[0] = value[0];
    int n = leftPoint.size();

    for (int j = 1; j < n; ++j){
        int maxValue = 0;
        for (int i = 0; i < j; ++i){
            if (rightPoint[i] <= leftPoint[j] && maxValue < d[i]) 
                maxValue = d[i];
        }
        d[j] = maxValue + value[j];
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> leftPoint(n), rightPoint(n), value(n);
    for (int i = 0; i < n; ++i){
        cin >> leftPoint[i] >> rightPoint[i] >> value[i];
    }
    LIS(leftPoint, rightPoint, value);
    cout << *max_element(d.begin(), d.begin() + n) << endl;

    return 0;
}
```

