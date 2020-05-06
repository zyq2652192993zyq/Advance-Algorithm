> # POJ 2259 Team Queue或牛客OJ Team Queue（基础队列模拟+哈希）

# Description

Queues and Priority Queues are data structures which are known to most computer scientists. The Team Queue, however, is not so well known, though it occurs often in everyday life. At lunch time the queue in front of the Mensa is a team queue, for example.

In a team queue each element belongs to a team. If an element enters the queue, it first searches the queue from head to tail to check if some of its teammates (elements of the same team) are already in the queue. If yes, it enters the queue right behind them. If not, it enters the queue at the tail and becomes the new last element (bad luck). Dequeuing is done like in normal queues: elements are processed from head to tail in the order they appear in the team queue.

Your task is to write a program that simulates such a team queue.

# Input

The input will contain one or more test cases. Each test case begins with the number of teams t (1<=t<=1000). Then t team descriptions follow, each one consisting of the number of elements belonging to the team and the elements themselves. Elements are integers in the range 0 - 999999. A team may consist of up to 1000 elements.
Finally, a list of commands follows. There are three different kinds of commands:

- ENQUEUE x - enter element x into the team queue
- DEQUEUE - process the first element and remove it from the queue
- STOP - end of test case

The input will be terminated by a value of 0 for t.
Warning: A test case may contain up to 200000 (two hundred thousand) commands, so the implementation of the team queue should be efficient: both enqueing and dequeuing of an element should only take constant time.

# Output

For each test case, first print a line saying "Scenario #k", where k is the number of the test case. Then, for each DEQUEUE command, print the element which is dequeued on a single line. Print a blank line after each test case, even after the last one.

# Sample Input

```
2
3 101 102 103
3 201 202 203
ENQUEUE 101
ENQUEUE 201
ENQUEUE 102
ENQUEUE 202
ENQUEUE 103
ENQUEUE 203
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
STOP
2
5 259001 259002 259003 259004 259005
6 260001 260002 260003 260004 260005 260006
ENQUEUE 259001
ENQUEUE 260001
ENQUEUE 259002
ENQUEUE 259003
ENQUEUE 259004
ENQUEUE 259005
DEQUEUE
DEQUEUE
ENQUEUE 260002
ENQUEUE 260003
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
STOP
0
```

# Sample Output

```
Scenario #1
101
102
103
201
202
203

Scenario #2
259001
259002
259003
259004
259005
260001

```

----

模拟排队，有很多个`team`，每个`team`里人数不一定相同，有一个大的队列，每次遇到操作`ENQUEUE`就将后面的数值加入到队列，如果队列里有同组的人，就站在同组人的后面，没有就排在大队列的末尾。

因为涉及到和组号的对应，于是用一个哈希表建立数值和对应组号的映射，然后用一个`vector`存储各个队列。当一个元素加入的时候，首先去判断`vector`里对应的队列是否为空，如果为空，那么对应的组号加入到大的队列。删除的时候，取出队首的组号，如果对应的队列出队后为空，大队列删掉头部元素。所有操作为$O(1)$。时间复杂度$O(n)$，其中`n`是操作数。

这个题额外注意`queue`不支持`clear()`，`deque`支持`clear()`操作。

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

vector<queue<int> > seq(1005);
queue<int> total;
map<int, int> HashTable;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int teamNum, cnt = 0;
	string ops;
	while ((cin >> teamNum) && teamNum) {
		for (int i = 0; i < teamNum; ++i) {
			int memberNum; cin >> memberNum;
			for (int j = 0; j < memberNum; ++j) {
				int value; cin >> value;
				HashTable[value] = i; //数值和组号对应
			}
		}
		++cnt;
		cout << "Scenario #" << cnt << endl;
		while ((cin >> ops) && ops[0] != 'S') {
			int num;
			if (ops[0] == 'E') {
				cin >> num;
				int number = HashTable[num];
				if (seq[number].empty()) total.push(number);
				seq[number].push(num);
			}
			else {
				int number = total.front();
				if (seq[number].size() == 1) total.pop();
				cout << seq[number].front() << endl;
				seq[number].pop();
			}
		}
		cout << endl;
		//队列不支持clear()操作
		for (int i = 0; i < teamNum; ++i) seq[i] = queue<int>();
		HashTable.clear();
		total = queue<int>();
	}

	return 0;
}
```

