> # POJ-1580 String Matching（分数化简+字符串基础）

# Description

It's easy to tell if two words are identical - just check the letters. But how do you tell if two words are almost identical? And how close is "almost"?

There are lots of techniques for approximate word matching. One is to determine the best substring match, which is the number of common letters when the words are compared letter-byletter.

The key to this approach is that the words can overlap in any way. For example, consider the words CAPILLARY and MARSUPIAL. One way to compare them is to overlay them:

CAPILLARY

MARSUPIAL

There is only one common letter (A). Better is the following overlay:

```
CAPILLARY

     MARSUPIAL
```

with two common letters (A and R), but the best is:

```
   CAPILLARY

MARSUPIAL
```

Which has three common letters (P, I and L).

The approximation measure appx(word1, word2) for two words is given by:

common letters * 2
\-----------------------------
length(word1) + length(word2)

Thus, for this example, appx(CAPILLARY, MARSUPIAL) = 6 / (9 + 9) = 1/3. Obviously, for any word W appx(W, W) = 1, which is a nice property, while words with no common letters have an appx value of 0.

# Input

The input for your program will be a series of words, two per line, until the end-of-file flag of -1.
Using the above technique, you are to calculate appx() for the pair of words on the line and print the result.
The words will all be uppercase.

# Output

Print the value for appx() for each pair as a reduced fraction,Fractions reducing to zero or one should have no denominator.

# Sample Input

```
CAR CART
TURKEY CHICKEN
MONEY POVERTY
ROUGH PESKY
A A
-1
```

# Sample Output

```
appx(CAR,CART) = 6/7
appx(TURKEY,CHICKEN) = 4/13
appx(MONEY,POVERTY) = 1/3
appx(ROUGH,PESKY) = 0
appx(A,A) = 1
```

-----

```c++
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <cctype>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

string s1, s2;

inline int GCD(int a, int b)
{
	return b == 0 ? a : GCD(b, a % b);
}

int cal(const string & str1, const string & str2)
{
	int m = str1.size(), n = str2.size();
	int cnt = 0;
	for (int i = 0; i < m && i < n; ++i) {
		if (str1[i] == str2[i]) ++cnt;
	}
	return cnt;
}

int matchLength()
{
	int res = 0;
	int m = s1.size(), n = s2.size();
	for (int i = 0; i < m; ++i) 
		res = max(res, cal(s1.substr(i), s2));
	for (int i = 0; i < n; ++i)
		res = max(res, cal(s2.substr(i), s1));

	return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	while ((cin >> s1) && s1 != "-1") {
		cin >> s2;
		int len = s1.size() + s2.size(); //总长度
		int common = matchLength() * 2; //求公共字母的最大个数 * 2
		int g = GCD(common, len); //求最大公约数，用来化简分数

		cout << "appx(" << s1 << "," << s2 << ") = ";
		if (common == 0) cout << 0 << endl; //没有公共字母
		else if (len == common) cout << 1 << endl; //两个字符一样
		else cout << (common / g) << "/" << (len / g) << endl;
	}

	return 0;
}
```

