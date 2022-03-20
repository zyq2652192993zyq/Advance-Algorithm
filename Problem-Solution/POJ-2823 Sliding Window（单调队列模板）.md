> # POJ-2823 Sliding Window（单调队列模板）

# Description

An array of size *n* ≤ 10 6 is given to you. There is a sliding window of size *k* which is moving from the very left of the array to the very right. You can only see the *k* numbers in the window. Each time the sliding window moves rightwards by one position. Following is an example:
The array is [1 3 -1 -3 5 3 6 7], and *k* is 3.

| Window position     | Minimum value | Maximum value |
| ------------------- | ------------- | ------------- |
| [1 3 -1] -3 5 3 6 7 | -1            | 3             |
| 1 [3 -1 -3] 5 3 6 7 | -3            | 3             |
| 1 3 [-1 -3 5] 3 6 7 | -3            | 5             |
| 1 3 -1 [-3 5 3] 6 7 | -3            | 5             |
| 1 3 -1 -3 [5 3 6] 7 | 3             | 6             |
| 1 3 -1 -3 5 [3 6 7] | 3             | 7             |

Your task is to determine the maximum and minimum values in the sliding window at each position.

# Input

The input consists of two lines. The first line contains two integers *n* and *k* which are the lengths of the array and the sliding window. There are *n* integers in the second line.

# Output

There are two lines in the output. The first line gives the minimum values in the window at each position, from left to right, respectively. The second line gives the maximum values.

# Sample Input

```
8 3
1 3 -1 -3 5 3 6 7
```

# Sample Output

```
-1 -3 -3 -3 3 3
3 3 5 5 6 7
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

int n, k;
//vector<int> seq(1000005);
int seq[1000005];


ostream & operator<<(ostream & os, vector<int> & v)
{
	int len = v.size();
	for (int i = 0; i < len; ++i) {
		os << v[i];
		if (i != len - 1) os << ' ';
	}
	os << endl;

	return os;
}


void monotonQueue()
{
	deque<int> dq;
	vector<int> res;
	//minimum
	for (int i = 0; i < n; ++i) {
		if (!dq.empty() && dq.front() == i - k) dq.pop_front();
		while (!dq.empty() && seq[dq.back()] >= seq[i]) dq.pop_back();
		dq.push_back(i);
		if (i >= k - 1) res.push_back(seq[dq.front()]);
	}
	cout << res;
	res.clear();
	dq.clear();

	//maximum
	for (int i = 0; i < n; ++i) {
		if (!dq.empty() && dq.front() == i - k) dq.pop_front();
		while (!dq.empty() && seq[dq.back()] <= seq[i]) dq.pop_back();
		dq.push_back(i);
		if (i >= k - 1) res.push_back(seq[dq.front()]);
	}
	cout << res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < n; ++i) cin >> seq[i];
    monotonQueue();

	return 0;
}
```

模板题，但是注意此题很坑，选择C++编译会TLE，选择G++无需任何改动。