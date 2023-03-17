> # ALGOSPORT-BOGGLE (动态规划)

link: https://algospot.com/judge/problem/read/BOGGLE

#### Problem



![img](ALGOSPORT-BOGGLE (动态规划).assets/boggle.png)

The Boggle game is a
game to find the English words that are made by arranging the letters that meet while moving the pen, starting from one letter on the game board, which is a 5x5 alphabet grid like the picture (a). The pen can move up, down, left, right, or diagonally to adjacent cells and cannot skip text. It is possible to go through past characters again, but you cannot write the same character multiple times without moving the pen.

For example, (b), (c), and (d) in the figure show the results of finding PRETTY, GIRL, and REPEAT in the grid of (a), respectively.

Given a board and a list of known words, write a program that prints whether each word can be found on the board.

> **Caution** : Be careful if you are trying to solve this problem after reading Chapter 6 of Algorithmic Problem Solving Strategies. The example code in Chapter 6 is too slow to solve this problem. See later in Chapter 6 and Chapter 8.



#### input



The first line of input is given the number of test cases C (C <= 50). On the first line of each test case, you will be given a 5 letter board for each 5 lines. All squares on the board are uppercase letters.
The next line is given the number of words we know N (1 <= N <= 10). Then in line N we are given the words we know, one per line. Each word consists of at least 1 uppercase letter and no more than 10 letters.



#### Print



Print N lines for each test case. Each line prints known words in the order given in the input, YES if the word can be found, and NO if not.



#### example input

```
1
URLPM
XPRET
GATE
XTNZY
XOQRS
6
PRETTY
GIRL
REPEAT
KARA
PANDORA
GIAZAPX
```

#### Example output

```
PRETTY YES
GIRL YES
REPEAT YES
KARA NO
PANDORA NO
GIAZAPX YES
```

----

用`d[len][i][j]`表示字符串前`len`个字符能否在`board`的第`i`行第`j`列结尾，转台转移方程就是当前位置`(i, j)`的八个相邻位置中有效的位置是`true`。初始化过程中`d[0][i][j] = true`，其他为`false`。

时间复杂度$O(n)$，因为本题中board的尺寸和方向都是常数。

```c++
#include <bits/stdc++.h>

using namespace std;


vector<string> grid(5);
vector<vector<int>> direction {
	{1, -1}, {1, 1}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}, {-1, 1}, {-1, -1}
};


void printResult(string & word, bool flag) {
	if (flag) {
		cout << word << " YES" << endl;
	} else {
		cout << word << " NO" << endl;
	}
}

void solve(string & word) {
	vector<vector<vector<bool>>> d(word.size() + 1, vector<vector<bool>>(5, vector<bool>(5, false)));
	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			d[0][i][j] = true;
		}
	}
	int n = word.size();
	for (int len = 1; len <= word.size(); ++len) {
		for (int i = 0; i < 5; ++i) {
			for (int j = 0; j < 5; ++j) {
				for (int k = 0; k < 8; ++k) {
					int preX = i + direction[k][0];
					int preY = j + direction[k][1];
					if (0 <= preX && preX < 5 && 0 <= preY && preY < 5 && d[len - 1][preX][preY] && grid[i][j] == word[len - 1]) {
						d[len][i][j] = true;
						break;
					}
				}
			}
		}
	}

	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			if (d[n][i][j]) {
				printResult(word, true);
				return;
			}
		}
	}
	printResult(word, false);
}



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
    	for (int i = 0; i < grid.size(); ++i) {
    		cin >> grid[i];
    	}

    	int letterNum; cin >> letterNum;
    	while (letterNum--) {
    		string word;
    		cin >> word;
    		solve(word);
    	}
    }



    return 0;
}
```

