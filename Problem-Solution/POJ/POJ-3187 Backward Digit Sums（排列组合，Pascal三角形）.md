> # POJ-3187 Backward Digit Sums（排列组合，Pascal三角形）

# Description

FJ and his cows enjoy playing a mental game. They write down the numbers from 1 to N (1 <= N <= 10) in a certain order and then sum adjacent numbers to produce a new list with one fewer number. They repeat this until only a single number is left. For example, one instance of the game (when N=4) might go like this:

```
    3   1   2   4

      4   3   6

        7   9

         16
```

Behind FJ's back, the cows have started playing a more difficult game, in which they try to determine the starting sequence from only the final total and the number N. Unfortunately, the game is a bit above FJ's mental arithmetic capabilities.

Write a program to help FJ play the game and keep up with the cows.

# Input

Line 1: Two space-separated integers: N and the final sum.

# Output

Line 1: An ordering of the integers 1..N that leads to the given sum. If there are multiple solutions, choose the one that is lexicographically least, i.e., that puts smaller numbers first.

# Sample Input

```
4 16
```

# Sample Output

```
3 1 2 4
```

# Hint

```
Explanation of the sample:

There are other possible sequences, such as 3 2 1 4, but 3 1 2 4 is the lexicographically smallest.
```

-----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sequence(10);

ostream & operator<<(ostream & os, const vector<int> & v)
{
    for (size_t i = 0; i < v.size(); ++i) {
        os << v[i];
        if (i != v.size() - 1) os << " ";
    }
    return os;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    //初始化序列
    for (int i = 0; i < 10; ++i) sequence[i] = i + 1;
    int n, sum;
    cin >> n >> sum;

    int pos = 0;
    while (pos + n - 1 < 10) {
        vector<int> tmp(sequence.begin() + pos, sequence.begin() + pos + n);
        //计算系数，确定每个数被计算的次数
        vector<int> pascal(n);
        pascal[0] = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = i; j >= 1; --j) {
                pascal[j] += pascal[j - 1];
            }
        }

        do {
            int res = 0;
            for (int i = 0; i < n; ++i) res += tmp[i] * pascal[i];
            if (res == sum) {
                cout << tmp << endl;
                return 0;
            }
        } while (next_permutation(tmp.begin(), tmp.end()));
        ++pos;
    }
 
    return 0;
}
```

不光要输出一个正确的答案，还要输出字典序最小的，受此启发可能会用`next_permutation`。

这个题目灵感其实来源于Huffman编码，在Huffman中，最终的消耗计算紧和结点所在的深度和自身权重有关。受此启发，是不是有同样或者类似的结论。

把中间计算过程展开，发现样例里面，3计算了一次，1和2计算了3次，4计算了一次，虽然和Huffman编码不尽相同，但是可以发现，每个数字被累加的次数恰好是Pascal三角形里面对应的一行，那么就意味着只要知道了这一行的Pascal三角形的结果，便可以很快得出结论。那么每次如何去判断选取哪些数字呢？自然是从头开始的搜索了。

生成Pascal三角形的过程，很容易想到 LeetCode 119里面的方法，只用$O(k)$的空间来生成最终的结果。

