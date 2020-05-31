> # 动态规划——区间动态规划

区间DP相较于线性DP，需要两个坐标（区间左端点、区间右端点）来描述每个维度，区间DP还是树型DP的基础，并且对记忆化搜索的理解很有帮助。

参考资料：https://blog.csdn.net/u011815404/category_7813197.html

# 石子合并

石子合并并不意味着最终题目会以石子作为背景，类似于背包问题，石子作为一种典型的代表，其实石子这个模型可以被项链、水果、矩阵等代替。

## 无顺序的情况

有N堆石子，现要将石子有序的合并成一堆，规定如下：每次只能移动**任意**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

- [x] 洛谷-P6033 合并果子 加强版（基数排序 + 单调队列）
- [x] 一本通-1369：合并果子(fruit)

数据量小的时候可以用优先级队列选出最小（大）的两个，相当于去构建一棵Huffman树；数据量很大的时候，需要挖掘隐含单调信息，用队列来进行优化，不可避免的要进行排序，这时候最保险通用的就是基数排序，然后利用单调队列求解即可。

## 线性排列的情况

- [ ] 洛谷-P5569 [SDOI2008]石子合并（线性排列的石子合并，大数据）
- [ ] POJ-1738 An old Stone Game
- [x] 一本通-1274：【例9.18】合并石子（小数据）

### 朴素区间DP

有N堆石子直线排列，现要将石子有序的合并成一堆，规定如下：每次只能移动**相邻**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。

设$d[i][j]$表示将区间`[i,j]`内的石子进行合并的最小代价，状态转移方程：
$$
d[i][j] = \min_{i \leq k < j} (d[i][k] + d[k + 1][j]) + \sum_{n = i}^{j} A_n
$$
通过状态转移方程可知，需要计算连续区间段的和，那么就需要计算前缀和。

初始化，当`i == j`的时候，就是单独的石子，并不需要合并，所以`d[i][i] = 0`，其余初始化为正无穷，求解的目标值是`d[1][n]`。

```c++
int solve()
{
    for (int i = 1; i <= n; ++i) d[i][i] = 0;
    for (int i = 1; i <= n; ++i) preSum[i] = preSum[i - 1] + seq[i - 1];

    for (int len = 2; len <= n; ++len) { //根据长度划分阶段
        for (int i = 1; i <= n - len + 1; ++i) { //左端点
            int j = i + len - 1; //右端点
            for (int k = i; k < j; ++k) d[i][j] = min(d[i][j], d[i][k] + d[k + 1][j]);
            d[i][j] += preSum[j] - preSum[i - 1];
        }
    }

    return d[1][n];
}
```

未经优化的情况下，时间复杂度是$O(n^3)$，空间复杂度是$O(n^2)$。

### 四边形不等式

**时间优化**

时间复杂度$O(n^3)$，比如洛谷-P5569，三次方的算法肯定会TLE的，所以需要进行优化。四边形不等式进行优化，时间复杂度优化到$O(n^2)$。主要参考了《算法竞赛进阶指南》中的证明。

**四边形不等式定义**：设$w(i, j)$是整数集合上的二元函数，对于定义域上任意整数$a \leq b \leq c \leq d$，都有
$$
w(a, d) + w(b, c) \geq w(a,c) + w(b, d)
$$
就认为函数$w(i, j)$满足四边形不等式。

**四边形不等式的等价定义**：如果对于定义域上的任意整数$a, b$，有$a < b$，都有$w(a, b + 1) + w(a + 1, b) \geq w(a, b) + w(a + 1, b + 1)$，那么称函数$w(i, j)$满足四边形不等式。

证明：

对于$a < c$，有$w(a, c + 1) + w(a + 1, c) \geq w(a, c) + w(a+1, c+1)$

对于$a + 1 < c$，有$w(a + 1, c + 1) + w(a + 2, c) \geq w(a + 1, c) + w(a + 2, c + 1)$

上面两式相加：
$$
w(a, c+1)+w(a+2, c)\geq w(a, c) + w(a+2, c+1) \\
当a + 2< c时，有w(a,c+1)+w(a+3, c) \geq w(a, c) + w(a+3,c+1)\\
令a+3 = b\\
\therefore a \leq b \leq c, w(a, c + 1) + w(b, c) \geq w(a, c) + w(b, c + 1)
$$

上面这样构造不等式意味着b取遍`[a,c]`之间的数值，不等式仍然成立。但是上面的还缺少一个数字`d`，其实只需要将`b`视为`a`，然后继续按照`b < d`和`b +1< d, b+2<d`的思路，就可以得到：
$$
\forall a \leq b \leq c \leq d, w(a,d) + w(b, c) \geq w(a, c) + w(b, d)
$$
于是就证明了四边形不等式。










```c++
int solve()
{
    for (int i = 1; i <= n; ++i) { 
        d[i][i] = 0; 
        p[i][i] = i; 
        preSum[i] = preSum[i - 1] + seq[i - 1];
    }

    for (int len = 1; len < n; ++len) { //枚举区间长度
        for (int i = 1; i + len <= n; ++i) { //区间左端点
            int j = i + len; //区间右端点
            for (int k = p[i][j - 1]; k <= p[i + 1][j]; ++k) {
                if (d[i][k] + d[k + 1][j] + preSum[j] - preSum[i - 1] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k + 1][j] + preSum[j] - preSum[i - 1];
                    p[i][j] = k;
                }
            }
        }
    }

    return d[1][n];
}
```











### Garsia-Wachs算法

Garsia-Wachs算法可以将空间复杂度优化到$O(n)$，时间复杂度优化到$O(n \log n)$。该算法深刻的揭示了石子合并的本质是最优树问题，详细的证明在《计算机程序设计艺术》第三卷的6.2.2节里。















## 环形排列的情况

- [ ] P1880 [NOI1995]石子合并

有N堆石子环形排列，现要将石子有序的合并成一堆，规定如下：每次只能移动**相邻**的2堆石子合并，合并花费为新合成的一堆石子的数量。求将这N堆石子合并成一堆的总花费最小（或最大）。







# 山区建小学

- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624



# 括号匹配

括号匹配也是很典型的一种区间DP问题，因为括号问题的背景性很强，所以单独拿出来在《典型问题——括号相关的问题》做了总结。



# 机器分配

- [x] 一本通-1266：【例9.10】机器分配 或 洛谷-P2066 机器分配

【题目描述】
总公司拥有高效设备M台，准备分给下属的N个分公司。各分公司若获得这些设备，可以为国家提供一定的盈利。问：如何分配这M台设备才能使国家得到的盈利最大？求出最大盈利值。其中M≤15，N≤10。分配原则：每个公司有权获得任意数目的设备，但总台数不超过设备数M.

【输入】
第一行有两个数，第一个数是分公司数N，第二个数是设备台数M；

接下来是一个N*M的矩阵，表明了第 I个公司分配 J台机器的盈利。

【输出】
第一行输出最大盈利值；

接下N行，每行有2个数，即分公司编号和该分公司获得设备台数。

【输入样例】

```
3 3           //3个分公司分3台机器
30 40 50
20 30 50
20 25 30
```

【输出样例】

```
70                                         //最大盈利值为70
1 1                                        //第一分公司分1台
2 1                                        //第二分公司分1台
3 1                                        //第三分公司分1台
```

用`d[i][j]`代表前`i`个公司分得`j`台机器所能获得最大价值，状态转移方程（state transition equation）是：
$$
d[i][j] = \max(d[i - 1][k] + \text{value}[i][j - k]), 0 \leq k \leq j
$$
思路就是前`i-1`个公司分配`k`台机器，最后一个公司分配`j-k`台，取所有价值中的最大值。注意题目条件里数据范围在20，所以$O(n^3)$是可行的。另外路径输出的技巧也很值得学习。

```c++
#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<vector<int> > d(20, vector<int>(20)), 
	value(20, vector<int>(20)), pre(20, vector<int>(20));

void PathPrint(int i, int j, int sum)
{
	if (!i) return; //递归终止条件
	for (int k = 0; k <= j; ++k) {
		if (sum == d[i - 1][k] + value[i][j - k]) {
			PathPrint(i - 1, k, d[i - 1][k]);
			cout << i << ' ' << (j - k) << endl;
			break;
		}
	}
}

void solve()
{
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			for (int k = 0; k <= j; ++k) {
				d[i][j] = max(d[i][j], d[i - 1][k] + value[i][j - k]);
			}
		}
	}
	cout << d[n][m] << endl;
	PathPrint(n, m, d[n][m]);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			cin >> value[i][j];
		}
	}

	solve();

	return 0;
}
```



# 删除回文子数组

- [x] LeetCode 1246.删除回文子数组

Given an integer array `arr`, in one move you can select a palindromic subarray `arr[i], arr[i+1], ..., arr[j]` where `i <= j`, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

**Example 1:**

```
Input: arr = [1,2]
Output: 2
```

**Example 2:**

```
Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
```

**Constraints:**

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= 20`

------

```c++
class Solution {
public:
    int minimumMoves(vector<int>& arr) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int n = arr.size();
        vector<vector<int>> d(n + 1, vector<int>(n + 1, INT_MAX - 1000));
        //每个字母单独删除需要1次
        d[0][0] = 0;
        for (int i = 1; i <= n; ++i) d[i][i] = 1; 
        for (int i = 1; i <= n; ++i) d[i][i - 1] = 0;

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i < n - len + 1; ++i) {
                int j = i + len - 1;
                //第i个字母单独删除
                d[i][j] = 1 + d[i + 1][j];
                if (arr[i] == arr[i + 1]) 
                    d[i][j] = min(d[i][j], 1 + d[i + 2][j]);

                for (int k = i + 2; k <= j; ++k) {
                    if (arr[i] == arr[k])
                        d[i][j] = min(d[i][j], d[i + 1][k - 1] + d[k + 1][j]);
                }
            }
        }

        return d[0][n - 1];
    }
};
```

数组长度小于100，意味着可能存在多重循环。

设$d[i][j]$代表删除区间$[i,j]$的字符的最少操作数。初始$d[i][i] = 1, d[i][i - 1] = 0$。其余为较大数值。

* 删除字符的方式可以单独删除，那么$d[i][j] = \min (d[i][j], 1 + d[i + 1][j])$
* 如果$arr[i] == arr[i + 1]$，意味着构成回文串，可以一起删除：$d[i][j] = \min (d[i][j], 1 + d[i + 2][j])$。
* 另外如果$k \geq i + 2, arr[i] == arr[k]$，那么意味着$arr[i], arr[k]$可以和区间$[i + 1, k - 1]$一起删除，那么$d[i][j] = \min (d[i][j], d[i + 1][k - 1] + d[k + 1][j])$。

注意一下边界条件即可。

另外这道题还是微软的笔试题，可以变化的形式比如改成字符串，方法一样，引起重视。







典型题目：

- [x] Uva 348 Optimal Array Multiplication Sequence/ ZOJ 1276
- [x] 洛谷 1063 能量项链
- [ ] [十个利用矩阵乘法解决的经典题目](http://www.matrix67.com/blog/archives/276)
- [ ] 洛谷 P1880 石子合并
- [ ] 洛谷 P1005 矩阵取数游戏
- [x] POJ 3280 Cheapest Palindrome
- [x] POJ-2955 Brackets （最大括号匹配，区间动态规划）
- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624
- [x] OpenJudge 162:Post Office