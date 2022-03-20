> # POJ-1050 To the Max（二维矩阵的最大部分和）

#Description

Given a two-dimensional array of positive and negative integers, a sub-rectangle is any contiguous sub-array of size 1*1 or greater located within the whole array. The sum of a rectangle is the sum of all the elements in that rectangle. In this problem the sub-rectangle with the largest sum is referred to as the maximal sub-rectangle.
As an example, the maximal sub-rectangle of the array:

0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2
is in the lower left corner:

9 2
-4 1
-1 8
and has a sum of 15.

# Input

The input consists of an N * N array of integers. The input begins with a single positive integer N on a line by itself, indicating the size of the square two-dimensional array. This is followed by N^2 integers separated by whitespace (spaces and newlines). These are the N^2 integers of the array, presented in row-major order. That is, all numbers in the first row, left to right, then all numbers in the second row, left to right, etc. N may be as large as 100. The numbers in the array will be in the range [-127,127].

# Output

Output the sum of the maximal sub-rectangle.

# Sample Input

```
4
0 -2 -7 0 9 2 -6 2
-4 1 -4  1 -1
8  0 -2
```

# Sample Output

```
15
```

---

```c++
//HDU 1081
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int maxSubArray(vector<int> & nums)
{
    int n = nums.size();
    if (n == 0) return INF;

    int res = -INF, tmpSum = 0;
    // for (auto e : nums) {
    //     tmpSum = max(tmpSum + e, e);
    //     res = max(res, tmpSum);
    // }
    for (int i = 0; i < n; ++i) {
        tmpSum = max(tmpSum + nums[i], nums[i]);
        res = max(res, tmpSum);
    }

    return res;
}


int maxSubMatrix(vector<vector<int> > & nums)
{
    int m = nums.size();
    int res = -INF;
    int n = nums[0].size();

    vector<int> subMax(n, 0);

    for (int i = 0; i < m; ++i) {
        fill(subMax.begin(), subMax.end(), 0);
        for (int j = i; j < m; ++j) {
            for (int k = 0; k < n; ++k) {
                subMax[k] += nums[j][k];
            }
            res = max(res, maxSubArray(subMax));
        }
    }

    return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<vector<int> > matrix(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    cout << maxSubMatrix(matrix) << endl;

    return 0;
}
```

测试数据的生成：

```c++
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	srand(time(NULL));
    int n = 0;
	while (true) {
		n = rand() % 101;
		if (n == 0) continue;
		else break;
	}
	cout << n << endl;

	for (int i = 0; i < n; ++i) {
		int num = rand() % 127;
		int flag = rand() % 2;
		if (flag) cout << num << " ";
		else cout << -num << " ";
	}
	cout << endl;

	return 0;
}
```

这道题目算是很坑的一种了，比如网上的这个程序：

```c++
#include<iostream>
#include<cstdio>
#include<algorithm>
#include <string.h>
#include <math.h>
using namespace std;
const int N = 101;
int mp[N][N],b[N];
int n;

int getMax()
{
    int t = 0,mx = -1;
    int dp[N+1]= {0};
    for(int i=1; i<=n; i++)///从1开始枚举
    {
        if(dp[i-1]>0) dp[i] = dp[i-1]+b[i-1];
        else dp[i]=b[i-1];
        mx = max(mx,dp[i]);
    }
    return mx;
}
int solve()
{
    int mx = -1;
    for(int i=0; i<n; i++)
    {
        for(int j=i; j<n; j++)
        {
            memset(b,0,sizeof(b));
            for(int k=0; k<n; k++)
                for(int l=i; l<=j; l++)
                    b[k]+=mp[l][k];
            mx = max(mx,getMax());
        }
    }
    return mx;
}
int main()
{
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
                scanf("%d",&mp[i][j]);
        }
        int mx = solve();
        printf("%d\n",mx);
    }
    return 0;
}
```

思路和我的是一致的，但是如果拿测试数据

```
1
-95
```

正解应该是`-95`，但是这个代码或生成-1，并且还能通过HDU 1081的测试。