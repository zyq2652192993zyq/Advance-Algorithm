> # tyvj-1241 硬币问题（完全背包 或 DAG固定终点的最长最短路径）

# 题目描述

有n种硬币，面值为别为a[1],a[2],a[3]……a[n]，每种都有无限多。给定非负整数s，可以选取多少个硬币使得面值和恰好为s？输出硬币数目最小值和最大值

# 输入格式

第1行n
第2行s
第3到n+2行为n种不同的面值

# 提示

1<=n<=100
1<=s<=10000
1<=a[i]<=s

# 样例输入

```
3
6
1
2
3
```

# 样例输出

```
2
6
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//无效值，不要用0x7FFFFFFF，执行加运算后会变成负数
const int INF = 0x0FFFFFFF; 

int main()
{
    int n, totalValue;
    cin >> n;
    cin >> totalValue;

    vector<int> coin(n + 1), d(totalValue + 1, INF), f(totalValue + 1, -INF);
    for (int i = 1; i <= n; ++i)
        cin >> coin[i];

    d[0] = f[0] = 0;
    for (int i = 1; i <= n; ++i){
        for (int j = coin[i]; j <= totalValue; ++j){
            d[j] = min(d[j], d[j - coin[i]] + 1);
            f[j] = max(f[j], f[j - coin[i]] + 1);
        }
    }

    cout << d[totalValue] << endl;
    cout << f[totalValue] << endl;

    return 0;
}
```

完全背包问题，可以参考`HDU-1114 Piggy-Bank`的解法，只不过需要考虑最大值部分。两题的区别在于，前者并不一定能找到解，此题是数据保证一定能找到最小值和最大值，所以放心输出即可。