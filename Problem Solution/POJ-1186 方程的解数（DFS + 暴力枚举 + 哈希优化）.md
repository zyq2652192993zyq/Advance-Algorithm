> # POJ-1186 方程的解数（DFS + 暴力枚举 + 哈希优化）

# Description

已知一个n元高次方程：
![img](https://vj.z180.cn/14b190da52aea171a65d889a60800219?v=1585239504)
其中：x1, x2,...,xn是未知数，k1,k2,...,kn是系数，p1,p2,...pn是指数。且方程中的所有数均为整数。
假设未知数1 <= xi <= M, i=1,,,n，求这个方程的整数解的个数。
1 <= n <= 6；1 <= M <= 150。
![img](https://vj.z180.cn/db6996e48f80e40cb3b2c7966edc0f19?v=1585239504)
方程的整数解的个数小于2 31。
★本题中，指数Pi(i=1,2,...,n)均为正整数。

# Input

第1行包含一个整数n。第2行包含一个整数M。第3行到第n+2行，每行包含两个整数，分别表示ki和pi。两个整数之间用一个空格隔开。第3行的数据对应i=1，第n+2行的数据对应i=n。

# Output

仅一行，包含一个整数，表示方程的整数解的个数。

# Sample Input

```
3
150
1  2
-1  2
1  2
```

# Sample Output

```
178
```

--------

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 4000000; //150^3 = 3375000

int n, m, mid;
vector<int> k(6), p(6);
int res = 0;

struct Node
{
	int num;
	int value;
};

vector<Node> HashTable(INF); //用数字本身作为哈希地址
vector<bool> used(INF, false); //标记被占据的位置

//快速幂计算
inline int powValue(int x, int mode)
{
	int res = 1;
	while (mode) {
		if (mode & 1) res *= x;
		x *= x;
		mode >>= 1;
	}

	return res;
}

//线性探测法
int findPos(int sum)
{
	int tmp = sum;
	while (tmp < 0) tmp += INF;
	while (tmp >= INF) tmp -= INF;
	while (used[tmp] && HashTable[tmp].value != sum) {
		++tmp; //不是直接取模，因为INF很大，需要很多次后才取模
		if (tmp >= INF) tmp -= INF;
	}
	return tmp;
}

void insert(int sum)
{
	int pos = findPos(sum); //查找可存放的位置
	HashTable[pos].value = sum;
	used[pos] = true; //标记被占据的位置
	++HashTable[pos].num;
}


void leftEnum(int cnt, int sum)
{
	if (cnt == mid) {
		insert(sum);
		return;
	}

	for (int i = 1; i <= m; ++i) {
		leftEnum(cnt + 1, sum + k[cnt] * powValue(i, p[cnt]));
	}
}

void rightCal(int cnt, int sum)
{
	if (cnt == n) {
		sum *= -1; //需要查找的左半部分和
		int pos = findPos(sum);
		if (HashTable[pos].value == sum) {
			res += HashTable[pos].num;
		}
		return;
	}

	for (int i = 1; i <= m; ++i) {
		rightCal(cnt + 1, sum + k[cnt] * powValue(i, p[cnt]));
	}
}


int solve()
{
	mid = n >> 1; //左边枚举的个数
	leftEnum(0, 0); //左边枚举
	rightCal(mid, 0);

	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
   	for (int i = 0; i < n; ++i) {
   		cin >> k[i] >> p[i];
   	} 
   	cout << solve() << endl;
   
    return 0;
}
```

这道题如果直接暴力枚举，那么就是$150^6$，肯定会超时。如果最多6个数，可以考虑对前三个数进行暴力，这样就不会超时。

思路是首先对前半部分进行枚举，那么就是一个DFS爆搜，哈希部分采用的方法就是直接定址法，冲突解决是采用线性探测的方法。然后对后半部分枚举，在前半部分的里面查找相反数，查找到就加上对应的个数即可。

当然我们也可以利用`map`来求解，但是就达不到训练手写哈希的目的了。测试了以下，只是把`HashTable`的部分换成用`map`，最后TLE了，其实可以分析，标准库的`map`部分肯定不会预先知道需要用多少个数据，频繁的申请空间很耗时，所以不如手写的部分。

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 4000000; //150^3 = 3375000

int n, m, mid;
vector<int> k(6), p(6);
int res = 0;

map<int, int> HashTable;


//快速幂计算
inline int powValue(int x, int mode)
{
	int res = 1;
	while (mode) {
		if (mode & 1) res *= x;
		x *= x;
		mode >>= 1;
	}

	return res;
}

void leftEnum(int cnt, int sum)
{
	if (cnt == mid) {
		++HashTable[sum];
		return;
	}

	for (int i = 1; i <= m; ++i) {
		leftEnum(cnt + 1, sum + k[cnt] * powValue(i, p[cnt]));
	}
}

void rightCal(int cnt, int sum)
{
	if (cnt == n) {
		sum *= -1; //需要查找的左半部分和
		if (HashTable.find(sum) != HashTable.end()) {
			res += HashTable[sum];
		}
		return;
	}

	for (int i = 1; i <= m; ++i) {
		rightCal(cnt + 1, sum + k[cnt] * powValue(i, p[cnt]));
	}
}


int solve()
{
	mid = n >> 1; //左边枚举的个数
	leftEnum(0, 0); //左边枚举
	rightCal(mid, 0);

	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
   	for (int i = 0; i < n; ++i) {
   		cin >> k[i] >> p[i];
   	} 
   	cout << solve() << endl;
   
    return 0;
}
```

