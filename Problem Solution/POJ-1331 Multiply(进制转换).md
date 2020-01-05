> # POJ-1331 Multiply(进制转换)

# Description

$6*9 = 42$" is not true for base 10, but is true for base 13. That is,$ 6(13) * 9(13) = 42(13) $because $42(13) = 4 * 13^1 + 2 * 13^0 = 54(10)$.

You are to write a program which inputs three integers p, q, and r and determines the base B (2<=B<=16) for which p * q = r. If there are many candidates for B, output the smallest one. For example, let p = 11, q = 11, and r = 121. Then we have 11(3) * 11(3) = 121(3) because $11(3) = 1 * 3^1 + 1 * 3^0 = 4(10)$ and $121(3) = 1 * 3^2 + 2 * 3^1 + 1 * 30 = 16(10)$. For another base such as 10, we also have 11(10) * 11(10) = 121(10). In this case, your program should output 3 which is the smallest base. If there is no candidate for B, output 0.

# Input

The input consists of T test cases. The number of test cases (T ) is given in the first line of the input file. Each test case consists of three integers p, q, and r in a line. All digits of p, q, and r are numeric digits and 1<=p,q, r<=1,000,000.

# Output

Print exactly one line for each test case. The line should contain one integer which is the smallest base for which p * q = r. If there is no such base, your program should output 0.

# Sample Input

```
3
6 9 42
11 11 121
2 2 2
```

# Sample Output

```
13
3
0
```

----

```c++
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

inline long long conversion(int n, int mode)
{
	long long sum = 0;
	long long extra = 1;
	do {
		int num = n % 10; //取出最后一位
		sum += num * extra;
		extra *= mode;
		n /= 10;
	} while (n != 0);

	return sum;
}

int maxDigit(int n)
{
	int res = 0;
	do {
		int num = n % 10;
		res = max(res, num);
		n /= 10;
	} while (n != 0);

	return res;
}

int baseNum(int p, int q, int r)
{
	int base = max(maxDigit(p), max(maxDigit(q), maxDigit(r)));
	base = max(2, base + 1);

	for (int i = base; i <= 16; ++i) {
		if (conversion(p, i) * conversion(q, i) == conversion(r, i)) return i;
	}

	return 0;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		int p, q, r;
		cin >> p >> q >> r;
		cout << baseNum(p, q, r) << endl;
	}

	return 0;
}
```

注意第36行的`base = max(2, base + 1);`，最开始忘记`base+1`了。