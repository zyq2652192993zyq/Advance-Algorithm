> # 动态规划-最长公共子序列(LCS)

LIS和LCS在模型上存在很多相近之处。

# 基本模型

## 动态规划方法

求两个序列X和Y的最长公共子序列（可以不连续）。

设序列$X=\left(x_{1}, x_{2}, \cdots, x_{m}\right)$和$y = \left(y_{1}, y_{2}, \cdots, y_{n}\right)$的最长公共子序列为$Z=\left(z_{1}, z_{2}, \cdots, z_{k}\right)$

* 若$x_m = y_n$， 则$z_k = x_m = y_n$，且$z_{k - 1}$是$x_{m-1} $和$y_{n-1}$的最长公共子序列
* 若$x_{m} \neq y_{n}$,且$z_{k} \neq x_{m}$，则$z$是$x_{m-1}$和$y_n$的最长公共子序列
* 若$x_{m} \neq y_{n}$,且$z_{k} \ne y_{n}$，则$z$是$x$和$y_{n-1}$的最长公共子序列。

设状态为$d[i][j]$，表示序列$X$和$Y$的最长公共子序列的长度，状态转移方程是：
$$
d[i][j]=\left\{\begin{array}{ll}{0} & {i=0, j=0} \\ {d[i-1][j-1]+1} & {i, j>0 ; x_{i}=y_{i}} \\ {\max \{d[i][j-1], d[i-1][j]\}} & {i, j>0 ; x_{i} \neq y_{i}}\end{array}\right.
$$
```c++
//POJ 1458 Common Subsequence 最长公共子序列模板题
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//vector<int> line(200);
//vector<vector<int>> d(200, line); /* d[i][j] 表示序列s1 和s2的最长公共子序列的长度*/

void longestCommonSequence(const string &s1, const string & s2)
{
    vector<vector<int>> d(201, vector<int>(201, 0)); /* 字符串最大长度为200 */
    int m = s1.size(), n = s2.size();

    for (int i = 1; i <= m; ++i){
        for (int j = 1; j <= n; ++j){
            if (s1[i - 1] == s2[j - 1]) d[i][j] = d[i-1][j-1] + 1;
            else d[i][j] = d[i-1][j] > d[i][j-1] ? d[i-1][j] : d[i][j-1];
        }
    }

    cout << d[m][n] << endl;
}

int main()
{
    string s1, s2;
    while (cin >> s1 >> s2){
        longestCommonSequence(s1, s2);
    }

    return 0;
}
```

## LCS的路径输出

如果要打印出最长公共子序列，则需要另外一个数组$p$，其中$p[i][j]$记录状态$d[i][j]$是由哪个子问题得到的。

如果想进一步输出公共子序列的具体形式：

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void printCommonSequence(const string & s1, const int m, const string & s2, const int n, vector<vector<int>> & p)
{
    if (m == 0 || n == 0) return;
    if (p[m][n] == 1) {
        printCommonSequence(s1, m - 1, s2, n - 1, p);
        cout << s1[m-1];
    } 
    else if (p[m][n] == 2) {
        printCommonSequence(s1, m - 1, s2, n, p);
    } 
    else {
        printCommonSequence(s1, m, s2, n - 1, p);
    }
}

void longestCommonSequence(const string &s1, const string & s2)
{
    vector<vector<int>> d(201, vector<int>(201, 0)); /* 字符串最大长度为200 */
    vector<vector<int>> p(201, vector<int>(201, 0));
    int m = s1.size(), n = s2.size();

    for (int i = 1; i <= m; ++i){
        for (int j = 1; j <= n; ++j){
            if (s1[i - 1] == s2[j - 1]){
                d[i][j] = d[i-1][j-1] + 1;
                p[i][j] = 1;
            } 
            else{
                if (d[i-1][j] >= d[i][j-1]){
                    d[i][j] = d[i-1][j];
                    p[i][j] = 2;
                }
                else{
                    d[i][j] = d[i][j-1];
                    p[i][j] = 3;
                }
            } 
        }
    }
    cout << d[m][n] << " ";
    printCommonSequence(s1, m, s2, n, p);
    cout << endl;
}

int main()
{
    string s1, s2;
    while (cin >> s1 >> s2){
        longestCommonSequence(s1, s2);
    }

    return 0;
}
```

上面的方法时间复杂度$O(m \times n)$，空间复杂度$O(m \times n)$，适合需要准确输出公共子序列的问题。如果只是求长度的结果，空间上还可以进行优化。

## 动态规划方法的`O(n)`空间优化

发现`d[i][j]`只是和`d[i - 1][j - 1], d[i][j - 1], d[i - 1][j]`有关，所以可以将空间优化到$O(n)$。

很明显`i, i - 1`必定是一个奇数，一个偶数，那么很典型的奇偶优化。

- [x] 一本通-1265：【例9.9】最长公共子序列

```c++
#include <bits/stdc++.h>

using namespace std;

string s1, s2;
int m, n;
vector<vector<int> > d(2, vector<int>(1005));

int LCS()
{
	for (int i = 1; i <= m; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (s1[i - 1] == s2[j - 1]) {
				d[i & 1][j] = d[(i - 1) & 1][j - 1] + 1; 
			}
			else {
				d[i & 1][j] = max(d[i & 1][j - 1], d[(i - 1) & 1][j]);
			}
		}
	}

	return d[m & 1][n];
}


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> s1 >> s2;
	m = s1.size(); n = s2.size();
	cout << LCS() << endl;

	return 0;
}
```

## `nlogn`优化的方法

上面动态规划的思路很好理解，但是在解决洛谷 P1439 [模板]最长公共子序列的时候会超时，因为动态规划算法的时间复杂度是$O(n^2)$，而洛谷的数据是$10^5$，所以肯定超时。这时可以利用LIS的思路来求解。

就以洛谷的题目为例，两个序列的元素都是从1到n的n个数，打乱顺序排列，比如例子：

```
3 2 1 4 5
1 2 3 4 5
```

现在我们用一种办法映射，将3映射成`a`，2映射成`b`，以此类推，则第一个序列变成了：

```
a b c d e
```

然后看第二个序列按照这个规则的映射：

```
c b a d e
```

两个的公共子序列，无论这个子序列怎么从第一个序列里面选，它都是升序的，所以只需要从第二个序列找LIS即可，于是就可以用二分优化了。

需要思考的地方：

* 如果存在重复元素如何解决？
* $n\log n$情况下如何输出路径？
* 如果要求输出所有公共子串该怎么办？

比如两个字符串：

```
abdba
dbaaba
```

先扫描第一个字符串，取其在第二个字符串中的尾置：

```
a: 2 3 5 
b: 1 4
d: 0
```

用每个字母的反序列替换，求最长（严格）上升子序列即可。

替换后为

```
5 3 2 4 1 0 4 1 5 3 2
```

首先如果求出一个最长上升子序列，那么这个子序列必然是第二个字符串的子串，因为是按照下标顺序的，求出来的一定严格对应第二个字符串中字符出现的先后顺序。

```c++
//一本通-1265：【例9.9】最长公共子序列
#include <bits/stdc++.h>

using namespace std;

string s1, s2;
int m, n;
map<char, vector<int> > um;
vector<int> seq;

int LCS()
{
	int length = seq.size(); if (length == 0) return 0;
	vector<int> d(length + 5);
	d[1] = seq[0];
	int len = 1;
	for (int i = 1; i < length; ++i) {
		int target = seq[i];

		int left = 1, right = len + 1;
		while (left < right) {
			int mid = left + ((right - left) >> 1);
			if (d[mid] < target) left = mid + 1;
			else right = mid;
		}
		if (left == len + 1) d[++len] = target;
		else d[left] = target;
	}

	return len;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> s1 >> s2;
	m = s1.size(); n = s2.size();

	for (int i = 0; i < n; ++i) {
		um[s2[i]].push_back(i);
	}

	for (int i = 0; i < m; ++i) {
		if (um.find(s1[i]) != um.end()) {
			vector<int> & v = um[s1[i]];
			int len = v.size();
			for (int j = len - 1; j >= 0; --j) {
				seq.push_back(v[j]);
			}
		}
	}

	cout << LCS() << endl;

	return 0;
}
```

**注意可能存在第一个字符串的所有字符在第二个字符串都没有出现的情况，那么就需要特判**

但是这种办法并非严格的时间复杂度是$O(n \log n)$，比如两个字符串：

```
aaa m
aaaa n
```

长度分别为`m`和`n`，动态规划的方法是$O(m \times n)$，如果替换序列：

```
3 2 1 0 3 2 1 0 3 2 1 0
```

序列长度为`m * n`，时间复杂度是$O(m \times n \log(m \times n))$，时间复杂度反而不如用动态规划的办法。

如果是输出路径，方法和LIS输出路径的方法差不多。

## 带限制的LCS

- [ ] BZOJ 3304: [SHOI2005]带限制的最长公共子序列( LCS )



## 最长公共上升子序列

- [ ] 一本通-1306：最长公共子上升序列





## 合并字符串

- [x] HDU 1503 Advanced Fruits

对于两个字符串`s1`和`s2`，找出包含`s1`和`s2`所有字符并且各自保持顺序的最短序列。





额外思考：第K长的LCS，统计区间LCS长度为k的个数，生成LCS序列。







典型题目：

- [x] 洛谷 P1439 [模板]最长公共子序列（用二维数组会MLE，需要用nlogn的方法）


- [x] POJ 1458 Common Subsequence（LCS模板题，动态规划方法即可AC）
- [x] HDU 1503 Advanced Fruits
- [x] HDU 1080 Human Gene Functions
- [x] LeetCode 1143 Longest Common Subsequence
- [x] LeetCode 1035.Uncrossed Lines
- [ ] BZOJ 3304: [SHOI2005]带限制的最长公共子序列( LCS )

另外考虑如果是字符串类型的问题，要求子串连续，那么最长匹配怎么求解？比如`abbcd`和`abbe`，那么`abb`就是最长的公共子串。