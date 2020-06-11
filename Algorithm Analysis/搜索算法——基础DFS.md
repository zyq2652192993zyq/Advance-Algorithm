> # 搜索算法——基础深度优先搜索

## 八皇后问题

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <set>
#include <algorithm>

using namespace std;

int n;
vector<int> res(8, -1);
int cnt = 0;
vector<vector<int> > grid(8, vector<int>(8));

bool canPlace(int row, int col)
{
	for (int i = 0; i < row; ++i) {
		if (res[i] == col || abs(row - i) == abs(res[i] - col))
			return false;
	}

	return true;
}

void DFS(int row, int n)
{
	for (int col = 0; col < n; ++col) {
		if (canPlace(row, col)) {
			res[row] = col;
			if (row == n - 1) {
				++cnt; //找到一种解决方案
				cout << "No. " << cnt << endl;
				for (int i = 0; i < 8; ++i) grid[i][res[i]] = 1;
				for (int i = 0; i < 8; ++i) {
					for (int j = 0; j < 8; ++j) {
						cout << grid[i][j];
						if (j != n - 1) cout << ' ';
					}
					cout << endl;
				}

				for (int i = 0; i < 8; ++i)
					fill(grid[i].begin(), grid[i].end(), 0);
			}
			else DFS(row + 1, n);
		}
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    DFS(0, 8);
    
    return 0;
}
```

八皇后问题是很经典的搜索问题，按照行的顺序，一行一行的放置，关键点在如何判断某个位置是否可行。对于第`row`行，放置在`col`列，首先需要检验前`row - 1`行是否放置在了`col`列造成冲突。另外的检验就是对角线上不能冲突，所以区分为主对角线和次对角线。主对角线的特点是`列 - 行`的差值都相同，次对角线的特点是`行 + 列`的值相同，前`row - 1`行，假如取第`i`行，那么其对应的列是`res[i]`。

* 不在同一列`res[i] != col`
* 不在同一主对角线：`res[i] - i != col - row`
* 不在同一次对角线：`res[i] + i != row + col`。

对角线上的检查通过移项发现`abs(row - i) = abs(col - res[i])`，也就是行对应相减，列对应相减，差值的绝对值如果相同，那么肯定在对角线上，只是不知道是主对角线还是次对角线，所以检验变得简单了。



## 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

**示例 1:**

```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

**提示：**

* 0 <= num < $2^{31}$

```c++
class Solution {
    int cnt;
    string number;
    int n;
public:
    int translateNum(int num) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        cnt = 0;
        number = to_string(num);
        n = number.size();
        DFS(0);

        return cnt;
    }

    void DFS(int pos) {
        for (int len = 1; len <= 2; ++len) {
            if (pos + len - 1 < n && stoi(number.substr(pos, len)) <= 25) {
                if (len == 2 && number.substr(pos, len)[0] - '0' == 0) continue;

                if (pos + len - 1 == n - 1) {
                    ++cnt;
                }
                else DFS(pos + len);
            }
        }
    }
};
```

属于搜索框架的第一种，注意如果不加上`22`行的代码，会在`506`这个样例错误，也就是`06`不能按照6来计算，所以需要去掉两位数中0开头的数字。



典型题目

- [x] codevs 1116 四色问题
- [ ] HDU 5113 四色问题
- [x] POJ 1129 四色问题
- [x] UVA 10004 Bicoloring (二部图染色)
- [x] 一本通-1213：八皇后问题
- [x] 一本通-1214：八皇后
- [x] 一本通-1212：LETTERS（很好的DFS练习）
- [x] 一本通-1215：迷宫（迷宫类型的DFS的经典练习）
- [x] 一本通-1216：红与黑（flood fill的典型题目）
- [x] 一本通-1250：The Castle 或 POJ 1164（稍加思考的DFS，也可以BFS）
- [x] POJ 1321 棋盘问题（一本通-1217：棋盘问题）
- [x] LeetCode 51 N Queens
- [x] LeetCode 52 N Queens II
- [x] CODE[VS] N皇后问题
- [x] POJ 1321 棋盘问题
- [x] ==数独类型问题==（抽取出来单独总结）
- [x] UVA-524 Prime Ring Problem（素数环，输出细节很多）