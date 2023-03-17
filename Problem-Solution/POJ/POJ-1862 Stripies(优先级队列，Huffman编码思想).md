> # POJ-1862 Stripies(优先级队列，Huffman编码思想)

# Description

Our chemical biologists have invented a new very useful form of life called stripies (in fact, they were first called in Russian - polosatiki, but the scientists had to invent an English name to apply for an international patent). The stripies are transparent amorphous amebiform creatures that live in flat colonies in a jelly-like nutrient medium. Most of the time the stripies are moving. When two of them collide a new stripie appears instead of them. Long observations made by our scientists enabled them to establish that the weight of the new stripie isn't equal to the sum of weights of two disappeared stripies that collided; nevertheless, they soon learned that when two stripies of weights m1 and m2 collide the weight of resulting stripie equals to 2*sqrt(m1*m2). Our chemical biologists are very anxious to know to what limits can decrease the total weight of a given colony of stripies.
You are to write a program that will help them to answer this question. You may assume that 3 or more stipies never collide together.

# Input

The first line of the input contains one integer N (1 <= N <= 100) - the number of stripies in a colony. Each of next N lines contains one integer ranging from 1 to 10000 - the weight of the corresponding stripie.

# Output

The output must contain one line with the minimal possible total weight of colony with the accuracy of three decimal digits after the point.

# Sample Input

```
3
72
30
50
```

# Sample Output

```
120.000
```

----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <iomanip>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

priority_queue<double> pq;

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	while (n--) {
		double tmp;
		cin >> tmp;
		pq.push(tmp);
	}

	while (pq.size() > 1) {
		double num1 = pq.top(); pq.pop();
		double num2 = pq.top(); pq.pop();
		pq.push(2 * sqrt(num1 * num2));
	}
	cout << fixed << setprecision(3) << pq.top() << endl;

    return 0;
}
```

利用的是Huffman编码的思想，与中间过程无关，越大的数字应该越先被合并，这样其经过的根号运算就越多，那么减小的数值就越多，所以每次采取两个最大的数来进行合并。所以采用