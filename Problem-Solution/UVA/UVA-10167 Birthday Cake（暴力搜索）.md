> # UVA-10167 Birthday Cake（暴力搜索）

Links: https://vjudge.net/problem/UVA-10167

## Description

Lucy and Lily are twins. Today is their birthday. Mother buys a birthday cake for them. Now we put the cake onto a Descartes coordinate. Its center is at (0, 0), and the cake’s length of radius is 100. There are 2N (N is a integer, 1 ≤ N ≤ 50) cherries on the cake. Mother wants to cut the cake into two halves with a knife (of course a beeline). The twins would like to be treated fairly, that means, the shape of the two halves must be the same (that means the beeline must go through the center of the cake) , and each half must have N cherrie(s). Can you help her? Note: the coordinate of a cherry (x, y) are two integers. You must give the line as form two integers A, B (stands for Ax + By = 0) each number mustn’t in [−500, 500]. Cherries are not allowed lying on the beeline. For each dataset there is at least one solution.

![image-20211217222516846](/Users/yzhang68/Documents/Yuqi/project/Advance-Algorithm/Problem Solution/UVA-10167 Birthday Cake（暴力搜索）.assets/image-20211217222516846.png)

## Input

The input file contains several scenarios. Each of them consists of 2 parts: The first part consists of a line with a number N, the second part consists of 2N lines, each line has two number, meaning (x, y). There is only one space between two border numbers. The input file is ended with N = 0.

## Output

For each scenario, print a line containing two numbers A and B. There should be a space between them. If there are many solutions, you can only print one of them.

## Sample Input

```
2
-20 20
-30 20
-10 -50
10 -5
0
```

## Sample Output

```
0 1
```

-----

看了数据范围直接暴力搜索，枚举系数a和b，相当于直线把一个圆形分成两半，那么必然存在一半的点使得ax + by < 0，另外一半大于0.因为题目限定不能在直线上，所以当结果为0的时候，直接判定为失败。

```c++
#include <bits/stdc++.h>

using namespace std;


vector<vector<int>> seq(105, vector<int>(2));
int n;


bool isfFind(int a, int b) {
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		if (a * seq[i][0] + b * seq[i][1] == 0) return false;
		if (a * seq[i][0] + b * seq[i][1] < 0) ++cnt;
	}

	return cnt == n / 2;
}

vector<int> solve() {
	vector<int> res(2);
	for (int a = -500; a <= 500; ++a) {
		for (int b = -500; b <= 500; ++b) {
			if (isfFind(a, b)) {
				res[0] = a;
				res[1] = b;
				return res;
			}
		}
	}

	return res;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    while (cin >> n) {
    	if (n == 0) break;
    	n *= 2;
    	for (int i = 0; i < n; ++i) {
    		cin >> seq[i][0] >> seq[i][1];
    	}

    	vector<int> && res = solve();
    	cout << res[0] << " " << res[1] << endl;
    }

    return 0;
}
```

