> # 字符串算法-KMP算法 & 扩展KMP算法

参考资料：

* <https://blog.csdn.net/u013480600/article/details/44646517

* 邝斌带你飞专题
* [一本通提高篇 KMP算法](https://blog.csdn.net/dhdhdhx/article/details/103208555)
* [LOJ 一本通提高篇2.2KMP算法 例题+练习（坑）](https://blog.csdn.net/seeker_LJYing/article/details/96422953)

## KMP算法——查找模式串在文本串中是否出现

查找模式串在文本串中是否出现是KMP的模板题，或者说是查找模式串在文本串中第一次出现的位置。

- [x] HDU 1711Number Sequence(KMP:找模板第一次出现的位置)：KMP模板题。



## KMP算法——统计模式串在文本串中出现的次数

给定模式串和文本串，查找模式串在文本串中的所有出现位置并输出。

- [x] POJ 3461Oulipo(KMP:统计一个串出现的次数)：KMP模板题。（或者用字符串哈希解决）



## KMP算法——求多个字符串的LCM



## Z函数——

扩展KMP算法也叫做Z函数。



模板题目：

- [x] POJ 3461Oulipo(KMP:统计一个串出现的次数)：KMP模板题。
- [x] HDU 1711Number Sequence(KMP:找模板第一次出现的位置)：KMP模板题。
- [ ] HDU 3336Count the string(KMP:串前缀匹配自身+DP)：简单的前缀匹配+DP问题。
- [ ] POJ3080 Blue Jeans(KMP:最长连续公共子序列)：求多个字符串的最长公共连续子串，如果存在多个长度相同的就输出字典序最小的那个。
- [ ] POJ3450 Corporate Identity(KMP:最长连续公共子序列)：类似于上一题。
- [ ] HDU2087剪花布条(KMP:贪心)：需要贪心的从左到右有考虑。
- [ ] HDU2203亲和串(KMP:循环移位):给你串T和串P问你串P是否能和T循环移K位后的串匹配。
- [ ] HDU1867 A + B for you again(KMP:后缀与前缀)：字符串合并

KMP 前缀与后缀

- [ ] HDU 2594Simpsons’ HiddenTalents(KMP:后缀与前缀)：KMP的思想。
- [ ] POJ 2752Seek the Name, Seekthe Fame(KMP:后缀与前缀)：找出所有前缀与后缀匹配的长度。

求字符串最短循环节

- [ ] UVA 1328Period(KMP:最短循环节)：如何求字符串的循环节？ 或者POJ 1961
- [x] POJ 2406Power Strings(KMP:找串循环节)：求出最小循环节个数。
- [ ] HDU 3746Cyclic Nacklace(KMP:补齐循环节):要你补充完整一个串，使得该串有循环节构成
- [ ] POJ 2185Milking Grid(KMP:循环节加强版)：转换思维。

讲解较好的文章：阮一峰

<http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html>

但是文章的不足是并没有解释为什么移动的步数 = 部分匹配的字符串长度 - 部分匹配表对应的值。

比如文章里所指的ABCDABD，加入ABCDAB部分匹配，但是在最后一个D不匹配，求得部分匹配表。试想如果部分匹配的部分前缀三个字符和后缀三个字符匹配，那么前两个字符和后两个字符必定匹配，那么也就是说余下不匹配的部分不需要去检查了（也就是部分匹配的字符串长度 - 部分匹配表对应的值）。

在《算法》一书中，还涉及了DFA（有限状态自动机），但是这部分适合单独拿出来写。

<https://www.cnblogs.com/LUO77/p/5603893.html>

<https://www.cnblogs.com/renjiashuo/p/6896062.html>

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

int KMP(string S, string T)
{
    vector<int> next = getNext(T);
    int i = 0, j = 0;
    while (S[i] != '\0' && T[j] != '\0')
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
    if (T[j] == '\0')
        return i - j;
    else
        return -1;
}

int main()
{
    string S = "ababaababcb";
    string T = "ababc";
    int num = KMP(S, T);
    cout << num;
    return 0;
}
```


**扩展KMP算法**

参考博客：

<https://segmentfault.com/a/1190000008663857>

<https://subetter.com/algorithm/extended-kmp-algorithm.html>

- [ ] POJ 2185
- [ ] POJ 2752
- [ ] POJ 1699
- [ ] POJ 3376(扩展KMP + Trie树)
- [ ] HDU 2594
- [ ] HDU 6629
- [ ] HDU 4333
- [ ] HDU 4300(KMP 或扩展KMP)
- [ ] HDU 6153
- [ ] 洛谷【模板】P5410 扩展KMP

**Input**

```
aaaaabbb
aaaaac
abc
def
```

**Program**

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

/* 求解 T 中 next[]，注释参考 GetExtend() */
vector<int> GetNext(string & T)
{
    int a = 0, p = 0, m = T.size();
    vector<int> next(m);
    next[0] = m;

    for (int i = 1; i < m; i++)
    {
        if (i >= p || i + next[i - a] >= p)
        {
            if (i >= p)
                p = i;

            while (p < m && T[p] == T[p - i])
                p++;

            next[i] = p - i;
            a = i;
        }
        else
            next[i] = next[i - a];
    }

    return next;
}

/* 求解 extend[] */
vector<int> GetExtend(string & S, string & T, vector<int> & next)
{
    int a = 0, p = 0, n = S.size(), m = T.size();
    vector<int> extend(n);

    for (int i = 0; i < n; i++)
    {
        if (i >= p || i + next[i - a] >= p) // i >= p 的作用：举个典型例子，S 和 T 无一字符相同
        {
            if (i >= p)
                p = i;

            while (p < n && p - i < m && S[p] == T[p - i])
                p++;

            extend[i] = p - i;
            a = i;
        }
        else
            extend[i] = next[i - a];
    }

    return extend;
}

ostream & operator<<(ostream & os, vector<int> &v)
{
    for (const auto &e : v)
        os << e << " ";

    return os;
}

int main()
{
    string S, T;
    
    while (cin >> S >> T)
    {
        vector<int> next = GetNext(T);
        vector<int> extend = GetExtend(S, T, next);

        // 打印 next
        cout << "next:   " << next << endl;     
 
        // 打印 extend
        cout << "extend: " << extend << endl;
    }
    return 0;
}
```

```shell
# run result
next:   6 4 3 2 1 0 
extend: 5 4 3 2 1 0 0 0 
next:   3 0 0 
extend: 0 0 0
```

**问题定义：**给定两个字符串 S 和 T（长度分别为 n 和 m），下标从 0 开始，定义`extend[i]`等于`S[i]...S[n-1]`与 T 的最长相同前缀的长度，求出所有的`extend[i]`。举个例子，看下表：

| i         | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| S         | a    | a    | a    | a    | a    | b    | b    | b    |
| T         | a    | a    | a    | a    | a    | c    |      |      |
| extend[i] | 5    | 4    | 3    | 2    | 1    | 0    | 0    | 0    |

为什么说这是 KMP 算法的扩展呢？显然，如果在 S 的某个位置 i 有`extend[i]`等于 m，则可知在 S 中找到了匹配串 T，并且匹配的首位置是 i。而且，扩展 KMP 算法可以找到 S 中所有 T 的匹配。接下来具体介绍下这个算法。



