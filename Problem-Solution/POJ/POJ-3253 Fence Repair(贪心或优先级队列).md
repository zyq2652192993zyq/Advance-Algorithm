> # POJ-3253 Fence Repair(贪心或优先级队列)

# Description

Farmer John wants to repair a small length of the fence around the pasture. He measures the fence and finds that he needs *N* (1 ≤ *N* ≤ 20,000) planks of wood, each having some integer length *Li* (1 ≤ *Li* ≤ 50,000) units. He then purchases a single long board just long enough to saw into the *N* planks (i.e., whose length is the sum of the lengths *Li*). FJ is ignoring the "kerf", the extra length lost to sawdust when a sawcut is made; you should ignore it, too.

FJ sadly realizes that he doesn't own a saw with which to cut the wood, so he mosies over to Farmer Don's Farm with this long board and politely asks if he may borrow a saw.

Farmer Don, a closet capitalist, doesn't lend FJ a saw but instead offers to charge Farmer John for each of the *N*-1 cuts in the plank. The charge to cut a piece of wood is exactly equal to its length. Cutting a plank of length 21 costs 21 cents.

Farmer Don then lets Farmer John decide the order and locations to cut the plank. Help Farmer John determine the minimum amount of money he can spend to create the *N* planks. FJ knows that he can cut the board in various different orders which will result in different charges since the resulting intermediate planks are of different lengths.

# Input

Line 1: One integer *N*, the number of planks
Lines 2.. *N*+1: Each line contains a single integer describing the length of a needed plank

# Output

Line 1: One integer: the minimum amount of money he must spend to make *N*-1 cuts

# Sample Input

```
3
8
5
8
```

# Sample Output

```
34
```

----

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    int tmp;
    priority_queue<int, vector<int>, greater<int> > pq;
    while (cin >> tmp) {pq.push(tmp);}
    long long res = 0;
    while (pq.size() >= 2) {
        int num1 = pq.top(); pq.pop();
        int num2 = pq.top(); pq.pop();
        res += num1 + num2;
        pq.push(num1 + num2);
    }
    cout << res << endl;
    
    return 0;
}
```

这道题其实就是霍夫曼编码(在《C++程序设计思想与方法》里面解释的很详细)的一个应用例子，采用优先级队列，时间复杂度是$O(nlogn)$。

在《挑战程序设计竞赛》里还给出了一种$O(n^2)$的解法，对于书中给出的解释做一些补充，首先这道题的突破口是要想到最后得到的木板一定是一棵树的叶节点，因为如果不是叶节点，此节点还有子节点，那么当前节点对应的木板长度是没法保留的，所以只能是叶节点。

第二点，要分析出开销的合计表达式，这是最后写出正确计算表达式的关键：开销合计 = 木板的长度 $\times$ 节点的深度。节点深度其实对应的实际意义是需要切割多少次来得到这个木板长度。

第三点：得出“最短的板与次短的板的节点是兄弟节点”的结论，这个结论是选定解决方案和写出正确程序的关键。应该分析出最短的板一定是深度不小于其他板的节点，因为如果最短的板的节点深度比其他节点小，那么根据第二步的表达式，为了让开销最小，就可以选择所有板里面的最大值与此节点交换，那么总开销一定是减少的。试想如果最短的板所在的节点没有兄弟节点，那么意味着父节点和当前节点是一样的，所以也就没必要单独列出一个叶节点，所以最短板所在的节点一定是有兄弟节点的（存在性证明）。第二点，最短的板的兄弟节点是否其长度不是次短板？也不可能，因为如果最短的板的节点深度大于其他所有节点，那么其兄弟节点如果不是次短板，一定可以用次短板与兄弟节点交换，根据第二步的表达式可以知道总消耗一定是减少的；如果存在其他节点和最短板节点深度相同，也就是有至少四个节点的深度是相同的，那么根据第一步的证明，这四个节点的父节点一定是有兄弟节点的，根据第二步推出的表达式可知，如果不改变节点的深度，那么将其安排在任意位置是等价的。所以可以用最短板的父节点的兄弟节点，与另外两个深度与最短板深度相同的节点的父节点交换，总消耗不变，那么此时设四个深度相同的点代表的数值分别为：
$$
0 < a < b < c < d
$$
那么合并之后意味着：`a+b`和`c+d`对应的节点成为了兄弟节点，显然`c+d`的节点可以被单独的`c`代替让总消耗减小，那么也就证明：最短的板是深度最大的节点，只能是其兄弟节点与之深度相同，其他所有节点的深度都要小于最短板的节点深度，这样再根据第一种情况直到最短板的兄弟节点一定是次短板。

![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/graphviz.png)

但是这种分析有一种特例，比如四个点分别是6，7，10，11

![](https://raw.githubusercontent.com/zyq2652192993zyq/Picture-Bed/master/graphviz%20(1).png)

这种情况下，两两结合都不影响，所以结论应该略作修改，如果节点个数是2的幂，比如1，2，4，8等，则任意两两组合都不影响最终结果，因为所有点的深度都是一样的，其他情况则符合上述分析。

特殊情况和一般情况都可以用统一的合并最短板和次短板来解决，那么总体采用此策路也是没问题的。

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n = 20000;
vector<long long> sequence(n);

long long minCost()
{
    long long res = 0;

    while (n > 1) {
        int pos1 = 0, pos2 = 1; //依次记录最短板和次短板的下标
        if (sequence[pos1] > sequence[pos2]) swap(pos1, pos2);
        
        for (int i = 2; i < n; ++i) {
            if (sequence[i] < sequence[pos1]) {
                pos2 = pos1;
                pos1 = i;
            }
            else if (sequence[i] < sequence[pos2])
                pos2 = i;
        }
        long long tmpSum = sequence[pos1] + sequence[pos2];
        //cout << "(" << sequence[pos1] << "," << sequence[pos2] << ")" << endl;
        res += tmpSum;
        if (pos1 == n - 1) swap(pos1, pos2); //因为最后一个节点是要被去掉的
        sequence[pos1] = tmpSum;
        sequence[pos2] = sequence[n - 1];
        --n;
    }

    return res;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; ++i) cin >> sequence[i];
    cout << minCost() << endl;
    
    return 0;
}
```

进一步思考，如果要求输出是如何切割的，比如要输出第一步切割`(8,13)`，第二步切割成`(3,5)`，其实只需要把注释掉的输出语句稍加修改即可。