> # 洛谷-P5569 [SDOI2008]石子合并（区间DP-Garsia-Wachs算法）

## 题目描述

在一个操场上摆放着一排 N*N* 堆石子。现要将石子有次序地合并成一堆。规定每次只能选相邻的 22 堆石子合并成新的一堆，并将新的一堆石子数记为该次合并的得分。

试设计一个算法，计算出将 N*N* 堆石子合并成一堆的最小得分。

## 输入格式

第一行一个整数 N*N*。

接下来 N*N* 行，第 i*i* 行一个整数 a_i*a**i*，代表第 i*i* 堆石子的石子数。

## 输出格式

输出将所有石子合并为一堆的最小得分。

## 输入输出样例

**输入 #1**

```
4
1
1
1
1
```

**输出 #1**

```
8
```

## 说明/提示

N \leq 40000, a_i \leq 200*N*≤40000,*a**i*≤200

**请注意 N\*N\* 的范围（来自上传者的提示）**

------

```c++
//洛谷-P5569 [SDOI2008]石子合并
#include <bits/stdc++.h>

using namespace std;

vector<int> seq(40005);
int n;

int stoneMerge()
{
	int start = 1, res = 0;
	int i;
	while (start < n - 1) {
		for (i = start; i < n - 1; ++i) {
			if (seq[i] < seq[i + 2]) {
				seq[i + 1] += seq[i], res += seq[i + 1];
				for (int j = i; j > start; --j) seq[j] = seq[j - 1];
				++start;
				int j = i + 1;
				while (seq[j] > seq[j - 1] && j > start) {
					std::swap(seq[j], seq[j - 1]);
					--j;
				}
				break;
			}
		}
		if (i == n - 1) {
			seq[n - 1] += seq[n];
			res += seq[--n];
		}
	}
	res += seq[n - 1] + seq[n];

	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> seq[i];

	cout << stoneMerge() << endl;

	return 0;
}
```

详细解释在《动态规划——区间DP》里，石子合并的线性排列情况的优化，Garsia-Wachs算法可以将空间复杂度优化到$O(n)$，时间复杂度优化到$O(n \log n)$。该算法深刻的揭示了石子合并的本质是最优树问题，详细的证明在《计算机程序设计艺术》第三卷的6.2.2节里。

这里只写构造方法：

假定数据存储在数组`seq`里，下标从$1$ 到 $n$

1. 找到满足$\text{seq}[i]< \text{seq}[i+2]$的最小下标 $i$
2. 将$\text{seq}[i]$的数据加到$\text{seq}[i+1]$，同时代价`res`加上 $\text{seq}[i+1]$的数据
3. 从列表清除$\text{seq}[i]$的数据
4. 在列表中寻找满足$\text{seq}[j] > \text{seq}[i+1], j \leq i$的最大$j$
5. 将$\text{seq}[0] = +\infty, \text{seq}[n + 1] = +\infty$处理

如果利用数组模拟并利用`insert`和`erase`性能会比较差，我们这里选择用数组模拟列表。











