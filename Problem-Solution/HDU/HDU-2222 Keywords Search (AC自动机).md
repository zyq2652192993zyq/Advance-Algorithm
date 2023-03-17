> # HDU-2222 Keywords Search (AC自动机)

# Problem Description

In the modern time, Search engine came into the life of everybody like Google, Baidu, etc.
Wiskey also wants to bring this feature to his image retrieval system.
Every image have a long description, when users type some keywords to find the image, the system will match the keywords with description of image and show the image which the most keywords be matched.
To simplify the problem, giving you a description of image, and some keywords, you should tell me how many keywords will be match.

# Input

First line will contain one integer means how many cases will follow by.
Each case will contain two integers N means the number of keywords and N keywords follow. (N <= 10000)
Each keyword will only contains characters 'a'-'z', and the length will be not longer than 50.
The last line is the description, and the length will be not longer than 1000000.

# Output

Print how many keywords are contained in the description.

# Sample Input

```
1
5
she
he
say
shr
her
yasherhs
```

# Sample Output

```
3
```

----

```c++
#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct Node
{
    int end;
    Node * fail;
    Node * child[26];
    Node() : end(0), fail(nullptr)
    {
        for (int i = 0; i < 26; i++)
            child[i] = nullptr;
    }
};

class AC
{
private:
    Node * root;

public:
    AC()
    {
        root = new Node();
    }

    ~AC()
    {
        remove(root);
        root = nullptr;
    }

    void remove(Node * &t)
    {
        for (int i = 0; i < 26; i++)
            if (t -> child[i])
                remove(t -> child[i]);
        delete t;
        t = nullptr;
    }

    void insert(string  &s)
    {
        Node * t = root;
        for (size_t i = 0; i < s.size(); ++i){
            int id  = s[i] - 'a';
            if (!t -> child[id]){
                t -> child[id] = new Node();
            }
            t = t -> child[id];
        }
        ++(t -> end);
    }

    void buildFailPointer()
    {
        queue<Node*> Q;

        for (int i = 0; i < 26; i++)
        {
            if (root -> child[i])
            {
                Q.push(root -> child[i]);
                root -> child[i] -> fail = root;
            }
        }

        while (!Q.empty())
        {
            Node * parent = Q.front();
            Q.pop();
            for (int i = 0; i < 26; i++)
            {
                if (parent -> child[i])
                {
                    Q.push(parent -> child[i]);
                    Node * son = parent -> child[i];
                    Node * p = parent -> fail;
                    while (p) // 沿着它的父亲结点的 fail 指针走
                    {
                        if (p -> child[i])
                        {
                            son -> fail = p -> child[i];
                            break;
                        }
                        p = p -> fail;
                    }

                    // 走到了根结点都没找到
                    if (!p)
                        son -> fail = root;
                }
            }
        }
    }

    int ac_automaton(string &s)
    {
        int ans = 0, i = 0;
        Node * pre = root;

        while (s[i] != '\0'){
            int id = s[i] - 'a';
            if (pre -> child[id]){
                Node * cur = pre -> child[id];
                while (cur != root) {
                    if (cur -> end >= 0) {
                        ans += cur -> end;
                        cur -> end = -1;  // 避免重复查找
                    }
                    else
                        break;  // 等于 -1 说明以前这条路径已找过，现在无需再找
                    cur = cur -> fail;
                }
                pre = pre -> child[id];
                ++i;
            }
            else{
                if (pre == root)
                    ++i;
                else
                    pre = pre -> fail;
            }  
        }

        return ans;
    }
};


int main()
{
    int caseNum;
    cin >> caseNum;

    while (caseNum--) {
        int n;
        cin >> n;

        string s;
        AC acTree;
        while (n--){
            cin >> s;
            acTree.insert(s);
        }

        cin >> s;

        acTree.buildFailPointer();
        cout << acTree.ac_automaton(s) << endl;
    }

    return 0;
}
```

模板题目