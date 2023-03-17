> # POJ-3190 Stall Reservations（贪心，区间划分+路径输出）

# Description

Oh those picky N (1 <= N <= 50,000) cows! They are so picky that each one will only be milked over some precise time interval A..B (1 <= A <= B <= 1,000,000), which includes both times A and B. Obviously, FJ must create a reservation system to determine which stall each cow can be assigned for her milking time. Of course, no cow will share such a private moment with other cows.

Help FJ by determining:

- The minimum number of stalls required in the barn so that each cow can have her private milking period
- An assignment of cows to these stalls over time

Many answers are correct for each test dataset; a program will grade your answer.

# Input 

Line 1: A single integer, N

Lines 2..N+1: Line i+1 describes cow i's milking interval with two space-separated integers.

# Output

Line 1: The minimum number of stalls the barn must have.

Lines 2..N+1: Line i+1 describes the stall to which cow i will be assigned for her milking period.

# Sample Input

```
5
1 10
2 4
3 6
5 8
4 7
```

# Sample Output

```
4
1
2
3
2
4
```

# Hint

Explanation of the sample:

Here's a graphical schedule for this output:

```
Time     1  2  3  4  5  6  7  8  9 10

Stall 1 c1>>>>>>>>>>>>>>>>>>>>>>>>>>>

Stall 2 .. c2>>>>>> c4>>>>>>>>> .. ..

Stall 3 .. .. c3>>>>>>>>> .. .. .. ..

Stall 4 .. .. .. c5>>>>>>>>> .. .. ..
```

Other outputs using the same number of stalls are possible.

-----

```c++
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node
{
	int left, right;
	int no; //记录输入的原始序号
	//左端点升序，右端点降序
	bool operator<(const Node & n) const
	{
		return (left < n.left || (left == n.left && right < n.right));
	}
};

struct Stall
{
	int end;
	int pos;
	bool operator<(const Stall & s) const
	{
		return end > s.end;
	}
	Stall(int e, int p) : end(e), pos(p) {}
};

int n = 50001;

vector<Node> sequence(n);
vector<int> record(n); //记录每头牛被分配到stall的编号

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> sequence[i].left >> sequence[i].right;
		sequence[i].no = i;
	} 
	sort(sequence.begin() + 1, sequence.begin() + 1 + n);

	int cnt = 0;
	priority_queue<Stall> pq;

	for (int i = 1; i <= n; ++i) {
		if (pq.empty()) { //队列为空，还没有安排围栏
			++cnt;
			pq.push(Stall(sequence[i].right, cnt));
			record[sequence[i].no] = cnt;
		}
		else { //队列不为空，存在两种情况
			Stall tmp = pq.top();
			if (tmp.end < sequence[i].left) { //当前围栏可以加入
				pq.pop(); //删除原来的元素，更新
				pq.push(Stall(sequence[i].right, tmp.pos));
				record[sequence[i].no] = tmp.pos;
			}
			else { //已经没有可以加入的位置了，需要增加围栏
				++cnt;
				pq.push(Stall(sequence[i].right, cnt));
				record[sequence[i].no] = cnt;
			}
		}
	}

	cout << cnt << endl;
	for (int i = 1; i <= n; ++i) cout << record[i] << endl;

    return 0;
}
```

我们把问题抽象一下再描述：

时间限制: 1 Sec 内存限制: 128 MB
时间轴上有n个开区间(ai, bi)，把这些区间至少划分成多少个集合，使得每个集合中的区间两两没有公共点。因为是开区间，所以(1, 2)和(2,3)可在一个集合中

### 输入

第1行：一个整数N(1 <= N <=10^5)
接下来N行，每行2个整数Ai，Bi(0<= Ai < Bi < 10^7)

### 输出

第1行：1个整数，需要划分成的最少集合数。

### 样例输入

```
6
4 7
2 5
1 2
3 5
3 6
7 9
```

### 样例输出

```
4
```

------

```c++
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node
{
	int left, right;
	//左端点升序，右端点降序
	bool operator<(const Node & n) const
	{
		return (left < n.left || (left == n.left && right > n.right));
	}
};

int n = 1001;

vector<Node> sequence(n); //记录所有区间的左右端点
vector<int> record(n); //记录各个集合的最右端点

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) cin >> sequence[i].left >> sequence[i].right;
	sort(sequence.begin(), sequence.begin() + n);

	int cnt = 0;
	record[0] = sequence[0].right;

	for (int i = 1; i < n; ++i) {
		bool havePos = false; //判断已知的集合是否可以加入当前区间
        //遍历集合的右端点
		for (int j = 0; j <= cnt; ++j) {
			if (sequence[i].left >= record[j]) {
				record[j] = sequence[i].right;
				havePos = true;
				break;
			}
		}
        //遍历完发现没有集合可以加入，那么需要增加一个集合
		if (!havePos) {
			++cnt;
			record[cnt] = sequence[i].right;
		}
	}

	cout << (cnt + 1) << endl; 

    return 0;
}
```

但是注意，这种方法在处理POJ 3190的时候会超时，因为考虑特殊情况，如果每个区间一个集合，那么这就是$O(n^2)$的算法，所以应该考虑用优先级队列来进行优化。

上面的算法之所以会超时，是因为对于整个过程分析的不够细致，因为考虑如果每一次加入新的一头奶牛就要全部对比，这样很耗时间，是否可以利用数据结构来优化这个过程？

首先肯定是要对输入的序列进行排序，那么目前见过的排序技巧有区间调度里面的右端点排序，初始排序左端点升序，左端点相同，右端点升序。

利用优先级队列的优化，每次取出最早结束的时间，如果最早结束的时间小于序列的开始时间，那么就可以加入围栏，否则就需要新开一个围栏。这样就只需要去进行一次比较，我们需要对这个过程进行证明。

首先考虑队列为空和不为空的两种情形。队列为空的情形比较好处理，不为空的情形需要细节分析。

首先队列的优先级是根据结束时间来确定的，结束的时间越早，优先级就越高。那么需要证明为什么只需要去比较一次。考虑最早结束的时间，如果其小于序列的开始时间，那么第二早结束的时间虽然也有可能小于序列开始的时间，所以会不会存在一种情况，就是最早结束的时间和序列开始的时间内可以插入一个新的序列点。答案是不会的，因为排序是按照序列开始时间升序排列的，当前序列的后面的点的开始时间是不会比当前的开始时间早的。那么此时去更新这个结束时间即可（删掉队列原有的点，加入一个新的点）。

如果最早结束的时间大于等于序列的开始时间，因为队列是按照最早结束的时间来确定优先级的，那么意味着队列里的其他的结束时间肯定也比序列的开始时间要大，意味着已经没有围栏合适了，那么就需要去增加一个围栏。

题目特殊的地方是需要“输出路径”，也就是需要按照输入的顺序去输出每头牛被分配的围栏号，所以需要去记录初始的输入顺序和用一个数组`record` 去记录每头牛被分配的围栏号。