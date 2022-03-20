> # CodeForces-1380A Three Indices（思维或单调栈）

Contest: Educational Codeforces Round 91

Tags: `brute force` `data structure` `900`

Links: http://codeforces.com/contest/1380/problem/A

-----

# Description

ou are given a permutation $p_1, p_2, \cdots, p_n$. Recall that sequence of $n$ integers is called a permutation if it contains all integers from $1$ to $n$ exactly once.

Find three indices ii, jj and kk such that:

- $1 \leq i < j < k \leq n$
- $p_i < p_j$ and $p_j > p_k$

Or say that there are no such indices.

# Input

The first line contains a single integer $T(1 \leq T \leq 200)$ the number of test cases.

Next $2T$  lines contain test cases — two lines per test case. The first line of each test case contains the single integer $n(3 \leq n \leq 1000)$ — the length of the permutation $p$.

The second line contains $n$ integers $p_1, p_2, \cdots , p_n(1 \leq p_i \leq n; p_i \neq p_j, \text{if} \quad i \neq j)$ — the permutation $p$.

# Output

For each test case:

- if there are such indices $i, j$ and $k$, print $\text{YES}$ (case insensitive) and the indices themselves;
- if there are no such indices, print $\text{NO}$ (case insensitive).

If there are multiple valid triples of indices, print any of them.

# Example

## Input

```
3
4
2 1 4 3
6
4 6 1 2 5 3
5
5 3 1 2 4
```

## Output

```
YES
2 3 4
YES
3 5 6
NO
```

-----

一种暴力的解法是对于每个数，去寻找其左边小于它的数，和右边小于它的数，时间复杂度为$O(n^2)$，因为只是找小于它的数，可以简化找找其两侧第一个小于它的数，就变成了单调栈了，需要维护两个数组去记录左右两边小于它的数的坐标，这样时间复杂度为$O(n)$。

```c++
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> seq(1005);
vector<int> leftNum(1005, -1), rightNum(1005, -1);

void solve()
{
    bool flag = false;
    stack<int> s;
    for (int i = 0; i < n; ++i) {
        if (s.empty()) {
            s.push(i);
        }
        else {
            while (!s.empty() && seq[s.top()] > seq[i]) {
                rightNum[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
    }

    s = stack<int>();
    for (int i = n - 1; i >= 0; --i) {
        if (s.empty()) {
            s.push(i);
        }
        else {
            while (!s.empty() && seq[s.top()] > seq[i]) {
                leftNum[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
    }

    int i;
    for (i = 1; i < n - 1; ++i) {
        if (leftNum[i] != -1 && rightNum[i] != -1) {
            flag = true; break;
        }
    }

    if (flag) {
        cout << "YES" << endl;
        cout << (leftNum[i] + 1) << ' ' << (i + 1) << ' ' << (rightNum[i] + 1) << endl;

    }
    else cout << "NO" << endl;

    fill(leftNum.begin(), leftNum.begin() + n, -1);
    fill(rightNum.begin(), rightNum.begin() + n, -1);
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> seq[i];

        solve();
    }


    return 0;
}
```

但是本体存在更简单的写法，只需要考察$p_{i - 1}, p_i, p_{i+1}$，只要找到满足的一个即可输出。假设$p_{i-1} > p_i$，那么此时考察$p_{i-2}, p_{i-1}, p_i$，如果一直考察到首部也不满足，那么说明左侧是单调下降的，右侧同理，所以只要数组中存在，那么必然存在一个相邻的三元组满足题目条件，这样只需要计算`n -2`个元素，时间复杂度$O(n)$，空间复杂度$O(1)$。

```c++
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> seq(1005);

void solve()
{
    for (int i = 1; i < n - 1; ++i) {
        if (seq[i] > seq[i - 1] && seq[i] > seq[i + 1]) {
            cout << "YES" << endl;
            cout << i << ' ' << (i + 1) << ' ' << (i + 2) << endl;
            return;
        }
    }

    cout << "NO" << endl;
}


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> seq[i];

        solve();
    }

    return 0;
}
```

