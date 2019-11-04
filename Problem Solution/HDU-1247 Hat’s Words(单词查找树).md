> # HDU-1247 Hat’s Words(单词查找树)

# Problem Description

A hat’s word is a word in the dictionary that is the concatenation of exactly two other words in the dictionary.
You are to find all the hat’s words in a dictionary.

# Input

Standard input consists of a number of lowercase words, one per line, in alphabetical order. There will be no more than 50,000 words.
Only one case.

# Output

Your output should contain all the hat’s words, one per line, in alphabetical order.

# Sample Input

```
a
ahat
hat
hatword
hziee
word
```

# Sample Output

```
ahat
hatword
```

---

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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
	vector<string> store;
	Trie trie;
	string inputStr;

	while(cin >> inputStr){
		trie.insert(inputStr);
		store.push_back(inputStr);
	}

	for (size_t i = 0; i < store.size(); ++i){
		for (size_t j = 1; j < store[i].size(); ++j){
			string tmp1 = store[i].substr(0, j);
			string tmp2 = store[i].substr(j, store[i].size());
			if (trie.search(tmp1) && trie.search(tmp2)){
				cout << store[i] << endl;
				break;
			} 
		}
	}
	
    return 0;
}
```

查找单词的思路是顺序遍历数组中的每个单词，将每个单词拆分成两个单词并进行查找，只要找到一个就跳出内层循环并输出，但是此代码一直得到`Wrong Answer`