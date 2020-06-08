> # UVA-725 Division（递归组合型枚举）

# Description

Write a program that finds and displays all pairs of 5-digit numbers that between them use the digits 0 through 9 once each, such that the first number divided by the second is equal to an integer N, where 2 ≤ N ≤ 79. That is,
$$
\frac{\text{abcde}}{\text{fghij}} = N
$$
where each letter represents a different digit. The first digit of one of the numerals is allowed to be zero.

# Input

Each line of the input file consists of a valid integer N. An input of zero is to terminate the program.

# Output

Your program have to display ALL qualifying pairs of numerals, sorted by increasing numerator (and, of course, denominator). Your output should be in the following general form: 

xxxxx / xxxxx = N 

xxxxx / xxxxx = N

# Sample Input

```
61
62
0
```

# Sample Output

```
There are no solutions for 61.

79546 / 01283 = 62
94736 / 01528 = 62
```

-----

如果生成0-9共10个数字的全排列，然后从指间拆分，需要计算$10!=3628800$次，其实可以只枚举分母的5位数字，因为这5位确定了，分子的5位也确定了。

题目有多组输入，如果每次都去生成一个全排列是浪费时间的，因为只需要枚举后5位，相当于从0-9这10个数字中选出5个，于是很自然的想到用《搜索算法——递归与回溯》中的递归生成组合型枚举的方法，优先生成所有的组合，共$\frac{10!}{5! \times 5!} = 252$种，存储数组`seq`备用。

对于每个分母，使用`next_permutation`的标准库算法来生成5位数的全排列，然后`str`记录分子的部分，利用`check()`来进行检验。

对于无法满足条件的处理，用`flag`标记，如果在搜索的过程中出现了一个满足条件的结果，那么就修改`flag`标记。

时间复杂度是$252 \times 5!=30340$，是一个很小的数据。

```c++
#include <bits/stdc++.h>

using namespace std;

string s;
int n;
bool flag = false; //标记是否存在一个满足条件的解
string str; //除数
vector<string> seq; //存储所有的全排列
vector<vector<string>> result(10005, vector<string>(2)); //存储所有的结果
int totalNum = 0; //记录result的长度

//检验生成的组合是否满足条件
bool check(string & tmp)
{
	int b = stoi(tmp);
	str = to_string(b * n);

	if (str.size() != 5) return false;

	string res = str + tmp;
	sort(res.begin(), res.end());

	for (int i = 0; i < 10; ++i) {
		if (res[i] - '0' != i) return false;
	}

	return true;
}

//对长度为5的字符串进行全排列并检验
void calculate(string  tmp)
{
	sort(tmp.begin(), tmp.end());
	do {
		if (check(tmp)) {
			flag = true;
			result[totalNum][0] = str, result[totalNum][1] = tmp;
			++totalNum;
		}
	} while (next_permutation(tmp.begin(), tmp.end()));
}

//预处理生成所有的长度为5的字符串
//存入seq备用
void generate(int step)
{
	if (s.size() > 5 || s.size() + 10 - step < 5) return;

	if (step == 10) {
		seq.push_back(s);		
		return;
	}

	s.push_back('0' + step);
	generate(step + 1);
	s.pop_back();
	generate(step + 1);
}

inline void solve()
{
	int len = seq.size();
	for (int i = 0; i < len; ++i) {
		calculate(seq[i]);
	}
}

ostream & operator<<(ostream & os, vector<vector<string>> & v)
{
	for (int i = 0; i < totalNum; ++i) {
		os << v[i][0] << " / " << v[i][1] << " = " << n << endl;
	}
	return os;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	generate(0); //预处理

	int caseNum = 0;
	while ((cin >> n) && n) {
		if (caseNum++) cout << endl;

		//初始化
		flag = false;
		totalNum = 0;

		solve();
		if (!flag) cout << "There are no solutions for " << n << '.' << endl;
		else {
			sort(result.begin(), result.begin() + totalNum); //按照递增顺序输出
			cout << result;
		}
	}

	return 0;
}
```













