> # 字符串算法-Manacher算法

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**

```
Input: "cbbd"
Output: "bb"
```

-----

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        
        preProcess(s);
        int n = s.size();
        vector<int> p(n);
        //mx 是回文串能延伸到的最右端的位置
        //mid为能延伸到最右端的位置的那个回文子串的中心点位置
        int mid = 1, mx = 1, len = 0;
        int pos = 1;
        for (int i = 1; i < n; ++i) {
            if (i < mx) p[i] = min(mx - i, p[2 * mid - i]);
            else p[i] = 1;
            while (s[i + p[i]] == s[i - p[i]]) ++p[i];
            if (i + p[i] > mx) {
                mid = i;
                mx = i + p[i];
            }
            if (p[i] - 1 > len) {
                len = p[i] - 1;
                pos = i;
            }
        }
        
        string tmp = s.substr(pos - p[pos] + 1, 2 * p[pos] - 1);
        string res;
        for (auto e : tmp) {
            if (e == '#') continue;
            else res.push_back(e);
        }
        
        return res;
    }
    
    void preProcess(string & s)
    {
        string tmp = "$#";
        for (int i = 0; i < s.size(); ++i) {
            tmp.push_back(s[i]);
            tmp.push_back('#');
        }
        tmp.push_back('@');
        s = tmp;
    }
};
```

# 典型题目

LeetCode 关键词搜索palindrome即可。

- [x] 洛谷-P3805 【模板】manacher算法
- [x] LeetCode 5.Longest Palindromic Substring
- [ ] LeetCode 647