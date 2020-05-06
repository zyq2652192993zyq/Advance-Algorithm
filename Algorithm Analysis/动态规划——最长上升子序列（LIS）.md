> # 动态规划——最长上升子序列（LIS）

# 基本模型

如果在判断条件上存在犹豫，只需要在纸上举几个数字自然就知道属于二分的哪种情况了。

## 最长上升子序列

相当于每次去找第一个不小于目标值的数。

- [x] 一本通-1281：最长上升子序列
- [x] LeetCode 300.Longest Increasing Subsequence

```c++
int n;
vector<int> seq(1005), d(1005);

int LIS()
{
	d[1] = seq[0];
	int len = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (d[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len + 1) d[++len] = target;
		else d[left] = target;
	}

	return len;
}
```

## 最长不降子序列

相当于查找第一个大于目标值的数。

- [x]  一本通-1259：【例9.3】求最长不下降序列（附加路径输出）

```c++
int n;
vector<int> seq(205), d(205), pre(205, INT_MIN);

void print(int pos)
{
	if (pos == INT_MIN) return;

	print(pre[pos]);
	cout << seq[pos] << ' ';
}

void solve()
{
	d[1] = 0;
	d[0] = INT_MIN;
	int len = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (seq[d[mid]] <= target) left = mid + 1;
			else right = mid;
		}
		if (left == len	+ 1) {
			d[++len] = i;
			pre[i] = d[len - 1];
		}
		else {
			d[left] = i;
			pre[i] = d[left - 1];
		}
	}

	cout << "max=" << len << endl;
	print(d[len]);
	cout << endl;
}

```

这里数组`d[i] = pos`表示最长不降子序列长度为`i`的时候，以原数组下标`pos`作为结尾，用`pre[i]`记录构成最长不降子序列的前一个元素的下标。最后递归输出路径即可。

## 最长下降子序列

- [x] 一本通-1286：怪盗基德的滑翔翼（前向和后向两次计算LIS）

这时候数组`d`降序排列，相当于查找第一个小于等于目标值的数。

```c++
int n;
vector<int> seq(1005), d(1005);

int LIS()
{
	d[1] = seq[0];
	int len = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (d[mid] > target) left = mid + 1;
			else right = mid;
		}
		if (left == len + 1) d[++len] = target;
		else d[left] = target;
	}

	return len;
}
```

## 最长不升子序列

相当于查找第一个小于目标值的数。

- [x] 一本通-1289：拦截导弹

```c++
int n;
vector<int> seq(205), d(205);

int solve()
{
	d[1] = seq[0];
	int len = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (d[mid] >= target) left = mid + 1;
			else right = mid;
		}
		if (left == len + 1) d[++len] = target;
		else d[left] = target;
	}

	return len;
}
```

## 动态规划的方法

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

上面是$O(n^2)$的解法，但是在某些时间限制比较严的情况下是无法通过的，比如POJ 1631。所以需要采用二分优化将时间复杂度降到$O(nlogn)$。

## 最大上升子序列和

- [x] 一本通-1285：最大上升子序列和

一个数的序列bi，当b1<b2<...<bS的时候，我们称这个序列是上升的。对于给定的一个序列(a1,a2,...,aN)，我们可以得到一些上升的子序列(ai1,ai2,...,aiK)，这里1≤i1<i2<...<iK≤N。比如，对于序列(1,7,3,5,9,4,8)，有它的一些上升子序列，如(1,7),(3,4,8)等等。这些子序列中和最大为18，为子序列(1,3,5,9)的和。

你的任务，就是对于给定的序列，求出最大上升子序列和。注意，最长的上升子序列的和不一定是最大的，比如序列(100,1,2,3)的最大上升子序列和为100，而最长上升子序列为(1,2,3)。

其实就是LIS动态规划方法的稍微变动，用`d[i]`表示以`seq[i]`结尾的最大上升子序列和，状态转移方程是：
$$
d[i] = \max(d[i], d[j] + seq[i]), 0 \leq j < i
$$
但是需要注意一点是，数组`d[i]`的元素应该初始化为`seq[i]`。假如还是初始化为0，考虑特殊情况：

```
4
-1 -2 -100 -3
```

不初始化输出结果会为0。

```c++
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> seq(1005);
vector<int> d(1005);

int LISsum()
{
	d[0] = seq[0];
	for (int i = 1; i < n; ++i) {
		d[i] = seq[i];
		for (int j = 0; j < i; ++j) {
			if (seq[j] < seq[i]) {
				d[i] = max(d[i], d[j] + seq[i]);
			}
		}
	}

	return *max_element(d.begin(), d.begin() + n);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> seq[i];
	cout << LISsum() << endl;

	return 0;
}
```

## 合并LIS（JLIS）

- [ ] ALGOSPOT JLIS（《算法问题实战策略》8.5）



## 第K个最大自增子序列（KLIS）

- [ ] ALGOSPOT KLIS（《算法竞赛实战策略》9.7）



## 最长公共上升子序列
- [ ] 一本通-1306：最长公共子上升序列

将LIS和LCS进行结合



## 统计区间长度为k的LIS个数

- [ ] HDU 4352 XHXJ's LIS
- [x] LeetCode 115.不同的子序列（可以转化成LIS模型，也可以用普通动态规划做，注意数据溢出问题）







## 生成LIS序列

- [ ] CodeForces 1304D Shortest and Longest LIS

这种题目属于逆向思维题，以往的都是给定序列求LIS长度，现在是给定比较关系来生成序列。



## LIS路径输出

- [x] 一本通-1259：【例9.3】求最长不下降序列

**LIS路径输出用动态规划应该是最好理解的，但是也可以用$n \log n$的方法**

设有由n(1≤n≤200)个不相同的整数组成的数列，记为:b(1)、b(2)、……、b(n)且b(i)≠b(j)(i≠j)，若存在i1<i2<i3<…<ie 且有b(i1)<b(i2)<…<b(ie)则称为长度为e的不下降序列。程序要求，当原数列出之后，求出最长的不下降序列。

例如13，7，9，16，38，24，37，18，44，19，21，22，63，15。

例中13，16，18，19，21，22，63就是一个长度为7的不下降序列，同时也有7 ，9，16，18，19，21，22，63组成的长度为8的不下降序列。

【输入】
第一行为n,第二行为用空格隔开的n个整数。

【输出】
第一行为输出最大个数max(形式见样例)；

第二行为max个整数形成的不下降序列,答案可能不唯一，输出一种就可以了，本题进行特殊评测。

【输入样例】

```
14
13 7 9 16 38 24 37 18 44 19 21 22 63 15
```

【输出样例】

```
max=8
7 9 16 18 19 21 22 63
```

```c++
//动态规划方法输出路径
#include <bits/stdc++.h>

using namespace std;

vector<int> num(205);
int n;
vector<int> d(205);
vector<int> pre(205, -1);


void print(int pos)
{
	if (pos == -1) return;
	else {
		print(pre[pos]);
		cout << num[pos] << ' ';
	}
}


void LIS()
{
	if (n == 1) {
		cout << "max=" << 1 << endl;
		cout << num[0] << endl;
		return;
	}

	d[0] = 1;
	for (int j = 1; j < n; ++j) {
		int maxLen = 0;
		int pos = -1;
		for (int i = 0; i < j; ++i) {
			if (num[i] <= num[j] && maxLen < d[i]) {
				maxLen = d[i];
				pos = i;
			}
		}
		d[j] = maxLen + 1;
		pre[j] = pos;
	}

	int position = -1;
	int res = INT_MIN;
	for (int i = 0; i < n; ++i) {
		if (d[i] > res) {
			res = d[i];
			position = i;
		}
	}

	cout << "max=" << res << endl;
	print(position);
	cout << endl;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> num[i];
	LIS();

	return 0;
}
```

# 拦截导弹（二分优化）

- [x] 洛谷-P1020 导弹拦截（最典型的LIS练习，两种形式）

【题目描述】
某国为了防御敌国的导弹袭击，发展出一种导弹拦截系统。但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于前一发的高度。某天，雷达捕捉到敌国的导弹来袭。由于该系统还在试用阶段，所以只有一套系统，因此有可能不能拦截所有的导弹。

输入导弹依次飞来的高度（雷达给出的高度数据是不大于30000的正整数，导弹数不超过1000），计算这套系统最多能拦截多少导弹，如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。

【输入】
输入导弹依次飞来的高度。

【输出】
第一行：最多能拦截的导弹数；

第二行：要拦截所有导弹最少要配备的系统数。

【输入样例】

```
389 207 155 300 299 170 158 65
```

【输出样例】

```
6
2
```

```c++
#include <bits/stdc++.h>

using namespace std;

int n = 0;
vector<int> seq(1005);
vector<int> num(1005); //计算最长不升子序列
vector<int> cnt(1005); //计算所需的导弹数

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int height;
	while (cin >> height) {
		seq[n++] = height;
	}

	num[1] = seq[0];
	cnt[1] = seq[0];
	int len1 = 1, len2 = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];
		//caculate LIS
		int left = 1, right = len1 + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (num[mid] >= target) left = mid + 1;
			else right = mid;
		}
		if (left == len1 + 1) num[++len1] = target;
		else num[left] = target;

		//calculate the number of the system
		left = 1, right = len2 + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (cnt[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len2 + 1) cnt[++len2] = target;
		else cnt[left] = target;
	}
	cout << len1 << endl;
	cout << len2 << endl;

	return 0;
}
```

# 城市架桥

- [x] POJ 1631 Bridging signals（二进制优化后的LIS）或 HDU 1950 Bridging signals
- [x] 一本通-1263：【例9.7】友好城市(和POJ 1631一样的方法)

【题目描述】
Palmia国有一条横贯东西的大河，河有笔直的南北两岸，岸上各有位置各不相同的N个城市。北岸的每个城市有且仅有一个友好城市在南岸，而且不同城市的友好城市不相同。

每对友好城市都向政府申请在河上开辟一条直线航道连接两个城市，但是由于河上雾太大，政府决定避免任意两条航道交叉，以避免事故。编程帮助政府做出一些批准和拒绝申请的决定，使得在保证任意两条航线不相交的情况下，被批准的申请尽量多。

【输入】
第1行，一个整数N(1≤N≤5000)，表示城市数。

第2行到第n+1行，每行两个整数，中间用1个空格隔开，分别表示南岸和北岸的一对友好城市的坐标。(0≤xi≤10000)

【输出】
仅一行，输出一个整数，表示政府所能批准的最多申请数。

【输入样例】

```
7
22 4
2 6
10 3
15 12
9 8
17 17
4 2
```

【输出样例】

```
4
```

```c++
#include <bits/stdc++.h>

using namespace std;

struct Node
{
	int start, end;
	bool operator<(const Node & obj) const
	{
		return start < obj.start;
	}
};

int n;
vector<Node> seq(5005);
vector<int> d(5005);

int solve()
{
	sort(seq.begin(), seq.begin() + n);

	d[1] = seq[0].end;
	int len = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i].end;

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (d[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len + 1) d[++len] = target;
		else d[left] = target;
	}

	return len;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> seq[i].start >> seq[i].end;
	}

	cout << solve() << endl;

	return 0;
}
```

# 合唱队形

- [x] 一本通-1264：【例9.8】合唱队形
- [x] 一本通-1283：登山（背景不同，模型相同）

【题目描述】
N位同学站成一排，音乐老师要请其中的(N−K)位同学出列，使得剩下的KK位同学排成合唱队形。

合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1,2,…,K，他们的身高分别为T1,T2,…,TK，则他们的身高满足T1<T2<…<Ti,Ti>Ti+1>…>TK(1≤i≤K)。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

【输入】
输入的第一行是一个整数N（2≤N≤100），表示同学的总数。第二行有n个整数，用空格分隔，第i个整数Ti（130≤Ti≤230）是第i位同学的身高（厘米）。

【输出】
输出包括一行，这一行只包含一个整数，就是最少需要几位同学出列。

【输入样例】
8
186 186 150 200 160 130 197 220

【输出样例】
4

```c++
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> seq(105), forwardSeq(105), backwardSeq(105);
vector<int> d(105), c(105);

int solve()
{
	forwardSeq[1] = seq[0];
	int len1 = 1;
	d[1] = 1;
	for (int i = 1; i < n; ++i) {
		int target = seq[i];

		int left = 1, right = len1 + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (forwardSeq[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len1 + 1) {
			forwardSeq[++len1] = target;
			d[i + 1] = len1;
		}
		else {
			forwardSeq[left] = target;
			d[i + 1] = left;
		}
	}

	backwardSeq[1] = seq[n - 1];
	int len2 = 1;
	c[n] = 1;
	for (int i = n - 2; i >= 0; --i) {
		int target = seq[i];

		int left = 1, right = len2 + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (backwardSeq[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len2 + 1) {
			backwardSeq[++len2] = target;
			c[i + 1] = len2;
		}
		else {
			backwardSeq[left] = target;
			c[i + 1] = left;
		}
	}

	int maxVal = -1;
	for (int i = 1; i <= n; ++i) {
		maxVal = max(maxVal, c[i] + d[i] - 1);
	}

	return n - maxVal;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> seq[i];
	cout << solve() << endl;

	return 0;
}
```

第一遍正向遍历，寻找最长上升子序列，用`d[i]`表示以`seq[i - 1]`结尾的最长上升子序列长度，第二遍逆序遍历，用`c[i]`记录以`seq[i - 1]`结尾的最长上升子序列长度（从后往前看），那么最终形成的先上升后下降的最大长度是`d[i] + c[i] + 1`，因为第`i`个人被重复计算了一次。那么最后只需要删掉`n - max(d[i] + c[i] - 1)`个人即可。





典型题目： 

- [x] 洛谷-P1020 导弹拦截（最典型的LIS练习，两种形式）
- [x] LeetCode 300.Longest Increasing Subsequence
- [x] POJ 2533 Longest Ordered Subsequence
- [x] POJ 1631 Bridging signals（二进制优化后的LIS）
- [x] 一本通-1263：【例9.7】友好城市(和POJ 1631一样的方法)
- [x] HDU 1257 最少拦截系统
- [x] 一本通-1259：【例9.3】求最长不下降序列
- [ ] 硬币问题（DAG方法和完全背包的解法，记得区分一下备忘录法、自顶向下和自底向上的概念《算法导论》）
- [ ] POJ 3903 Stock Exchange
- [ ] POJ 1836