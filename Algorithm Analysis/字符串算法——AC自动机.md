> # 字符串算法-AC自动机

* 参考链接：https://www.cnblogs.com/Parsnip/p/12369642.html

**AC自动机的基本应用**

- [ ] UVA 1449 Dominating Patterns(AC自动机)：注意输入中有重复单词输入的情况。
- [x] HDU 2222 Keywords Search(AC自动机)：给你一个文本和多个单词，问你出现了多少个单词。注意单词可能会重复。
- [x] HDU 2896 病毒侵袭(AC自动机)：AC自动机基本应用。
- [ ] HDU 3065 病毒侵袭持续中(AC自动机)：AC自动机基本应用。
- [ ] ZOJ 3430 Detect the Virus(AC自动机+字符串转换)：本题麻烦在于匹配AC自动机之前需要先把64位编码转换为字符串。
- [ ] ZOJ 3228 Searching the String(AC自动机)：相同模板串不可重叠如何求最大出现次数？

**AC自动机+DP**

- [ ] UVA 11468 Substring(AC自动机+概率DP)：需要用改造后的AC自动机且注意概率dp的实现。
- [ ] POJ 2778 DNA Sequence(AC自动机+矩阵幂DP)：需要先用DP求出递推公式，然后找出递推矩阵，本题就是一个矩阵幂运算的题。
- [ ] HDU 2243 考研路茫茫——单词情结(AC自动机+矩阵幂)：POJ2778的加强版。
- [ ] POJ 1625 Censored!(AC自动机+DP)：类似POJ2778，不过不需要矩阵幂。
- [ ] HDU 2825 Wireless Password(AC自动机+状态压缩DP)：依然是生成字符串，但是这次要正好包含K个不同的模板单词。
- [ ] HDU 2296 Ring(AC自动机+DP): 注意match数组的值。
- [ ] HDU 2457 DNA repair(AC自动机+DP)：很巧妙的DP定义。
- [ ] HDU 3341 Lost's revenge(AC自动机+DP)：另类的状态压缩DP题，以后记得这么压缩状态。

 KMP算法专门解决**长文本的单模板匹配问题**，字典树专门解决**单个单词(短文本)多模板匹配问题**。而AC自动机解决的是**长文本的多模板匹配问题**。且AC自动机不但时间上具有优势，空间上也颇具优势。

**AC自动机*通配符匹配**

- [ ] HDU 3901

**Input**

```
2
sher
he
sher
5
she
he
say
shr
her
yasherhs
1
h
hhhh
```

**Program**

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
    int n;
    string s;
    while (cin >> n)
    {
        AC tree;
        while (n--)
        {
            cin >> s;
            tree.insert(s);
        }

        cin >> s;

        tree.buildFailPointer();
        cout << "共有 " << tree.ac_automaton(s) << " 个单词匹配" << endl;
    }

    return 0;
}
```

**Output**

```
共有 2 个单词匹配
共有 3 个单词匹配
共有 1 个单词匹配
```



