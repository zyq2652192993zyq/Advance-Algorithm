> # ALGOSPOT-PICNIC（递归）

> 原文为韩文，这里翻译成中文，提交在algospot。

#### 问题

仙女座幼稚园特快班将在Yuldong公园旁野餐。老师想让两个学生在野餐时成对表演。但是，如果结交了不是朋友的学生，则您不会互相争斗或四处走动，因此，您应该始终仅将彼此为朋友的学生配对。

对于每对学生，编写一个程序，计算给学生配对的方式，并确定他们是否是彼此的朋友。即使只有几个配对的学生是不同的，它也是不同的。例如，以下两种方法是不同的。

- （泰妍，杰西卡）（晴天，蒂芙尼）（孝延，尤里）
- （泰妍，杰西卡）（晴天，格拉斯）（孝妍，蒂芙尼）

#### 输入项

输入的第一行给出了测试用例C的数量（C <= 50）。每个测试用例的第一行都给出学生数n（2 <= n <= 10）和朋友对数m（0 <= m <= n *（n-1）/ 2）。下一行给出m个整数对，两个彼此成为朋友的学生的数量。这些数字都是0到n-1之间的整数，并且不会重复输入同一对。学生人数是偶数。

#### 输出量

对于每个测试用例，打印出将所有学生配对成一行的几种方法。

#### 输入示例

```
3 
2 1 
0 1 
4 6 
0 1 1 2 2 3 3 0 0 2 1 3 
6 10 
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5
```

#### 输出示例

```
1
3
4
```

----

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n = 10, m = 45;
vector<vector<int>> ground(n, vector<int>(n, 0)); 
vector<bool> visit(n, false);

int solve()
{
    int firstFree = -1;
    for (int i = 0; i < n; ++i) {
        if (!visit[i]) {
            firstFree = i;
            break;
        }
    }
    if (firstFree == -1) return 1;
    int cnt = 0;
    for (int i = firstFree + 1; i < n; ++i) {
        if (!visit[i] && ground[firstFree][i]) {
            visit[firstFree] = visit[i] = true;
            cnt += solve();
            visit[firstFree] = visit[i] = false;
        }
    }

    return cnt;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum;
    cin >> caseNum;
    while (caseNum--) {
        cin >> n >> m;
        for (int i = 0; i < m; ++i) {
            int point1, point2;
            cin >> point1 >> point2;
            ground[point1][point2] = 1;
            ground[point2][point1] = 1;
        }
        cout << solve() << endl;
        fill(visit.begin(), visit.end(), false);
        for (int i = 0; i < n; ++i)
            fill(ground[i].begin(), ground[i].end(), 0);
    }
    
    return 0;
}
```

