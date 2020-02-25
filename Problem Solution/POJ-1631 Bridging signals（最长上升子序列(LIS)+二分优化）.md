> # POJ-1631 Bridging signals（最长上升子序列(LIS)+二分优化）

# Description

'Oh no, they've done it again', cries the chief designer at the Waferland chip factory. Once more the routing designers have screwed up completely, making the signals on the chip connecting the ports of two functional blocks cross each other all over the place. At this late stage of the process, it is too expensive to redo the routing. Instead, the engineers have to bridge the signals, using the third dimension, so that no two signals cross. However, bridging is a complicated operation, and thus it is desirable to bridge as few signals as possible. The call for a computer program that finds the maximum number of signals which may be connected on the silicon surface without crossing each other, is imminent. Bearing in mind that there may be thousands of signal ports at the boundary of a functional block, the problem asks quite a lot of the programmer. Are you up to the task?
![img](https://vj.z180.cn/226e776304cadfd23e680d3bc5e28f06?v=1580504429)
A typical situation is schematically depicted in figure 1. The ports of the two functional blocks are numbered from 1 to p, from top to bottom. The signal mapping is described by a permutation of the numbers 1 to p in the form of a list of p unique numbers in the range 1 to p, in which the i:th number specifies which port on the right side should be connected to the i:th port on the left side.Two signals cross if and only if the straight lines connecting the two ports of each pair do.

# Input

On the first line of the input, there is a single positive integer n, telling the number of test scenarios to follow. Each test scenario begins with a line containing a single positive integer p < 40000, the number of ports on the two functional blocks. Then follow p lines, describing the signal mapping:On the i:th line is the port number of the block on the right side which should be connected to the i:th port of the block on the left side.

# Output

For each test scenario, output one line containing the maximum number of signals which may be routed on the silicon surface without crossing each other.

# Sample Input

```
4
6
4
2
6
3
1
5
10
2
3
4
5
6
7
8
9
10
1
8
8
7
6
5
4
3
2
1
9
5
8
9
2
3
1
7
4
6
```

# Sample Output

```
3
9
1
4
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node
{
	int left, right;

	bool operator<(const Node & obj) const
	{
		return (left < obj.left || 
			(left == obj.left && right < obj.right));
	}
};


vector<Node> sequence(40000);

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		int n;
		cin >> n;
		for (int i = 1; i <= n; ++i) {
			cin >> sequence[i].right;
			sequence[i].left = i;
		}
        
		vector<int> d(n + 1, 0);
		d[1] = sequence[1].right;
		int len = 1;
		for (int i = 2; i <= n; ++i) {
			if (sequence[i].right > d[len])
				d[++len] = sequence[i].right;
			else {
				int pos = lower_bound(d.begin() + 1, d.begin() + 1 + len, sequence[i].right) - d.begin();
				d[pos] = sequence[i].right;
			}
		}
		cout << len << endl;
	}

    return 0;
}
```

因为左端点本来就是排好序的，所以无需再排序了，如果题目不是这样的，比如初始是乱序输入，那么需要先排序再利用LIS的优化写法。

需要新开一个和原数组等长的新数组`d`，以及一个记录目前最长上升子序列长度的`len`，`d[len]`表示最长上升子序列长度为`len`时的序列末尾最小的数。比如有两个LIS为1，2，4，另一个为1，3，5，长度都是3，那么应该选择1，2，4的序列，因为末尾的数字越小，就越能给后面的数字留空间。

然后分析更新的问题，如果对于当前数字`sequence[i]`，出现`sequence[i] > d[len]`，那么更新数组`d`和`len`的值。如果出现`sequence[i] <= d[len]`，说明之前在某个长度的上升子序列的末尾最小值需要更新，，比如序列1，2，4，5，3，当访问到3的时候，长度为3的LIS需要更新末尾的值，显然我们定义的数组`d`是升序的，那么就可以利用二分查找来快速确定位置。那么就是去寻找第一个不小于目标值的数，所以用`lower_bound`。

进一步可以通过HDU 1257来理解，当时没有意识到是LIS的优化写法，其实本质上是一致的。