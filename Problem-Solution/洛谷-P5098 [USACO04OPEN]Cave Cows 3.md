> # 洛谷-P5098 [USACO04OPEN]Cave Cows 3

## 题目描述

约翰的$ N ( 1 \leq N \leq 50000)$只牛在一个黑魃魃的洞里探险，他们只能通过叫声交流。

两只牛之间的曼哈顿距离决定了声音传播的时间。即牛1与牛2交流，需要的时间为 $|x_1-x_2|+|y_1-y_2|$ 。其中 $-10^6 \leq x_1,x_2,y_1,y_2 \leq 10^6$。

那任意一对牛之间交流时间的最大值为多少？

## 输入格式

第1行输入 N*N* ，接下来每行输入一只牛的坐标。

## 输出格式

交流时间最大值（即最大曼哈顿距离）。

## 输入输出样例

**输入 #1**

```
5
1 1
3 5
2 7
8 1
4 4
```

**输出 #1**

```
12
```

## 说明/提示

样例解释：

(2,7)(2,7) 和 (8,1)(8,1) 两点间的距离最大，为12。

------

分为四种情况讨论：

* $x_1, x_2 \geq 0, y_1, y_2 \geq 0$：

$$
\begin{aligned}
&\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right| \\
=& x_{1}-x_{2}+y_{1}-y_{2} \\
=&\left(x_{1}+y_{1}\right)-\left(x_{2}+y_{2}\right)
\end{aligned}
$$

* $x_1, x_2 < 0, y_1, y_2 \geq 0$

$$
\begin{aligned}
&\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right| \\
=& x_{2}-x_{1}+y_{1}-y_{2} \\
=&\left(x_{2}-y_{2}\right)-\left(x_{1}-y_{1}\right)
\end{aligned}
$$

* $x_1, x_2 \geq 0, y_1, y_2 < 0$

$$
\begin{aligned}
&\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right| \\
=& x_{1}-x_{2}+y_{2}-y_{1} \\
=&\left(x_{1}-y_{1}\right)-\left(x_{2}-y_{2}\right)
\end{aligned}
$$

* $x_1, x_2 < 0, y_1, y_2 < 0$

$$
\begin{aligned}
&\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right| \\
=& x_{2}-x_{1}+y_{2}-y_{1} \\
=&\left(x_{2}+y_{2}\right)-\left(x_{1}+y_{1}\right)
\end{aligned}
$$

所以最终结果是$\max \left\{\max \left\{x_{i}+y_{i}\right\}-\min \left\{x_{i}+y_{i}\right\}, \max \left\{x_{i}-y_{i}\right\}-\min \left\{x_{i}-y_{i}\right\}\right\}$



```c++
#include <bits/stdc++.h>

using namespace std;


int n;



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    cin >> n;
    int x, y;
    int minX = INT_MAX, maxX = INT_MIN, minY = INT_MAX, maxY = INT_MIN;
    for (int i = 0; i < n; ++i) {
    	cin >> x >> y;
    	minX = min(minX, x + y), maxX = max(maxX, x + y);
    	minY = min(minY, x - y), maxY = max(maxY, x - y);
    }

    cout << max(maxX - minX, maxY - minY) << endl;

    return 0;
}
```

