> # 一本通-weight (LibreOj-10249 DFS)

## 问题描述

已知原数列$a_1, a_2, a_3 \cdots, a_n$中前1项，2项，3项……前`n`项的和，以及后1项，后2项……后`n`项的和，但是所有数据已经被打乱了顺序，还知道数列中的数存在于集合`S`中，求原数列。当存在多组可能的数列时，求左边最小的数列。

## 输入格式

第一行，一个整数`n`

第二行，`2  *n`个整数，注意数据被打乱

第三行，一个整数`m`，表示集合`S`的大小

第四行，`m`个整数，表示`S`集合中的元素

----

解析：

想将前缀和和后缀和组成的序列进行排序，然后从小到大依次判断前缀和在究竟是前缀和还是后缀和，也就是维护当前前缀和和后缀和的大小，然后用取出来的数字和两者作差，看是否在集合`S`中，如果存在，那么可能是一个满足答案的选择。

时间复杂度最坏为$2^{1000}$

```c++
#include <bits/stdc++.h>

using namespace std;


int n, m;
vector<int> preSufSum(2005);
unordered_set<int> us;
vector<int> res(1005);
bool isFind = false;


bool contain(int x) {
    return us.find(x) != us.end();
}


void DFS(int k, int l, int r, int lSum, int rSum) {
    if (isFind)
        return;

    if (l == r) {
        if (! contain(preSufSum[k] - lSum) && ! contain(preSufSum[k] - rSum))
            return;

        int number = preSufSum[n * 2] - lSum - rSum;

        if (number < 1 || number > 500)
            return;

        res[l] = number;
        isFind = true;
        return;
    }

    if (contain(preSufSum[k] - lSum)) {
        res[l] = preSufSum[k] - lSum;
        DFS(k + 1, l + 1, r, preSufSum[k], rSum);
    }

    if (isFind)
        return;

    if (contain(preSufSum[k] - rSum)) {
        res[r] = preSufSum[k] - rSum;
        DFS(k + 1, l, r - 1, lSum, preSufSum[k]);
    }
}



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 1; i <= n * 2; ++i) {
        cin >> preSufSum[i];
    }

    cin >> m;
    int tmp;

    for (int i = 0; i < m; ++i) {
        cin >> tmp;
        us.insert(tmp);
    }

    sort(preSufSum.begin() + 1, preSufSum.begin() + 2 * n + 1);

    DFS(1, 1, n, 0, 0);

    for (int i = 1; i <= n; ++i) {
        cout << res[i];

        if (i != n)
            cout << " ";
    }

    cout << endl;

    return 0;
}
```

