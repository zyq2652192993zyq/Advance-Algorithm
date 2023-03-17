> # HDU-1864 Brave Game（巴什博弈板子题）

# Description

十年前读大学的时候，中国每年都要从国外引进一些电影大片，其中有一部电影就叫《勇敢者的游戏》（英文名称：Zathura），一直到现在，我依然对于电影中的部分电脑特技印象深刻。
今天，大家选择上机考试，就是一种勇敢（brave）的选择；这个短学期，我们讲的是博弈（game）专题；所以，大家现在玩的也是“勇敢者的游戏”，这也是我命名这个题目的原因。
当然，除了“勇敢”，我还希望看到“诚信”，无论考试成绩如何，希望看到的都是一个真实的结果，我也相信大家一定能做到的~

各位勇敢者要玩的第一个游戏是什么呢？很简单，它是这样定义的：
1、  本游戏是一个二人游戏;
2、  有一堆石子一共有n个；
3、  两人轮流进行;
4、  每走一步可以取走1…m个石子；
5、  最先取光石子的一方为胜；

如果游戏的双方使用的都是最优策略，请输出哪个人能赢。

# Input

输入数据首先包含一个正整数C(C<=100)，表示有C组测试数据。
每组测试数据占一行，包含两个整数n和m（1<=n,m<=1000），n和m的含义见题目描述。

# Output

如果先走的人能赢，请输出“first”，否则请输出“second”，每个实例的输出占一行。

# Sample Input

```
2
23 2
4 3
```

# Sample Output

```
first
second
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
#include <stack>
#include <map>
#include <set>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
    	int n, m;
    	cin >> n >> m;
    	if (n % (m + 1)) cout << "first" << endl;
    	else cout << "second" << endl;
    }

    return 0;
}
```

