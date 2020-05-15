> # CodeForces-1350A Orac and Factors(数学规律)

Tags: `900` `math`

Links: http://codeforces.com/problemset/problem/1350/A

-------

# Description

Orac is studying number theory, and he is interested in the properties of divisors.

For two positive integers $a$ and $b$, $a$ is a divisor of $b$ if and only if there exists an integer $c$, such that $a⋅c=b$.

For $n \geq 2$, we will denote as f(n)f(n) the smallest positive divisor of $n$, except $1$.

For example,$ f(7)=7$,$f(10)=2$,$f(35)=5$.

For the fixed integer $n$, Orac decided to add $f(n)$ to $n$.

For example, if he had an integer $n=5$, the new value of $n$ will be equal to $10$. And if he had an integer $n=6$, $n$ will be changed to $8$.

Orac loved it so much, so he decided to repeat this operation several times.

Now, for two positive integers $n$ and $ k$, Orac asked you to add $f(n)$ to $n$ exactly $k$ times (note that $n$ will change after each operation, so $f(n)$ may change too) and tell him the final value of $n$.

For example, if Orac gives you $n=5$ and $k=2$, at first you should add $f(5)=5$ to $n=5$, so your new value of $n$ will be equal to $n=10$, after that, you should add $f(10)=2$ to $10$, so your new (and the final!) value of $n$ will be equal to $12$.

Orac may ask you these queries many times.

# Input

The first line of the input is a single integer $t(1 \leq t \leq 100)$，the number of times that Orac will ask you.

Each of the next $t$ lines contains two positive integers $n, k(2 \leq n \leq 10^6, 1 \leq k \leq 10^9)$, corresponding to a query by Orac.

It is guaranteed that the total sum of $n$ is at most $10^6$.

# Output

Print $t$ lines, the $i$-th of them should contain the final value of $n$ in the $i$-th query by Orac.

# Sample Input

```
3
5 1
8 2
3 4
```

# Sample Output

```
10
12
12
```

-----

```c++
#include <bits/stdc++.h>

using namespace std;

long long solve(long long n, long long k)
{
	if (n & 1) { //n是奇数特判
		int val;
		for (int i = 3; i <= n; i += 2) {
			if (n % i == 0) {
				val = i; break;
			}
		}
		return solve(n + val, k - 1);
	}

	return n + k * 2;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum; cin >> caseNum;
	while (caseNum--) {
		long long n, k; cin >> n >> k;
		cout << solve(n, k) << endl;
	}

	return 0;
}
```

数据范围`n`是$10^6$，但是$k \leq 10^9$，数据范围告诉我们直接模拟肯定GG。根据例子很容易发现，偶数的时候，每次增加的数值就是2，奇数的时候，增加的是数字最小的因数（除了1），并且这个因数一定是奇数，所以变化完后这个数就是偶数了，又会增加2。所以只需要奇数的时候特判一下。