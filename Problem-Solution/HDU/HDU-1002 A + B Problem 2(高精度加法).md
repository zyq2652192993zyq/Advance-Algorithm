> # HDU-1002 A + B Problem 2(高精度加法)

# Problem Description

I have a very simple problem for you. Given two integers A and B, your job is to calculate the Sum of A + B.

# Input

The first line of the input contains an integer T(1<=T<=20) which means the number of test cases. Then T lines follow, each line consists of two positive integers, A and B. Notice that the integers are very large, that means you should not process them by using 32-bit integer. You may assume the length of each integer will not exceed 1000.

# Output

For each test case, you should output two lines. The first line is "Case #:", # means the number of the test case. The second line is the an equation "A + B = Sum", Sum means the result of A + B. Note there are some spaces int the equation. Output a blank line between two test cases.

# Sample Input

```
2
1 2
112233445566778899 998877665544332211
```

# Sample Output

```
Case 1:
1 + 2 = 3

Case 2:
112233445566778899 + 998877665544332211 = 1111111111111111110
```

----

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> bigNumPlus(vector<char> & num1, vector<char> & num2)
{
	int extra = 0;
	for (size_t i = 0; i < num1.size(); ++i) {
		int sum = (num1[i] - '0') + (num2[i] - '0') + extra;
		extra = sum / 10;
		num1[i] = '0' + sum % 10;
	}
	if (extra & 1) num1[num1.size() - 1] = '1';
	reverse(num1.begin(), num1.end());

	return num1;
}

template <typename T>
ostream & operator<<(ostream & os, const vector<T> & v)
{
	size_t i = 0;
	if (v[0] == '0') i = 1; 
	for ( ; i < v.size(); ++i) {
		os << v[i];
	}

	return os;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int caseNum, num = 0;
	cin >> caseNum;
	while (caseNum--) {
		++num;
		string str1, str2;
		cin >> str1 >> str2;
		int length = max(str1.size(), str2.size()) + 1; //可能存在进位，所以多留出一位

		vector<char> num1(length, '0'), num2(length, '0');
		for (size_t i = 0; i < str1.size(); ++i) {
			num1[str1.size() - 1 - i] = str1[i];
		}

		for (size_t i = 0; i < str2.size(); ++i)
			num2[str2.size() - 1 - i] = str2[i];

		cout << "Case " << num << ":" << endl;
		cout << str1 << " + " << str2 << " = " << bigNumPlus(num1, num2) << endl;
		if(caseNum != 0) cout << endl;
	}

	return 0;
}
```

