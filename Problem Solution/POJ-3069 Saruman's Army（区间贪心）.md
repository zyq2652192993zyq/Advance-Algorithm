> # POJ-3069 Saruman's Army（贪心）

# Description

Saruman the White must lead his army along a straight path from Isengard to Helm’s Deep. To keep track of his forces, Saruman distributes seeing stones, known as palantirs, among the troops. Each palantir has a maximum effective range of *R* units, and must be carried by some troop in the army (i.e., palantirs are not allowed to “free float” in mid-air). Help Saruman take control of Middle Earth by determining the minimum number of palantirs needed for Saruman to ensure that each of his minions is within *R* units of some palantir.

# Input

The input test file will contain multiple cases. Each test case begins with a single line containing an integer *R*, the maximum effective range of all palantirs (where 0 ≤ *R* ≤ 1000), and an integer *n*, the number of troops in Saruman’s army (where 1 ≤ *n* ≤ 1000). The next line contains n integers, indicating the positions *x*1, …, *xn* of each troop (where 0 ≤ *xi* ≤ 1000). The end-of-file is marked by a test case with *R* = *n* = −1.

# Output

For each test case, print a single integer indicating the minimum number of palantirs needed.

# Sample Input

```
0 3
10 20 20
10 7
70 30 1 7 15 20 50
-1 -1
```

# Sample Output

```
4
2
```

----

```c++
//POJ 3069
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sequence(1000);
int range, n;

int mark()
{
    int cnt = 0;
    int pos = 0;
    while (true) {
        int target = sequence[pos] + range; //下面去寻找最后一个不大于目标值的数
        while (pos < n && sequence[pos] <= target) {++pos;}
        ++cnt;
        if (pos >= n) break;
        pos = pos - 1;
        target = sequence[pos] + range; //寻找第一个大于目标值的数
        while (pos < n && sequence[pos] <= target) {++pos;}
        if (pos >= n) break;
    }

    return cnt;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while ((cin >> range >> n) && range != -1 && n != -1) {
        for (int i = 0; i < n; ++i) {
            cin >> sequence[i];
        }
        sort(sequence.begin(), sequence.begin() + n);
        cout << mark() << endl;
    }
    
    return 0;
}
```

对于整个序列，总可以找到一个没有标记的点，然后以此开始，为了让标记的点尽可能地少，那么就应该去寻找最后一个小于**当前坐标值+覆盖范围**的点，这时候会出现两种情况，第一种，到了序列地最后也没能找到，这时候肯定要`++cnt`，直接退出循环；如果没有到末尾并且找到了这样一个位置，那么就在这个位置放置标记点，也需要`++cnt`，所以两种情况地区别只在于多了一行判断。找到了一个标记点，然后去寻找下一个不在覆盖区域地点，仍然会有两种情况，第一种，到了末尾那么直接退出就好；第二种，找到了这样一个点，会发现此时和我们最初分析问题地情景是一致地，这样就形成了循环，也相当于验证了我们程序地正确性。程序只需要把上述分析内容转成代码即可。

注意地一点是，这里用了“寻找最后一个不大于目标值地数”，“寻找第一个大于目标值地数”，很容易联想到二分法里面的`upper_bound()`，之所以不采用是因为二分查找位置， 一次查找的效率是$O(logn)$，如果最坏的情况下每个坐标点都不互相覆盖，那么时间复杂度就是$O(nlogn)$，而这里的方法最坏情况也是$O(n)$，所以最好不要采用二分的办法。

当然如果考虑到了因为我们在执行`mark()`函数前对数组排了序，时间复杂度已经是$O(nlogn)$了，那么是否可以采用二分来代替程序里面搜索下一个位置呢？最好也不要，因为如果题目变换一下，输入序列是有序的，时间卡的严格一点可能就不行了，所以保险起见还是不用二分来搜索位置。