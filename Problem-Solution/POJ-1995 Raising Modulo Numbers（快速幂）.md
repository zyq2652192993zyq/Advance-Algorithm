> # POJ-1995 Raising Modulo Numbers（快速幂）

# Description

People are different. Some secretly read magazines full of interesting girls' pictures, others create an A-bomb in their cellar, others like using Windows, and some like difficult mathematical games. Latest marketing research shows, that this market segment was so far underestimated and that there is lack of such games. This kind of game was thus included into the KOKODáKH. The rules follow:

Each player chooses two numbers Ai and Bi and writes them on a slip of paper. Others cannot see the numbers. In a given moment all players show their numbers to the others. The goal is to determine the sum of all expressions AiBi from all players including oneself and determine the remainder after division by a given number M. The winner is the one who first determines the correct result. According to the players' experience it is possible to increase the difficulty by choosing higher numbers.

You should write a program that calculates the result and is able to find out who won the game.

# Input

The input consists of Z assignments. The number of them is given by the single positive integer Z appearing on the first line of input. Then the assignements follow. Each assignement begins with line containing an integer M (1 <= M <= 45000). The sum will be divided by this number. Next line contains number of players H (1 <= H <= 45000). Next exactly H lines follow. On each line, there are exactly two numbers Ai and Bi separated by space. Both numbers cannot be equal zero at the same time.

# Output

For each assingnement there is the only one line of output. On this line, there is a number, the result of expression

(A1B1+A2B2+ ... +AHBH)mod M.

# Sample Input

```
3
16
4
2 3
3 4
4 5
5 6
36123
1
2374859 3029382
17
1
3 18132
```

# Sample Output

```
2
13195
13
```

------

核心考察点是快速幂。

```c++
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

long long MODE, n;

long long calculate(long long a, long long b)
{
	long long res = 1;
	while (b) {
		if (b & 1) res = res * a % MODE;
		a = a * a % MODE;
		b >>= 1;
	}

	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum; cin >> caseNum;
	while (caseNum--) {
		cin >> MODE >> n;
		long long a, b;
		long long res = 0;
		for (long long i = 0; i < n; ++i) {
			cin >> a >> b;
			res = (res + calculate(a, b)) % MODE;
		} 
		cout << res << endl;
	}

	return 0;
}
```

