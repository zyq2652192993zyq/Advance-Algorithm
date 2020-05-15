> # CodeForces-1008A Romaji（基础字符串）

Tags: `Implementation` `strings` `900`

Links: http://codeforces.com/contest/1008/problem/A

# Description

Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word ss is Berlanese.

# Input

The first line of the input contains the string ss consisting of |s||s| (1≤|s|≤1001≤|s|≤100) lowercase Latin letters.

# Output

Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).

# Examples

Input

```
sumimasen
```

Output

```
YES
```

Input

```
ninja
```

Output

```
YES
```

Input

```
codeforces
```

Output

```
NO
```

# Note

n the first and second samples, a vowel goes after each consonant except "n", so the word is Berlanese.

In the third sample, the consonant "c" goes after the consonant "r", and the consonant "s" stands on the end, so the word is not Berlanese.

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string s;
	cin >> s;

	int len = s.size();
	set<char> store{'a', 'e', 'i', 'o', 'u'};

	bool flag = true;
	for (int i = 0; i < len; ++i) {
		if (store.find(s[i]) != store.end() || s[i] == 'n') continue;
		else {
			if (i + 1 < len && store.find(s[i + 1]) != store.end()) {
				continue;
			}
			else {
				flag = false;
				break;
			}
		}
	}
	if (flag) cout << "YES" << endl;
	else cout << "NO" << endl;
	
	return 0;
}
```

基础字符串模拟，可以用`set`或大小为26的数组来实现$O(1)$查询。