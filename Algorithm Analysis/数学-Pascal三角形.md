> # 数学-Pascal三角形

很多题目都喜欢以Pascal三角形为背景，熟悉Pascal三角形的基本构造方法，对于解题可以起到加速作用。

最基本的构造方法：

```c++
//LeetCode 118，写最精简的版本，输出全部
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res(numRows, vector<int>());
        for (int i = 0; i < numRows; ++i) {
            res[i].resize(i + 1, 1);
            for (int j = 1; j < i; ++j) {
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
            }
        }
        
        return res;
    }
};
```

输出某一行的最节省空间的写法：

```c++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex + 1, 0);
        res[0] = 1;
        for (int i = 1; i <= rowIndex; ++i) {
            for (int j = i; j >= 1; --j)
                res[j] += res[j - 1];
        }
        
        return res;
    }
};
```



典型题目：

- [x] LeetCode 118 Pascal's Triangle
- [x] LeetCode 119 Pascal's Triangle II
- [x] POJ 3187 Backward Digit Sums(其实题面是倒置的Pascal三角形，本质是排列组合问题)