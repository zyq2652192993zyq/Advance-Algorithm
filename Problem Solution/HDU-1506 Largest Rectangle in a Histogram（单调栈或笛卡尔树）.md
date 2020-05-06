> # HDU-1506 Largest Rectangle in a Histogram（单调栈或笛卡尔树）

# Description

A histogram is a polygon composed of a sequence of rectangles aligned at a common base line. The rectangles have equal widths but may have different heights. For example, the figure on the left shows the histogram that consists of rectangles with the heights 2, 1, 4, 5, 1, 3, 3, measured in units where 1 is the width of the rectangles:
![img](https://vj.z180.cn/eb5960f09a1245ebe970bb7af6446b63?v=1582536935)
Usually, histograms are used to represent discrete distributions, e.g., the frequencies of characters in texts. Note that the order of the rectangles, i.e., their heights, is important. Calculate the area of the largest rectangle in a histogram that is aligned at the common base line, too. The figure on the right shows the largest aligned rectangle for the depicted histogram.

# Input

The input contains several test cases. Each test case describes a histogram and starts with an integer n, denoting the number of rectangles it is composed of. You may assume that 1 <= n <= 100000. Then follow n integers h1, ..., hn, where 0 <= hi <= 1000000000. These numbers denote the heights of the rectangles of the histogram in left-to-right order. The width of each rectangle is 1. A zero follows the input for the last test case.

# Output

For each test case output on a single line the area of the largest rectangle in the specified histogram. Remember that this rectangle must be aligned at the common base line.

# Sample Input

```
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
```

# Sample Output

```
8
4000
```

----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

int n = 100005;
// vector<int> sequence(n);

long long maxRectangle(vector<long long> & sequence)
{
	long long res = 0;
	stack<int> s;
	sequence.push_back(-1);
	for (int i = 0; i < sequence.size(); ++i) {
		while (!s.empty() && sequence[i] < sequence[s.top()]) {
			int cur = s.top(); s.pop();
			res = max(res, sequence[cur] * (s.empty() ? i : i - s.top() - 1));
		}
		s.push(i);
	}
	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while ((cin >> n) && n) {
		vector<long long> sequence(n);
		for (int i = 0; i < n; ++i) cin >> sequence[i];
		cout << maxRectangle(sequence) << endl;
	}
	
	return 0;
}
```

