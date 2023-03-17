> # HDU-1517 A Multiplication Game（找规律，类似巴什博弈）

# Description

Stan and Ollie play the game of multiplication by multiplying an integer p by one of the numbers 2 to 9. Stan always starts with p = 1, does his multiplication, then Ollie multiplies the number, then Stan and so on. Before a game starts, they draw an integer `1 < n < 4294967295` and the winner is who first reaches `p >= n`.

# Input

Each line of input contains one integer number n.

# Output

For each line of input output one line either

Stan wins.

or

Ollie wins.

assuming that both of them play perfectly.

# Sample Input

```
162
17
34012226
```

# Sample Output

```
Stan wins.
Ollie wins.
Stan wins.
```

------

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

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double n;
    while (cin >> n) {
    	while (n > 18) { n /= 18; }
    	if (n <= 9) cout << "Stan wins." << endl;
    	else cout << "Ollie wins." << endl;
    }

    return 0;
}
```

如果在$1 \sim 9$，先手获胜，如果在$10 \sim 18$，则后手获胜，后面的数字依次除以18，看最后落入哪个区间。**注意每一步计算的时候要取浮点数**

