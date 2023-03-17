> # 一本通-1443：【例题4】Addition Chains

### 【题目描述】

已知一个数列a0,a1……ama0,a1……am，其中a0=1,am=na0=1,am=n; a0<a1<a2<……<am−1<ama0<a1<a2<……<am−1<am。对于每个k(1<=k<=m)k(1<=k<=m)满足ak=ai+aj(0<=i,j<=k−1)ak=ai+aj(0<=i,j<=k−1),这里ii与jj可以相等。

现给定nn的值，要求mm的最小值（并不要求输出）及这个数列的值（可能存在多个数列，只输出任意一个满足条件的就可以）。

### 【输入】

多组数据，每行给定一个正整数nn。输入以0结束。

### 【输出】

对于每组数据，输出满足条件的长度最小的数列。

### 【输入样例】

```
5 7 12 15 77 0
```

### 【输出样例】

```
1 2 4 5 1 2 4 6 7 1 2 4 8 12 1 2 4 5 10 15 1 2 4 8 9 17 34 68 77
```

$1 \leq n \leq 100$

----

这道题目思路是很简单，倒序搜索即可，终点在于如何保证不重不漏。假设数字$a_k$由$a_{k - 1}, a_p$相加得到，是否存在另外一组$a_i, a_j$来组成$a_k$呢？假设这种情况存在，并且不是一般性，假设$a_i < a_j$，那么当搜索到$a_j$的时候，$a_j$就相当于现在的$a_{k - 1}$，注意是相当于而不是相等。

很显然按照这种思路，通过$a_i, a_{j}$得到$a_{j + 1}$显然会让序列更短，但是也可能会让序列不满足要求，所以两种情况并不矛盾。

```c++
#include <bits/stdc++.h>

using namespace std;

int n, res;
vector<int> seq(100005), tmp(100005);


void DFS(int step) {
    if (tmp[step - 1] > n) return;
    if (step - 1 > res) return;
    
    if (tmp[step - 1] == n) {
        if (step - 1 < res) {
            res = step - 1;
            for (int i = 0; i < step - 1; ++i) {
                seq[i] = tmp[i];
            }
        }
        return;
    }

    for (int i = step - 1; i >= 0; --i) {
        if (tmp[step - 1] + tmp[i] <= n) {
            tmp[step] = tmp[step - 1] + tmp[i];
            DFS(step + 1);
            tmp[step] = 0;
        }
    }
}


int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (cin >> n) {
        if (n == 0) break;

        fill(tmp.begin(), tmp.end(), 0);
        fill(seq.begin(), seq.end(), 0);
        res = n;
        tmp[0] = 1;
        seq[0] = 1;
        DFS(1);
        
        for (int i = 0; i < res; ++i) {
            cout << seq[i] << " ";
        }
        cout << n << endl;
    }

    return 0;
}

```



