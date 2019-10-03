> # POJ-1458 Common Subsequence（动态规划 最长公共子序列）

# Description

A subsequence of a given sequence is the given sequence with some elements (possible none) left out. Given a sequence X = < x1, x2, ..., xm > another sequence Z = < z1, z2, ..., zk > is a subsequence of X if there exists a strictly increasing sequence < i1, i2, ..., ik > of indices of X such that for all j = 1,2,...,k, xij = zj. For example, Z = < a, b, f, c > is a subsequence of X = < a, b, c, f, b, c > with index sequence < 1, 2, 4, 6 >. Given two sequences X and Y the problem is to find the length of the maximum-length common subsequence of X and Y.

# Input

The program input is from the std input. Each data set in the input contains two strings representing the given sequences. The sequences are separated by any number of white spaces. The input data are correct.

# Output

For each set of data the program prints on the standard output the length of the maximum-length common subsequence from the beginning of a separate line.

# Sample Input

```
abcfbc         abfcab
programming    contest 
abcd           mnp
```

# Sample  Output

```
4
2
0
```

---

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//vector<int> line(200);
//vector<vector<int>> d(200, line); /* d[i][j] 表示序列s1 和s2的最长公共子序列的长度*/

void longestCommonSequence(const string &s1, const string & s2)
{
    vector<int> line(201);
    vector<vector<int>> d(201, line); /* 字符串最大长度为200 */

    int m = s1.size(), n = s2.size();
    for (int i = 0; i <= m; ++i) d[i][0] = 0;
    for (int i = 0; i <= n; ++i) d[0][i] = 0;

    for (int i = 1; i <= m; ++i){
        for (int j = 1; j <= n; ++j){
            if (s1[i - 1] == s2[j - 1]) d[i][j] = d[i-1][j-1] + 1;
            else d[i][j] = d[i-1][j] > d[i][j-1] ? d[i-1][j] : d[i][j-1];
        }
    }

    cout << d[m][n] << endl;
}

int main()
{
    string s1, s2;
    while (cin >> s1 >> s2){
        longestCommonSequence(s1, s2);
    }

    return 0;
}
```

设序列$X=\left(x_{1}, x_{2}, \cdots, x_{m}\right)$和$y = \left(y_{1}, y_{2}, \cdots, y_{n}\right)$的最长公共子序列为$Z=\left(z_{1}, z_{2}, \cdots, z_{k}\right)$

* 若$x_m = y_n$， 则$z_k = x_m = y_n$，且$z_{k - 1}$是$x_{m-1} $和$y_{n-1}$的最长公共子序列
* 若$x_{m} \neq y_{n}$,且$z_{k} \neq x_{m}$，则$z$是$x_{m-1}$和$y_n$的最长公共子序列
* 若$x_{m} \neq y_{n}$,且$z_{k} \ne y_{n}$，则$z$是$x$和$y_{n-1}$的最长公共子序列。

设状态为$d[i][j]$，表示序列$X$和$Y$的最长公共子序列的长度，状态转移方程是：
$$
d[i][j]=\left\{\begin{array}{ll}{0} & {i=0, j=0} \\ {d[i-1][j-1]+1} & {i, j>0 ; x_{i}=y_{i}} \\ {\max \{d[i][j-1], d[i-1][j]\}} & {i, j>0 ; x_{i} \neq y_{i}}\end{array}\right.
$$
如果要打印出最长公共子序列，则需要另外一个数组$p$，其中$p[i][j]$记录状态$d[i][j]$是由哪个子问题得到的。

如果想进一步输出公共子序列的具体形式：

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void printCommonSequence(const string &s1, const int m, const string &s2, const int n, vector<vector<int>> &p)
{
    if (m == 0 || n == 0) return;
    if (p[m][n] == 1) {
        printCommonSequence(s1, m - 1, s2, n - 1, p);
        cout << s1[m-1];
    } 
    else if (p[m][n] == 2) {
        printCommonSequence(s1, m - 1, s2, n, p);
    } 
    else {
        printCommonSequence(s1, m, s2, n - 1, p);
    }
}

void longestCommonSequence(const string &s1, const string & s2)
{
    vector<int> line(201);
    vector<vector<int>> d(201, line); /* 字符串最大长度为200 */
    vector<vector<int>> p(201, line);

    int m = s1.size(), n = s2.size();
    for (int i = 0; i <= m; ++i) d[i][0] = 0;
    for (int i = 0; i <= n; ++i) d[0][i] = 0;

    for (int i = 1; i <= m; ++i){
        for (int j = 1; j <= n; ++j){
            if (s1[i - 1] == s2[j - 1]){
                d[i][j] = d[i-1][j-1] + 1;
                p[i][j] = 1;
            } 
            else{
                if (d[i-1][j] >= d[i][j-1]){
                    d[i][j] = d[i-1][j];
                    p[i][j] = 2;
                }
                else{
                    d[i][j] = d[i][j-1];
                    p[i][j] = 3;
                }
            } 
        }
    }
    cout << d[m][n] << " ";
    printCommonSequence(s1, m, s2, n, p);
    cout << endl;
}

int main()
{
    string s1, s2;
    while (cin >> s1 >> s2){
        longestCommonSequence(s1, s2);
    }

    return 0;
}
```

```shell
# run result
4 abcb
2 on
0 
```

