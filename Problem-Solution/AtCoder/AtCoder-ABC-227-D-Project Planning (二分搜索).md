> # AtCoder-ABC-227-D-Project Planning (二分搜索)

Links: https://atcoder.jp/contests/abc227/tasks/abc227_d

----

### Problem Statement

KEYENCE has N departments, where $A_i$ employees belong to the i-th department ($1 \leq i \leq N$). No employee belongs to multiple departments.

The company is planning cross-departmental projects. Each project will be composed of exactly K employees chosen from Kdistinct departments.

At most how many projects can be made? No employee can participate in multiple projects.

## Constrains

* $1 \leq K \leq N \leq 2 \times 10^5$
* $1 \leq A_i \leq 10^{12}$

* All values in input are integers.

## Input

Input is given from Standard Input in the following format:

```
N K
a1 a2 a3 ... an
```

## Output

Print the maximum possible number of projects.

## Sample Input1

```
3 3
2 3 4
```

## Sample Output1

```
2
```

## Sample input 2

```
3 3
2 3 4
```

## Sample output2

```
4
```

## Sample Input3

```
4 3
1 1 3 4
```

## Sample Output3

```
2
```

----

道题和以下问题等价：

* LeetCode 2141

* 有n个数，每次从中选出`k`个数字减1，一共可以减去多少次。
* 有`a1, a2, an`共`n`组球，每组球的数量为`ai`，一个盒子可以装`k`个球，问最多可以装多少个盒子。

假设可以装`p`个盒子，那么共需要`p * k`个球，对于每组球，其可以贡献的球的数量为`min(p, ai)`，求出$\sum_{i = 1}^n \min{(a_i, P)}$，如果小于`p * k`，则不能实现，否则可以。于是可以采用二分法来进行求解。

```c++
#include <bits/stdc++.h>

using namespace std;


long long n, k;
vector<long long> seq(2e5 + 5);


void solve() {
    long long left = 0, right = (2e17 + 5) / k;
    while (left < right) {
        long long mid = left + ((right - left + 1) >> 1), sum = 0;
        for (int i = 0; i < n; ++i) sum += min(mid, seq[i]);
        if (sum >= mid * k) left = mid;
        else right = mid - 1;
    }

    cout << left << endl;
}




int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> seq[i];
    }

    solve();



    return 0;
}
```

注意这里初始化的时候，需要除以`k`，否则存在溢出的风险。















