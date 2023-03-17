> # AOJ-0033 Ball(DFS + 贪心)

> 原题是日文，由于我看不懂日文，所以就直接翻译成中文了，评测是在virtual judge上。

![img](http://judge.u-aizu.ac.jp/onlinejudge/IMAGE1/ball.gif)

如图所示，有些容器是分叉的。从容器的开口A放下10个编号为1到10的球，并将其放在左管B或右管C中。板D可以绕支点E左右旋转，因此您可以通过移动板D来确定要插入哪个管B或C。

给一排球使其从开口A掉落。按顺序将它们放在气缸B或C中。此时，创建一个程序，如果气缸B和C都可以将大球排列在数量较小的球上，则输出YES，否则，则输出NO。但是，不能改变容器中球的顺序。另外，圆柱体可以相继放置在同一圆柱体中，并且圆柱体B和C具有足够的空间容纳所有十个球。

## 输入项

给出了多个数据集。第一行给出数据集的数量*N。*然后，给出具有*N*行的数据集。每个数据集都有10个数字，左右之间用空格隔开。

## 输出量

每个数据集在一行上输出YES或NO。

## 样本输入

```
2 
3 1 4 2 5 6 7 8 9 10 
10 9 8 7 6 5 4 3 2 1
```

## 样本输入的输出

```
YES 
NO
```

----

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sequence(10);
int leftTop = -1, rightTop = -1;

bool DFS(int num)
{
    if (num == 10) return true;
    //两边同时可以放置则采取贪心策略，找与顶部数字差距最小的放
    if (sequence[num] > leftTop && sequence[num] > rightTop) {
        if (sequence[num] - leftTop < sequence[num] - rightTop) {
            leftTop = sequence[num];
            return DFS(num + 1);
        }
        else {
            rightTop = sequence[num];
            return DFS(num + 1);
        }
    }
    else if (sequence[num] > leftTop) {
        leftTop = sequence[num];
        return DFS(num + 1);
    }
    else if (sequence[num] > rightTop) {
        rightTop = sequence[num];
        return DFS(num + 1);
    }

    return false;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum;
    cin >> caseNum;
    while (caseNum--) {
        for (int i = 0; i < 10; ++i) cin >> sequence[i];
        if (DFS(0)) cout << "YES" << endl;
        else cout << "NO" << endl;
        leftTop = rightTop = -1;
    }

    return 0;
}
```

每一个球的放置策略只有两种选择：左边和右边，但是能否放置有多种情况：

* 左右都能放置
* 只能放在左边
* 只能放在右边
* 两边都不能放置

都不能放置的情况最好处理，直接返回即可。比较难处理的是两边都能放置的情况，可以参考的一种思路是《挑战程序设计竞赛》在2.1.4的部分和例子，考虑每个数加上和不加上能否成功。这里就是先试试放在左边，然后试试放在右边。但是发现这个题目有个特殊的地方，考虑第一个样例，如果最开始1放在左边，3放在右边，然后4两边都可以放，如果选择4放在1的上面，到了2就没法放置了。

根据上面的分析可以直到，如果两边都可以放，那么选择与顶部数字差距最小的一边放置是最优选择，因为这样为后面的数字留出了最大的空间（很类似《算法导论》里的任务安排用的贪心的策略），这样就避免了很多无意义的搜索。

本题的数据是10， 考虑如果从1到100个数或者更大的数据，如果按照没有采取贪心的方法去搜索，显然分支情况就会过多，所以使用贪心其实也算是起到了剪枝的作用。

----

这道题目还可以换一种等价问法：一个序列能否被划分(按顺序的从序列中选取数字)成两个单增序列，两个序列中的一个可以为空。

所以题目还可以从**最长上升子序列**的角度来考虑。先用一个数组`sequence`来存储所有的数字，然后用一个等长的数组`visit`，存储的内容是`bool`类型，初始化为`false`，然后在寻找最长上升子序列时，把在最长上升序列的数字对应的`visit`设为`true`。最后去检查`visit`数组里标记为`false`的部分是否满足单调上升。

但是这种方法的时间复杂度$O(n^2)$空间复杂度显然不如上面的DFS+贪心的方法好。

```c++
//也可以AC的O(n^2)的方法
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sequence(10);
vector<bool> visit(10, false);
vector<int> path(10, -1);

void mark(int num)
{
    if (num == -1) return;
    else {
        visit[num] = true;
        mark(path[num]);
    } 
}

void LIS()
{
    vector<int> d(10, 0);
    d[0] = 1;

    for (int j = 1; j < 10; ++j) {
        int maxLength = 0;
        int pos = -1;
        for (int i = 0; i < j; ++i) {
            if (sequence[j] > sequence[i] && maxLength < d[i]) {
                maxLength = d[i];
                pos = i;
            }
        }
        path[j] = pos;
        d[j] = maxLength + 1;
    }
    int endPos = max_element(d.begin(), d.end()) - d.begin();
    mark(endPos);
}

bool split()
{
    LIS();
    int pre = -1;
    for (int i = 0; i < 10; ++i) {
        if (!visit[i]) {
            if (sequence[i] > pre) pre = sequence[i];
            else return false;
        }
    }
    return true;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum;
    cin >> caseNum;
    while (caseNum--) {
        for (int i = 0; i < 10; ++i) cin >> sequence[i];
        if (split()) cout << "YES" << endl;
        else cout << "NO" << endl;
        fill(visit.begin(), visit.end(), false);
        fill(path.begin(), path.end(), -1);
    }

    return 0;
}
```

用数组`sequence`来记录输入的数字，用函数`split()`来判断序列是否可以分成单增的两部分，函数`split()`先通过函`LIS()`来寻找最长上升子序列，这里有一个技巧，就是增加一个`path()`数组，用来记录当前最大长度是将数字加入到哪一个序列得到的，`path()`数组初始化为-1，最后可以通过递归的方式得到最长上升子序列，-1就标记着当前位置就是子序列的起始位置。这里需要注意的就是因为`sequence`数组下一次输入的时候会覆盖原来的数字，所以并不需要去处理，但是`path, visit`需要在下一个算例开始前进行初始化。

（如果想进一步优化）其实最后一个算例的时候是没有必要对`path,visit`进行初始化的，只需要增加一句：

```c++
if (caseNum != 0) {
    fill(visit.begin(), visit.end(), false);
    fill(path.begin(), path.end(), -1);
}
```



