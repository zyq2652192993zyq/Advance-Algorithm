> # Aizu - ALDS1_1_C Prime Numbers(数论-质数检验)

# Description

A prime number is a natural number which has exactly two distinct natural number divisors: 1 and itself. For example, the first four prime numbers are: 2, 3, 5 and 7.

Write a program which reads a list of *N* integers and prints the number of prime numbers in the list.

# Input

The first line contains an integer *N*, the number of elements in the list.

*N* numbers are given in the following lines.

# Output

Print the number of prime numbers in the given list.

# Constraints

1 ≤ *N* ≤ 10000

2 ≤ *an element of the list* ≤ 108

**Sample Input1**

```
5
2
3
4
5
6
```

**Sample Output**1

```
3
```

## Sample Input 2

```
11
7
8
9
10
11
12
13
14
15
16
17
```

## Sample Output 2

```
4
```

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

bool isPrime(int n)
{
	if (n == 2) return true;
	if (!(n & 1)) return false;
	int limit = sqrt(n) + 1;
	for (int i = 3; i <= limit; i += 2) {
		if (n % i == 0) return false;
	}

	return true;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum;
    cin >> caseNum;

    int cnt = 0;
    while (caseNum--) {
    	int n;
    	cin >> n;
    	if (isPrime(n)) ++cnt;
    }
    cout << cnt << endl;

	return 0;
}
```

