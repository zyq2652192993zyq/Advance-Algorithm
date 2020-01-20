> #HDU-1114 Piggy-Bank(动态规划 完全背包)

# Problem Description

Before ACM can do anything, a budget must be prepared and the necessary financial support obtained. The main income for this action comes from Irreversibly Bound Money (IBM). The idea behind is simple. Whenever some ACM member has any small money, he takes all the coins and throws them into a piggy-bank. You know that this process is irreversible, the coins cannot be removed without breaking the pig. After a sufficiently long time, there should be enough cash in the piggy-bank to pay everything that needs to be paid.

But there is a big problem with piggy-banks. It is not possible to determine how much money is inside. So we might break the pig into pieces only to find out that there is not enough money. Clearly, we want to avoid this unpleasant situation. The only possibility is to weigh the piggy-bank and try to guess how many coins are inside. Assume that we are able to determine the weight of the pig exactly and that we know the weights of all coins of a given currency. Then there is some minimum amount of money in the piggy-bank that we can guarantee. Your task is to find out this worst case and determine the minimum amount of cash inside the piggy-bank. We need your help. No more prematurely broken pigs!

# Input

The input consists of T test cases. The number of them (T) is given on the first line of the input file. Each test case begins with a line containing two integers E and F. They indicate the weight of an empty pig and of the pig filled with coins. Both weights are given in grams. No pig will weigh more than 10 kg, that means 1 <= E <= F <= 10000. On the second line of each test case, there is an integer number N (1 <= N <= 500) that gives the number of various coins used in the given currency. Following this are exactly N lines, each specifying one coin type. These lines contain two integers each, Pand W (1 <= P <= 50000, 1 <= W <=10000). P is the value of the coin in monetary units, W is it's weight in grams.

# Output

Print exactly one line of output for each test case. The line must contain the sentence "The minimum amount of money in the piggy-bank is X." where X is the minimum amount of money that can be achieved using coins with the given total weight. If the weight cannot be reached exactly, print a line "This is impossible.".

# Sample Input

```
3
10 110
2
1 1
30 50
10 110
2
1 1
50 30
1 6
2
10 3
20 4
```

# Sample Output

```
The minimum amount of money in the piggy-bank is 60.
The minimum amount of money in the piggy-bank is 100.
This is impossible.
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//无效值，不要用0x7FFFFFFF，执行加运算后会变成负数
const int INF = 0x0ffffff; 

int main()
{
    int caseNum;
    cin >> caseNum;

    while (caseNum--){
        int potWeight, totalWeight;
        cin >> potWeight >> totalWeight;
        int gap = totalWeight - potWeight;

        int typeNum;
        cin >> typeNum;

        vector<int> weight(typeNum + 1), value(typeNum + 1);
        for (int i = 1; i <= typeNum; ++i){
            cin >> value[i];
            cin >> weight[i];
        }

        vector<int> d(gap + 1, INF);
        d[0] = 0;
        for (int i = 1; i <= typeNum; ++i){
            for (int j = weight[i]; j <= gap; ++j){
                d[j] = min(d[j], d[j - weight[i]] + value[i]);
            }
        }

        if (d[gap] == INF) cout << "This is impossible." << endl;
        else cout << "The minimum amount of money in the piggy-bank is " << d[gap] << "." << endl;
    }

    return 0;
}
```

令$dp[i][j]==x$ 表示只用前`i`种货币, 且当总重量达到j克时的最小价值和为`x`.

 初始化: 所有`dp`都为INF(无穷大), 且`dp[0]==0`. (因为本题的目标是价值最小,所以初始化为无穷大. 如果要让目标最大, 那么应该初始化为`-1`. )

状态转移: `dp[i][j] = min( dp[i-1][j] , dp[i][j-cost[i]]+val[i])`

上面方程前者表示第i种硬币一个都不选, 后者表示至少选1个第i种硬币.

最终所求为`dp[n][m]`. (如果`dp[n][m]==INF`, 说明m克是一个不可达的状态)

本题注意两点：

1. `dp[0] = 0`，不然永远是`impossible`的结果
2. 最后输出`d[gap]`数字后面还有一个句号，不然会`wrong answer`。