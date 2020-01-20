> # ALGOSPOT-PACKING(01背包，输出路径)

> 原文为韩文，这里翻译成中文，提交在algospot。

#### 问题问题

在旅行之前的一天，Jaehun从来没有打包过习惯，但在飞行前一天仍然坐下来打包一个包。根据飞行规则，Jaehoon只能携带一名承运人，但他要携带的物品不会进入承运人。Jaehun通过调查他想拿的每件物品的数量以及表示他需要多少的绝望程度，列出了以下清单。

| 东西     | 笔记本电脑 | 摄影机 | XBOX365 | 咖啡研磨机 | 哑铃 | 百科全书 |
| -------- | ---------- | ------ | ------- | ---------- | ---- | -------- |
| 数量     | 4          | 2      | 6       | 4          | 2    | 10       |
| 紧急程度 | 7          | 10     | 6       | 7          | 5    | 4        |

由于承运人的能力是固定的，因此要取走的物品的总和必须小于或等于承运人的能力。编写一个程序，计算出可以使您的紧急程度最大化的项目列表。

#### 输入项

输入的第一行给出了测试用例C的数量（1≤C≤50）。每个测试用例的第一行都有项目数N（1≤N≤100）和载体的容量W（1≤W≤1000）。之后，在第N行给出每个项目的信息。有关对象的信息按对象的名称，大小和拼写的顺序给出，名称是不超过一个字母，不超过20个字母，不超过1000个自然数的字符串。

#### 输出量

每个测试用例的输出的第一行显示可以采取的措施的最大绝望总和和采取的措施的数量。然后打印每个对象的名称，每行一个。如果您有多个项目组合来最大化您的紧急性，则可以打印任何内容。

#### 输入示例

```
2
6 10
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
6 17
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
```

#### 输出示例

```
24 3
laptop
camera
grinder
30 4
laptop
camera
xbox
grinder
```

-----

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n = 101, totalWeight = 1001;
vector<int> w(n + 1), v(n + 1);
vector<string> name(n + 1);
vector<int> d(totalWeight + 1, 0);

vector<string> zeroOnePack()
{
	
	vector<vector<int> > store(totalWeight + 1);
	for (int i = 1; i <= n; ++i) {
		for (int j = totalWeight; j >= w[i]; --j) {
			if (d[j] < d[j - w[i]] + v[i]) {
				d[j] = d[j - w[i]] + v[i];
				store[j] = store[j - w[i]];
				store[j].push_back(i);
			}
		}
	}
	vector<string> path;
	for (auto e : store[totalWeight]) {
		path.push_back(name[e]);
	}

	return path;
}

ostream & operator<<(ostream & os, const vector<string> & v)
{
	for (auto & e : v) os << e << endl;
	return os; 
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		cin >> n >> totalWeight;
		for (int i = 1; i <= n; ++i) cin >> name[i] >> w[i] >> v[i];
		vector<string> res = zeroOnePack();
		cout << d[totalWeight] << " " << res.size() << endl;
		cout << res;
		fill(d.begin() + 1, d.end(), 0);
	}

	return 0;
}
```

这道题目和传统的01背包问题略有不同，多了一步输出路径，其实输出路径的思路和记录最大价值是一致的，对于容量为$j$时的背包，如果加入$w[i]$，则一定是从$d[j-w[i]]$转移过来的，利用一个二维的$store$数组来存储实现背包容量为$j$时，记录组成最大价值的项对应的下标，那么$store[j]$就是在$store[j - w[i]]$的基础上添加了一个下标$i$（符合判断条件的情况下）。注意多个case，所以需要初始化数组$d$。

另外书中给了一种递归的实现思路，也是很值得学习。