> # POJ-3280 Cheapest Palindrome（动态规划，回文字符串）

# Description

Keeping track of all the cows can be a tricky task so Farmer John has installed a system to automate it. He has installed on each cow an electronic ID tag that the system will read as the cows pass by a scanner. Each ID tag's contents are currently a single string with length *M* (1 ≤ *M* ≤ 2,000) characters drawn from an alphabet of *N* (1 ≤ *N* ≤ 26) different symbols (namely, the lower-case roman alphabet).

Cows, being the mischievous creatures they are, sometimes try to spoof the system by walking backwards. While a cow whose ID is "abcba" would read the same no matter which direction the she walks, a cow with the ID "abcb" can potentially register as two different IDs ("abcb" and "bcba").

FJ would like to change the cows's ID tags so they read the same no matter which direction the cow walks by. For example, "abcb" can be changed by adding "a" at the end to form "abcba" so that the ID is palindromic (reads the same forwards and backwards). Some other ways to change the ID to be palindromic are include adding the three letters "bcb" to the begining to yield the ID "bcbabcb" or removing the letter "a" to yield the ID "bcb". One can add or remove characters at any location in the string yielding a string longer or shorter than the original string.

Unfortunately as the ID tags are electronic, each character insertion or deletion has a cost (0 ≤ *cost* ≤ 10,000) which varies depending on exactly which character value to be added or deleted. Given the content of a cow's ID tag and the cost of inserting or deleting each of the alphabet's characters, find the minimum cost to change the ID tag so it satisfies FJ's requirements. An empty ID tag is considered to satisfy the requirements of reading the same forward and backward. Only letters with associated costs can be added to a string.

# Input

Line 1: Two space-separated integers: *N* and *M*
Line 2: This line contains exactly *M* characters which constitute the initial ID string
Lines 3.. *N*+2: Each line contains three space-separated entities: a character of the input alphabet and two integers which are respectively the cost of adding and deleting that character.

# Output

Line 1: A single line with a single integer that is the minimum cost to change the given name tag.

# Sample Input

```
3 4
abcb
a 1000 1100
b 350 700
c 200 800
```

# Sample Output

```
900
```

# Hint

If we insert an "a" on the end to get "abcba", the cost would be 1000. If we delete the "a" on the beginning to get "bcb", the cost would be 1100. If we insert "bcb" at the begining of the string, the cost would be 350 + 200 + 350 = 900, which is the minimum.

---

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int n = 26, m = 2005;
vector<int> cost(n);
string str;
vector<vector<int> > d(m, vector<int>(m));

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	cin >> str;
	for (int i = 0; i < n; ++i) {
		char ch;
		int add, del;
		cin >> ch >> add >> del;
		cost[ch - 'a'] = min(add, del);
	}
    
	for (int j = 1; j < m; ++j) {
		for (int i = j - 1; i >= 0; --i) {
			if (str[i] == str[j]) d[i][j] = d[i + 1][j - 1];
			else d[i][j] = min(d[i + 1][j] + cost[str[i] - 'a'], d[i][j - 1] + cost[str[j] - 'a']);
		}
	}

	cout << d[0][m - 1] << endl;

    return 0;
}
```

很典型的一道题目，LeetCode上应该有类似的题目，额外需要思考如果让输出最终结果怎么办？

用$d[i][j]$表示使字符串位置`i`到`j`为回文的代价。如果`s[i] = s[j]`，则相当于在`d[i + 1][j - 1]`的左右两边增加了相同的字符，则代价和`d[i + 1][j - 1 ]`是一样的。

如果`s[i] != s[j]`，那么则相当于在`d[i + 1][j]`删掉`s[i]`或者在右边添加`s[i]`，或者相当于`d[i][j - 1]`删掉`s[j]`或者在左边添加`s[j]`。因为不需要输出解决方案，所以只需要保留添加和删除的最小代价。