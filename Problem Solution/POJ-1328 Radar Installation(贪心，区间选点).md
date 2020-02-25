> # POJ-1328 Radar Installation(贪心，区间选点)

# Description

Assume the coasting is an infinite straight line. Land is in one side of coasting, sea in the other. Each small island is a point locating in the sea side. And any radar installation, locating on the coasting, can only cover d distance, so an island in the sea can be covered by a radius installation, if the distance between them is at most d.

We use Cartesian coordinate system, defining the coasting is the x-axis. The sea side is above x-axis, and the land side below. Given the position of each island in the sea, and given the distance of the coverage of the radar installation, your task is to write a program to find the minimal number of radar installations to cover all the islands. Note that the position of an island is represented by its x-y coordinates.
![img](https://vj.z180.cn/f6ffe515205096387436c13c7449b0ed?v=1579590817)
Figure A Sample Input of Radar Installations

# Input

The input consists of several test cases. The first line of each case contains two integers n (1<=n<=1000) and d, where n is the number of islands in the sea and d is the distance of coverage of the radar installation. This is followed by n lines each containing two integers representing the coordinate of the position of each island. Then a blank line follows to separate the cases.

The input is terminated by a line containing pair of zeros

# Output

For each test case output one line consisting of the test case number followed by the minimal number of radar installations needed. "-1" installation means no solution for that case.

# Sample Input

```
3 2
1 2
-3 1
2 1

1 2
0 2

0 0
```

# Sample Output

```
Case 1: 2
Case 2: 1
```

---

```c++
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;
struct Node
{
	double left, right;
	bool operator<(const Node & n) const
	{
		return left < n.left;
	}
};

int n = 1001;
double d;
vector<Node> sequence(n);

int circleNum()
{
	sort(sequence.begin(), sequence.begin() + n);

	int cnt = 1;
	double range = sequence[0].right;
	for (int i = 1; i < n; ++i) {
		if (sequence[i].left <= range) range = min(range, sequence[i].right);
		else {
			++cnt;
			range = sequence[i].right;
		}
	}

	return cnt;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum = 0;
    while ((cin >> n >> d) && n && d) {
    	++caseNum;
    	bool isBeyond = false;
    	for (int i = 0; i < n; ++i) {
    		int x, y;
    		cin >> x >> y;
    		if (y > d) isBeyond = true;
    		else {
    			sequence[i].left = x * 1.0 - sqrt(d * d - y * y);
    			sequence[i].right = x * 1.0 + sqrt(d * d - y * y);
    		}
    	}
    	cout << "Case " << caseNum << ": ";
    	if (isBeyond) cout << -1 << endl;
    	else cout << circleNum() << endl;
    }

    return 0;
}
```

此题需要反向思考，对于每个小岛，如果在小岛上放置一个雷达，它和海岸线的相交部分是一个区间，那么也就是雷达放置在这个区间内都可以覆盖小岛，所以问题转化成：

如何选点来保证每个区间至少有一个点，一个点可以同时处于多个有重叠区间的部分。

这其实就是很常见的区间选点问题。

另外这题有两个细节，第一个细节是可能存在不合法的输入，也就是`y >d`的情况，那么此时就不应该计算`sequence`的部分，否则会出错。

第二个，如果最开始`d`的类型是`int`，那么编译器会报错`'sqrt' : ambiguous call to overloaded function`，这是因为它会试图去找一个`sqrt(int)`的函数，但是找不到。于是退而求其次，找一个可以从`in`t转换过去的`sqrt`，结果一下找到了两个，一个是`qrt(long double)`，另一个是`sqrt(float)`。而这两个转换是优先级相同的，所以为了避免这个错误，应该将`d`的类型设置成`double`.