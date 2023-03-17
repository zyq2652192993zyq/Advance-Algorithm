> # POJ-2533 Longest Ordered Subsequence(最长上升子序列 LIS)

# Description

A numeric sequence of *ai* is ordered if *a1* < *a2* < ... < *aN*. Let the subsequence of the given numeric sequence (*a1*, *a2*, ..., *aN*) be any sequence (*ai1*, *ai2*, ..., *aiK*), where 1 <= *i1* < *i2* < ... < *iK* <= *N*. For example, sequence (1, 7, 3, 5, 9, 4, 8) has ordered subsequences, e. g., (1, 7), (3, 4, 8) and many others. All longest ordered subsequences are of length 4, e. g., (1, 3, 5, 8).
Your program, when given the numeric sequence, must find the length of its longest ordered subsequence.

# Input

The first line of input file contains the length of sequence N. The second line contains the elements of sequence - N integers in the range from 0 to 10000 each, separated by spaces. 1 <= N <= 1000

# Output

Output file must contain a single integer - the length of the longest ordered subsequence of the given sequence.

# Sample Input

```
7
1 7 3 5 9 4 8
```

# Sample Output

```
4
```

---

```c++
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define maxNum 1000
vector<int> d(maxNum, 0);

void LIS(vector<int> & v) //longest increasing subsequence
{
    
    d[0] = 1;
    int n = v.size();

    for (int j = 1; j < n; ++j){
        int maxLength = 0;
        for (int i = 0; i < j; ++i){
            if (v[i] < v[j] && maxLength < d[i]) 
                maxLength = d[i];
        }
        d[j] = maxLength + 1;
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> v(maxNum);
    for (int i = 0; i < n; ++i)
        cin >> v[i];
    LIS(v);

    cout << *max_element(d.begin(), d.begin() + n) << endl;

    return 0;
}
```

