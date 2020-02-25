> # POJ-2453 An Easy Problem（位运算，集合的整数表示）

# Description

As we known, data stored in the computers is in binary form. The problem we discuss now is about the positive integers and its binary form.

Given a positive integer I, you task is to find out an integer J, which is the minimum integer greater than I, and the number of '1's in whose binary form is the same as that in the binary form of I.

For example, if "78" is given, we can write out its binary form, "1001110". This binary form has 4 '1's. The minimum integer, which is greater than "1001110" and also contains 4 '1's, is "1010011", i.e. "83", so you should output "83".

# Input

One integer per line, which is I (1 <= I <= 1000000).

A line containing a number "0" terminates input, and this line need not be processed.

# Output

One integer per line, which is J.

# Sample Input

```
1
2
3
4
78
0
```

# Sample Output

```
2
4
5
8
83
```

------

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>

using namespace std;

const int INF = 0x0ffffff;

int cal(int n)
{
	int x = n & (-n); //取出最后一个1
	int t = n + x; //将最后连续的1最左边的1往左移动1位
	return t | (((n ^ t) / x) >> 2);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	while ((cin >> n) && n) {
		cout << cal(n) << endl;
	}

    return 0;
}
```

详细解释在《基础算法——位运算》里整数的集合表示，核心思路是最后连续的1，最左边的1左移一个位置，余下的1放到最右边，这样一定是比当前数字大但又是满足条件的最小的数字。