> # HDU-2602 Bone Collector（动态规划 01背包）

# Problem Description

Many years ago , in Teddy’s hometown there was a man who was called “Bone Collector”. This man like to collect varies of bones , such as dog’s , cow’s , also he went to the grave …
The bone collector had a big bag with a volume of V ,and along his trip of collecting there are a lot of bones , obviously , different bone has different value and different volume, now given the each bone’s value along his trip , can you calculate out the maximum of the total value the bone collector can get ?

![img](http://acm.hdu.edu.cn/data/images/C154-1003-1.jpg)

# Input

The first line contain a integer T , the number of cases.
Followed by T cases , each case three lines , the first line contain two integer N , V, (N <= 1000 , V <= 1000 )representing the number of bones and the volume of his bag. And the second line contain N integers representing the value of each bone. The third line contain N integers representing the volume of each bone.

# Output

One integer per line representing the maximum of the total value (this number will be less than $2^{31}$).

# Sample Input

```
1
5 10
1 2 3 4 5
5 4 3 2 1
```

# Sample Output

```
14
```

---

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int caseNum;
    cin >> caseNum;

    while (caseNum--){
        int boneNum, bagVolume; //boneNum <= 100, bagVolume <= 1000
        cin >> boneNum >> bagVolume;

        vector<int> boneValue(boneNum + 1), boneWeight(boneNum + 1);
        for (int i = 1; i <= boneNum; ++i)
            cin >> boneValue[i];
        for (int i = 1; i <= boneNum; ++i)
            cin >> boneWeight[i];

        vector<int> line(bagVolume + 1, 0);
        vector<vector<int>> f(boneNum + 1, line);

        for (int i = 1; i <= boneNum; ++i){
            for (int j = 0; j <= bagVolume; ++j){
                f[i][j] = f[i - 1][j];
                if (j >= boneWeight[i]) 
                    f[i][j] = max(f[i][j], f[i-1][j - boneWeight[i]] + boneValue[i]);
            }
        }

        cout << f[boneNum][bagVolume] << endl;
    }

    return 0;
}
```

使用滚动数组：

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int caseNum;
    cin >> caseNum;

    while (caseNum--){
        int boneNum, bagVolume; //boneNum <= 100, bagVolume <= 1000
        cin >> boneNum >> bagVolume;

        vector<int> boneValue(boneNum + 1), boneWeight(boneNum + 1);
        for (int i = 1; i <= boneNum; ++i)
            cin >> boneValue[i];
        for (int i = 1; i <= boneNum; ++i)
            cin >> boneWeight[i];

        
        vector<int> f(bagVolume + 1, 0);

        for (int i = 1; i <= boneNum; ++i){
            for (int j = bagVolume; j >= boneWeight[i]; --j){
                f[j] = max(f[j], f[j - boneWeight[i]] + boneValue[i]);
            }
        }

        cout << f[bagVolume] << endl;
    }

    return 0;
}
```

定义状态$f[i]][j]$，表示“把前`i `个物品装进容量为`j` 的背包可以获得的最大价值”（此种定义解释保证了每种物品使用0次或者1次），则其状态转移方程便是：
$$
f[i][j]=\max \{f[i-1][j], f[i-1][j-w[i]]+v[i]\}
$$

* 第`i `个不装进去，这时所得价值为：$f[i - 1][j]$
* 第`i`个装进去，价值为$f[i-1][j-w[i]] + v[i]$


使用滚动数组的方法并不一定好理解，不妨从数学形式来看，对于$f[i][j]$的求解，始终需要去访问$f[i-1]*$，其中*代表`(1)`中的两种形式，也就是说，二维的表示可以退化成一维的。即可以用$f[j]$来表示。$f[j] = max(f[j], f[j - boneWeight[i]] + boneValue[i])$，但是需要考虑遍历的顺序。这里是逆序遍历，保证每个物品最多使用一次，如果顺序遍历，则是完全背包问题。

解释一下为什么顺序遍历就会出现可能多次存储的情况，因为要考虑的是针对01背包这一类问题的解法，考虑如果还是顺序遍历，程序的核心代码是：

```c++
vector<int> d(totalWeight + 1, 0);
for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= totalWeight; ++j) {
        d[j] = max(d[j], d[j - w[i]] + v[i]);
    }
}
```

所以可能存在$j - 2w[i]\geq0$的情况，所以在计算$d[j-2*w[i]]$对应的值的时候，用到了$d[j - w[i]]$的结果，那么就意味着第$i$个物品被放入了2次，所以违背了题意。逆序的时候，$d[totalWeight]$只与$d[totalWeight], d[totalWeight-w[i]] + v[i]$有关，所以不会存在重复计算的过程。