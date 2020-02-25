> # 字符串算法-KMP算法 & 扩展KMP算法

参考：

<https://blog.csdn.net/u013480600/article/details/44646517

邝斌带你飞专题

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

设长字符串为`S`，短字符串为`T`，`next`数组的长度与短字符串T的长度一致，`next[j]`代表使`T[0]~T[k-1]=T[j-k]~T[j-1]`成立的最大`k`值。

当`T="ababc"`时，`next=[-1,0,0,1,2]`。

通俗的讲，`next[j]`代表了从`0`往后查`k`个字母与从`j-1`往前查`k`个字母，这k个字母按角标排列，正好完全一样的最大`k`值，其作用是减少回溯的距离，从而减少比较次数。

好，先把这个放一边，我们自己来推导思路，现在要始终记住一点，`next[j]`的值（也就是k）表示，当`P[j] != T[i]时，j`指针的下一步移动位置。

先来看第一个：当j为0时，如果这时候不匹配，怎么办？

 ![img](https://images0.cnblogs.com/blog/416010/201308/17084258-efd2e95d3644427ebc0304ed3d7adefb.png)

像上图这种情况，**j****已经在最左边了，不可能再移动了，这时候要应该是i****指针后移**。所以在代码中才会有next[0] = -1;这个初始化。

如果是当j为1的时候呢？

 ![img](https://images0.cnblogs.com/blog/416010/201308/17084310-29f9f8dbb6034151a383e7ccf6f5583e.png)

显然，j指针一定是后移到0位置。因为它前面也就只有这一个位置了~~~

 

下面这个是最重要的，请看如下图：

 ![img](https://images0.cnblogs.com/blog/416010/201308/17084327-8a3cdfab03094bfa9e5cace26796cae5.png) ![img](https://images0.cnblogs.com/blog/416010/201308/17084342-616036472ab546c082aa991004bb0034.png)

 

请仔细对比这两个图。

我们发现一个规律：

当`P[k] == P[j]`时，

有`next[j+1] == next[j] + 1`

其实这个是可以证明的：

因为在`P[j]`之前已经有`P[0 ~ k-1] == p[j-k ~ j-1]。（next[j] == k)`

这时候现有`P[k] == P[j]`，我们是不是可以得到`P[0 ~ k-1] + P[k] == p[j-k ~ j-1] + P[j]`。

即：`P[0 ~ k] == P[j-k ~ j]`，即`next[j+1] == k + 1 == next[j] + 1`。

这里的公式不是很好懂，还是看图会容易理解些。

 

那如果`P[k] != P[j]`呢？比如下图所示：

![img](https://images0.cnblogs.com/blog/416010/201308/17122358-fd7e52dd382c4268a8ff52b85bff465d.png) 

像这种情况，如果你从代码上看应该是这一句：`k = next[k];`为什么是这样子？你看下面应该就明白了。

 ![img](https://images0.cnblogs.com/blog/416010/201308/17122439-e349fed25e974e7886a27d18871ae48a.png)

现在你应该知道为什么要`k = next[k]`了吧！像上边的例子，我们已经不可能找到[ A，B，A，B ]这个最长的后缀串了，但我们还是可能找到[ A，B ]、[ B ]这样的前缀串的。所以这个过程像不像在定位[ A，B，A，C ]这个串，当C和主串不一样了（也就是k位置不一样了），那当然是把指针移动到next[k]啦。

---

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

## 一：算法流程

（1）

![img](https://subetter.com/images/figures/20180412_01.png)

如上图，假设当前遍历到 S 串位置 i，即`extend[0]...extend[i - 1]`这 i 个位置的值已经计算得到。设置两个变量，a 和 p。p 代表以 a 为起始位置的字符匹配成功的最右边界，也就是 "p = 最后一个匹配成功位置 + 1"。相较于字符串 T 得出，**S[a...p) 等于 T[0...p-a)**。

再定义一个辅助数组`int next[]`，其中`next[i]`含义为：`T[i]...T[m - 1]`与 T 的最长相同前缀长度，m 为串 T 的长度。举个例子：

| i       | 0    | 1    | 2    | 3    | 4    | 5    |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- |
| T       | a    | a    | a    | a    | a    | c    |
| next[i] | 6    | 4    | 3    | 2    | 1    | 0    |

（2）

![img](https://subetter.com/images/figures/20180412_02.png)

`S[i]`对应`T[i - a]`，如果`i + next[i - a] < p`，如上图，三个椭圆长度相同，根据 next 数组的定义，此时`extend[i] = next[i - a]`。

（3）

![img](https://subetter.com/images/figures/20180412_03.png)

如果`i + next[i - a] == p`呢？如上图，三个椭圆都是完全相同的，`S[p] != T[p - a]`且`T[p - i] != T[p - a]`，但`S[p]`有可能等于`T[p - i]`，所以我们可以直接从`S[p]`与`T[p - i]`开始往后匹配，加快了速度。

（4）

![img](https://subetter.com/images/figures/20180412_04.png)

如果`i + next[i - a] > p`呢？那说明`S[i...p)`与`T[i-a...p-a)`相同，注意到`S[p] != T[p - a]`且`T[p - i] == T[p - a]`，也就是说`S[p] != T[p - i]`，所以就没有继续往下判断的必要了，我们可以直接将`extend[i]`赋值为`p - i`。

（5）最后，就是求解 next 数组。我们再来看下`next[i]`与`extend[i]`的定义：

- **next[i]**： `T[i]...T[m - 1]`与 T 的最长相同前缀长度；
- **extend[i]**： `S[i]...S[n - 1]`与 T 的最长相同前缀长度。

恍然大悟，求解`next[i]`的过程不就是 T 自己和自己的一个匹配过程嘛。

