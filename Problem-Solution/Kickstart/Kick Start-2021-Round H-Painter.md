> # Kick Start-2021-Round H-Painter

Links: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88

-----

### Problem

You have recently started to study how to paint, and in one of the first classes you learned about the three primary colors: *Red*, *Yellow*, and *Blue*. If you combine these colors, you can produce many more colors. For now, the combinations that you have studied are the following:

- *Red* + *Yellow* = *Orange*
- *Red* + *Blue* = *Purple*
- *Yellow* + *Blue* = *Green*
- *Red* + *Yellow* + *Blue* = *Gray*

You still do not understand shades of colors, therefore the proportion and order of each color in the combination does not matter. For example, combining *Red* and *Yellow* produces the same result as combining *Yellow* and *Red*, as well as the same result as combining *Red*, *Yellow*, and *Red* again.

To practice your skills, you want to paint a 1-dimensional painting PP of length NN. Your painting consists of NN squares. From left to right, PiPi represents the color of the i-th square. Initially all squares are *Uncolored*, that is, PiPi = *Uncolored* for every 1≤i≤N1≤i≤N.

In a single stroke, you can choose one of the three primary colors and apply it to a sequence of consecutive squares. In other words, you can choose a color cc and two integers ll and rr, such that 1≤l≤r≤N1≤l≤r≤N, and apply color cc to all squares PjPj such that l≤j≤rl≤j≤r. If the square being painted is currently *Uncolored*, then its color will become cc. Otherwise, the color will be a combination of all the colors applied on this square so far and the new color cc, as described in the list above.

In order to save time, you want to use as few strokes as possible. Given the description of the painting that you want to paint, figure out what is the minimum number of strokes required to paint it.

### Input

The first line of the input gives the number of test cases, TT. TT test cases follow.

Each test case starts with a line containing an integer NN, representing the length of the painting. Then on the next line, there will be a string PP of length NN, representing the painting. The ii-th character represents the color of square PiPi, according to the following list:

- `U` = *Uncolored*
- `R` = *Red*
- `Y` = *Yellow*
- `B` = *Blue*
- `O` = *Orange*
- `P` = *Purple*
- `G` = *Green*
- `A` = *Gray*

### Output

For each test case, output one line containing `Case #xx: yy`, where xx is the test case number (starting from 1) and yy is the minimum number of strokes required to paint the painting.

### Limits

Memory limit: 1 GB.
1≤T≤1001≤T≤100.
1≤N≤1051≤N≤105.

#### Test Set 1

Time limit: 20 seconds.
PiPi will be one of {`Y, B, G`}.

#### Test Set 2

Time limit: 40 seconds.
PiPi will be one of {`U, R, Y, B, O, P, G, A`}.

### Sample

*Note: there are additional samples that are not run on submissions down below.*

## Sample Input

```
2
9
YYYBBBYYY
6
YYGGBB
```

## Sample Output

```
Case #1: 3
Case #2: 2
```

----





```c++
#include <bits/stdc++.h>

using namespace std;


int n;
string s;

unordered_map<char, vector<int>> um {
	{'U', vector<int>{0}},
	{'R', vector<int>{1}},
	{'Y', vector<int>{2}},
	{'B', vector<int>{3}},
	{'O', vector<int>{1, 2}},
	{'P', vector<int>{1, 3}},
	{'G', vector<int>{2, 3}},
	{'A', vector<int>{1, 2, 3}}
};


bool findVal(int target, vector<int> & tmp) {
	for (auto & e : tmp) {
		if (e == target) return true;
	}

	return false;
}


int count(vector<vector<int>> & d, int target) {
	int res = 0;
	for (int i = 0; i < n; ++i) {
		int left = i;
		int right = i;
		while (right < n && findVal(target, d[right])) ++right;
		if (right - left > 0) {
			++res;
			i = right;
		}
	}

	return res;
}



int solve() {
	vector<vector<int>> d;
	for (auto & e : s) {
		d.push_back(um[e]);
	}
// 	d.push_back(um['U']);
// 	n += 1;

    // for (auto & e : d) {
    //     for (auto & ele : e) {
    //         cout << ele << ' ';
    //     }
    //     cout << endl;
    // }

	return count(d, 1) + count(d, 2) + count(d, 3);
}






int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    int cnt = 0;
    while (caseNum--) {
        cin >> n >> s;

        cout << "Case #" << (++cnt) << ": " << solve() << endl;
    }


    return 0;
}
```

