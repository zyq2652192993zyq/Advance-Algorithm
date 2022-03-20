> # 搜索算法——双向BFS

以LeetCode 127为例，从`beginWord`转移到`endWord`，思路为（参考`宫水三叶`的题解）：

* 创建两个队列分别用于两个方向的搜索
* 创建两个哈希表存储从出发点到当前位置转移的次数，并且记录当前状态在历史是否出现过
* 为了尽可能让两个方向搜索方向平均，每次从队列容量小的队列进行搜索。
* 如果在搜索过程中，出现了在另一个BFS中出现过得节点，那么认为找到了最短路

```c++
class Solution {
	unordered_map<string, int> um1, um2;
	unordered_set<string> us;
	queue<string> q1, q2;

public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    	std::ios_base::sync_with_stdio(false);
    	cin.tie(NULL);
    	cout.tie(NULL);

    
    	for (auto & e : wordList) us.insert(e);
    	if (us.find(endWord) == us.end()) return 0;
    	us.insert(beginWord);
    	q1.push(beginWord);
    	um1[beginWord] = 0;
    	q2.push(endWord);
    	um2[endWord] = 0;

    	int res = BFS();

    	return res == -1 ? 0 : res + 1;
    }

    int BFS() {
    	while (!q1.empty() && !q2.empty()) {
    		int tmp;
    		if (q1.size() < q2.size()) {
    			tmp = helper(q1, um1, um2);
	    	}
	    	else {
	    		tmp = helper(q2, um2, um1);
	    	}

	    	if (tmp != -1) return tmp;
    	}

    	return -1;
    }

    int helper(queue<string> & q, unordered_map<string, int> & cur, unordered_map<string, int> & other) {
    	string word = q.front(); q.pop();
    	int n = word.size();

    	for (int i = 0; i < n; ++i) {
    		for (int j = 0; j < 26; ++j) {
    			if ('a' + j == word[i]) continue;

    			string tmpWord = word;
    			tmpWord[i] = 'a' + j;
    			if (us.find(tmpWord) != us.end() && cur.find(tmpWord) == cur.end()) {
    				if (other.find(tmpWord) != other.end()) {
    					return cur[word] + 1 + other[tmpWord];
    				}
    				else {
    					q.push(tmpWord);
    					cur[tmpWord] = cur[word] + 1;
    				}
    			}
    		}
    	}

    	return -1;
    }
};
```

这道题目还需要注意一种特殊情况

```
beginWord = "hog", endWord = "cog", list = ["cog"]
```

在初始化的时候，需要把`beginWord`也加入到`set`里面，不然双向BFS无法成功。

假设`wordList`的长度为`n`，字符串`beginWord`的长度为`m`，由于所有的搜索结果都必须在`wordlist`出现，所以最多`n + 1`个节点，假设所有节点联通，那么时间复杂度为$O(n^2)$，对`beginWord`的每个字符进行替换，时间复杂度为$O(m)$，所以总体时间复杂度为$O(m \times n^2)$。

## 典型题目

- [x] LeetCode 127.Word Ladder （hard，单词接龙）
- [x] LeetCode 752.Open the Lock (medium)
