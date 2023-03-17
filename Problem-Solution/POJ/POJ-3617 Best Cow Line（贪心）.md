> # POJ-3617 Best Cow Line

# Description

FJ is about to take his *N* (1 ≤ *N* ≤ 2,000) cows to the annual"Farmer of the Year" competition. In this contest every farmer arranges his cows in a line and herds them past the judges.

The contest organizers adopted a new registration scheme this year: simply register the initial letter of every cow in the order they will appear (i.e., If FJ takes Bessie, Sylvia, and Dora in that order he just registers BSD). After the registration phase ends, every group is judged in increasing lexicographic order according to the string of the initials of the cows' names.

FJ is very busy this year and has to hurry back to his farm, so he wants to be judged as early as possible. He decides to rearrange his cows, who have already lined up, before registering them.

FJ marks a location for a new line of the competing cows. He then proceeds to marshal the cows from the old line to the new one by repeatedly sending either the first or last cow in the (remainder of the) original line to the end of the new line. When he's finished, FJ takes his cows for registration in this new order.

Given the initial order of his cows, determine the least lexicographic string of initials he can make this way. 

# Input

* Line 1: A single integer: *N*
* Lines 2..*N*+1: Line *i*+1 contains a single initial ('A'..'Z') of the cow in the *i*th position in the original line

# Output

The least lexicographic string he can make. Every line (except perhaps the last one) contains the initials of 80 cows ('A'..'Z') in the new line.

# Sample Input

```
6
A
C
D
B
C
B
```

# Sample Output

```
ABCBCD
```

---

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int findCow(vector<char> & v, int head, int tail)
{
    int num = tail - head + 1;
    if (num == 1) return head;
    if (num == 2) {
        if (v[head] > v[tail]) return tail;
        else return head;
    }
    if (v[head] < v[tail]) return head;
    else if (v[head] > v[tail]) return tail;
   
    int pos = findCow(v, head + 1, tail - 1);
    if (pos - head <= tail - pos) return head;
    else return tail;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<char> v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    string res;
    int head = 0, tail = n - 1;
    do {
        int pos = findCow(v, head, tail);
        res.push_back(v[pos]);
        if (pos == head) ++head;
        else --tail;
    } while (head <= tail);
    
    for (size_t i = 0; i < res.size(); ++i) {
        if (i != 0 && i % 80 == 0) cout << endl;
        cout << res[i];
    }

    return 0;
}
```

这道题目虽然确实是贪心的方法，但是编程的思路和递归是很接近的。

函数`findCow`的作用是，由`v[head]-v[tail]`字符组成的序列，选择插入头部的字符还是尾部的字符，返回值是应该选择的位置。传入的参数一个是`head`，一个是`tail`，如果传入的这个字符序列长度是1，直接返回`head`；字符序列长度为2，仍然直接比较。长度大于等于3，采用递归的思路（如果`v[head] == v[tail]`），去寻找在`[head+1, tail-1]`插入的位置，所以最后只需要去判断一下head和tail哪个离插入的位置近，则返回相应的位置。

最初出错是在输出上，忽略了每行只能显示80个字符，多余的要换行显示，注意`i != 0`这个条件不能少。