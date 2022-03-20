> # NYOJ-16 嵌套矩形（最长上升子序列LIS）

# 描述

有n个矩形，每个矩形可以用a,b来描述，表示长和宽。矩形X(a,b)可以嵌套在矩形Y(c,d)中当且仅当a<c,b<d或者b<c,a<d（相当于旋转X90度）。例如（1,5）可以嵌套在（6,2）内，但不能嵌套在（3,4）中。你的任务是选出尽可能多的矩形排成一行，使得除最后一个外，每一个矩形都可以嵌套在下一个矩形内。

# 输入

第一行是一个正正数N(0<N<10)，表示测试数据组数，每组测试数据的第一行是一个正正数n，表示该组测试数据中含有矩形的个数(n<=1000)随后的n行，每行有两个数a,b(0<a,b<100)，表示矩形的长和宽

# 输出

每组测试数据都输出一个数，表示最多符合条件的矩形数目，每组输出占一行

# 样例输入

```
1
10
1 2
2 4
5 8
6 10
7 9
3 1
5 8
12 10
9 7
2 2
```



# 样例输出

```
5
```

---

````c++
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define maxNum 1000
vector<int> d(maxNum, 0);

void LIS(vector<int> & lengh, vector<int> & width) //longest increasing subsequence
{
    
    d[0] = 1;
    int n = length.size();

    for (int j = 1; j < n; ++j){
        int maxLength = 0;
        for (int i = 0; i < j; ++i){
            if (length[i] < length[j] && width[i] < width[j] && maxLength < d[i]) 
                maxLength = d[i];
        }
        d[j] = maxLength + 1;
    }
}

int main()
{
    int caseNum;
    cin >> caseNum;

    while (caseNum--){
        int rectangleNum;
        cin >> rectangleNum;

        vector<int> lengh(rectangleNum), width(rectangleNum);
        for (int i = 0; i < rectangleNum; ++i){
            cin >> lengh[i] >> width[i];
        }
        LIS(lengh, width);
        cout << *max_element(d.begin(), d.begin() + rectangleNum) << endl;

        fill(d.begin(), d.begin() + rectangleNum, 0);
    }

    return 0;
}
````

其实就是相当于同时判断

``