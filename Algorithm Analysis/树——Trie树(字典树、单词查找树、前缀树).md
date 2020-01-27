> #Trie树(字典树、单词查找树、前缀树)

《算法》 第四版

《C++17 STL cook book》

典型题目：

- [x] HDU 1251
- [ ] UVA 1401
- [x] HDU 1671
- [ ] HDU 1247
- [ ] POJ 1056
- [ ] HDU 4099
- [ ] POJ 2001
- [ ] POJ 2503
- [ ] POJ 1816
- [ ] POJ 2001
- [ ] POJ 2513
- [ ] POJ 1451
- [ ] POJ 2503
- [ ] POJ 3283

## 5.2 单词查找树

功能实现：（静态 和 动态）`LeetCode 208`

插入，删除，查找，最长前缀，包含前缀的单词个数

```c++
#include <iostream>
#include <string>

using namespace std;

class TrieNode{
public:
    int wordNum;
    bool isWord; //到当前字符为止是否是一个完整的单词
    TrieNode *child[26];

    TrieNode() : wordNum(0), isWord(false) {
    	for (auto & a : child) a = nullptr;
    }
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root  = new TrieNode();
    }

    ~Trie(){
    	clear();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *p = root;
        ++(p -> wordNum);

        for (auto &a : word){
        	int id = a - 'a';
        	if (!p -> child[id]) p -> child[id] = new TrieNode();
        	p = p -> child[id];
            ++(p -> wordNum);
        }

        p -> isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    int search(string word) {
        TrieNode *p = root;

        for (auto a : word){
        	int id = a - 'a';
        	if (!p -> child[id]) return 0;
        	p = p -> child[id];
        }

        return p -> wordNum;
    }

    void clear()
    {
    	remove(root);

    	for (int i = 0; i < 26; ++i)
    		root -> child[i] = nullptr;
    }

private:
	TrieNode *root;

	void remove(TrieNode * &p)
	{
		for (int i = 0; i < 26; ++i){
			if (!p -> child[i]) continue;
			remove(p -> child[i]);
			delete p -> child[i];
			p -> child[i] = nullptr;
			if ( (--(p -> wordNum)) == 0 ) break;
		}
	}
};
```

比较好的C++实现：<https://www.cnblogs.com/luxiaoxun/archive/2012/09/03/2668611.html>

思考路径压缩，如果路径上没有分支那么就可以压缩（如何实现压缩？）





