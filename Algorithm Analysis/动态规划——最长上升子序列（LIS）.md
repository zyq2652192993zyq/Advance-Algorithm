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

典型题目：

- [x] LeetCode 300
- [x] POJ 2533
- [ ] NYOJ 79 拦截导弹
- [ ] NYOJ 16 嵌套矩形（实质上是求DAG 中不固定起点的最长路径）
- [ ] CODE[VS] 线段覆盖
- [ ] 硬币问题（DAG方法和完全背包的解法，记得区分一下备忘录法、自顶向下和自底向上的概念《算法导论》）
- [ ] POJ 3903 Stock Exchange
- [ ] POJ 1836
- [ ] tyoj-1241 硬币问题