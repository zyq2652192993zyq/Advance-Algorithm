> # POJ-1703 Find them, Catch them（基础并查集开双倍空间）

# Description

The police office in Tadu City decides to say ends to the chaos, as launch actions to root up the TWO gangs in the city, Gang Dragon and Gang Snake. However, the police first needs to identify which gang a criminal belongs to. The present question is, given two criminals; do they belong to a same clan? You must give your judgment based on incomplete information. (Since the gangsters are always acting secretly.)

Assume N (N <= 10^5) criminals are currently in Tadu City, numbered from 1 to N. And of course, at least one of them belongs to Gang Dragon, and the same for Gang Snake. You will be given M (M <= 10^5) messages in sequence, which are in the following two kinds:

1. `D [a][b]`
where [a] and [b] are the numbers of two criminals, and they belong to different gangs.

2.` A [a] [b]`
where [a] and [b] are the numbers of two criminals. This requires you to decide whether a and b belong to a same gang.

# Input

The first line of the input contains a single integer T (1 <= T <= 20), the number of test cases. Then T cases follow. Each test case begins with a line with two integers N and M, followed by M lines each containing one message as described above.

# Output

For each message "`A [a][b]`" in each case, your program should give the judgment based on the information got before. The answers might be one of "In the same gang.", "In different gangs." and "Not sure yet."

# Sample Input

```
1
5 5
A 1 2
D 1 2
A 1 2
D 2 4
A 1 4
```

# Sample Output

```
Not sure yet.
In different gangs.
In the same gang.
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <algorithm>

using namespace std;

int n = 200005;
vector<int> parent(n);
vector<int> rankNum(n); //树的高度
//vector<int> rela(n);

//初始化
void init(int num)
{
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

inline bool isSame(int x, int y)
{
	return find(x) == find(y);
}


int main()
{
	// std::ios_base::sync_with_stdio(false);
	// cin.tie(NULL);
	// cout.tie(NULL);

	int caseNum;
	scanf("%d", &caseNum);
	//cin >> caseNum;

	while (caseNum--) {
		int m;
		scanf("%d%d", &n, &m);
		//cin >> n >> m;
		init(n * 2);
		
		while (m--) {
			char opt[2];
			int x, y;
			scanf("%s%d%d", &opt, &x, &y);
			//cin >> opt >> x >> y;
			if (opt[0] == 'A') {
				if (isSame(x, y) || isSame(x + n, y + n))
					printf("In the same gang.\n");
					//cout << "In the same gang." << endl;
				else if (isSame(x, y + n) || isSame(x + n, y))
					printf("In different gangs.\n");
					//cout << "In different gangs." << endl;
				else 
					printf("Not sure yet.\n");
					//cout << "Not sure yet." << endl;
			}
			else { //操作为D
				unite(x, y + n);
				unite(x + n, y);
			}
		}

		fill(parent.begin(), parent.end(), 0);
		fill(rankNum.begin(), rankNum.end(), 0);
	}
	
    return 0;
}
```

这道题还是老样子，用`cin`和`cout`会超时，即使关掉了同步也不起作用。思路和POJ 1182 食物链基本是一致的，只不过是开双倍空间。属于不同的集合，那么就合并x，y+n和y，x+n。然后就是查询操作。