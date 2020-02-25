> # POJ-3111 K Best（01分数规划==最大化平均值）

# Description

Demy has *n* jewels. Each of her jewels has some value *vi* and weight *wi*.

Since her husband John got broke after recent financial crises, Demy has decided to sell some jewels. She has decided that she would keep *k* best jewels for herself. She decided to keep such jewels that their specific value is as large as possible. That is, denote the specific value of some set of jewels *S* = {*i*1, *i*2, …, *ik*} as

![img](https://vj.z180.cn/0389497dbaae925e36b0db87a8ec2f48?v=1581301952).

Demy would like to select such *k* jewels that their specific value is maximal possible. Help her to do so.

# Input

The first line of the input file contains *n* — the number of jewels Demy got, and *k* — the number of jewels she would like to keep (1 ≤ *k* ≤ *n* ≤ 100 000).

The following *n* lines contain two integer numbers each — *vi* and *wi* (0 ≤ *vi* ≤ 106, 1 ≤ *wi* ≤ 106, both the sum of all *vi* and the sum of all *wi* do not exceed 107).

# Output

Output *k* numbers — the numbers of jewels Demy must keep. If there are several solutions, output any one.

# Sample Input

```
3 2
1 1
1 2
1 3
```

# Sample Output

```
1 2
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

struct Node
{
	double num;
	int from;
	int value, weight;
	bool operator<(const Node & obj) const
	{
		return num > obj.num;
	}
};

int n = 100005, k;
vector<Node> sequence(n);

bool check(double x)
{
	for (int i = 0; i < n; ++i) {
		sequence[i].num = sequence[i].value - x * sequence[i].weight;
	}
	sort(sequence.begin(), sequence.begin() + n);

	double sum = 0;
	for (int i = 0; i < k; ++i) sum += sequence[i].num;

	return sum >= 0;
}

ostream & operator<<(ostream & os, vector<Node> & v)
{
	for (int i = 0; i < k; ++i)
		os << v[i].from << " ";
	os << endl;

	return os;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
    while (cin >> n >> k) {
    	//scanf("%d %d", &n, &k) != EOF
    	for (int i = 0; i < n; ++i) {
    		cin >> sequence[i].value >> sequence[i].weight;
    		sequence[i].from = i + 1;
    	}	
    		//scanf("%d%d", &value[i], &weight[i]);

    	double left = 0, right = INF;
    	for (int i = 0; i < 100; ++i) {
    		double mid = (left + right) / 2;
    		if (check(mid)) left = mid;
    		else right = mid;
    	}
    	//output();
    	cout << sequence;
    }
   	
    return 0;
}
```

思路其实很好想，就是《挑战程序设计竞赛》里最大化平均值的例题，无非就是输出路径。

但是这道题目很神奇的一点是，在算法原理不改变的情况下，如果把`weight`，`value`分开存储在数组里面就会TLE。

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

struct Node
{
	double num;
	int from;
	bool operator<(const Node & obj) const
	{
		return num > obj.num;
	}
};

int n = 100005, k;
vector<int> value(n), weight(n);
vector<Node> result(n);

bool check(double x)
{
	for (int i = 0; i < n; ++i) {
		result[i].num = value[i] - x * weight[i];
		result[i].from = i + 1;
	}
	sort(result.begin(), result.begin() + n);

	double sum = 0;
	for (int i = 0; i < k; ++i) sum += result[i].num;

	return sum >= 0;
}

ostream & operator<<(ostream & os, vector<Node> & v)
{
	for (int i = 0; i < k; ++i)
		os << v[i].from << " ";
	os << endl;

	return os;
}

// void output()
// {
// 	for (int i = 0; i < k; ++i) {
// 		printf("%d ", result[n - i - 1].from);
// 	}
// 	printf("\n");
// }

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
    while (cin >> n >> k) {
    	//scanf("%d %d", &n, &k) != EOF
    	for (int i = 0; i < n; ++i) cin >> value[i] >> weight[i];
    		//scanf("%d%d", &value[i], &weight[i]);

    	double left = 0, right = INF;
    	for (int i = 0; i < 100; ++i) {
    		double mid = (left + right) / 2;
    		if (check(mid)) left = mid;
    		else right = mid;
    	}
    	//output();
    	cout << result;
    }
   	
    return 0;
}
```

最初以为是输入输出的问题，但是也无法改变TLE，直到上面写成一个结构体。

**猜测**：可能是因为分开写，每个测试用例的时候需要分开申请三倍的空间，也就是说，虽然最后的存储空间大小是一样的，但是分开申请肯定要比一次性申请慢。