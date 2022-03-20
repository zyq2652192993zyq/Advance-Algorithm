> # POJ-3264 Balanced Lineup（线段树）

# Description

For the daily milking, Farmer John's *N* cows (1 ≤ *N* ≤ 50,000) always line up in the same order. One day Farmer John decides to organize a game of Ultimate Frisbee with some of the cows. To keep things simple, he will take a contiguous range of cows from the milking lineup to play the game. However, for all the cows to have fun they should not differ too much in height.

Farmer John has made a list of *Q* (1 ≤ *Q* ≤ 200,000) potential groups of cows and their heights (1 ≤ *height* ≤ 1,000,000). For each group, he wants your help to determine the difference in height between the shortest and the tallest cow in the group.

# Input

Line 1: Two space-separated integers, *N* and *Q*.
Lines 2..*N*+1: Line *i*+1 contains a single integer that is the height of cow *i*
Lines *N*+2..*N*+*Q*+1: Two integers *A* and *B* (1 ≤ *A* ≤ *B* ≤ *N*), representing the range of cows from *A* to *B* inclusive.

# Output

Lines 1..*Q*: Each line contains a single integer that is a response to a reply and indicates the difference in height between the tallest and shortest cow in the range.

# Sample Input

```
6 3
1
7
3
4
2
5
1 5
4 6
2 2
```

# Sample Output

```
6
3
0
```

---

这个题很坑，最初提交了三次一直是TLE，以为自己算法逻辑有问题，后来查资料发现POJ没有开O2优化，对C++标准库支持很差，其实发现我只是把原来用模板`vector`部分替换成了数组就过了。

另外POJ不支持C++11，无论是选`c++`编译还是`g++`编译，都会报CE的，所以最好还是去HDU练习把。

```c++
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

const int INF = 0x0ffffff;
const int N = 50001;

struct Node {
	int left, right;
	int maxNum;
	int minNum;

	Node() : left(0), right(0), maxNum(0), minNum(0) {}
};

//vector<Node> v(n << 2);
//vector<int> num(n);

Node v[N * 4];
int num[N];

int minx,maxx;

inline void update(int k)
{
	v[k].maxNum = max(v[k << 1].maxNum, v[k << 1 | 1].maxNum);
	v[k].minNum = min(v[k << 1].minNum, v[k << 1 | 1].minNum);
}

void build(int k, int leftPos, int rightPos)
{
	v[k].left = leftPos;
	v[k].right = rightPos;

	if (leftPos == rightPos) {
		v[k].maxNum = num[leftPos];
		v[k].minNum = num[leftPos];
		return;
	}

	int mid = v[k].left + ((v[k].right - v[k].left) >> 1);
	build(k << 1, leftPos, mid);
	build(k << 1 | 1, mid + 1, rightPos);
	update(k);
}

void query(int k, int leftPos, int rightPos)
{
	if (v[k].left == leftPos && v[k].right == rightPos) {
		maxx = max(maxx, v[k].maxNum);
		minx = min(minx, v[k].minNum);
		return;
	}

	int mid = v[k].left + ((v[k].right - v[k].left) >> 1);
	if (rightPos <= mid) query(k << 1, leftPos, rightPos);
	else if (leftPos > mid) query(k << 1 | 1, leftPos, rightPos);
	else {
		query(k << 1, leftPos, mid);
		query(k << 1 | 1, mid + 1, rightPos);
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, Q;
	cin >> n >> Q;
	for (int i = 1; i <= n; ++i) {
		cin >> num[i];
	}

	memset(v, 0, sizeof(v));
	build(1, 1, n);

	while (Q--) {
		int leftPos, rightPos;
		cin >> leftPos >> rightPos;
		minx = INF;
		maxx = -INF;
		query(1, leftPos, rightPos);
		cout << (maxx - minx) << endl;
	}

	return 0;
}
```

