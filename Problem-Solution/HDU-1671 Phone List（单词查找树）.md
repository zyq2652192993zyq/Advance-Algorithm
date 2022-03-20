> # HDU-1671 Phone List（单词查找树）

# Problem Description

Given a list of phone numbers, determine if it is consistent in the sense that no number is the prefix of another. Let’s say the phone catalogue listed these numbers:

```
1. Emergency 911
2. Alice 97 625 999
3. Bob 91 12 54 26
```

In this case, it’s not possible to call Bob, because the central would direct your call to the emergency line as soon as you had dialled the first three digits of Bob’s phone number. So this list would not be consistent.

# Input

The first line of input gives a single integer, 1 <= t <= 40, the number of test cases. Each test case starts with n, the number of phone numbers, on a separate line, 1 <= n <= 10000. Then follows n lines with one unique phone number on each line. A phone number is a sequence of at most ten digits.

# Output

For each test case, output “YES” if the list is consistent, or “NO” otherwise.

# Sample Input

```
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
```

# Sample Output

```
NO
YES
```

---

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

这个需要一个`vector`来存储输入量，最后遍历整个数组。没有办法一边输入一边检查，比如第一个测试用例，把911的位置放到最后，边输入边检查就会失效。