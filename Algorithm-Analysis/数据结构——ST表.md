> # 数据结构——ST表

参考资料：

* https://www.bilibili.com/video/BV1LW411e7jo

用于解决 **可重复贡献问题** 的数据结构。

Sparse-Table算法是Tarjan发明的，预处理时间是$O(n \log n)$，查询只需要$O(1)$，常数很小。

模板题型（洛谷P3865）：

求静态区间最大值或最小值，给出一个$n$个元素的数组$A_1,A_2,\cdots, A_n$，设计一个数据结构，支持查询操作Query(L,R): 计算$min(A_L,A_{L+1},\cdots,A_R)$.

用$d[i][j]$表示从$i$开始，长度为$2^j$的一段元素中的最小值，则可以利用递推关系计算$d[i][j] = \min(d[i][j - 1],d[i + 2^{j-1}, j -1])$.原理图如下：

![1582371490919](F:\Project\ACM-Algorithm\Algorithm Analysis\assets\1582371490919.png)

因为$2^j \leq n$，所以数组$d$元素个数不超过$n\log n$，每一项在常数时间内计算完完毕，所以总时间为$O(n \log n)$。

查询操作，令$k$为满足$2^k \leq R - L + 1$的最大整数，则以$L$开头、以$R$结尾的两个长度为$2^k$的区间合起来覆盖了区间$[L, R]$。

```c++
//洛谷P3865
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>

using namespace std;

int n = 100005, m;
//log2(1e5) = 16.6096，log2(2000000) = 20.931
//vector<vector<int>> d(n, vector<int>(21));
int d[100005][21];

void init()
{
	//当j为0的时候，肯定就是元素本身
	for (int i = 1; i <= n; ++i) scanf("%d", &d[i][0]);
	//根据递推关系完善d[i][j]
	for (int j = 1; (1 << j) <= n; ++j) {
		for (int i = 1; i + (1 << j) - 1 <= n; ++i) {
			d[i][j] = max(d[i][j - 1], d[i + (1 << (j - 1))][j - 1]);
		}
	}
}

int RMQ(int L, int R)
{
	int k = log2(R - L + 1);

	return max(d[L][k], d[R - (1 << k) + 1][k]);
}


int main()
{
	// std::ios_base::sync_with_stdio(false);
	// cin.tie(NULL);
	// cout.tie(NULL);

	//cin >> n >> m;
	scanf("%d%d", &n, &m);
	init();
	while (m--) {
		int left, right;
		//cin >> left >> right;
		scanf("%d%d", &left, &right);
		//cout << RMQ(left, right) << endl;
		printf("%d\n", RMQ(left, right));
	}

	return 0;
}
```

洛谷的这个题的评测有些奇怪，因为和以往的不同，即使关了同步和选了O2优化也会TLE，改用`scanf`后从892ms立刻降到了391ms。另外，在初始化阶段，可以不用新开一个数组存储数组，直接保存在数组`d`中即可。





# 典型题目

- [x] 洛谷P3865
- [ ] LOJ 2279 降雨量
- [ ] 洛谷P2880 或 POJ 3264
- [ ] UVA 11235（算法竞赛训练指南-RMQ）