> # POJ-3176 Cow Bowling(DP，数字三角形)

# Description

The cows don't use actual bowling balls when they go bowling. They each take a number (in the range 0..99), though, and line up in a standard bowling-pin-like triangle like this:

```
          7



        3   8



      8   1   0



    2   7   4   4



  4   5   2   6   5
```

Then the other cows traverse the triangle starting from its tip and moving "down" to one of the two diagonally adjacent cows until the "bottom" row is reached. The cow's score is the sum of the numbers of the cows visited along the way. The cow with the highest score wins that frame.

Given a triangle with N (1 <= N <= 350) rows, determine the highest possible sum achievable.

# Input

Line 1: A single integer, N

Lines 2..N+1: Line i+1 contains i space-separated integers that represent row i of the triangle.

# Output

Line 1: The largest sum achievable using the traversal rules

# Sample Input

```
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```

# Sample Output

```
30
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 355;
vector<vector<int> > d(n, vector<int>(n)), sequence(n, vector<int>(n));

int numTriangle()
{
	d[0][0] = sequence[0][0];
	for (int i = 1; i < n; ++i) {
		for (int j = 0; j <= i; ++j) {
			d[i][j] = sequence[i][j] + (j >= 1 ? max(d[i-1][j], d[i-1][j-1]) : d[i-1][j]);
		}
	}
	return *max_element(d[n - 1].begin(), d[n - 1].begin() + n);
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= i; ++j) {
			cin >> sequence[i][j];
		} 
	}
	cout << numTriangle() << endl;

    return 0;
}
```

数字三角形的模板题，注意两点，一点是初始条件`d[0][0] = sequence[0][0];`，第二个是判断列是否大于0，即`j >= 1 ? max(d[i-1][j], d[i-1][j-1]) : d[i-1][j])`