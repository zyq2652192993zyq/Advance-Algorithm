> # 6.10 动态规划-最长上升子序列（LIS）

设$d[i]$表示以$a_i$为终点的最长上升子序列的长度，状态转移方程：
$$
d[j]=\left\{\begin{array}{ll}
{1} & {j=1} \\
{\max \{d[i]\}+1} & {1<i<j, a_{i}<a_{j}}
\end{array}\right.
$$
核心代码

```c++
int lengthOfLIS(vector<int>& nums) {
    if (nums.size() == 0) return 0;

    int n = nums.size();
    vector<int> d(n, 0);
    d[0] = 1;

    for (int j = 1; j < n; ++j){
        int maxLength = 0;
        for (int i = 0; i < j; ++i){
            if (nums[i] < nums[j] && maxLength < d[i])
                maxLength = d[i];
        }
        d[j] = maxLength + 1;
    }

    return *max_element(d.begin(), d.end());
}
```

上面是$O(n^2)$的解法，但是在某些时间限制比较严的情况下是无法通过的，比如POJ 1631。所以需要采用二分优化将时间复杂度降到$O(nlogn)$。非常类似于单调栈的方法。

需要新开一个和原数组等长的新数组`d`，以及一个记录目前最长上升子序列长度的`len`，`d[len]`表示最长上升子序列长度为`len`时的序列末尾最小的数。比如有两个LIS为1，2，4，另一个为1，3，5，长度都是3，那么应该选择1，2，4的序列，因为末尾的数字越小，就越能给后面的数字留空间。

然后分析更新的问题，如果对于当前数字`sequence[i]`，出现`sequence[i] > d[len]`，那么更新数组`d`和`len`的值。如果出现`sequence[i] <= d[len]`，说明之前在某个长度的上升子序列的末尾最小值需要更新，，比如序列1，2，4，5，3，当访问到3的时候，长度为3的LIS需要更新末尾的值，显然我们定义的数组`d`是升序的，那么就可以利用二分查找来快速确定位置。那么就是去寻找第一个不小于目标值的数，所以用`lower_bound`。

进一步可以通过HDU 1257来理解，当时没有意识到是LIS的优化写法，其实本质上是一致的。

典型题目： 

- [x] LeetCode 300
- [x] POJ 2533 Longest Ordered Subsequence
- [x] POJ 1631 Bridging signals（二进制优化后的LIS）
- [x] HDU 1257 最少拦截系统
- [ ] NYOJ 79 拦截导弹
- [ ] NYOJ 16 嵌套矩形（实质上是求DAG 中不固定起点的最长路径）
- [ ] CODE[VS] 线段覆盖
- [ ] 硬币问题（DAG方法和完全背包的解法，记得区分一下备忘录法、自顶向下和自底向上的概念《算法导论》）
- [ ] POJ 3903 Stock Exchange
- [ ] POJ 1836
- [ ] tyoj-1241 硬币问题