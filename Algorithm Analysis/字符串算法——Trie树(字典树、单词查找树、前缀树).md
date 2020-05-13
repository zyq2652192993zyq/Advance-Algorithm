> # Trie树(字典树、单词查找树、前缀树)



参考资料：https://www.luogu.com.cn/training/4897

P3369 【模板】普通平衡树
P2922 [USACO08DEC]Secret Message G
P3065 [USACO12DEC]First! G
P4735 最大异或和
P5283 [十二省联考2019]异或粽子
P3346 [ZJOI2015]诸神眷顾的幻想乡





# 基本模型

实现一个 `Trie `(前缀树)，包含 `insert`, `search`, 和 `startsWith `这三个操作。

```c++
class Trie {
    struct TrieNode {
        bool isWord;
        TrieNode *child[26];

        TrieNode(): isWord(false) {
            for (auto &e : child) e = NULL;
        }
    };

    TrieNode *root;
public:
    /** Initialize your data structure here. */
    Trie() {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *p = root;

        for (auto & e : word) {
            int id = e - 'a';
            if (!p -> child[id]) p -> child[id] = new TrieNode();
            p = p -> child[id];
        }

        p -> isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *p = root;

        for (auto &e : word) {
            int id = e - 'a';
            if (!p -> child[id]) return false;
            p = p -> child[id];
        }

        return p -> isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *p = root;
        
        for (auto & e : prefix) {
            int id = e - 'a';
            if (!p -> child[id]) return false;
            p = p -> child[id];
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

比较好的C++实现：<https://www.cnblogs.com/luxiaoxun/archive/2012/09/03/2668611.html>

思考路径压缩，如果路径上没有分支那么就可以压缩（如何实现压缩？）

# 单词前缀统计

- [x] HDU-1251 统计难题

Ignatius最近遇到一个难题,老师交给他很多单词(只有小写字母组成,不会有重复的单词出现),现在老师要他统计出以某个字符串为前缀的单词数量(单词本身也是自己的前缀).

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

int main()
{
	Trie trie;
    string inputStr;

    while (getline(cin, inputStr) && inputStr != ""){
    	trie.insert(inputStr);
    }

    while (cin >> inputStr)
    	cout << trie.search(inputStr) << endl;
  
    return 0;
}
```

- [x] HDU 1671 Phone List（单词查找树）

Given a list of phone numbers, determine if it is consistent in the sense that no number is the prefix of another. Let’s say the phone catalogue listed these numbers:

```
1. Emergency 911
2. Alice 97 625 999
3. Bob 91 12 54 26
```

In this case, it’s not possible to call Bob, because the central would direct your call to the emergency line as soon as you had dialled the first three digits of Bob’s phone number. So this list would not be consistent.

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class TrieNode{
public:
    int wordNum;
    bool isWord; //到当前字符为止是否是一个完整的单词
    TrieNode *child[10];

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
        	int id = a - '0';
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
        	int id = a - '0';
        	if (!p -> child[id]) return 0;
        	p = p -> child[id];
        }

        return p -> wordNum;
    }

    void clear()
    {
    	remove(root);

    	for (int i = 0; i < 10; ++i)
    		root -> child[i] = nullptr;
    }

private:
	TrieNode *root;

	void remove(TrieNode * &p)
	{
		for (int i = 0; i < 10; ++i){
			if (!p -> child[i]) continue;
			remove(p -> child[i]);
			delete p -> child[i];
			p -> child[i] = nullptr;
			if ( (--(p -> wordNum)) == 0 ) break;
		}
	}
};

int main()
{
	int caseNum;
	cin >> caseNum;

	while (caseNum--){
		int n;
		cin >> n;

		string phoneNum;
		Trie trie;
		vector<string> store;

		for (int i = 0; i < n; ++i){
			cin >> phoneNum;
			trie.insert(phoneNum);
			store.push_back(phoneNum);
		}
		
		bool flag = true;
		for (auto a : store){
			if (trie.search(a) > 1){
				flag = false;
				break;
			} 
		}

		if (flag) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
  
    return 0;
}
```

# 统计字典树节点个数

- [x] 一本通-1337：【例3-2】单词查找树

**【题目描述】**
在进行文法分析的时候，通常需要检测一个单词是否在我们的单词列表里。为了提高查找和定位的速度，通常都画出与单词列表所对应的单词查找树，其特点如下：

1．根结点不包含字母，除根结点外每一个结点都仅包含一个大写英文字母；

2．从根结点到某一结点，路径上经过的字母依次连起来所构成的字母序列，称为该结点对应的单词。单词列表中的每个单词，都是该单词查找树某个结点所对应的单词；

3．在满足上述条件下，该单词查找树的结点数最少。

4．例如图3-2左边的单词列表就对应于右边的单词查找树。注意，对一个确定的单词列表，请统计对应的单词查找树的结点数（包含根结点）。

![img](http://ybt.ssoier.cn:8088/pic/1337.gif)

**【输入】**
为一个单词列表，每一行仅包含一个单词和一个换行/回车符。每个单词仅由大写的英文字母组成，长度不超过63个字母 。文件总长度不超过32K，至少有一行数据。

**【输出】**
仅包含一个整数，该整数为单词列表对应的单词查找树的结点数。

**【输入样例】**

```
A
AN
ASP
AS
ASC
ASCII
BAS
BASIC
```

**【输出样例】**

```
13
```

-----

```c++
#include <bits/stdc++.h>

using namespace std;

class Trie
{
	struct TrieNode
	{
		TrieNode *child[26];
		TrieNode() {
			for (int i = 0; i < 26; ++i) child[i] = NULL;
		}
	};
	TrieNode *root;


public:
	Trie() { root = new TrieNode(); }
	~Trie() { makeEmpty(root); }

	void makeEmpty(TrieNode *&root)
	{
		if (root) {
			for (int i = 0; i < 26; ++i) {
				makeEmpty(root -> child[i]);
			}
			delete root;
			root = NULL;
		}
	}
	
	void insert(string & s)
	{
		TrieNode *p = root;
		int n = s.size();
		for (int i = 0; i < n; ++i) {
			int id = s[i] - 'A';
			if (!p -> child[id]) p -> child[id] = new TrieNode();
			p = p -> child[id];
		}
	}

	int calculate()
	{
		int cnt = 0;
		queue<TrieNode *> q;
		for (int i = 0; i < 26; ++i) {
			if (root -> child[i]) q.push(root -> child[i]);
		}

		while (!q.empty()) {
			TrieNode *tmp = q.front(); q.pop();
			++cnt;
			for (int i = 0; i < 26; ++i) {
				if (tmp -> child[i]) q.push(tmp -> child[i]);
			}
		}

		return cnt + 1; //root节点也算进去
	}

};


int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	Trie trie;
	string s;
	while (cin >> s) {
		trie.insert(s);
	}
	cout << trie.calculate() << endl;

	return 0;
}
```









# 可持久化字典树







典型题目：

- [x] LeetCode 208（模板题）
- [x] HDU 1251 统计难题（单词前缀统计）
- [x] 一本通-1337：【例3-2】单词查找树
- [ ] UVA 1401
- [x] HDU 1671 Phone List（单词查找树）
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





