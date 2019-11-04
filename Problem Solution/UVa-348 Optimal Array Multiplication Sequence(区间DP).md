> # UVa-348 Optimal Array Multiplication Sequence(区间DP)

# Description

Given two arrays A and B, we can determine the array C = A B using the standard definition of matrix multiplication:
$$
\begin{equation}
C_{i, j}=\sum_{k} A_{i, k} \times B_{k, j}
\end{equation}
$$
The number of columns in the A array must be the same as the number of rows in the B array.
Notationally, let’s say that rows(A) and columns(A) are the number of rows and columns, respectively,
in the A array. The number of individual multiplications required to compute the entire C array (which
will have the same number of rows as A and the same number of columns as B) is then rows(A)
columns(B) columns(A). For example, if A is a 10 × 20 array, and B is a 20 × 15 array, it will take
10 × 15 × 20, or 3000 multiplications to compute the C array.

To perform multiplication of more than two arrays we have a choice of how to proceed. For example,
if X, Y , and Z are arrays, then to compute X Y Z we could either compute (X Y ) Z or X (Y Z).
Suppose X is a 5 × 10 array, Y is a 10 × 20 array, and Z is a 20 × 35 array. Let’s look at the number
of multiplications required to compute the product using the two different sequences:
(X Y ) Z

* 5 × 20 × 10 = 1000 multiplications to determine the product (XY ), a 5 × 20 array.
* Then 5 × 35 × 20 = 3500 multiplications to determine the final result.
* Total multiplications: 4500.

X (Y Z)

* 10 × 35 × 20 = 7000 multiplications to determine the product (Y Z), a 10 × 35 array
* Then 5 × 35 × 10 = 1750 multiplications to determine the final result.
* Total multiplications: 8750

Clearly we’ll be able to compute (X Y ) Z using fewer individual multiplications.
Given the size of each array in a sequence of arrays to be multiplied, you are to determine an
optimal computational sequence. Optimality, for this problem, is relative to the number of individual
multiplications required.

# Input

For each array in the multiple sequences of arrays to be multiplied you will be given only the dimensions
of the array. Each sequence will consist of an integer N which indicates the number of arrays to be multiplied, and then N pairs of integers, each pair giving the number of rows and columns in an array; the order in which the dimensions are given is the same as the order in which the arrays are to be multiplied. A value of zero for N indicates the end of the input. N will be no larger than 10.

# Output

Assume the arrays are named A1, A2, . . . , AN. Your output for each input case is to be a line containing
a parenthesized expression clearly indicating the order in which the arrays are to be multiplied. Prefix
the output for each case with the case number (they are sequentially numbered, starting with 1). Your
output should strongly resemble that shown in the samples shown below. If, by chance, there are
multiple correct sequences, any of these will be accepted as a valid answer.

# Sample Input

```
3
1 5
5 20
20 1
3
5 10
10 20
20 35
6
30 35
35 15
15 5
5 10
10 20
20 25
0
```

# Sample Output

```
Case 1: (A1 x (A2 x A3))
Case 2: ((A1 x A2) x A3)
Case 3: ((A1 x (A2 x A3)) x ((A4 x A5) x A6))
```

----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0FFFFFFF; 
vector<vector<int>> d(15, vector<int>(15, 0)), s(15, vector<int>(15));

void output(const int i, const int j)
{
    if (i == j) cout << "A" << i;
    else{
        cout << "(";
        output(i, s[i][j]);
        cout << " x ";
        output(s[i][j] + 1, j);
        cout << ")";
    }
}

void intervalDP(vector<int> & p, int n)
{
    for (int length = 2; length <= n; ++length){
        for (int i = 1; i <= n - length + 1; ++i){
            int j = i + length - 1;
            d[i][j] = INF;
            for (int k = i; k < j; ++k){
                if (d[i][j] > d[i][k] + d[k+1][j] + p[i-1]*p[k]*p[j]){
                    d[i][j] = d[i][k] + d[k+1][j] + p[i-1]*p[k]*p[j];
                    s[i][j] = k;
                }
            }
        }
    }
}

void init()
{
    fill(d.begin(), d.end(), vector<int>(15, 0));
    fill(s.begin(), s.end(), vector<int>(15, 0));
}

int main()
{
    int n, caseNum = 0;
    while ((cin >> n) && n){
        ++caseNum;
        vector<int> p(n + 1);
        for (int i = 1; i <= n; ++i)
            cin >> p[i - 1] >> p[i];

        intervalDP(p, n);

        cout << "Case " << caseNum << ": ";
        output(1, n);
        cout << endl;
        init();
    }

    return 0;
}
```

上面这种方法是非递归的方法，还可以用递归的方法，更符合状态转移方程的表达式。

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0FFFFFFF; 
vector<vector<int>> d(15, vector<int>(15, -1)), s(15, vector<int>(15, 0));
vector<int> p(11, 0);

void output(const int i, const int j)
{
    if (i == j) cout << "A" << i;
    else{
        cout << "(";
        output(i, s[i][j]);
        cout << " x ";
        output(s[i][j] + 1, j);
        cout << ")";
    }
}

int intervalDP(const int a, const int b)
{
    if (d[a][b] != -1) return d[a][b];
    if (a == b) return d[a][b] = 0;
    d[a][b] = INF;
    for (int i = a; i < b; ++i){
        int tmp = intervalDP(a, i) + intervalDP(i+1, b) + p[a-1] * p[i] * p[b];
        if (d[a][b] > tmp){
            d[a][b] = tmp;
            s[a][b] = i;
        }
    } 

    return d[a][b]; 
}

void init()
{
    fill(d.begin(), d.end(), vector<int>(15, -1));
    fill(s.begin(), s.end(), vector<int>(15, 0));
    fill(p.begin(), p.end(), 0);
}

int main()
{
    int n, caseNum = 0;
    while ((cin >> n) && n){
        ++caseNum;
        for (int i = 1; i <= n; ++i)
            cin >> p[i - 1] >> p[i];

        int result = intervalDP(1, n);

        cout << "Case " << caseNum << ": ";
        output(1, n);
        cout << endl;

        init();
    }

    return 0;
}
```

状态转移方程：
$$
d[i][j] = \min \{  d[i][k] + d[k+1][j] + p_{i-1} * p_k * p_j   \}
$$
