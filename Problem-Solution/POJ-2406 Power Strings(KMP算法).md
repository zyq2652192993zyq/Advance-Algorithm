> # POJ-2406 Power Strings(KMP算法)

#Description

Given two strings a and b we define a*b to be their concatenation. For example, if a = "abc" and b = "def" then a*b = "abcdef". If we think of concatenation as multiplication, exponentiation by a non-negative integer is defined in the normal way: a^0 = "" (the empty string) and a^(n+1) = a*(a^n).

# Input

Each test case is a line of input representing s, a string of printable characters. The length of s will be at least 1 and will not exceed 1 million characters. A line containing a period follows the last test case.

# Output

For each s you should print the largest n such that s = a^n for some string a.

# Sample Input

```
abcd
aaaa
ababab
.
```

# Sample Output

```
1
4
3
```

---

```c++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getNext(string T)
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

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string str;
    while ((cin >> str) && str != "."){
        int n = str.size();
        str += "#";
        vector<int> next = getNext(str);
        if (n % (n - next[n]) == 0)
            cout << n / (n - next[n]) << endl;
        else
            cout << 1 << endl;
        
    }
    
    return 0;
}
```

