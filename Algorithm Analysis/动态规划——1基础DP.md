> # 动态规划——1基础DP

洛谷题单：

* https://www.luogu.com.cn/training/1435
* https://www.luogu.com.cn/training/3045
* https://blog.csdn.net/u011815404/category_7813170.html





# 矩阵中的最大正方形

- [x] LeetCode 221.最大正方形
- [x] Aizu - DPL_3_A Largest Square（《挑战程序设计竞赛》数据结构篇）

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

```
输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
```

用`d[i][j]`代表从`(i, j)`向左上角所能扩展的最大正方形的边长。状态转移方程是：
$$
d[i][j] = min(d[i - 1][j], min(d[i - 1][j - 1], d[i][j - 1])) + 1;
$$
也就是其左上、上方、左侧元素中最小的值加1。

![image-20200425103611172](D:\Kylin\Advance-Algorithm\Algorithm Analysis\动态规划——1基础DP.assets\image-20200425103611172.png)

```c++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int m = matrix.size(); if (!m) return 0;
        int n = matrix[0].size(); if (!n) return 0;

        vector<vector<int>> d(m + 1, vector<int>(n + 1, 0));
        int maxLen = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '1') d[i][j] = 1;
                maxLen |= d[i][j];
            }
        }

        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] == '1') {
                    d[i][j] = min(d[i - 1][j], min(d[i - 1][j - 1], d[i][j - 1])) + 1;
                    maxLen = max(maxLen, d[i][j]);
                }
            }
        }

        return maxLen * maxLen;
    }
};
```

时间复杂度$O(m \times n)$，空间复杂度$O(m \times n)$。

# 走方格

- [x] 一本通-1284：摘花生
- [x] 一本通-1287：最低通行费
- [x] LeetCode 62.Unique Paths
- [x] LeetCode 63.Unique Paths II

这种模型一般是从矩阵的左上角开始，走到矩阵的右下角，限定只能向下或者向右移动（或者变成`n * n`的矩阵，最多走`2*n-1`步，两个的意思是一样的）。常见的问题是：

* 格点上存在障碍，从左上角走到右下角的方法数，如果数字很大，对$10^9+7$取模
* 每个格点存在一定物品，物品价值不同，问到终点所能得到的最大价值。

虽然提问的形式千奇百怪，但是模型是不变的，对于动态规划问题来讲，就是状态转移方程的转移形式是类似的，变化的只是数组`d[i][j]`所表示的含义。`d[i][j]`的状态从其左侧或者上方转移过来，前提是这两个位置要在矩阵范围内。

针对方案数，则显然是两个位置的方案数的和：
$$
d[i][j] = d[i - 1][j] + d[i][j - 1]
$$
对于最大价值，显然是两个位置的价值转移过来，加上对应位置的价值，两者取最大值。
$$
d[i][j] = \max(d[i][j - 1], d[i - 1][j]) + value[i][j]
$$
需要注意的就是初始化问题，比如第一种方案数的问法，第一行和第一列需要初始化，方法是如果第一行或第一列存在一个障碍，那么这个障碍后面的都无法初始化，因为很显然，仅以行为例，第一行仅能从第一行的前一个位置转移过来。

针对价值问题，第一行或列的价值就等于当前价值加上前一个位置的最大价值。（类似于前缀和）

