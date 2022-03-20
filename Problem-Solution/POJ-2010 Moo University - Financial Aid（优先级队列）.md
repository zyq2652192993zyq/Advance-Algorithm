> # POJ-2010 Moo University - Financial Aid（优先级队列）

# Description

Bessie noted that although humans have many universities they can attend, cows have none. To remedy this problem, she and her fellow cows formed a new university called The University of Wisconsin-Farmside,"Moo U" for short.

Not wishing to admit dumber-than-average cows, the founders created an incredibly precise admission exam called the Cow Scholastic Aptitude Test (CSAT) that yields scores in the range 1..2,000,000,000.

Moo U is very expensive to attend; not all calves can afford it.In fact, most calves need some sort of financial aid (0 <= aid <=100,000). The government does not provide scholarships to calves,so all the money must come from the university's limited fund (whose total money is F, 0 <= F <= 2,000,000,000).

Worse still, Moo U only has classrooms for an odd number N (1 <= N <= 19,999) of the C (N <= C <= 100,000) calves who have applied.Bessie wants to admit exactly N calves in order to maximize educational opportunity. She still wants the median CSAT score of the admitted calves to be as high as possible.

Recall that the median of a set of integers whose size is odd is the middle value when they are sorted. For example, the median of the set {3, 8, 9, 7, 5} is 7, as there are exactly two values above 7 and exactly two values below it.

Given the score and required financial aid for each calf that applies, the total number of calves to accept, and the total amount of money Bessie has for financial aid, determine the maximum median score Bessie can obtain by carefully admitting an optimal set of calves.

# Input

* Line 1: Three space-separated integers N, C, and F
* Lines 2..C+1: Two space-separated integers per line. The first is the calf's CSAT score; the second integer is the required amount of financial aid the calf needs

# Output

Line 1: A single integer, the maximum median score that Bessie can achieve. If there is insufficient money to admit N calves,output -1.

# Sample Input

```
3 5 70
30 25
50 21
20 20
5 18
35 30
```

# Sample Output

```
35
```

# Hint

**Sample output:**If Bessie accepts the calves with CSAT scores of 5, 35, and 50, the median is 35. The total financial aid required is 18 + 30 + 21 = 69 <= 70.

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

struct Node
{
	int score, aid;
	bool operator<(const Node & obj) const
	{
		return score < obj.score;
	}
};

int n = 20000, c = 100005, f = 2000000000;
vector<Node> sequence(c);

int solve()
{
	priority_queue<int> pq; //大根堆，始终保持size为half
	int half = n >> 1;
	int sum = 0; //记录大于中位数的half个学生种aid总和最小值
	for (int i = c - 1; i >= c - half; --i){
		pq.push(sequence[i].aid);
		sum += sequence[i].aid;
	} 

	int pos = c - half - 1; //中位数在数组中对应的下标
	vector<int> lower(pos + 1); //lower[i]表示在位置i之前的最小的half个和
	priority_queue<int> pre;
	int leftSum = 0;
	for (int i = 0; i <= pos; ++i) {
		if (i < half) {
			lower[i] = INF;
			leftSum += sequence[i].aid;
			pre.push(sequence[i].aid);
		} 
		else {
			lower[i] = leftSum;
			if (sequence[i].aid <= pre.top()) {
				leftSum -= pre.top(); pre.pop();
				leftSum += sequence[i].aid;
				pre.push(sequence[i].aid);
			}
		}
	}

	while (pos >= half) { //余下至少有half个可选
		//需要从数组0到pos - 1的学生中找出half个学生，需要aid总和不超过rest
		int rest = f - sum - sequence[pos].aid;
		
		if (lower[pos] <= rest) return sequence[pos].score;
		else {
			if (sequence[pos].aid <= pq.top()) {
				sum -= pq.top(); pq.pop();
				sum += sequence[pos].aid;
				pq.push(sequence[pos].aid);
			}
			--pos;
		}
	}

	return -1;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> c >> f;
	for (int i = 0; i < c; ++i) cin >> sequence[i].score >> sequence[i].aid;

	sort(sequence.begin(), sequence.begin() + c);
	cout << solve() << endl;
	
    return 0;
}
```

这道题的还是很不错的一个题目，需要用到两个优先级队列。题目需要在满足总金额不超过F的情况下有最大的中位数，一共选`n`个数，那么比中位数大的和小的数都是`half = n / 2`个，而这`half`究竟选哪些并不重要，因为并不影响中位数，所以肯定选择金额小的。

先对输入的数据依据其分数进行排序，然后从大到小进行搜索。用`pos`标注中位数所在位置的下标，那么分数大于中位数的点下标是在`pos + 1`到`c - 1`，余下的是小于中位数的部分。大于中位数的部分，选出最小的`half`个记录总和，每次`pos`减小进行搜索的时候，比中位数大的数增加了一个，那么需要判断这个增加的数是不是在最小的`half`个数内，于是我们用大根堆来始终维持堆内有`half`个数，并用`sum`来记录堆内数据的和。

难点在于如何处理小于中位数的部分，如果像大于中位数的部分一样，在搜索的时候进行计算显然会遇到困难，因为中位数的位置左移的时候，相当于从小于中位数的部分里面抽走了一个数，那么这个数是在前`half`个数内还是不在并不确定，而且较难去调整小于中位数的前`half`个数的和`leftSum`，所以巧妙地用一个数组`lower[i]`来记录下标**小于**`i`地数据里面前`half`个数地和。

搜索到地第一个满足总金额小于F的`pos`对应的`score`就是最大的中位数，如果都不满足，那么就返回-1.