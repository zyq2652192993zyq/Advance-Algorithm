> # 树——Huffman树

参考资料：

* 《数据结构：思想与实现》

一般情况下，计算机采用的是ASCII编码，也就是等长的编码，每个字符的编码长度是相同的，但是有时为了提高存储和处理文本的效率，希望采用不等长的编码，使用频率比较高的字符有较短的编码，使用频率较小的有较长的编码（实际上就是一种压缩算法）。比如某段文字，只出现7个字符，空格用字母b来表示，换行用字母e来表示。

| 字符 | 编码 | 出现频率 | 占用空间 |
| :--: | :--: | :------: | :------: |
|  a   | 000  |    10    |    30    |
|  e   | 001  |    15    |    45    |
|  i   | 010  |    12    |    36    |
|  s   | 011  |    3     |    9     |
|  t   | 100  |    4     |    12    |
|  b   | 101  |    13    |    39    |
|  n   | 110  |    1     |    3     |

上表采用等长编码，需要$3\times(10+15+12+3+4+13+1)=174 bit$，但是采用不等长编码，如：

| 字符 | 编码  | 出现频率 | 占用空间 |
| :--: | :---: | :------: | :------: |
|  a   |  001  |    10    |    30    |
|  e   |  01   |    15    |    45    |
|  i   |  10   |    12    |    36    |
|  s   | 00000 |    3     |    9     |
|  t   | 0001  |    4     |    12    |
|  b   |  11   |    13    |    39    |
|  n   | 00001 |    1     |    3     |

更换了一种不等长的编码方式，则存储占用的空间是146`bit`，也就是说采用非等长编码可以减少存储的空间，自然就会引发一个问题，采取何种编码方式是最优的，也就是占用的存储空间最小。先构建哈夫曼树，再从哈夫曼树获得哈夫曼编码，这个编码就是最优编码。另外还有一个问题，有编码过程自然也需要解码过程，所以还存在一个如何将编码进行唯一解码的问题，比如a用0表示，e用00表示，如果传入一个编码后的序列00，可以得到的解码方案是aa或e，存在二义性，所以编码方案不能让解码过程出现歧义。

将需要编码的字符用完全二叉树来表示，叶节点表示需要编码的字符，如果字符$c_i$所在的深度为$L_i$，在文件出现的频率是$w_i$，则占据的存储量是$L_i \times w_i$，全部的存储量是$\sum L_i \times w_i$。

字符编码可以有不同的长度，只要每个字符的编码和其他字符的编码的前缀不同即可，这种编码称为**前缀编码**。采用二叉树进行编码的方式是可以保证没有二义性的，左子结点用0表示，右子节点用1表示。Huffman算法就是解决如何构建最优二叉树的算法。

算法步骤：

* 给定一个具有n个权值${w_1, w_2 \cdots w_n}$的结点的集合，构造一片森林$F={T_1, T_2 \cdots T_n}$，$F$中的每棵树都是只有树根结点的二叉树，$T_i$的权值是$w_i$。
* 初始时，设森林$A=F$
* 在$i = n-1$到$i=1$之间，每个循环里面，从当前森林里面选取权值最小和次小的两棵树，以这两棵树作为左右子树构建一颗新树，从森林中去除两个权值最小的树，将新树加入森林中。

构建哈夫曼树由于是用二叉树来存储，很容易想到采用例如`LeetCode`上很经典的`Node`来存储数据并构建，但是仔细分析发现，由于除了叶节点外其他结点的度数都为2，根据前面总结的二叉树的性质，可以知道，$n_0=n_2+1$，也就是只需$2n-1$的空间来存储，并且因为一开始就知道了需要对多少个字符进行编码，所以可以考虑采用数据这样连续内存存储的方式，而避免了频繁申请内存空间带来的开销。前面所举的例子的内存表示是：

```
value                               a   e   i   s   t   b   n
weight   0  58  33  25  18   8   4  10  15  12   3   4  13   1
parent   0   0   1   1   2   4   5   4   2   3   6   5   3   6
  left   0   3   8   9   5   6  13   0   0   0   0   0   0   0
 right   0   2   4  12   7  11  10   0   0   0   0   0   0   0
number   0   1   2   3   4   5   6   7   8   9  10  11  12  13
```

构建的具体程序见下面：


```c++
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

const int INF = 0x0ffffff;

template <typename T>
class HuffmanTree
{
private:
    struct Node
    {
        T data;
        int weight;
        int parent, left, right;
    };

    vector<Node> sequence;

public:
    HuffmanTree(vector<T> & v, vector<int> & w)
    {
        int n = v.size();
        sequence.resize(2 * n);
        for (int i = n; i < 2 * n; ++i) {
            sequence[i].data = v[i - n];
            sequence[i].weight = w[i - n];
        }

        for (int i = n - 1; i > 0; --i) {
            int min1 = INF, min2 = INF; //用来记录最小的权值和次小的权值
            int pos1 = 0, pos2 = 0;
            for (int j = i + 1; j < 2 * n; ++j) {
                if (sequence[j].parent == 0) {
                    if (sequence[j].weight < min1) {
                        min2 = min1;
                        min1 = sequence[j].weight;
                        pos2 = pos1;
                        pos1 = j;
                    }
                    else if (sequence[j].weight < min2) {
                        min2 = sequence[j].weight;
                        pos2 = j;
                    }
                }
            }
            sequence[i].weight = min1 + min2;
            sequence[i].left = pos1;
            sequence[i].right = pos2;
            sequence[pos1].parent = sequence[pos2].parent = i;
        }
        //哈夫曼树在内存中的表示
        int m = sequence.size();
        cout << setw(6) << "value";
        for (int i = 0; i < n; ++i) cout << setw(4) << "    ";
        for (int i = n; i < m; ++i) cout << setw(4) << sequence[i].data;
        cout << endl;
        
        cout << setw(6) << "weight";
        for (int i = 0; i < m; ++i) cout << setw(4) << sequence[i].weight;
        cout << endl;
        
        cout << setw(6) << "parent";
        for (int i = 0; i < m; ++i) cout << setw(4) << sequence[i].parent;
        cout << endl;
        
        cout << setw(6) << "left";
        for (int i = 0; i < m; ++i) cout << setw(4) << sequence[i].left;
        cout << endl;
        
        cout << setw(6) << "right";
        for (int i = 0; i < m; ++i) cout << setw(4) << sequence[i].right;
        cout << endl;
        
        cout << setw(6) << "number";
        for (int i = 0; i < m; ++i) cout << setw(4) << i;
        cout << endl;
    }

    vector<string> getCode()
    {
        int n = sequence.size() / 2;
        vector<string> res(n);
        for (int i = n; i < 2 * n; ++i) {
            string tmp;
            int cur = i;
            int p = sequence[cur].parent;
            while (p != 0) {
                if (sequence[p].left == cur) tmp.push_back('0');
                else tmp.push_back('1');
                cur = p;
                p = sequence[cur].parent;
            }
            reverse(tmp.begin(), tmp.end());
            res[i - n] = tmp;
        }

        return res;
    }

    vector<T> decode(string & str, vector<string> & code)
    {
        vector<T> res;
        string tmp;
        int n = sequence.size() / 2;

        for (size_t i = 0; i < str.size(); ++i) {
            tmp.push_back(str[i]);
            for (int j = 0; j < n; ++j) {
                if (tmp == code[j]) {
                    res.push_back(sequence[n + j].data);
                    tmp = "";
                    break;
                }
                else if (i == str.size() - 1 && j == n - 1 && tmp != "") {
                    cout << "decode error!" << endl;
                    return vector<T>();
                }
            }
        }
        return res;
    }

    ~HuffmanTree() = default;
};

template <typename T>
ostream & operator<<(ostream & os, const vector<T> & v)
{
    for (const T & e : v) os << setw(8) << e;
    os << endl;
    return os;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<char> v = {'a', 'e', 'i', 's', 't', 'b', 'n'};
    vector<int> w = {10, 15, 12, 3, 4, 13, 1};

    HuffmanTree<char> tree(v, w);
    cout << v;
    vector<string> code = tree.getCode();
    cout << code; //编码后的结果

    string str; //期望的结果是nbbiea，按照上面编码结果进行编码
    cin >> str; //输入为1100001010010111
    cout << tree.decode(str, code); //验证是否正确解码
    
    return 0;
}
```

```
value                               a   e   i   s   t   b   n
weight   0  58  33  25  18   8   4  10  15  12   3   4  13   1
parent   0   0   1   1   2   4   5   4   2   3   6   5   3   6
  left   0   3   8   9   5   6  13   0   0   0   0   0   0   0
 right   0   2   4  12   7  11  10   0   0   0   0   0   0   0
number   0   1   2   3   4   5   6   7   8   9  10  11  12  13
       a       e       i       s       t       b       n
     111      10      00   11001    1101      01   11000
       n       b       b       i       e       a
```

程序的56-81行其实并不需要，这么做只是为了更加清晰地去了解整个编码地过程，以及可以作为验证程序地一个方法。实际编写程序时可以把输出内存表示地部分删去。

==Huffman算法地正确性需要参照《算法导论》里的证明==

典型题目可以参照《挑战程序设计竞赛》笔记里总结的习题。

可以让解码的速度更快，就是利用前缀树将编码后的结果用一棵二叉树表示，这样查询效率更高。