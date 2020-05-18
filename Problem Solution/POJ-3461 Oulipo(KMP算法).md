> # POJ-3461 Oulipo(KMP算法)

# Description

The French author Georges Perec (1936–1982) once wrote a book, La disparition, without the letter `'e'`. He was a member of the Oulipo group. A quote from the book:

> Tout avait Pair normal, mais tout s’affirmait faux. Tout avait Fair normal, d’abord, puis surgissait l’inhumain, l’affolant. Il aurait voulu savoir où s’articulait l’association qui l’unissait au roman : stir son tapis, assaillant à tout instant son imagination, l’intuition d’un tabou, la vision d’un mal obscur, d’un quoi vacant, d’un non-dit : la vision, l’avision d’un oubli commandant tout, où s’abolissait la raison : tout avait l’air normal mais…

Perec would probably have scored high (or rather, low) in the following contest. People are asked to write a perhaps even meaningful text on some subject with as few occurrences of a given “word” as possible. Our task is to provide the jury with a program that counts these occurrences, in order to obtain a ranking of the competitors. These competitors often write very long texts with nonsense meaning; a sequence of 500,000 consecutive `'T'`s is not unusual. And they never use spaces.

So we want to quickly find out how often a word, i.e., a given string, occurs in a text. More formally: given the alphabet {`'A'`, `'B'`, `'C'`, …, `'Z'`} and two finite strings over that alphabet, a word *W* and a text *T*, count the number of occurrences of *W* in *T*. All the consecutive characters of W must exactly match consecutive characters of *T*. Occurrences may overlap.

# Input

The first line of the input file contains a single number: the number of test cases to follow. Each test case has the following format:

- One line with the word *W*, a string over {`'A'`, `'B'`, `'C'`, …, `'Z'`}, with 1 ≤ |*W*| ≤ 10,000 (here |*W*| denotes the length of the string *W*).
- One line with the text *T*, a string over {`'A'`, `'B'`, `'C'`, …, `'Z'`}, with |*W*| ≤ |*T*| ≤ 1,000,000.

# Output

For every test case in the input file, the output should contain a single number, on a single line: the number of occurrences of the word *W* in the text *T*.

# Sample Input

```
3
BAPC
BAPC
AZA
AZAZAZA
VERDI
AVERDXIVYERDIAN
```

# Sample Output

```
1
3
0
```

---

```c++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int sum = 0;

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

void KMP(string S, string T) //T = pattern
{
    vector<int> next = getNext(T);
    int i = 0, j = 0;
    while (S[i] != '\0')
    {
        if (T[j] == '@'){
            ++sum;
            j = next[j];
            continue;
        }
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
}

int main()
{
    int caseNum;
    cin >> caseNum;

    while(caseNum--){
        string str, pattern;
        cin >> pattern;
        cin >> str;

        str += "#";
        pattern += "@";

        KMP(str, pattern);
        cout << sum << endl;
        sum = 0;
    }

    return 0;
}
```

这里给str和pattern加上一个必定不一样的字符，是因为我们不是找到第一次出现，而是找出现了多少次，所以next数组需要扩大。同时和传统KMP相比，我们只会在str到末尾的时候停止循环，所以在pattern到了末尾的时候，相应的操作应该是改变j的位置，增加sum值，进行下一次循环。