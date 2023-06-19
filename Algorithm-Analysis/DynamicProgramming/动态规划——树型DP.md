> # 动态规划——树型DP

参考资料：

* https://www.bilibili.com/video/BV1vT4y1g7vN
* https://www.bilibili.com/video/BV1Px411B7gK
* https://blog.csdn.net/u011815404/category_8104361.html
* 《算法竞赛进阶指南》 0x54 树形DP
* 《算法竞赛入门经典》 9.4.3 树上的动态规划

----

树型DP除了裸题外，经常和背包问题结合，形成有依赖的背包问题。

通常给定一个`n`个节点的树，通常是无根树，有`n-1`条边，一般以节点从深到浅作为DP的阶段。

## 树型DP经典入门题

### 没有上司的舞会

- [x] 洛谷-P1352 没有上司的舞会（树型DP经典入门题）

某大学有 $n$个职员，编号为 $1\ldots n$。

他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树，父结点就是子结点的直接上司。

现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数 $r_i$，但是呢，如果某个职员的直接上司来参加舞会了，那么这个职员就无论如何也不肯来参加舞会了。

所以，请你编程计算，邀请哪些职员可以使快乐指数最大，求最大的快乐指数。

分析：用`d[i][0]`表示当`i`不参加时的最大快乐指数和，状态转移方程：
$$
d[i][0] = \sum_{s \in \text{son}(i)} \max (d[s][0], d[s][1])
$$
上面方程的意思是，上司`i`选择不参加，那么`i`的直接下属可以选择参加，也可以选择不参加，应该选择两者中的最大值，最后对所有下属的快乐指数求和。

用`d[i][1]`表示上司`i`参加的最大快乐指数，设上司`i`个人的快乐指数是`happiness[i]`，如果上司`i`参加，那么它们的下属都不能参加，于是状态转移方程：
$$
d[i][1] = \text{happiness}[i] + \sum_{s \in \text{son}(i)} d[s][0]
$$
那么最终的结果就是`d[i][0], d[i][1]`中的最大值了。因为只需要一次遍历，时间复杂度$O(n)$，空间复杂度$O(n)$。

```c++
//洛谷-P1352 没有上司的舞会
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> happiness(6005);
vector<vector<int>> d(6005, vector<int>(2)), son(6005);
vector<bool> haveParent(6005, false);


void solve(int start)
{
	d[start][1] = happiness[start];
	for (const auto & e : son[start]) {
		solve(e);
		d[start][0] += max(d[e][0], d[e][1]);
		d[start][1] += d[e][0];
	}
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> happiness[i];
	int employee, boss;
	for (int i = 1; i < n; ++i) {
		cin >> employee >> boss;
		haveParent[employee] = true;
		son[boss].push_back(employee);
	}

	int start = 0;
	for (int i = 1; i <= n; ++i) {
		if (!haveParent[i]) { start = i; break; }
	}

	solve(start);
	cout << max(d[start][0], d[start][1]) << endl;

	return 0;
}
```

另外上面的代码使用了C++11新标准的`auto`，在POJ里是不能使用的，注意改写。

### 二叉苹果树

- [x]  一本通-1575：【例 1】二叉苹果树（没有上司的舞会的变形）





这道题虽然背景换成了苹果，其实就是没有上司的舞会的变形题，某个节点被删掉，连同它的子树肯定一并被删掉，相当于没有上司的舞会的上司和下属的模型。





## 树型背包

### 选课

- [ ] 一本通-1576：【例 2】选课





## 二次扫描与换根法

对于“不定根”的树型DP问题，一般的特点是，给定一个树型结构，需要以每个点为根做一次统计，一般进行两次扫描来求解。

1. 第一次扫描时，任选一个点为根，做一次树型DP，是自底向上的状态转移。
2. 第二次扫描，从上面选的根出发，做树型DP，是自顶向下的状态转移。

时间复杂度$O(n)$。

### Computer(树上最大距离)

- [x] HDU-2196 Computer（树型DP经典入门题，树上最大距离）

A school bought the first computer some time ago(so this computer's id is 1). During the recent years the school bought N-1 new computers. Each new computer was connected to one of settled earlier. Managers of school are anxious about slow functioning of the net and want to know the maximum distance Si for which i-th computer needs to send signal (i.e. length of cable to the most distant computer). You need to provide this information.

![img](https://vj.z180.cn/3f5ab5c3d97280e16503ce9ef614b5c5?v=1592865094)

Hint: the example input is corresponding to this graph. And from the graph, you can see that the computer 4 is farthest one from 1, so S1 = 3. Computer 4 and 5 are the farthest ones from 2, so S2 = 2. Computer 5 is the farthest one from 3, so S3 = 3. we also get S4 = 4, S5 = 4.

很明显这是一个无根树，但其实可以认为节点1就是根，按照以往的树型DP，求出从根节点到叶节点的最大距离很容易，但是现在存在可能从它的父节点转移过来的最大长度（图片引自[shuangde800](https://blog.csdn.net/shuangde800)）：

![img](https://img-blog.csdn.net/20130803223338546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2h1YW5nZGU4MDA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

比如求以2为根的最长路径，可能是蓝色部分内的最长路径（也就是根节点到叶节点的最长路径），也可能是2的父节点1的红色部分，1到叶节点的最长路径加上1和2之间的距离。所以问题求解的关键是如何解决从节点的父节点转移过来的这部分。

用数组`d[i][0]`代表以节点`i`为根的子树，从根节点`i`到叶节点的最长路径，`d[i][1]`代表从根节点`i`到叶节点的第二长的路径，`d[i][2]`通过节点`i`的父节点转移过来的最长路径（也就是上图红色的部分）。

状态转移方程的建立需要分两个阶段，第一个阶段，求`d[i][0], d[i][1]`，状态转移方程：
$$
d[i][0] = \max_{j \in \text{son}(x)} d[j][0] + \text{dis}(i, j)
$$
第二个阶段才是计算最终答案，去计算`d[i][2]`，注意和第一个阶段的区别。第一个阶段是把子阶段的影响传递给父阶段，第二个阶段，要想求从父节点转移过来的最大距离，父节点必须已经计算出从父节点的父节点转移到父节点的最大距离，也就是影响是从父阶段传递给子阶段的，体现在程序里就是递归的发生位置。

```c++
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

struct Node
{
	int to, dis;
	Node(int x, int y) : to(x), dis(y) {}
};

int n;
vector<vector<int> > d(10005, vector<int>(3));
vector<vector<Node> > son(10005);

void searchAnswer(int start)
{
	for (int i = 0; i < son[start].size(); ++i) {
		Node & e = son[start][i];
		
		if (d[start][0] == d[e.to][0] + e.dis) //最大值经过e.to
			d[e.to][2] = max(d[start][2], d[start][1]) + e.dis;
		else d[e.to][2] = max(d[start][2], d[start][0]) + e.dis;	

		searchAnswer(e.to);
	}
}

void treeDP(int start)
{
	for (int i = 0; i < son[start].size(); ++i) {
		Node & e = son[start][i];
		treeDP(e.to);
		int tmp = e.dis + d[e.to][0];
		//寻找最大值和次大值
		if (tmp > d[start][0]) {
			d[start][1] = d[start][0];
			d[start][0] = tmp;
		}
		else d[start][1] = max(d[start][1], tmp);
	}
}

void solve()
{
	treeDP(1);
	searchAnswer(1);

	for (int i = 1; i <= n; ++i) cout << max(d[i][0], d[i][2]) << endl;
}

void init()
{
	for (int i = 1; i <= n; ++i) {
		fill(d[i].begin(), d[i].end(), 0);
		son[i].clear();
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (cin >> n) {
		int from, dis;
		for (int i = 2; i <= n; ++i) {
			cin >> from >> dis;
			son[from].push_back(Node(i, dis));
		}
		solve();

		init();
	}

	return 0;
}
```



















典型题目

- [x] 洛谷-P1352 没有上司的舞会（树型DP经典入门题）
- [x] HDU-1520 Anniversary party（英文版的没有上司的舞会，多组输入有坑）
- [x] HDU-2196 Computer（树型DP经典入门题，树上最大距离）
- [ ] 一本通-1575：【例 1】二叉苹果树（没有上司的舞会的变形）