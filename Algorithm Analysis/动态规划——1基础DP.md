> # 动态规划——1基础DP

洛谷题单：

* https://www.luogu.com.cn/training/1435
* https://www.luogu.com.cn/training/3045
* https://blog.csdn.net/u011815404/category_7813170.html





## 矩阵中的最大正方形

- [x] LeetCode 221.最大正方形
- [x] Aizu - DPL_3_A Largest Square（《挑战程序设计竞赛》数据结构篇）
- [x]  LeetCode 1277.Count Square Submatrices with All Ones（221题的简单扩展）

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

## 走方格

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

## 传球游戏

- [x] 洛谷-P1057 传球游戏

上体育课的时候，小蛮的老师经常带着同学们一起做游戏。这次，老师带着同学们一起做传球游戏。

游戏规则是这样的：n个同学站成一个圆圈，其中的一个同学手里拿着一个球，当老师吹哨子时开始传球，每个同学可以把球传给自己左右的两个同学中的一个（左右任意），当老师再次吹哨子时，传球停止，此时，拿着球没有传出去的那个同学就是败者，要给大家表演一个节目。

聪明的小蛮提出一个有趣的问题：有多少种不同的传球方法可以使得从小蛮手里开始传的球，传了m*m*次以后，又回到小蛮手里。两种传球方法被视作不同的方法，当且仅当这两种方法中，接到球的同学按接球顺序组成的序列是不同的。比如有三个同学1号、2号、3号，并假设小蛮为1号，球传了3次回到小蛮手里的方式有1->2->3->1和1->3->2->1，共2种。

用`d[i][j]`表示传球`i`次后求落在标号为`j`的人手里的方法数。求解目标是`d[m][1]`，状态转移方程是：
$$
d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
$$
对于状态转移方程的解释：因为传球只能从相邻的位置传过来，那么标号为`j`的只能从`j-1`和`j+1`转移过来，也就是上一轮球在`j-1`和`j+1`手中。边界条件，注意`j=1`和`j=n`的情况，特殊处理。初始化，`d[1][1] = 1, d[1][n] = 1`。

```c++
#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<vector<int>> d(35, vector<int>(35));

int solve()
{
	d[1][n] = 1, d[1][2] = 1;
	for (int i = 2; i <= m; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (j == 1) d[i][j] = d[i - 1][n] + d[i - 1][2];
			else if (j == n) d[i][j] = d[i - 1][n - 1] + d[i - 1][1];
			else d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1];
		}
	}

	return d[m][1];
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	cout << solve() << endl;

	return 0;
}
```

另外如果这道题没有限制必须向相邻的人传球，而是可以传给任意一个人，那么就需要用两个数组`d[i], f[i]`，代表传球`i`次在小蛮手里和不在手里的方案数，那么：
$$
d[i] = f[i - 1] \times 1 \\
f[i] = d[i - 1] + f[i - 1] * (n - 2)
$$


