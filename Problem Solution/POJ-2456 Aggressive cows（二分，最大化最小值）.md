> # POJ-2456 Aggressive cows（二分，最大化最小值）

# Description

Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ want to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

# Input

* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi

# Output

Line 1: One integer: the largest minimum distance

# Sample Input

```
5 3
1
2
8
4
9
```

# Sample Output

```
3
```

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 100005, k;
vector<int> sequence(n);

// bool check(int d)
// {
// 	int last = 0;
// 	for (int i = 1; i < k; ++i) {
// 		int cur = last + 1;
// 		while (cur < n && sequence[cur] - sequence[last] < d) ++cur;
// 		if (cur == n) return false;
// 		else last = cur;
// 	}

// 	return true;
// }

bool check(int d)
{
	int cnt = k - 1, pre = 0;
	for (int i = 1; i < n; ++i) {
		if (sequence[i] - sequence[pre] >= d) {
			--cnt;
			pre = i;
		}
		if (cnt == 0) break;
	}
	return cnt == 0;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
   	while (cin >> n >> k) {
   		for (int i = 0; i < n; ++i) cin >> sequence[i];
   		
   		sort(sequence.begin(), sequence.begin() + n);
   		int left = 0, right = sequence[n - 1] - sequence[0];

   		while (left < right) {
   			int mid = left + ((right - left + 1) >> 1);
   			if (check(mid)) left = mid;
   			else right = mid - 1;
   		}
   		cout << left << endl;
   }
	
    return 0;
}
```

问题出现在`mid`的求法，考虑`lower_bound`的时候，如果最后剩下两个元素，那么满足条件`left = mid + 1`会使`left = right`退出循环，`upper_bound`同理，但是本题，满足条件时候`left`不改变，比如最后`left = 2, right = 3`，`mid`会等于2，如果2一直满足条件，就会造成死循环，也就是说，最后剩下两个元素，要保证满足判断条件的时候，`left`的数值是增加的，那么就需要去修改`mid`的求法，所以应该为`mid = int mid = left + ((right - left + 1) >> 1);`。