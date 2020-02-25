> # POJ-2773 Happy 2006（GCD技巧）

# Description

Two positive integers are said to be relatively prime to each other if the Great Common Divisor (GCD) is 1. For instance, 1, 3, 5, 7, 9...are all relatively prime to 2006.

Now your job is easy: for the given integer m, find the K-th element which is relatively prime to m when these elements are sorted in ascending order.

# Input

The input contains multiple test cases. For each test case, it contains two integers m (1 <= m <= 1000000), K (1 <= K <= 100000000).

# Output

Output the K-th element in a single line.

# Sample Input

```
2006 1
2006 2
2006 3
```

# Sample Output

```
1
3
5
```

------

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <algorithm>

using namespace std;

const int INF = 0X0ffffff;

int n = 1000005;
vector<int> num(n);

inline int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int k;
    while (cin >> n >> k) {
        int cnt = 0; k--; //注意这里的k--
        for (int i = 1; i <= n; ++i) {
            if (gcd(n, i) == 1) {
                num[cnt++] = i;
            }
        }
        cout << (n * (k / cnt) + num[k % cnt]) << endl;
    }
    
    return 0;
}
```

利用`gcd(a*t+b, a) = gcd(a,b)`技巧，因为本题k较大，暴力枚举肯定不可以，注意到m的数字较小，所以可以枚举m以内与m互质的数，根据gcd的变形公式，可以发现是存在循环节的。这里`k / cnt`就是公式里的`t`，而`num[k % cnt]`就是公式里的`b`，我们预先用一个和m等长的数组来记录。