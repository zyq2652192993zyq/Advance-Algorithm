> # POJ-2718 Smallest Difference（全排列，搜索或STL）

# Description

Given a number of distinct decimal digits, you can form one integer by choosing a non-empty subset of these digits and writing them in some order. The remaining digits can be written down in some order to form a second integer. Unless the resulting integer is 0, the integer may not start with the digit 0.

For example, if you are given the digits 0, 1, 2, 4, 6 and 7, you can write the pair of integers 10 and 2467. Of course, there are many ways to form such pairs of integers: 210 and 764, 204 and 176, etc. The absolute value of the difference between the integers in the last pair is 28, and it turns out that no other pair formed by the rules above can achieve a smaller difference.

# Input

The first line of input contains the number of cases to follow. For each case, there is one line of input containing at least two but no more than 10 decimal digits. (The decimal digits are 0, 1, ..., 9.) No digit appears more than once in one line of the input. The digits will appear in increasing order, separated by exactly one blank space.

# Output 

For each test case, write on a single line the smallest absolute difference of two integers that can be written from the given digits as described by the rules above.

# Sample Input

```
1
0 1 2 4 6 7
```

# Sample Output

```
28
```

----

```c++
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 

vector<int> num;

void removeBlank(string & line)
{
    for (size_t i = 0; i < line.size(); ++i) {
        if (line[i] == ' ') continue;
        else num.push_back(line[i] - '0');
    }
}

int mingap()
{
    int n = num.size();
    if (n == 2) return abs(num[0] - num[1]);

    int res = INF;
    do {
        int mid = n / 2;
        int num1 = num[0], num2 = num[mid];
        if (num1 == 0 || num2 == 0) continue;

        for (int i = 1; i < mid; ++i) num1 = num1 * 10 + num[i];
        for (int i = mid + 1; i < n; ++i) num2 = num2 * 10 + num[i];
        res = min(res, abs(num1 - num2));
    } while (next_permutation(num.begin(), num.begin() + n));

    return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum;
    cin >> caseNum;

    string line;
    getline(cin, line); //需要先把caseNum的换行符读取

    while (caseNum--) {
        getline(cin, line);
        removeBlank(line);
        cout << mingap() << endl;
        num.clear();
    }
    
    return 0;
}
```

设为n1，n2为两个新产生的数，那么n1，n2的位数越接近，其差的绝对值肯定越小。注意0不能作为数字的开头。使用了标准库算法`next_permutation`。以全排列为背景的题目还是很多的.