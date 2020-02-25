> # POJ-3320 Jessica's Reading Problem（尺取法）

# Description

Jessica's a very lovely girl wooed by lots of boys. Recently she has a problem. The final exam is coming, yet she has spent little time on it. If she wants to pass it, she has to master all ideas included in a very thick text book. The author of that text book, like other authors, is extremely fussy about the ideas, thus some ideas are covered more than once. Jessica think if she managed to read each idea at least once, she can pass the exam. She decides to read only one contiguous part of the book which contains all ideas covered by the entire book. And of course, the sub-book should be as thin as possible.

A very hard-working boy had manually indexed for her each page of Jessica's text-book with what idea each page is about and thus made a big progress for his courtship. Here you come in to save your skin: given the index, help Jessica decide which contiguous part she should read. For convenience, each idea has been coded with an ID, which is a non-negative integer.

# Input

The first line of input is an integer *P* (1 ≤ *P* ≤ 1000000), which is the number of pages of Jessica's text-book. The second line contains *P* non-negative integers describing what idea each page is about. The first integer is what the first page is about, the second integer is what the second page is about, and so on. You may assume all integers that appear can fit well in the signed 32-bit integer type.

# Output

Output one line: the number of pages of the shortest contiguous part of the book which contains all ideals covered in the book.

# Sample Input

```
5
1 8 8 8 1
```

# Sample Output

```
2
```

------

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
#include <climits>
#include <cstdio>

using namespace std;

const int INF = 0x0ffffff;

int n = 1000005;
vector<int> sequence(n);

int main()
{
	// std::ios_base::sync_with_stdio(false);
	// cin.tie(NULL);
	// cout.tie(NULL);
    
    set<int> s; //用来记录有多少个不同的知识点
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
    	scanf("%d", &sequence[i]);
    	s.insert(sequence[i]);
    }
    int total = s.size(); //知识点的总数
    
	map<int, int> m;
	int start = 0, end = 0;
	int cnt = 0; //记录当前包含了多少个知识点
	int len = n; //包含所有知识点的序列长度
	while (true) {
		while (end < n && cnt < total) {
			//出现了一个新的知识点,这里++的位置很关键
			if (m[sequence[end++]]++ == 0) ++cnt;
		}
		
		if (cnt < total) break;
		//这里不是end - start + 1是因为在统计知识点部分已经++end
		len = min(end - start, len);
		if (--m[sequence[start++]] == 0) {
			//某个知识点的个数为0
			--cnt;
		}
	}
	printf("%d\n", len);
    
    return 0;
}
```

首先去延长`end`的位置，找到第一个能包含所有知识点的长度，然后去`start`的位置向后移动一个位置，如果还能包含所有知识点，那么更新最短长度，然后继续前移`start`的位置，如果此时无法包含所有知识点了，那么就移动`end`的位置去寻找下一个包含所有知识点的序列，如此循环。

这里有个需要注意的地方是循环退出的条件不能写成`if (end >= n || cnt < total) break;`，因为可能存在恰好到了末尾并且`cnt == total`的情况，还是可能存在增加`start`的位置来缩短序列长度的情况。

时间复杂度$O(nlogn)$