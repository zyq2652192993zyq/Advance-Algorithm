> # POJ-1852 Ants（脑筋急转弯）

# Description

An army of ants walk on a horizontal pole of length l cm, each with a constant speed of 1 cm/s. When a walking ant reaches an end of the pole, it immediatelly falls off it. When two ants meet they turn back and start walking in opposite directions. We know the original positions of ants on the pole, unfortunately, we do not know the directions in which the ants are walking. Your task is to compute the earliest and the latest possible times needed for all ants to fall off the pole.

# Input

The first line of input contains one integer giving the number of cases that follow. The data for each case start with two integer numbers: the length of the pole (in cm) and n, the number of ants residing on the pole. These two numbers are followed by n integers giving the position of each ant on the pole as the distance measured from the left end of the pole, in no particular order. All input integers are not bigger than 1000000 and they are separated by whitespace.

# Output

For each case of input, output two numbers separated by a single space. The first number is the earliest possible time when all ants fall off the pole (if the directions of their walks are chosen appropriately) and the second number is the latest possible such time.

# Sample Input

```
2
10 3
2 6 7
214 7
11 12 7 13 176 23 191
```

# Sample Output

```
4 8
38 207
```

----

```c++
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int caseNum;
	cin >> caseNum;
	while (caseNum--) {
		int length, num;
		cin >> length >> num;
		int minTime = 0, maxTime = 0;
		for (int i = 0; i < num; ++i) {
			int tmp;
			cin >> tmp;
			minTime = max(minTime, min(tmp, length - tmp));
			maxTime = max(maxTime, max(tmp, length - tmp));
		}
		cout << minTime << " " << maxTime << endl;
	}
	
	return 0;
}
```

比较难思考的是最长时间，因为会存在蚂蚁碰撞的情况，如果采用直接模拟会陷入复杂的程序设计，实际上，两只蚂蚁相遇各自转头，可以看成是相遇后绕过对方继续走，所以每只蚂蚁的最长时间实际上是其到两端的最大距离。

最短时间注意一下细节，是所有蚂蚁距离两端最短距离中的最大值。