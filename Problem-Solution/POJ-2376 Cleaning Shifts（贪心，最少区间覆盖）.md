> # POJ-2376 Cleaning Shifts（贪心，最少区间覆盖）

# Description

Farmer John is assigning some of his N (1 <= N <= 25,000) cows to do some cleaning chores around the barn. He always wants to have one cow working on cleaning things up and has divided the day into T shifts (1 <= T <= 1,000,000), the first being shift 1 and the last being shift T.

Each cow is only available at some interval of times during the day for work on cleaning. Any cow that is selected for cleaning duty will work for the entirety of her interval.

Your job is to help Farmer John assign some cows to shifts so that (i) every shift has at least one cow assigned to it, and (ii) as few cows as possible are involved in cleaning. If it is not possible to assign a cow to each shift, print -1.

# Input

* Line 1: Two space-separated integers: N and T
* Lines 2..N+1: Each line contains the start and end times of the interval during which a cow can work. A cow starts work at the start time and finishes after the end time.

# Output

Line 1: The minimum number of cows Farmer John needs to hire or -1 if it is not possible to assign a cow to each shift.

# Sample Input

```
3 10
1 7
3 6
6 10
```

# Sample Output

```
2
```

----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 

struct Node
{
	int left, right;
	bool operator<(const Node & obj) const
	{
		return left < obj.left;
	}
};

int n = 25000, t;
vector<Node> sequence(n);

int cowNum()
{
	sort(sequence.begin(), sequence.begin() + n);

	int cnt = 0; //计数需要多少头牛
    //pos是下一轮搜索的下标，end是上一轮的最右边界，start是辅助去搜索下一个点
	int pos = 0, start = 0, end = 0;
	while (pos < n) {
        //之所以+1是因为需要覆盖的是整数值
		start = end + 1;
		for (int i = pos; i < n; ++i) {
			if (sequence[i].left <= start) {
				if (sequence[i].right > end) end = sequence[i].right;
				if (end >= t) {++cnt; return cnt;}
			}
			else {
                //更新pos
				pos = i;
				break;
			}
		}
        //没有找到一个合适的区间
		if (end < start) return -1;
		++cnt;
	}
    //搜索结束仍没有return，代表全部区间都无法覆盖，所以无解
	return -1;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	cin >> n >> t;
	for (int i = 0; i < n; ++i) {
		cin >> sequence[i].left >> sequence[i].right;
	}    
	cout << cowNum() << endl;
    
    return 0;
}
```

解题的算法可以写出很多种，无论哪种写法，最重要的是算法证明，写出伪代码证明整个搜索过程不重不漏，那么就是正确的算法。

用`pos`来记录下一轮搜索的起始位置下标，用`end`代表上一轮搜索后的最右边界，因为本题需要覆盖的是整数，那么用`start`代表本轮搜索的判断条件，`start = end + 1`，在整个搜索中，有：

* `sequence[i].left <= start`， 满足的时候，需要去判断是否会更新`end`：
  * 更新了`end`，那么可能`end >= t`，返回结果，否则就继续搜索
  * 没有更新end。需要去分析什么情况会造成没有更新。（1）所有需要被搜索的区间都无法和上一个区间“连续”，这里代表其`s[i].left > end`，那么造成`end < start`。（2）存在使“连续”的区间，但是其`s[i].right <= end`，那么也会造成`end < start`。为了避免死循环，所以需要在一轮搜索结束去检验一下是否更新了`end`。
* `sequence[i].left > start`，就需要去更新`pos`了，检查`end`是否更新了。

关键问题，如果更新了`pos`的值，在下一轮搜索中，是否会存在`pos`位置之前的区间也满足搜索的条件。答案是不存在的，因为如果存在一个点其`i < pos`，但是`s[i].right > end`，那么很显然应该令`pos=i`。