> # AOJ-0118 Property Distribution

> 原题目链接是：<http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0118>，是日文显示。我选择将其转成中文（转成英文也可以）。

# 物业分布

田中先生*HW*去世了，留下伯爵的果园。北园，南，东，西三方向*^ h*×*它*分为 *W个*部分，每个部分都种植苹果，牡蛎和橙子。田中留下了这样的遗愿。

果园应按地块划分为尽可能多的亲戚。但是，如果在包裹的东，西，北和南任一方向上的包裹中都种植了相同类型的水果，则将包裹视为一个大包裹，因为包裹的边界未知。

例如，如果是以下3×10的部分（“ li”表示苹果，“ ka”表示牡蛎，“ mi”表示普通话）

![img](F:\Project\ACM-Algorithm\Problem Solution\assets\property1.gif)

消除具有同一棵树的地块之间的边界可得出：

![img](F:\Project\ACM-Algorithm\Problem Solution\assets\property2.gif)

您最终将得到10个包裹或10个人。

必须在降雪和包裹边界变得不可见之前完成分配。您的任务是根据果园图确定要分发的包裹数量。

编写一个程序，读取果园的地图并输出可以分发的亲戚的数量。

## 输入项

给出了多个数据集。每个数据集由空格分隔*ħ*，*w ^*（*ħ*，*W¯¯*开始用含有≤100行），然后是 *ħ*×给出了由字母 *W*组成的 *H*行字符串。该字符串中仅出现三个字符：“@”代表苹果，“＃”代表牡蛎，“*”代表橙色。

输入在两行上为零终止。数据集数量不超过20。

## 输出量

对于每个数据集，输出要在一行上接受分配的人数。

## 样本输入

```
10 10
#### ***** @
@＃@@@@@＃* ## *
@ ## *** @@@ *
＃****＃* @ **
## @ *＃@@ * ##
* @@@@ * @@@＃
***＃@ * @ ## *
* @@@ * @@ ## @
* @ *＃* @ ## **
@ ****＃@@＃@
0 0
```

## 样本输入的输出

```
33
```

----

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int m = 100, n = 100;
vector<vector<char> > ground(m, vector<char>(n));

int direction[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void DFS(int row, int col)
{
    char symbol = ground[row][col];
    ground[row][col] = '.';
    for (int i = 0; i < 4; ++i) {
        int tmpRow = row + direction[i][0];
        int tmpCol = col + direction[i][1];
        if (0 <= tmpRow && tmpRow < m && 0 <= tmpCol && tmpCol < n && ground[tmpRow][tmpCol] == symbol) {
                DFS(tmpRow, tmpCol);
        }
    }       
}

int solve()
{
    int res = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (ground[i][j] != '.') {
                DFS(i, j);
                ++res;
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

    while ((cin >> m >> n) && m && n) {
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> ground[i][j];
            }
        }
        cout << solve() << endl;
    }

    return 0;
}
```

思路和lake counting基本一致，有一个很好的方法可以借鉴，最初的想法是利用一个`visit`数组来记录某个点是否被访问过，这里直接在原数组矩阵里面修改，节省了空间。