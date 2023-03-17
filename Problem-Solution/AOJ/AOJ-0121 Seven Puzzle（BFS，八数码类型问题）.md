> # AOJ-0121 Seven Puzzle（BFS，八数码类型问题）

7拼图由8个正方形的卡和这些卡片完全收纳的框构成。每张卡都编号为0, 1, 2, …, 7,以便相互区别。框架中，可以纵向排列2张，横向排列4张卡。

7当拼图开始时，首先把所有的卡放入框架。在框架中只有0的卡可以与上下左右相邻的卡交换位置。例如，当框架的状态为图A时，与0卡的右边相邻的、7的卡交换位置，就变成图B的状态。或者，从图(a)的状态与0卡下面邻接的2卡交换位置的话，成为图c的状态。在图(a)的状态下0卡与上下左右相邻的卡只有7 2卡，此外的位置不允许更换。

游戏的目的是将卡片排列整齐，使图形(d)的状态。请创建一个程序，输入第一个状态，直到卡片排列整齐为止，输出必要的最小麻烦。但是，输入了的卡的状态可以转移到图d的状态。

输入数据以空白分隔符给出1行中的8个数字。这些表示第一状态的卡片排列。例如，图(a)的数字表示为0 7 3 4 2 5 6，图(c)为2 7 3 4 0 5 1 6。

| ![img](https://vj.z180.cn/d394d06a52c6639d133fef1fa0103c8a?v=1578895972) | ![img](https://vj.z180.cn/7e11002ce6b9a60fc1cd7789120db956?v=1578895972) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 図(a) 0 7 3 4 2 5 1 6 の場合                                 | 図(b) 7 0 3 4 2 5 1 6 の場合                                 |

| ![img](https://vj.z180.cn/e18e2cda619090a8bc1f1167f617a82c?v=1578895972) | ![img](https://vj.z180.cn/9e536ad2ee1e96c22f6bf4bd6da49235?v=1578895972) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 図(c) 2 7 3 4 0 5 1 6 の場合                                 | 図(d) 0 1 2 3 4 5 6 7 (最終状態)                             |

# Input

以上格式提供多个谜题。请处理到输入的最后。给定的谜题的数量在1,000以下。

# Output

请将每个拼图输出到最后一行的最小步数。

# Sample Input

```
0 1 2 3 4 5 6 7
1 0 2 3 4 5 6 7
7 6 5 4 3 2 1 0
```

# Sample Input

```
0
1
28
```

----

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff; 

int direction[4] = {1, -1, 4, -4};
unordered_map<string, int> m;

inline bool canMove(int pos, int nextPos, int i)
{	
	return (0 <= nextPos && nextPos < 8 && !((pos == 3 || pos == 7) && i == 0)
		&& !((pos == 0 || pos == 4) && i == 1));
}

void BFS()
{
	queue<string> q;
	q.push("01234567");
	m["01234567"] = 0;

	while (!q.empty()) {
		string curStr = q.front(); q.pop();
		int pos = curStr.find('0');

		for (int i = 0; i < 4; ++i) {
			int nextPos = pos + direction[i];
			if (canMove(pos, nextPos, i)) {
				string tmpStr = curStr;
				swap(tmpStr[pos], tmpStr[nextPos]);
				if (m.find(tmpStr) == m.end()) { //还没有计算过的情形
					m[tmpStr] = m[curStr] + 1;
					q.push(tmpStr);
				}
			}
		}
	}
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    BFS();
    int num;
    while (cin >> num) {
    	string str;
    	str.push_back('0' + num);
    	for (int i = 0; i < 7; ++i) {
    		cin >> num;
    		str.push_back('0' + num);
    	}
    	cout << m[str] << endl;
    }

    return 0;
}
```

这个问题可以和《算法竞赛入门经典》的八数码问题归为一类，相比于八数码的终止状态的不确定，这里终止状态是统一确定的。华容道其实就是这样一类八数码问题（形状规则的那种）。

最开始BFS的作用是生成所有可能的组合，然后用`unordered_map`来存储状态转移需要的步数，关键点在于寻找合适的位置，也就是当前位置在3，7，不可以右移，位置在0或4，不可以左移，把握好这个判断条件才能写出无误的程序。