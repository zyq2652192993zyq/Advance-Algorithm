> # POJ-2559 Largest Rectangle in a Histogram（单调栈模板）

# Description

A histogram is a polygon composed of a sequence of rectangles aligned at a common base line. The rectangles have equal widths but may have different heights. For example, the figure on the left shows the histogram that consists of rectangles with the heights 2, 1, 4, 5, 1, 3, 3, measured in units where 1 is the width of the rectangles:

![img](https://vj.z180.cn/45660aba95464e61adfbbcc7cea2c44c?v=1588550995)

Usually, histograms are used to represent discrete distributions, e.g., the frequencies of characters in texts. Note that the order of the rectangles, i.e., their heights, is important. Calculate the area of the largest rectangle in a histogram that is aligned at the common base line, too. The figure on the right shows the largest aligned rectangle for the depicted histogram.

# Input

The input contains several test cases. Each test case describes a histogram and starts with an integer *n*, denoting the number of rectangles it is composed of. You may assume that *1<=n<=100000*. Then follow *n* integers *h1,...,hn*, where *0<=hi<=1000000000*. These numbers denote the heights of the rectangles of the histogram in left-to-right order. The width of each rectangle is *1*. A zero follows the input for the last test case.

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

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int n;
vector<long long> seq(100005);

long long monotonStack()
{
	seq[n] = -1;
	++n;
	stack<int> s;
	long long res = 0;
	for (int i = 0; i < n; ++i) {
		while (!s.empty() && seq[s.top()] > seq[i]) {
			int cur = s.top(); s.pop();
			res = max(res, seq[cur] * (s.empty() ? i : i - s.top() - 1));
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
    	for (int i = 0; i < n; ++i) cin >> seq[i];
    	cout << monotonStack() << endl;
    }

	return 0;
}
```

数据可能存在溢出，所以需要选用`long long`数据类型。

