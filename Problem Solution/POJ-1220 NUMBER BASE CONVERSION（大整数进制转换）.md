> # POJ-1220 NUMBER BASE CONVERSION（大整数进制转换）

# Description

Write a program to convert numbers in one base to numbers in a second base. There are 62 different digits:
{ 0-9,A-Z,a-z }
HINT: If you make a sequence of base conversions using the output of one conversion as the input to the next, when you get back to the original base, you should get the original number.

# Input

The first line of input contains a single positive integer. This is the number of lines that follow. Each of the following lines will have a (decimal) input base followed by a (decimal) output base followed by a number expressed in the input base. Both the input base and the output base will be in the range from 2 to 62. That is (in decimal) A = 10, B = 11, ..., Z = 35, a = 36, b = 37, ..., z = 61 (0-9 have their usual meanings).

# Output

The output of the program should consist of three lines of output for each base conversion performed. The first line should be the input base in decimal followed by a space then the input number (as given expressed in the input base). The second output line should be the output base followed by a space then the input number (as expressed in the output base). The third output line is blank.

# Sample Input

```
8
62 2 abcdefghiz
10 16 1234567890123456789012345678901234567890
16 35 3A0C92075C0DBF3B8ACBC5F96CE3F0AD2
35 23 333YMHOUE8JPLT7OX6K9FYCQ8A
23 49 946B9AA02MI37E3D3MMJ4G7BL2F05
49 61 1VbDkSIMJL3JjRgAdlUfcaWj
61 5 dl9MDSWqwHjDnToKcsWE1S
5 10 42104444441001414401221302402201233340311104212022133030
```

# Sample Output

```
62 abcdefghiz
2 11011100000100010111110010010110011111001001100011010010001

10 1234567890123456789012345678901234567890
16 3A0C92075C0DBF3B8ACBC5F96CE3F0AD2

16 3A0C92075C0DBF3B8ACBC5F96CE3F0AD2
35 333YMHOUE8JPLT7OX6K9FYCQ8A

35 333YMHOUE8JPLT7OX6K9FYCQ8A
23 946B9AA02MI37E3D3MMJ4G7BL2F05

23 946B9AA02MI37E3D3MMJ4G7BL2F05
49 1VbDkSIMJL3JjRgAdlUfcaWj

49 1VbDkSIMJL3JjRgAdlUfcaWj
61 dl9MDSWqwHjDnToKcsWE1S

61 dl9MDSWqwHjDnToKcsWE1S
5 42104444441001414401221302402201233340311104212022133030

5 42104444441001414401221302402201233340311104212022133030
10 1234567890123456789012345678901234567890
```

----

```c++
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int charToNum(char ch)
{
	if ('0' <= ch && ch <= '9') return ch - '0';
	if ('A' <= ch && ch <= 'Z') return ch - 'A' + 10;

	return ch - 'a' + 36;
}

char numToChar(int n)
{
	if (0 <= n && n <= 9) return '0' + n;
	if (10 <= n && n <= 35) return 'A' + (n - 10);

	return 'a' + (n - 36);
}

inline bool isAllZero(string & s)
{
	return s.size() == 0 ? true : false;
}

string conversion(string & sequence, int sourceBase, int targetBase)
{
	if (sequence == "0" || sequence == "1") return sequence;
	string res;
	string quotient = sequence; //商数

	while (!isAllZero(quotient)) {
		int extra = 0;
		string tmpStr;
		for (size_t i = 0; i < quotient.size(); ++i) {
			int tmp = extra * sourceBase + charToNum(quotient[i]);
			tmpStr.push_back(numToChar(tmp / targetBase));
			extra = tmp % targetBase;
		}
		res.push_back(numToChar(extra)); //进制转换中的余数

		size_t pos = 0;
		while (tmpStr[pos] == '0') ++pos;
		quotient = tmpStr.substr(pos);
	}
	reverse(res.begin(), res.end());

	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;

	while (caseNum--) {
		int sourceBase, targetBase;
		string sequence;
		cin >> sourceBase >> targetBase >> sequence;

		cout << sourceBase << " " << sequence << endl;
		cout << targetBase << " " << conversion(sequence, sourceBase, targetBase) << endl;
		if (caseNum != 0) cout << endl; 
	}
	
	return 0;
}
```

![十转二示意图](https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=5db6d89b81cb39dbc5c06054e01709a7/728da9773912b31b302371588618367adab4e170.jpg)

思路就以上面图片为例子，假如将十进制的6转为2进制，利用的是短除法。和这张图略有区别的是，应该在最后的1再进行一次除法，这样被除数就变为了0。程序就是去模拟这个过程，用变量`quotient`代表每次的被除数，用`extra`记录每一次除法的余数，并放在`res`里保存，因为要进行无法预知的多轮除法，所以采用`while`循环，终止条件就是被除数为0的时候，因为输入的数据是大整数，用`string`容器来存储，所以被除数为零意味着其长度为0。