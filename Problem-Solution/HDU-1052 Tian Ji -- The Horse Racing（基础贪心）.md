> # HDU-1052 Tian Ji -- The Horse Racing（基础贪心）

# Description

Here is a famous story in Chinese history.

"That was about 2300 years ago. General Tian Ji was a high official in the country Qi. He likes to play horse racing with the king and others."

"Both of Tian and the king have three horses in different classes, namely, regular, plus, and super. The rule is to have three rounds in a match; each of the horses must be used in one round. The winner of a single round takes two hundred silver dollars from the loser."

"Being the most powerful man in the country, the king has so nice horses that in each class his horse is better than Tian's. As a result, each time the king takes six hundred silver dollars from Tian."

"Tian Ji was not happy about that, until he met Sun Bin, one of the most famous generals in Chinese history. Using a little trick due to Sun, Tian Ji brought home two hundred silver dollars and such a grace in the next match."

"It was a rather simple trick. Using his regular class horse race against the super class from the king, they will certainly lose that round. But then his plus beat the king's regular, and his super beat the king's plus. What a simple trick. And how do you think of Tian Ji, the high ranked official in China?"

![img](https://vj.z180.cn/6fa9aa2f0590001c7074c427f5048537?v=1581169735)

Were Tian Ji lives in nowadays, he will certainly laugh at himself. Even more, were he sitting in the ACM contest right now, he may discover that the horse racing problem can be simply viewed as finding the maximum matching in a bipartite graph. Draw Tian's horses on one side, and the king's horses on the other. Whenever one of Tian's horses can beat one from the king, we draw an edge between them, meaning we wish to establish this pair. Then, the problem of winning as many rounds as possible is just to find the maximum matching in this graph. If there are ties, the problem becomes more complicated, he needs to assign weights 0, 1, or -1 to all the possible edges, and find a maximum weighted perfect matching...

However, the horse racing problem is a very special case of bipartite matching. The graph is decided by the speed of the horses --- a vertex of higher speed always beat a vertex of lower speed. In this case, the weighted bipartite matching algorithm is a too advanced tool to deal with the problem.

In this problem, you are asked to write a program to solve this special case of matching problem.

# Input

The input consists of up to 50 test cases. Each case starts with a positive integer n (n <= 1000) on the first line, which is the number of horses on each side. The next n integers on the second line are the speeds of Tian’s horses. Then the next n integers on the third line are the speeds of the king’s horses. The input ends with a line that has a single 0 after the last test case.

# Output

For each input case, output a line containing a single number, which is the maximum money Tian Ji will get, in silver dollars.

# Sample Input

```
3
92 83 71
95 87 74
2
20 20
20 20
2
20 19
22 18
0
```

# Sample Output

```
200
0
0
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int n = 1005;
vector<int> tianji(n), king(n);

int solve()
{
    sort(tianji.begin() + 1, tianji.begin() + 1 + n);
    sort(king.begin() + 1, king.begin() + 1 + n);

    int Tslow = 1, Tfast = n;
    int Kslow = Tslow, Kfast = Tfast;

    int res = 0;
    while (Tslow <= Tfast && Kslow <= Kfast) {
        if (tianji[Tslow] < king[Kslow]) { //tianji最慢的马比king所有的马都慢
            //选择用最慢的马和king最快的马比赛
            res -= 200;
            ++Tslow;
            --Kfast;
        }
        else if (tianji[Tslow] > king[Kslow]) { //tianji最慢的马比king最慢的马快
            //选择用最慢的马赢掉king最慢的马
            res += 200;
            ++Tslow;
            ++Kslow;
        }
        else { //最慢的马速度相同，考虑双方最快的马
            if (tianji[Tfast] > king[Kfast]) { //tianji最快的马比king最快的马快
                res += 200;
                --Tfast;
                --Kfast;
            }
            else { //去比较tianji最慢的马和king最快的马比赛
                if (tianji[Tslow] < king[Kfast]) res -= 200;
                //无论输赢都要比赛一场
                ++Tslow;
                --Kfast;
            }
        }
    }
    
    return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while (cin >> n && n) {
        for (int i = 1; i <= n; ++i) cin >> tianji[i];
        for (int i = 1; i <= n; ++i) cin >> king[i];
        cout << solve() << endl;
    }

    return 0;
}
```

1.若田忌最慢的马可以战胜齐王最慢的马，那么就让它战胜那匹慢马，胜利场次加1。（田忌最慢马 > 齐王最慢马）

2.若田忌最慢的马不能战胜齐王最慢的马，那么它更加不能战胜其他的马，那就让它输，而且输给齐王最快马，失败场次加1。（田忌最慢马 < 齐王最快马）

3.若田忌最慢的马与齐王最慢的马速度相等。此时，不能简单地认为与它打成平手就是最好情况，相反，打平是下下策，为什么呢？

因为自己后面的队友很有可能战胜此时对方的这匹慢马，所以就算自己输一场，队友也能帮忙赢回一场，而胜一场，输一场的收益和打平一场的收益是一样的，而且自己输的时候可以拉对方最快的马下水，给己方最快的马创造更大的胜利机会（因为它失去了一个强劲的对手），也就是说己方最快的马很可能因为自己的牺牲再胜利一场，从这个角度看，还是自己故意输掉比较好。

但是，还有一点需要注意，当自己放水前，如果己方最快的马原本就比对方最快的马快，然后还输给对方最快的马，那么己方最快的马的才华就浪费了，为什么？

很简单，它原本就能赢，需要你放水么？- -！换句话说，这种情况下，自己的牺牲没有一点价值。

所以，在放水时，一定要保证己方最快马不快于对方最快马。满足此条件后，让己方最慢马与对方最快马去比赛（有可能平局），这样，田忌的马就得到了充分的利用。