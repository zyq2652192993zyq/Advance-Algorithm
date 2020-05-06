> # HDU-3089 Josephus again（约瑟夫问题-优化）

# Description

In our Jesephus game, we start with n people numbered 1 to n around a circle, and we eliminated every k remaining person until only one survives. For example, here's the starting configuration for n = 10, k = 2, The elimination order is 2, 4, 6, 8, 10, 3, 7, 1, 9. So 5 survives.The problem: determine the survivor's number , J(n, k).

# Input

There are multiple cases, end with EOF
each case have two integer, n, k. (1<= n <= 10^12, 1 <= k <= 1000)

# Output

each case a line J(n, k)

# Sample Input

```
10 2
10 3
```

# Sample Output

```
5
4
```

----

```c++
//HDU 3089
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

long long Josephus(long long n, long long k)
{
	if (n == 1) return 0;
	if (k == 1) return n - 1;
	//k>n时退化成线性算法
	if (k > n) return (Josephus(n - 1, k) + k) % n;
	//判断补偿量
	long long res = Josephus(n - n / k, k);
	res -= n % k;
	if (res < 0) res += n;
	else res += res / (k - 1);

	return res;
}


int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n, k;
    while (cin >> n >> k) {
    	cout << (Josephus(n, k) + 1) << endl;
    }
   
    return 0;
}
```

但是如果$n$非常大，比如数据规模达到$n \leq 10^{12}$，比如HDU 3089，上面的算法就会超时，这种特殊情况下，一般会让$k$的数值比较小，算法复杂度达到$O(k \log n)$。

当$k$远小于$n$的时候，尽可能在第一圈就去除掉尽可能多的数，第一个去掉的是$k - 1$，第二个去掉的是$2k - 1$，依次类推，则第一圈最多去掉$[n/k]$个，余下$n - [n / k]$个数，写成序列就是：
$$
0,1,2,\cdots .k-2, k, \cdots, 2k-2, 2k, \cdots 3k - 2 \cdots k[n/k] - 2, k[n/k], \cdots ,n - 2, n-1
$$

去掉$[n/k]$个数后，接下来就要从$k[n/k]$开始，那么从$k[n/k]$到$n-1$的个数肯定是小于$k$的，那么调整顺序后是：
$$
k[n/k], k[n/k] + 1,\cdots, n-1, 0,1,\cdots k-2, k, \cdots k[n / k] - 2
$$
按照前面的分析，此时应该建立一个映射，对于从$k[n/k]$到$n-1$，仍然符合上面的递推关系：
$$
J_{n, k} = (J_{n - n/k, k} + k \times [n/k]) \% n
$$
这里的偏移量很好理解，前面每踢一个数，后面偏移时都要多一个$k$,因为踢了$[n/k]$个数，所以要偏移$[n/k]k$。

那么通过上面分析可知，每经过$k$个数就需要在偏移量补偿1，按照这个思路写一下标号的映射关系：
$$
k[n/k], k[n/k] + 1,\cdots, n-1, 0,1,\cdots k-2, k, \cdots k[n / k] - 2 \\
n - n \% k, n - n \% k + 1, \cdots, n - n \% k + (n - k[n/k]) - 1 \\
0,1,2,\cdots, n - k[n/k]-1
$$
其中第一行和第二行是相等的，第三行是子问题$J_{n - n/k, k}$的标号。

发现如果$J_{n - n/k, k} <  n-k\times [n/k]$，则$J_{n, k} = (J_{n - n / k, k} + k\times[n/k]) \% n$；

若$J_{n - n/k, k} \geq  n-k\times [n/k]$，则$J_{n, k} = (J_{n - n / k, k} + k\times[n/k] + p) \% n$，其中$p = (J_{n - n / k, k} -  n \% k) / (k - 1)$，$p$表示补偿量，注意一个很重要的隐藏关系：
$$
n - n \% k = k[n / k]
$$
上面的代码和公式有一些变化，其实是一致的，只是改进了计算顺序。首先需要去比较$J_{n - n / k, k}$和$n - k[n/k]$的关系，判断对应的原序列编号是否在$k[n / k]\cdots n-1$内。如果在，则对应关系就是：
$$
J_{n, k} = (J_{n - n / k, k} + k\times[n/k]) \% n \\
所以先减去n \% k，小于0则加上n即可。
$$
如果不在这个范围内，注意此时原序列编号0对应$n \% k$，因为$J_{n - n / k, k}$已经减去了$n % k$，对应的序列是：
$$
原编号：0,1,2,\cdots k - 2, k\cdots \\
子问题编号：n \%k, n\% k + 1 ,\cdots, 
$$
所以也就是每经过$k-1$的长度就需要补偿1，所以对应`else`部分的代码。

时间复杂度的证明：

假设递归的次数是$x$，那么每一次问题的规模会变成$n - [n / k]$，如果这里做一下近似处理，则可以认为规模变成了$n(1 - \frac{1}{n})$，于是得到：
$$
n(1 - \frac{1}{n})^ x = 1 \\
x = -\frac{\ln n}{\ln(1 - \frac{1}{k})}
$$
考虑计算$\lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right)$，有：
$$
\begin{aligned}
\lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right) &=\lim _{k \rightarrow \infty} \frac{\log \left(1-\frac{1}{k}\right)}{1 / k} \\
&=\lim _{k \rightarrow \infty} \frac{\frac{\frac{\mathrm{d}}{\mathrm{d} k} \log \left(1-\frac{1}{k}\right)}{\frac{\mathrm{d}}{\mathrm{d} k}\left(\frac{1}{k}\right)}}{ } \\
&=\lim _{k \rightarrow \infty} \frac{\frac{1}{k^{2}\left(1-\frac{1}{k}\right)}}{-\lim _{k \rightarrow \infty}-\frac{k}{k-1}} \\
&=-\lim _{k \rightarrow \infty} \frac{1}{1-\frac{1}{k}} \\
&=-1
\end{aligned}
$$
于是：
$$
x = -\frac{\ln n}{\ln(1 - \frac{1}{k})} =  -\frac{k\ln n}{k\ln(1 - \frac{1}{k})} = k\log n
$$
所以时间复杂度是$O(k \log n)$。