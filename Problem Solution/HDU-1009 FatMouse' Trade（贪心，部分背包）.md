> # HDU-1009 FatMouse' Trade（贪心，部分背包）

# Description

FatMouse prepared M pounds of cat food, ready to trade with the cats guarding the warehouse containing his favorite food, JavaBean.
The warehouse has N rooms. The i-th room contains J[i] pounds of JavaBeans and requires F[i] pounds of cat food. FatMouse does not have to trade for all the JavaBeans in the room, instead, he may get J[i]* a% pounds of JavaBeans if he pays F[i]* a% pounds of cat food. Here a is a real number. Now he is assigning this homework to you: tell him the maximum amount of JavaBeans he can obtain.

# Input

The input consists of multiple test cases. Each test case begins with a line containing two non-negative integers M and N. Then N lines follow, each contains two non-negative integers J[i] and F[i] respectively. The last test case is followed by two -1's. All integers are not greater than 1000.

# Output

For each test case, print in a single line a real number accurate up to 3 decimal places, which is the maximum amount of JavaBeans that FatMouse can obtain.

# Sample Input

```
5 3
7 2
4 3
5 2
20 3
25 18
24 15
15 10
-1 -1
```

# Sample Output

```
13.333
31.500
```

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <set>
#include <algorithm>

using namespace std;

struct Node {
    double weight, value;
    double ratio;
    bool operator<(const Node & obj) const
    {
        return ratio > obj.ratio;
    }
};

int n;
vector<Node> num(1005);
double m;

double solve()
{
    if (m == 0) return 0;
    sort(num.begin(), num.begin() + n);

    double res = 0;
    for (int i = 0; i < n; ++i) {
        if (num[i].weight >= m) {
            res += m * num[i].value / num[i].weight;
            m = 0;
        }
        else {
            m -= num[i].weight;
            res += num[i].value;
        }
        if (m == 0) break;
    } 

    return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while ((cin >> m >> n) && m != -1 && n != -1) {
        for (int i = 0; i < n; ++i) {
            cin >> num[i].value >> num[i].weight;
            num[i].ratio = num[i].value / num[i].weight;
        }
        cout << fixed << setprecision(3) << solve() << endl;
    }

    return 0;
}
```

