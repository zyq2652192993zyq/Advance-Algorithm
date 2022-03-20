> # HDU-1080 Human Gene Functions(动态规划 最长公共子序列)

# Problem Description

It is well known that a human gene can be considered as a sequence, consisting of four nucleotides, which are simply denoted by four letters, A, C, G, and T. Biologists have been interested in identifying human genes and determining their functions, because these can be used to diagnose human diseases and to design new drugs for them.

A human gene can be identified through a series of time-consuming biological experiments, often with the help of computer programs. Once a sequence of a gene is obtained, the next job is to determine its function. One of the methods for biologists to use in determining the function of a new gene sequence that they have just identified is to search a database with the new gene as a query. The database to be searched stores many gene sequences and their functions – many researchers have been submitting their genes and functions to the database and the database is freely accessible through the Internet.

A database search will return a list of gene sequences from the database that are similar to the query gene. Biologists assume that sequence similarity often implies functional similarity. So, the function of the new gene might be one of the functions that the genes from the list have. To exactly determine which one is the right one another series of biological experiments will be needed.

Your job is to make a program that compares two genes and determines their similarity as explained below. Your program may be used as a part of the database search if you can provide an efficient one.

Given two genes AGTGATG and GTTAG, how similar are they? One of the methods to measure the similarity of two genes is called alignment. In an alignment, spaces are inserted, if necessary, in appropriate positions of the genes to make them equally long and score the resulting genes according to a scoring matrix.

For example, one space is inserted into AGTGATG to result in AGTGAT-G, and three spaces are inserted into GTTAG to result in –GT--TAG. A space is denoted by a minus sign (-). The two genes are now of equal length. These two strings are aligned:

```
AGTGAT-G
-GT--TAG
```

In this alignment, there are four matches, namely, G in the second position, T in the third, T in the sixth, and G in the eighth. Each pair of aligned characters is assigned a score according to the following scoring matrix.

![img](http://acm.hdu.edu.cn/data/images/1080_1.gif)

`*`denotes that a space-space match is not allowed. The score of the alignment above is (-3)+5+5+(-2)+(-3)+5+(-3)+5=9.

Of course, many other alignments are possible. One is shown below (a different number of spaces are inserted into different positions):

```
AGTGATG
-GTTA-G
```

This alignment gives a score of (-3)+5+5+(-2)+5+(-1) +5=14. So, this one is better than the previous one. As a matter of fact, this one is optimal since no other alignment can have a higher score. So, it is said that the similarity of the two genes is 14.

# Input

The input consists of T test cases. The number of test cases ) (T is given in the first line of the input. Each test case consists of two lines: each line contains an integer, the length of a gene, followed by a gene sequence. The length of each gene sequence is at least one and does not exceed 100.

# Output

The output should print the similarity of each test case, one per line.

# Sample Input

```
2 
7 AGTGATG 
5 GTTAG 
7 AGCTATT 
9 AGCTTTAAA 
```

# Sample Output

```
14 
21 
```

---

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> table = {
    {5,-1,-2,-1,-3},
    {-1,5,-3,-2,-4},
    {-2,-3,5,-2,-2},
    {-1,-2,-2,5,-1},
    {-3,-4,-2,-1,0}
};

int transfer(char &c)
{
    if(c=='A') return 0;
    if(c=='C') return 1;
    if(c=='G') return 2;
    if(c=='T') return 3;

    return 4;
}

int main()
{
    int caseNum, m, n;
    string s1, s2;
    cin >> caseNum;

    while(caseNum--){
        vector<int> line(101);
        vector<vector<int>> d(101, line);
        cin >> m >> s1;
        cin >> n >> s2;
        vector<int> v1(m), v2(n);

        for (int i = 0; i < m; ++i) v1[i] = transfer(s1[i]);
        for (int i = 0; i < n; ++i) v2[i] = transfer(s2[i]);

        d[0][0] = 0;
        for (int i = 1; i <= m; ++i) d[i][0] = d[i - 1][0] + table[v1[i-1]][4];
        for (int i = 1; i <= n; ++i) d[0][i] = d[0][i - 1] + table[4][v2[i-1]];

        for (int i = 1; i <= m; ++i){
            for (int j = 1; j <= n; ++j)
                d[i][j] = max(d[i-1][j-1] + table[v1[i-1]][v2[j-1]], max(d[i-1][j]+table[v1[i-1]][4],d[i][j-1]+table[4][v2[j-1]]));
        }

        cout << d[m][n] << endl;
    }

    return 0;
}
```

状态转移，其中$dp[i][j]$表示$s1[i]$和$s2[j]$处能取到的最大分数。

