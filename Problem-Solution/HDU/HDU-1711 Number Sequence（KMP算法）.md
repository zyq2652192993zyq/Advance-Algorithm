> # HDU-1711 Number Sequence（KMP算法）

# Problem Description

```
Given two sequences of numbers : a[1], a[2], ...... , a[N], and b[1], b[2], ...... , b[M] (1 <= M <= 10000, 1 <= N <= 1000000). Your task is to find a number K which make a[K] = b[1], a[K + 1] = b[2], ...... , a[K + M - 1] = b[M]. If there are more than one K exist, output the smallest one.
```

# Input

```
The first line of input is a number T which indicate the number of cases. Each case contains three lines. The first line is two numbers N and M (1 <= M <= 10000, 1 <= N <= 1000000). The second line contains N integers which indicate a[1], a[2], ...... , a[N]. The third line contains M integers which indicate b[1], b[2], ...... , b[M]. All integers are in the range of [-1000000, 1000000].
```

# Output

For each test case, you should output one line which only contain K described above. If no such K exists, output -1 instead.

# Sample Input

```
2
13 5
1 2 1 2 3 1 2 3 1 3 2 1 2
1 2 3 1 3
13 5
1 2 1 2 3 1 2 3 1 3 2 1 2
1 2 3 2 1
```

# Sample Output

```
6
-1
```

---

```c++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getNext(vector<int> &T)
{
    vector<int> next(T.size(), 0);            // next矩阵，含义参考王红梅版《数据结构》p84。
    next[0] = -1;                            // next矩阵的第0位为-1
    int k = 0;                            // k值
    for (size_t j = 2; j < T.size(); ++j)        // 从字符串T的第2个字符开始，计算每个字符的next值
    {
        while (k > 0 && T[j - 1] != T[k])    
            k = next[k];
        if (T[j - 1] == T[k])
            k++;
        next[j] = k;
    }
    return next;                            // 返回next矩阵
}

int KMP(vector<int> &S, vector<int> &T)
{
    vector<int> next = getNext(T);
    int i = 0, j = 0, m = S.size(), n = T.size();
    while (i != m && j != n)
    {
        if (S[i] == T[j])
        {
            ++i;
            ++j;
        }
        else
        {
            j = next[j];
        }
        if (j == -1)
        {
            ++i;
            ++j;
        }
    }
    if (j == n)
        return i - j + 1;
    else
        return -1;
}

int main()
{
    int caseNum;
    cin >> caseNum;

    while(caseNum--){
        int num1, num2;
        cin >> num1 >> num2;

        vector<int> s(num1), pattern(num2);
        for (int i = 0; i < num1; ++i)
            cin >> s[i];
        for (int i = 0; i < num2; ++i)
            cin >> pattern[i];

        int position = KMP(s, pattern);
        cout << position << endl;
    }

    return 0;
}
```

注意输出第一次出现的位置是从1开始计数的。