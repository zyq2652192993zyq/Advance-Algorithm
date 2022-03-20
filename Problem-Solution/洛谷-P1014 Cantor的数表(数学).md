> # 洛谷-P1014 Cantor的数表(数学)

# Description

如下列数，第一项是1/1，第二项是1/2，第三项是2/1，第四项是3/1，第五项是2/2，……输入n，输出第n项。
$$
1/1 \quad  1/2 \quad 1/3 \quad 1/4 \quad 1/5 \\
2/1 \quad 2/2 \quad 2/3 \quad 2/4 \\
3 / 1 \quad 3/2 \quad 3/3 \\
4/1 \quad 4/2 \\
5/1
$$

# Sample Input

```
3
14
7
12345
```

# Sample Output

```
2/1
2/4
1/4
59/99
```

---

```c++
#include <iostream>

using namespace std;

int main()
{
    int num;
    while (cin >> num){
        int top = 1, cnt = 1;
        while(top < num){
            top = (cnt + 2) * top / cnt;
            ++cnt;
            if (top == num) break;
        }

        if (cnt % 2 == 0){
            cout << (cnt - (top - num)) << "/" << (1 + (top - num)) << endl;
        }
        else{
            cout << (1 + (top - num)) << "/" << (cnt - (top - num)) << endl;
        }
    }

    return 0;
}
```

输出起始就是数字对应的行坐标和列坐标（从1开始计数）。斜着看项数是$1,2,3,4\cdots$，所以只需要到所求数字对应的斜线数的最大项即可。奇数阶是在最大数下面，偶数阶是在最大数上面。

