> # HDU-2896 病毒侵袭（AC自动机）

# Problem Description

当太阳的光辉逐渐被月亮遮蔽，世界失去了光明，大地迎来最黑暗的时刻。。。。在这样的时刻，人们却异常兴奋——我们能在有生之年看到500年一遇的世界奇观，那是多么幸福的事儿啊~~
但网路上总有那么些网站，开始借着民众的好奇心，打着介绍日食的旗号，大肆传播病毒。小t不幸成为受害者之一。小t如此生气，他决定要把世界上所有带病毒的网站都找出来。当然，谁都知道这是不可能的。小t却执意要完成这不能的任务，他说：“子子孙孙无穷匮也！”（愚公后继有人了）。
万事开头难，小t收集了好多病毒的特征码，又收集了一批诡异网站的源码，他想知道这些网站中哪些是有病毒的，又是带了怎样的病毒呢？顺便还想知道他到底收集了多少带病毒的网站。这时候他却不知道何从下手了。所以想请大家帮帮忙。小t又是个急性子哦，所以解决问题越快越好哦~~

# Input

第一行，一个整数N（1<=N<=500），表示病毒特征码的个数。
接下来N行，每行表示一个病毒特征码，特征码字符串长度在20—200之间。
每个病毒都有一个编号，依此为1—N。
不同编号的病毒特征码不会相同。
在这之后一行，有一个整数M（1<=M<=1000），表示网站数。
接下来M行，每行表示一个网站源码，源码字符串长度在7000—10000之间。
每个网站都有一个编号，依此为1—M。
以上字符串中字符都是ASCII码可见字符（不包括回车）。

# Output

依次按如下格式输出按网站编号从小到大输出，带病毒的网站编号和包含病毒编号，每行一个含毒网站信息。
web 网站编号: 病毒编号 病毒编号 …
冒号后有一个空格，病毒编号按从小到大排列，两个病毒编号之间用一个空格隔开，如果一个网站包含病毒，病毒数不会超过3个。
最后一行输出统计信息，如下格式
total: 带病毒网站数
冒号后有一个空格。

# Sample Input

```
3
aaa
bbb
ccc
2
aaabbbccc
bbaacc
```

# Sample Output

```
web 1: 1 2 3
total: 1
```

---

```c++
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int num = 0;

struct Node
{
    int end;
    bool isVisited;
    Node * fail;
    Node * child[130];

    Node() : end(0), isVisited(false), fail(nullptr)
    {
        for (int i = 0; i < 130; i++)
            child[i] = nullptr;
    }

    Node(int End, Node * &Fail, bool visit)
    : end(End), isVisited(visit), fail(Fail)
    {
        for (int i = 0; i < 130; i++)
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
        for (int i = 0; i < 130; i++)
            if (t -> child[i])
                remove(t -> child[i]);
        delete t;
        t = nullptr;
    }

    void insert(string  &s)
    {
        Node * t = root;
        for (size_t i = 0; i < s.size(); ++i){
            int id = s[i];
            if (!t -> child[id]){
                t -> child[id] = new Node();
            }
            t = t -> child[id];
        }
        t -> end = ++num;
    }

    void buildFailPointer()
    {
        queue<Node*> Q;

        for (int i = 0; i < 130; i++)
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
            for (int i = 0; i < 130; i++)
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

    vector<int> ac_automaton(string &s)
    {
        int i = 0;
        vector<int> ans;
        queue<Node*> state;
        Node * pre = root;

        while (s[i] != '\0'){
            //int id = s[i] - 'a';
            int id = s[i];
            if (pre -> child[id]){
                Node * cur = pre -> child[id];
                while (cur != root) {
                    if (!cur -> isVisited){
                        if (cur -> end) ans.push_back(cur -> end);
                        cur -> isVisited = true;
                        state.push(cur); //记录状态改变的节点
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
        sort(ans.begin(), ans.end());

        //恢复被改变节点的状态
        while (!state.empty()){
            Node * tmp = state.front();
            tmp -> isVisited = false;
            state.pop();
        }

        return ans;
    }
};

ostream & operator<<(ostream & os, vector<int> &v)
{
    for (auto e : v)
        os << e << " ";

    return os; 
}


int main()
{
    int n;
    string s;
    AC acTree;
    cin >> n;

    while (n--){
        cin >> s;
        acTree.insert(s);
    }
    acTree.buildFailPointer();

    int m, caseNum = 0, sum = 0;
    cin >> m;

    while (m--){
        ++caseNum;
        cin >> s;
        
        vector<int> virus = acTree.ac_automaton(s);
        if (!virus.empty()){
            cout << "web " << caseNum << ": " << virus << endl;
            ++sum;
        }
        
    }
    cout << "total: " << sum << endl;

    return 0;
}
```

题目很容易看完想到AC自动机，但是需要在模板上进行修改。

首先模板AC自动机是一个长文本多个匹配模板，而本题是多个匹配模板，多个文本。每执行一次`acTree.ac_automaton(s)`，我们所构造的树结构里的部分信息就改变了，再一次执行前需要恢复原始状态。

恢复状态两种思路：1 写一个复制构造函数，复制执行完`acTree.buildFailPointer()`后的树结构；2. 在执行`acTree.ac_automaton(s)`时记录哪些节点状态改变了，在函数内部就直接恢复。显然第一种时间开销较大，选第二种，利用一个队列存储被改变状态的节点，增加了一个`bool isVisited`来记录当前节点是否被访问过，避免重复访问，`end`则用来记录下标。

另外就是注意一些细节：

* 题目并没有说全是小写字母，所以数组开多大需要注意。
* 输出病毒序号注意最后一个后面没有空格，否则会`Presentation Error`
* 病毒按升序排列，记得返回`ans`前要调用`sort`。