> # 典型问题——生成第K个数

经常会遇到一类问题，或者问题的某一步骤需要产生数据，比如某个集合最开始有数字1，这个数字乘上`a, b, c`，下一个数字是所有乘积结果里面最小的一个。

这种问题通常存在两种解决办法：

* 利用小根堆
* 三指针法（效率更高，更节省空间）

上面的两种方法最少需要消耗$O(n)$的空间，如果`n`达到$10^9$，就需要利用二分和容器原理来生成了。

## 生成第`n`个丑数

- [x] LeetCode 264.Ugly Number II

找第`n`个丑数，肯定不能暴力找了。第一种办法就是利用小根堆来做。下一个丑数一定是从前面的丑数乘上2，3，5其中的一个得到的，每次让小根堆的堆顶为第`k`个丑数，将这个数字乘上2，3，5的结果推入堆中，为了避免重复的数字，取出堆顶的元素，删掉堆种与它相等的元素。时间复杂度$o(n \log n)$。

```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        priority_queue<long long, vector<long long>, greater<long long>> pq;
        pq.push(1);

        for (int i = 1; i < n; ++i) {
            long long tmp = pq.top(); pq.pop();
            while (!pq.empty() && pq.top() == tmp) pq.pop();
            pq.push(tmp * 2), pq.push(tmp * 3), pq.push(tmp * 5);
        }

        return pq.top();
    }
};
```

第二种解法，用一个数组存储丑数，第`n`个丑数存储再下标为`n-1`的位置，分别用`p2, p3, p5`表示通过乘以2，3，5得到的丑数的上一个位置，开始三个指向0，数组里存储1，对`p2, p3, p5`指向的数字分别乘以2，3，5，看那个数字最小，最小的就让其下标增加一位。

```c++
class Solution {
public:
    int nthUglyNumber(int n) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        vector<long long> seq(1, 1);
        int p2 = 0, p3 = 0, p5 = 0;
        while (seq.size() < n) {
            long long tmp2 = seq[p2] * 2, tmp3 = seq[p3] * 3, tmp5 = seq[p5] * 5;
            long long res =  min(tmp2, min(tmp3, tmp5));
            seq.push_back(res);
            
            if (res == tmp2) ++p2;
            if (res == tmp3) ++p3;
            if (res == tmp5) ++p5;
        }
        
        return seq.back();
    }
};
```

注意只要14到17行的写法，只要是下一个丑数和产生的临时值相等，就需要移动指针。时间复杂度$O(n)$。

## 利用前`K`个数组成字符串

- [x]  洛谷-P1323 删数问题（基础贪心）

集合初始为1，如果一个数`a`存在于集合，那么`2 * a + 1`和`4 * a + 5`也存在于集合，生成的办法也同样可以利用上面的办法。

```c++
string generate()
{
	priority_queue<int, vector<int>, greater<int> > pq;
	pq.push(1);
	string res;

	for (int i = 0; i < m; ++i) {
		int tmp = pq.top(); pq.top();
		res += to_string(tmp);
		
		while (!pq.empty() && pq.top() == tmp) pq.pop();
		pq.push(tmp * 2 + 1);
		pq.push(tmp * 4 + 5);
	}

	return res;
}
```

第二种办法：

```c++
string generate()
{
	string res = "1";
	vector<int> seq(1, 1);

	int index1 = 0, index2 = 0;
	for (int i = 1; i < m; ++i) {
		int tmp1 = seq[index1] * 2 + 1;
		int tmp2 = seq[index2] * 4 + 5;
		int nextNum = min(tmp1, tmp2);
		seq.push_back(nextNum);
		res += to_string(seq.back());

		if (nextNum == tmp1) ++index1;
		if (nextNum == tmp2) ++index2;
	}

	return res;
}

```

## 容斥原理和二分法生成第`n`个丑数

- [x] LeetCode 1201.Ugly Number

这道题相对于前面的问题，在于需要生成的第`n`个丑数的数据范围到了$10^9$，所以前面的堆和三指针肯定会超过内存限制，这么大的数据范围其实就在暗示可以利用二分。

```c++
class Solution {
public:
    int nthUglyNumber(int n, long long a, long long b, long long c) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        long long x = a * b / GCD(a, b);
        long long y = a * c / GCD(a, c);
        long long z = b * c / GCD(b, c);
        long long t = x * c / GCD(x, c);

        long long left = 0, right = INT_MAX;
        while (left < right) {
            long long mid = left + ((right - left) >> 1);
            long long cnt = mid / a + mid / b + mid / c - mid / x - mid / y - mid / z + mid / t;
            if (cnt < n) left = mid + 1;
            else right = mid;
        }

        return left;
    }

    long long GCD(long long a, long long b)
    {
        return b == 0 ? a : GCD(b, a % b);
    }
};
```

