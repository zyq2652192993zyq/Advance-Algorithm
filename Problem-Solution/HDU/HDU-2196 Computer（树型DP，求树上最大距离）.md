> # HDU-2196 Computer（树型DP，求树上最大距离）

# Description

A school bought the first computer some time ago(so this computer's id is 1). During the recent years the school bought N-1 new computers. Each new computer was connected to one of settled earlier. Managers of school are anxious about slow functioning of the net and want to know the maximum distance Si for which i-th computer needs to send signal (i.e. length of cable to the most distant computer). You need to provide this information.

![img](https://vj.z180.cn/3f5ab5c3d97280e16503ce9ef614b5c5?v=1592865094)

Hint: the example input is corresponding to this graph. And from the graph, you can see that the computer 4 is farthest one from 1, so S1 = 3. Computer 4 and 5 are the farthest ones from 2, so S2 = 2. Computer 5 is the farthest one from 3, so S3 = 3. we also get S4 = 4, S5 = 4.

# Input

Input file contains multiple test cases.In each case there is natural number N (N<=10000) in the first line, followed by (N-1) lines with descriptions of computers. i-th line contains two natural numbers - number of computer, to which i-th computer is connected and length of cable used for connection. Total length of cable does not exceed 10^9. Numbers in lines of input are separated by a space.

# Output

For each case output N lines. i-th line must contain number Si for i-th computer (1<=i<=N).

# Sample Input

```
5
1 1
2 1
3 1
1 1
```

# Sample Output

```
3
2
3
4
4
```

-----

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

