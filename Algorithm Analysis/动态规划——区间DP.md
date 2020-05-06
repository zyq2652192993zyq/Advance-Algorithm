> # 6.6 动态规划-区间动态规划

区间类动态规划是线性动态规划的扩展，它在分阶段地划分问题时，与阶段中元素出现的顺序和由前一阶段的哪些元素合并而来由很大的关系。令状态  表示将下标位置  到  的所有元素合并能获得的价值的最大值，那么  ，  为将这两组元素合并起来的代价。

区间 DP 的特点：

**合并** ：即将两个或多个部分进行整合，当然也可以反过来；

**特征** ：能将问题分解为能两两合并的形式；

**求解** ：对整个问题设最优值，枚举合并点，将问题分解为左右两个部分，最后合并两个部分的最优值得到原问题的最优值。

> 上面出自OI Wiki <https://oi-wiki.org/dp/interval/>

解题思路：

有环和无环情况：

有环情况下两种思路，一种是把环拆分，逐个求解，也就是枚举的办法，但是相当于复杂度指数又增加了一级；第二种思路就是

优化方法：四边形不等式和Garsia-Wachs算法，尤其针对石子合并问题，证明主要参见《计算机程序设计艺术第三卷》的6.2.2节，用二叉树的性质去证明。还可以参考《guide to competitive programming》里面的15.4节，数学方法证明。

# 山区建小学

- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624





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

用`d[i][j]`代表第`i`个公司分得`j`台机器所能获得最大价值，状态转移方程（state transition equation）是：
$$
d[i][j] = \max(d[i - 1][k] + value[i][j - k]), 0 \leq k \leq j
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





典型题目：

- [x] Uva 348 Optimal Array Multiplication Sequence/ ZOJ 1276
- [x] 洛谷 1063 能量项链
- [ ] [十个利用矩阵乘法解决的经典题目](http://www.matrix67.com/blog/archives/276)
- [ ] 洛谷 P1880 石子合并
- [ ] 洛谷 P1005 矩阵取数游戏
- [x] POJ 3280 Cheapest Palindrome
- [x] poj2955 Brackets （最大括号匹配，区间动态规划）
- [x] 一本通-1197：山区建小学（区间DP）也是OpenJudge 7624
- [x] OpenJudge 162:Post Office