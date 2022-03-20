> # HDU-1213 How Many Tables（基础并查集）

# Description

Today is Ignatius' birthday. He invites a lot of friends. Now it's dinner time. Ignatius wants to know how many tables he needs at least. You have to notice that not all the friends know each other, and all the friends do not want to stay with strangers.

One important rule for this problem is that if I tell you A knows B, and B knows C, that means A, B, C know each other, so they can stay in one table.

For example: If I tell you A knows B, B knows C, and D knows E, so A, B, C can stay in one table, and D, E have to stay in the other one. So Ignatius needs 2 tables at least.

# Input

The input starts with an integer T(1<=T<=25) which indicate the number of test cases. Then T test cases follow. Each test case starts with two integers N and M(1<=N,M<=1000). N indicates the number of friends, the friends are marked from 1 to N. Then M lines follow. Each line consists of two integers A and B(A!=B), that means friend A and friend B know each other. There will be a blank line between two cases.

# Output

For each test case, just output how many tables Ignatius needs at least. Do NOT print any blanks.

# Sample Input

```
2
5 3
1 2
2 3
4 5

5 1
2 5
```

# Sample Output

```
2
4
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <queue>
#include <cstdio>
#include <algorithm>

using namespace std;

int n = 1005;
vector<int> parent(n);
vector<int> rankNum(n); //树的高度
//vector<int> rela(n);

//初始化
void init(int num)
{
	fill(parent.begin(), parent.end(), 0);
	fill(rankNum.begin(), rankNum.end(), 0);

	for (int i = 0; i <= num; ++i) {
		parent[i] = i;
	}
}

inline int find(int x)
{
	if (x == parent[x]) return x;
	
	return parent[x] = find(parent[x]);
}

void unite(int x, int y) 
{
	x = find(x);
	y = find(y);

	if (x == y) return;

	if (rankNum[x] < rankNum[y]) parent[x] = y;
	else {
		parent[y] = x;
		if (rankNum[x] == rankNum[y]) ++rankNum[x];
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;

	while (caseNum--) {
		int m;
		cin >> n >> m;
		init(n);
		for (int i = 0; i < m; ++i) {
			int x, y;
			cin >> x >> y;
			unite(x, y);
		}
		int cnt = 0;
		for (int i = 1; i <= n; ++i) {
			if (i == parent[i]) ++cnt;
		}
		cout << cnt << endl;
	}
	
    return 0;
}
```

基础并查集的简单变形，只需要注意每个样例开始计算前要对`parent`和`rankNum`继续宁初始化。