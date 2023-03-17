> # HDU-1564 Play a game（找规律，基础博弈论）

# Description

New Year is Coming!
ailyanlu is very happy today! and he is playing a chessboard game with 8600.
The size of the chessboard is n*n. A stone is placed in a corner square. They play alternatively with 8600 having the first move. Each time, player is allowed to move the stone to an unvisited neighbor square horizontally or vertically. The one who can't make a move will lose the game. If both play perfectly, who will win the game?

# Input

The input is a sequence of positive integers each in a separate line.
The integers are between 1 and 10000, inclusive,(means 1 <= n <= 10000) indicating the size of the chessboard. The end of the input is indicated by a zero.

# Output

Output the winner ("8600" or "ailyanlu") for each input line except the last zero.
No other characters should be inserted in the output.

# Sample Input

```
2
0
```

# Sample Output

```
8600
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

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    while ((cin >> n) && n) {
    	if ((n * n) & 1) cout << "ailyanlu" << endl;
    	else cout << "8600" << endl;
    }

    return 0;
}
```

