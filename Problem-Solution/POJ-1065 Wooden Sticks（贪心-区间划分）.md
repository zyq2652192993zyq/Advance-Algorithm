> # POJ-1065 Wooden Sticks（贪心-区间划分）

# Description

There is a pile of n wooden sticks. The length and weight of each stick are known in advance. The sticks are to be processed by a woodworking machine in one by one fashion. It needs some time, called setup time, for the machine to prepare processing a stick. The setup times are associated with cleaning operations and changing tools and shapes in the machine. The setup times of the woodworking machine are given as follows:
(a) The setup time for the first wooden stick is 1 minute.
(b) Right after processing a stick of length l and weight w , the machine will need no setup time for a stick of length l' and weight w' if l <= l' and w <= w'. Otherwise, it will need 1 minute for setup.
You are to find the minimum setup time to process a given pile of n wooden sticks. For example, if you have five sticks whose pairs of length and weight are ( 9 , 4 ) , ( 2 , 5 ) , ( 1 , 2 ) , ( 5 , 3 ) , and ( 4 , 1 ) , then the minimum setup time should be 2 minutes since there is a sequence of pairs ( 4 , 1 ) , ( 5 , 3 ) , ( 9 , 4 ) , ( 1 , 2 ) , ( 2 , 5 ) .

# Input

The input consists of T test cases. The number of test cases (T) is given in the first line of the input file. Each test case consists of two lines: The first line has an integer n , 1 <= n <= 5000 , that represents the number of wooden sticks in the test case, and the second line contains 2n positive integers l1 , w1 , l2 , w2 ,..., ln , wn , each of magnitude at most 10000 , where li and wi are the length and weight of the i th wooden stick, respectively. The 2n integers are delimited by one or more spaces.

# Output

The output should contain the minimum setup time in minutes, one per line.

# Sample Input

```
3 
5 
4 9 5 2 2 1 3 5 1 4 
3 
2 2 1 1 2 2 
3 
1 3 2 2 3 1 
```

# Sample Output

```
2
1
3
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node
{
	int length, weight;

	bool operator<(const Node & obj) const
	{
		return (length < obj.length || 
			(length == obj.length && weight < obj.weight));
	}
};

vector<Node> sequence(5005);
vector<Node> store;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> sequence[i].length >> sequence[i].weight;
		sort(sequence.begin(), sequence.begin() + n);

		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			if (store.empty()) {
				++cnt;
				store.push_back(sequence[i]);
			}
			else {
				bool havePos = false; //判断是否有位置可以放入
				for (int j = 0; j < cnt; ++j) {
					if (sequence[i].length >= store[j].length && 
						sequence[i].weight >= store[j].weight) {
						havePos = true;
						store[j].length = sequence[i].length;
						store[j].weight = sequence[i].weight;
						break;
					}
				}
				if (!havePos) { //没有位置就新增位置
					++cnt;
					store.push_back(sequence[i]);
				}
			}
		}
		cout << cnt << endl;
		store.clear();
	}


    return 0;
}
```

这道题目读完题目很容易就联想到贪心方法总结里面的区间划分问题，恰好是不使用优先级队列的方法，顺便可以复习一下POJ 3190 Stall Reservations的方法，回顾一下路径输出的解决方案。

可能最有疑问的是需要去更新放在数组`store`里的值，其实可以抛开题目背景，把这个题目化成一个简单易懂的模型。如果输入的序对看成是矩形的长和宽，那么题目的意思是，给定一系列矩形，矩形之间可以嵌套，能够嵌套的为一组，问这些矩形可以划分成多少组。这就转化成了可以用区间贪心方法种的区间划分类型的问题。时间复杂度$O(n^2)$。

