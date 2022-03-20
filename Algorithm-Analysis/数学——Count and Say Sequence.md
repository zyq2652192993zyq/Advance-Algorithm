> # 数学-count and say sequence

经常看到这样一组找规律的题目：

```
1
11
21
1211
111221
312211
```

```
1 读为 1个1，所以后一个数记为 11

11 读为 2个1，所以后一个数记为 21

21 读为 1个2,1个1，所以后一个数记为 1211

1211 读为 1个1,1个2,2个1，所以后一个数记为 111221

111221 读为 3个1,2个2,1个1，所以后一个数记为 312211
```

以此为背景的题目主要是`PAT 1140. Look-and-say Sequence `。

一般有两种形式

* 一种是编写程序实现这个序列
* 以此序列为背景衍生的题目，主要是`PAT 1140`.


典型题目：

- [x] Leetcode 38 

```c++
class Solution {
public:
    string countAndSay(int n) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        
        string res = "1";
        if (n == 1) return res;
        
        for (int i = 2; i <= n; ++i) {
            res.push_back('@');
            string tmp;
            int start = 0;
            for (int j = 0; j < res.size(); ++j) {
                if (res[j] != res[start]) {
                    tmp += to_string(j - start);
                    tmp += to_string(res[start] - '0');
                    start = j;
                }
            }
            res = tmp;
        }
        
        return res;
    }
};
```

当然LeetCode这道题目因为限定了数据范围是1-30，也可以暴力打表！！！