> # Kick Start-2021-Round H-Transform the String

Links: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461

------

### Problem

You are given a string SS which denotes a padlock consisting of lower case English letters. You are also given a string FF consisting of set of favorite lower case English letters. You are allowed to perform several operations on the padlock. In each operation, you can change one letter of the string to the one following it or preceding it in the alphabetical order. For example: for the letter `c`, you are allowed to change it to either `b` or `d` in an operation. The letters can be considered in a cyclic order, i.e., the preceding letter for letter `a` would be letter `z`. Similarly, the following letter for letter `z` would be letter `a`.

Your aim is to find the minimum number of operations that are required such that each letter in string SS after applying the operations, is present in string FF.

### Input

The first line of the input gives the number of test cases, TT. TT test cases follow.

Each test case consists of two lines.
The first line of each test case contains the string SS.
The second line of each test case contains the string FF.

### Output

For each test case, output one line containing `Case #xx: yy`, where xx is the test case number (starting from 1) and yy is the minimum number of operations that are required such that each letter in string SS after applying the operations, is one of the characters in string FF.

### Limits

Memory limit: 1 GB.
1≤T≤1001≤T≤100.
1≤1≤ the length of S≤105S≤105.
SS only consists of lower case English letters.
FF only consists of distinct lower case English letters.
The letters in string FF are lexicographically sorted.

#### Test Set 1

Time limit: 20 seconds.
The length of F=1F=1.

#### Test Set 2

Time limit: 40 seconds.
1≤1≤ the length of F≤26F≤26.

### Sample

*Note: there are additional samples that are not run on submissions down below.*

## Sample input

```
2
abcd
a
pppp
p
```

## Sample output

```
Case #1: 6
Case #2: 0
```

----

```c++
#include <bits/stdc++.h>

using namespace std;


string s, t;



int solve() {
	int res = 0;
	for (auto & ch : s) {
		int tmp = 26;
		int left = ch - 'a';
		for (auto & e : t) {
			int right = e - 'a';
			if (right == left) {
				tmp = 0;
				break;
			}
			else if (left < right) {
				tmp = min(tmp, min(right - left, left + 26 - right));
			}
			else {
				tmp = min(tmp, min(left - right, right + 26 - left));
			}
		}

		res += tmp;
	}

	return res;
}




int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    int cnt = 0;
    while (caseNum--) {
        cin >> s >> t;


        cout << "Case #" << (++cnt) << ": " << solve() << endl;
    }


    return 0;
}
```

