> # POJ-3104 Drying（二分法，思维）

# Description

It is very hard to wash and especially to dry clothes in winter. But Jane is a very smart girl. She is not afraid of this boring process. Jane has decided to use a radiator to make drying faster. But the radiator is small, so it can hold only one thing at a time.

Jane wants to perform drying in the minimal possible time. She asked you to write a program that will calculate the minimal time for a given set of clothes.

There are *n* clothes Jane has just washed. Each of them took *ai* water during washing. Every minute the amount of water contained in each thing decreases by one (of course, only if the thing is not completely dry yet). When amount of water contained becomes zero the cloth becomes dry and is ready to be packed.

Every minute Jane can select one thing to dry on the radiator. The radiator is very hot, so the amount of water in this thing decreases by *k* this minute (but not less than zero — if the thing contains less than *k* water, the resulting amount of water will be zero).

The task is to minimize the total time of drying by means of using the radiator effectively. The drying process ends when all the clothes are dry.

# Input

The first line contains a single integer *n* (1 ≤ *n* ≤ 100 000). The second line contains *ai* separated by spaces (1 ≤ *ai* ≤ 109). The third line contains *k* (1 ≤ *k* ≤ 109).

# Output

Output a single integer — the minimal possible number of minutes required to dry all clothes.

# Sample Input

```
sample input #1
3
2 3 9
5

sample input #2
3
2 3 6
5
```

# Sample Output

```
sample output #1
3

sample output #2
2
```

-----

```c++
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

int n = 100005, k;
vector<int> sequence(n);

bool check(int d)
{
	int sum = d;
	for (int i = 0; i < n; ++i) {
		if (sequence[i] > d)
			sum -= ceil((double)(sequence[i] - d)/ (k - 1));
		//如果需要的数量超过了d，说明数字偏小
		if (sum < 0) return true;
	}

	return false;
}

int main()
{
	// std::ios_base::sync_with_stdio(false);
	// cin.tie(NULL);
	// cout.tie(NULL);
    
   	while (cin >> n) {
   		int maxNum = 0;
   		for (int i = 0; i < n; ++i) {
   			scanf("%d",&sequence[i]);
   			//cin >> sequence[i];
   			maxNum = max(maxNum, sequence[i]);
   		}
   		cin >> k;

   		int left = 0, right = maxNum;
   		while (left < right) {
   			int mid = left + ((right - left) >> 1);
   			if (check(mid)) left = mid + 1;
   			else right = mid;
   		}
   		cout << left << endl;
   	}
	
    return 0;
}
```

很好的题目，但是很坑，首先是关了同步也会TLE，另外在virtual judge下很多人的解答都用了`long long` 的数据类型，根据题目的要求，其实发现用`int`是足够的。

思路难点在于处理烘干时间的计算，考虑第一个例子2，3，9，首先去烘干9一分钟，变为1，2，4，再去烘干4，用去一分钟，变为0，1，0，再花去一分钟，所以结果是3.

第二个例子，2，3，6，首先去烘干6一分钟，变成1，1，2，然后去烘干2，变为0，0，0，所以需要2分钟。

可以看到，每次都是去找最大的数值去烘干，很容易就想到使用优先级队列，但是难点在于，烘干需要花费一分钟，在队列里面的元素都要减去1，这个就不太好处理，总不能把元素取出来计算完再放回去，那样数据大了肯定超时。

通过上面的分析，发现无论是烘干还是自然晒干，每经过一分钟，水分都会减少1，也就是说烘干减少`k`，相当于除去自然减少的部分，它能减少`k-1`的水分，于是转为考虑用二分来解决。

假设需要用`d`分钟，所有的衣服分为两类，一类是需要烘干的，一类是不需要烘干即自然晒干（`sequence[i] <= d`），所以着重考虑需要烘干的部分。因为每次只能烘干一件衣服，因为必然是要经过`d`分钟的，所以每件衣服还含有`sequence[i] - d`的水分，所以余下的部分需要用烘干的方法。问题转化成用`k - 1`去对余下需要烘干的衣服操作，每次操作使用`ceil`函数向上取整，则总时间减少，用`tmp`记录，如果用完了还是无法全部烘干，说明猜测的时间小了，需要增大。