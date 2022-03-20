> #HDU-1024 Max Sum Plus Plus(动态规划 最大M子段和)

# Problem Description

Now I think you have got an AC in Ignatius.L's "Max Sum" problem. To be a brave ACMer, we always challenge ourselves to more difficult problems. Now you are faced with a more difficult problem.

Given a consecutive number sequence S*1*, S*2*, S*3*, S*4* ... S*x*, ... S*n* (1 ≤ x ≤ n ≤ 1,000,000, -32768 ≤ S*x* ≤ 32767). We define a function sum(i, j) = S*i* + ... + S*j* (1 ≤ i ≤ j ≤ n).

Now given an integer m (m > 0), your task is to find m pairs of i and j which make sum(i*1*, j*1*) + sum(i*2*, j*2*) + sum(i*3*, j*3*) + ... + sum(i*m*, j*m*) maximal (i*x* ≤ i*y* ≤ j*x* or i*x* ≤ j*y* ≤ j*x* is not allowed).

But I`m lazy, I don't want to write a special-judge module, so you don't have to output m pairs of i and j, just output the maximal summation of sum(i*x*, j*x*)(1 ≤ x ≤ m) instead. ^_^

# Input

Each test case will begin with two integers m and n, followed by n integers S*1*, S*2*, S*3* ... S*n*.
Process to the end of file.

# Output

Output the maximal summation described above in one line.

# Sample Input

```
1 3 1 2 3
2 6 -1 4 -2 3 -2 3
```

#Sample Output

```
6
8
```

---

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

const int inf=0x0ffffff;

int main()
{
    int m, n;
    while(cin >> m >> n){
        vector<int> nums(n + 1);
        for (int i = 1; i <= n; ++i)
            cin >> nums[i];

        int tmpMax;
        vector<int> d(n + 1), prev(n + 1);
        for (int i = 1; i <= m; ++i){
            tmpMax = -inf;
            for (int j = i; j <= n; ++j){
                d[j] = max(d[j - 1], prev[j - 1]) + nums[j];
                prev[j - 1] = tmpMax;
                tmpMax = max(tmpMax, d[j]);
            }
        }

        cout << tmpMax << endl;
    }

    return 0;
}
```

设状态为$d[i,j]$，表示前j 项分为$i$ 段的最大和，且第$i $段必须包含$S[j]$，则状态转移方程如下：
$$
d[i, j]=\max \{d[i, j-1]+S[j], \max \{d[i-1, t]+S[j]\}\}, 其中 i \leq j \leq n, i-1 \leq t<j \\
\text {target }=| \max \{d[m, j]\}，其中m \leq j \leq n
$$

* 情况一，$S[j] $包含在第$i $段之中，$d[i; j -1] + S[j]$。
* 情况二，$S[j]$独立划分为一段，$max{d[i-1,t] + S[j]}$

上述两种情况不需要二维数组，只需要两个一维数组，$d[j]$表示现阶段最大值，$prev[j-1]$表示上一阶段最大值。

注意点：

程序21行：`for (int j = i; j <= n; ++j)`，从1开始遍历错误。