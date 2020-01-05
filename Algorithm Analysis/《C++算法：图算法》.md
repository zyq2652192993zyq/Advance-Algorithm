> # 《C++算法：图算法》

[TOC]

OJ题目分类：

POJ ：<https://blog.csdn.net/cfzjxz/article/details/8476066>

HDU：<https://www.cnblogs.com/13224ACMer/p/4822852.html>

# 第一章 图的属性和类型

## 1.3 邻接矩阵表示

```c++
#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class DenseGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;
    vector <vector<bool>> adj;

public:
    DenseGRAPH(int V, bool digraph = false) : Vcnt(V), Ecnt(0), digraph(digraph), adj(V)
    { 
        for (int i = 0; i < V; i++) 
            adj[i].assign(V, false);
    }
 
    int V() const { return Vcnt; }

    int E() const { return Ecnt; }

    bool directed() const { return digraph; }

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == false) Ecnt++;
        adj[v][w] = true;
        if (!digraph) adj[w][v] = true; 
    } 

    void remove(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == true) Ecnt--;
        adj[v][w] = false;
        if (!digraph) adj[w][v] = false; 
    } 

    bool edge(int v, int w) const 
    { return adj[v][w]; }
    
    class adjIterator;
    friend class adjIterator;
};

class DenseGRAPH::adjIterator
{ 
    const DenseGRAPH &G;
    int i, v;
    
public:
    adjIterator(const DenseGRAPH &G, int v) : G{G}, i{-1}, v{v} { }
  
    int beg()
    { 
        i = -1; 
        return nxt(); 
    }

    int nxt()
    {
        for (i++; i < G.V(); i++)
            if (G.adj[v][i] == true) return i;
        return -1;
    }

    bool end()
    { return i >= G.V(); }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

int main()
{
    DenseGRAPH g{3};
    g.insert(Edge(0, 1));
    g.insert(Edge(0, 2));
    g.insert(Edge(1, 2));

    show(g);
}
```



## 1.4 邻接表表示和链式前向星

```c++
#include <iomanip>
#include <vector>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class SparseMultiGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;

    struct node
    { 
        int v; node* next;

        node(int x, node* t = nullptr): v{x}, next{t} {}
    };

    typedef node* link;
    vector<link> adj;

public:
    SparseMultiGRAPH(int V, bool digraph = false): Vcnt(V), Ecnt(0), digraph(digraph)
    {adj.assign(V, 0);}

    int V() const {return Vcnt;}

    int E() const {return Ecnt;}

    bool directed() const {return digraph;}

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        adj[v] = new node(w, adj[v]);
        if (!digraph) adj[w] = new node(v, adj[w]); 
        Ecnt++;
    } 

    class adjIterator;
    friend class adjIterator;
};

class SparseMultiGRAPH::adjIterator
{ 
    const SparseMultiGRAPH &G;
    int v;
    link t;

public:
    adjIterator(const SparseMultiGRAPH &G, int v) : G{G}, v{v}, t{0} {}
  
    int beg()
    { 
        t = G.adj[v]; 

        return t ? t->v : -1; 
    }

    int nxt()
    { 
        if (t) t = t->next; 

        return t ? t->v : -1; 
    }

    bool end()
    { 
        return t == 0; 
    }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

int main()
{
    SparseMultiGRAPH g{3};
    g.insert(Edge(0, 1));
    g.insert(Edge(0, 2));
    g.insert(Edge(1, 2));

    show(g);
}
```



## 1.5 变化、拓展和开销

```c++
//定点度类的实现及应用
#include <iomanip>
#include <vector>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class SparseMultiGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;

    struct node
    { 
        int v; 
        node* next;

        node(int x, node* t = nullptr): v{x}, next{t} {}
    };

    typedef node* link;
    vector<link> adj;

public:
    SparseMultiGRAPH(int V, bool digraph = false): Vcnt(V), Ecnt(0), digraph(digraph)
    {adj.assign(V, 0);}

    int V() const {return Vcnt;}

    int E() const {return Ecnt;}

    bool directed() const {return digraph;}

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        adj[v] = new node(w, adj[v]);
        if (!digraph) adj[w] = new node(v, adj[w]); 
        Ecnt++;
    } 

    class adjIterator;
    friend class adjIterator;
};

class SparseMultiGRAPH::adjIterator
{ 
    const SparseMultiGRAPH &G;
    int v;
    link t;

public:
    adjIterator(const SparseMultiGRAPH &G, int v) : G{G}, v{v}, t{0} {}
  
    int beg()
    { 
        t = G.adj[v]; 

        return t ? t->v : -1; 
    }

    int nxt()
    { 
        if (t) t = t->next; 

        return t ? t->v : -1; 
    }

    bool end()
    { 
        return t == 0; 
    }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

template <class Graph> 
class DEGREE
{ 
    const Graph &G;
    vector <int> degree; 

public:
    DEGREE(const Graph &G) : G(G), degree(G.V(), 0) 
    { 
        for (int v = 0; v < G.V(); v++)
        { 
            typename Graph::adjIterator A(G, v);

            for (int w = A.beg(); !A.end(); w = A.nxt()) 
                ++degree[v];
         }
    }

    int operator[](int v) const 
    { 
        return degree[v]; 
    }
};

int main()
{
    SparseMultiGRAPH g{3};
    g.insert(Edge(0, 1));
    //g.insert(Edge(0, 2));
    g.insert(Edge(1, 2));
    
    DEGREE deg(g);
    cout << deg[1] << endl;

    show(g);
}
```



## 1.6 图生成器

随机边通常应用于稀疏图。

随机图通常应用于稠密图。



## 1.7 简单路径、欧拉路径和哈密顿路径

## 17.1 哈密顿路径

**哈密顿周游路径**（Hamilton tour problem）：给定两个顶点，是否存在一条简单的路径，而且路径访问了途中的每个顶点一次，最后回到出发点。

此问题是NP完全问题（证明参见《算法导论》），其理论分析可以参考《组合学与图论》的第十一章。从中可以得到哈密顿图的充分条件。

典型题目：

- [x] 哈密顿绕行世界问题：HDU 2181

Travelling：HDU 3001(宽搜)

King Arthur's Knights：HDU 4337

Children's Dining：POJ 2438

Granny's Bike： ZOJ 1798

POJ 1776 竞赛图转哈密顿路径







## 17.2 欧拉路径

欧拉周游路径：是否存在一条路径连接了两个给定的顶点，同时用到图中的每一条边一次并且仅有一次，最后回到出发点。

理论分析可以参考《组合学与图论》的第十一章。相关联的算法是**Fleury算法**。

典型题目：

- [x] John's trip：POJ 1041
- [ ] The Necklace: UVa 10054
- [ ] Play on Words: Uva 10129
- [ ] POJ 2513 Colored Sticks（欧拉回路 + 字典树 + 并查集）
- [ ] POJ 1300 Door Man（有向图的欧拉回路）

《算法竞赛入门经典》111页的6.4.4节。

LeetCode 332.Reconstruct Itinerary

Frogs: HDU 5514 （相当于青蛙跳环）

<https://blog.csdn.net/HuangXinyue1017/article/details/80835350>

- [ ] Watchcow（双向欧拉回路）：POJ 2230

Door Man: POJ 1300

POJ 1386, 2337, 

HDU 6311（无向图+欧拉路径）, 5883, 1116, 5348(竞赛图+欧拉路径) 

- [x] HDU-1878（最基本的欧拉回路判断）
- [ ] HDU 3018 Ant Trip 欧拉回路一笔画问题



## 17.3 简单路径搜索

```c++
template <class Graph> 
class sPATH
{ 
    const Graph &G;
    vector<bool> visited;
    bool found; 

    bool searchR(int v, int w)
    { 
        if (v == w) return true;
        visited[v] = true;
        typename Graph::adjIterator A(G, v);

        for (int t = A.beg(); !A.end(); t = A.nxt()){
            if (!visited[t])
                if (searchR(t, w)) return true;
        } 
            
        return false;
    }

public:
    sPATH(const Graph &G, int v, int w): 
    G(G), visited(G.V(), false) 
    { found = searchR(v, w); }

    bool exists() const 
    { 
        return found; 
    }
};
```

典型题目：

八皇后问题：《C++程序设计思想与方法》

棋盘问题+<https://www.luogu.org/problem/P1548>(暴力枚举)



# 第二章 图搜索

 ## 2.5 DFS算法

###无向图的连通性

这里我们用邻接矩阵作为图的存储结构。

![](F:\学习笔记\c++\算法总结\assets\1567931991914.png)

```c++
#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class DenseGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;
    vector <vector<bool>> adj;

public:
    DenseGRAPH(int V, bool digraph = false) : Vcnt(V), Ecnt(0), digraph(digraph), adj(V)
    { 
        for (int i = 0; i < V; i++) 
            adj[i].assign(V, false);
    }

    int V() const { return Vcnt; }

    int E() const { return Ecnt; }

    bool directed() const { return digraph; }

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == false) Ecnt++;
        adj[v][w] = true;
        if (!digraph) adj[w][v] = true; 
    } 

    void remove(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == true) Ecnt--;
        adj[v][w] = false;
        if (!digraph) adj[w][v] = false; 
    } 

    bool edge(int v, int w) const 
    { return adj[v][w]; }
    
    class adjIterator;
    friend class adjIterator;
};

class DenseGRAPH::adjIterator
{ 
    const DenseGRAPH &G;
    int i, v;
    
public:
    adjIterator(const DenseGRAPH &G, int v) : G{G}, i{-1}, v{v} { }
  
    int beg()
    { 
        i = -1; 
        return nxt(); 
    }

    int nxt()
    {
        for (i++; i < G.V(); i++)
            if (G.adj[v][i] == true) return i;
        return -1;
    }

    bool end()
    { return i >= G.V(); }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

//检查图的连通性的类
template <class Graph> 
class CC
{ 
    const Graph &G;
    int ccnt;  //统计连通分量的个数
    vector <int> id; //用来记录连通分量的起始点

    void ccR(int w)
    { 
        id[w] = ccnt;
        typename Graph::adjIterator A(G, w);

        for (int v = A.beg(); !A.end(); v = A.nxt()) 
            if (id[v] == -1) ccR(v);
    }

public:
    CC(const Graph &G) : G{G}, ccnt{0}, id(G.V(), -1) 
    { 
        for (int v = 0; v < G.V(); v++)
            if (id[v] == -1){ 
                ccR(v); 
                ccnt++; 
            } 
    }

    int count() const { return ccnt; }

    bool connect(int s, int t) const 
    { 
        return id[s] == id[t]; 
    }
};

int main()
{
    DenseGRAPH g{13};
    g.insert(Edge(0, 1));
    g.insert(Edge(1, 9));
    g.insert(Edge(9, 0));
    g.insert(Edge(1, 4));
    
    g.insert(Edge(11, 8));
    
    g.insert(Edge(10, 6));
    g.insert(Edge(10, 2));
    g.insert(Edge(10, 7));
    g.insert(Edge(7, 2));
    g.insert(Edge(2, 12));
    g.insert(Edge(6, 12));
    g.insert(Edge(12, 3));
    g.insert(Edge(12, 5));
    
    CC<DenseGRAPH> m(g);
    cout << m.count() << endl;
    cout << m.connect(0,10) << " "
    << m.connect(0,11) << " "
    << m.connect(0,4) << endl;

    show(g);
}
```

```shell
# run result
3
0 0 1
 0: 1  9 
 1: 0  4  9 
 2: 7 10 12 
 3:12 
 4: 1 
 5:12 
 6:10 12 
 7: 2 10 
 8:11 
 9: 0  1 
10: 2  6  7 
11: 8 
12: 2  3  5  6 
```

OJ题目练习：SWUST OJ-1065 无向图的连通分量计算

###双向欧拉周游路径

![](F:\学习笔记\c++\算法总结\assets\1567931991914.png)

```c++
#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class DenseGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;
    vector <vector<bool>> adj;

public:
    DenseGRAPH(int V, bool digraph = false) : Vcnt(V), Ecnt(0), digraph(digraph), adj(V)
    { 
        for (int i = 0; i < V; i++) 
            adj[i].assign(V, false);
    }

    int V() const { return Vcnt; }

    int E() const { return Ecnt; }

    bool directed() const { return digraph; }

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == false) Ecnt++;
        adj[v][w] = true;
        if (!digraph) adj[w][v] = true; 
    } 

    void remove(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == true) Ecnt--;
        adj[v][w] = false;
        if (!digraph) adj[w][v] = false; 
    } 

    bool edge(int v, int w) const 
    { return adj[v][w]; }
    
    class adjIterator;
    friend class adjIterator;
};

class DenseGRAPH::adjIterator
{ 
    const DenseGRAPH &G;
    int i, v;
    
public:
    adjIterator(const DenseGRAPH &G, int v) : G{G}, i{-1}, v{v} { }
  
    int beg()
    { 
        i = -1; 
        return nxt(); 
    }

    int nxt()
    {
        for (i++; i < G.V(); i++)
            if (G.adj[v][i] == true) return i;
        return -1;
    }

    bool end()
    { return i >= G.V(); }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

template <class Graph> 
class CC
{ 
    const Graph &G;
    int ccnt;  //统计连通分量的个数
    vector <int> id; //用来记录连通分量的起始点

    void ccR(int w)
    { 
        id[w] = ccnt;
        typename Graph::adjIterator A(G, w);

        for (int v = A.beg(); !A.end(); v = A.nxt()) 
            if (id[v] == -1) ccR(v);
    }

public:
    CC(const Graph &G) : G{G}, ccnt{0}, id(G.V(), -1) 
    { 
        for (int v = 0; v < G.V(); v++)
            if (id[v] == -1){ 
                ccR(v); 
                ccnt++; 
            } 
    }

    int count() const { return ccnt; }

    bool connect(int s, int t) const 
    { 
        return id[s] == id[t]; 
    }
};

template <class Graph> 
class SEARCH
{
protected:
    const Graph &G;
    vector<int> ord;
    int cnt;

    virtual void searchC(Edge) = 0;

    void search()
    { 
        for (int v = 0; v < G.V(); v++)
          if (ord[v] == -1) searchC(Edge(v, v)); 
    }

public:
    SEARCH (const Graph &G) : G(G), ord(G.V(), -1), cnt(0) { }
    
    int operator[](int v) const { return ord[v]; }
};

template <class Graph> 
class EULER : public SEARCH<Graph> 
{ 
    void searchC(Edge e)
    { 
        int v = e.v, w = e.w;
        (this -> ord)[w] = (this -> cnt)++;

        cout << "-" << w; 

        typename Graph::adjIterator A(this -> G, w);

        for (int t = A.beg(); !A.end(); t = A.nxt()){
            if ((this -> ord)[t] == -1) 
                searchC(Edge(w, t));
            else if ((this -> ord)[t] < (this -> ord)[v])
                cout << "-" << t << "-" << w;
        }  
         
        if (v != w) cout << "-" << v; 
        else cout << endl;  
  }

public:
    EULER(const Graph &G) : SEARCH<Graph>(G) { this -> search(); }
};

int main()
{
    DenseGRAPH g{13};
    g.insert(Edge(0, 1));
    g.insert(Edge(1, 9));
    g.insert(Edge(9, 0));
    g.insert(Edge(1, 4));
    
    g.insert(Edge(11, 8));
    
    g.insert(Edge(10, 6));
    g.insert(Edge(10, 2));
    g.insert(Edge(10, 7));
    g.insert(Edge(7, 2));
    g.insert(Edge(2, 12));
    g.insert(Edge(6, 12));
    g.insert(Edge(12, 3));
    g.insert(Edge(12, 5));
    
    
    CC<DenseGRAPH> m(g);
    cout << m.count() << endl;
    cout << m.connect(0,10) << " "
    << m.connect(0,11) << " "
    << m.connect(0,4) << endl;
    
    cout << "-----------------------" << endl;
    
    EULER<DenseGRAPH> eu(g);

    cout << "-----------------------" << endl;

    show(g);
}
```

```shell
# run result
3
0 0 1
-----------------------
-0-1-4-1-9-0-9-1-0
-2-7-10-2-10-6-12-2-12-3-12-5-12-6-10-7-2
-8-11-8
-----------------------
 0: 1  9 
 1: 0  4  9 
 2: 7 10 12 
 3:12 
 4: 1 
 5:12 
 6:10 12 
 7: 2 10 
 8:11 
 9: 0  1 
10: 2  6  7 
11: 8 
12: 2  3  5  6 

```

### 2-着色性

以下问题等价：

* 是否存在方法可以将一个图中每个顶点指定为两种颜色中的一种，且不存在连接两个相同颜色的顶点的边。
* 一个给定的图是否是二部图。
* 一个给定的图是否存在长度为奇数的环。

典型题目：

- [x] UVa 110901/10004

## 2.6 可分离性与重连通性

本节所讲的**边连通分量**和**点连通分量**总结下来就是**双连通分量**。求双连通分量可用`Tarjan`算法。

**分离边**是指，如果删除这条边就能把一个连通图分解为不相交的两个子图。没有可分离边的图称为**边连通图**。

将一个不是边连通的图称为**边可分离图**。

![1569050531804](F:\学习笔记\c++\算法总结\assets\1569050531804.png)

```c++
#include <iostream>
#include <vector>

using namespace std;

#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class DenseGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;
    vector <vector<bool>> adj;

public:
    DenseGRAPH(int V, bool digraph = false) : Vcnt(V), Ecnt(0), digraph(digraph), adj(V)
    { 
        for (int i = 0; i < V; i++) 
            adj[i].assign(V, false);
    }

    int V() const { return Vcnt; }

    int E() const { return Ecnt; }

    bool directed() const { return digraph; }

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == false) Ecnt++;
        adj[v][w] = true;
        if (!digraph) adj[w][v] = true; 
    } 

    void remove(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == true) Ecnt--;
        adj[v][w] = false;
        if (!digraph) adj[w][v] = false; 
    } 

    bool edge(int v, int w) const 
    { return adj[v][w]; }
    
    class adjIterator;
    friend class adjIterator;
};

class DenseGRAPH::adjIterator
{ 
    const DenseGRAPH &G;
    int i, v;
    
public:
    adjIterator(const DenseGRAPH &G, int v) : G{G}, i{-1}, v{v} { }
  
    int beg()
    { 
        i = -1; 
        return nxt(); 
    }

    int nxt()
    {
        for (i++; i < G.V(); i++)
            if (G.adj[v][i] == true) return i;
        return -1;
    }

    bool end()
    { return i >= G.V(); }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

template <class Graph> 
class SEARCH
{
protected:
    const Graph &G;
    int cnt;
    vector <int> ord;
    virtual void searchC(Edge) = 0;

    void search()
    { 
        for (int v = 0; v < G.V(); v++)
            if (ord[v] == -1) searchC(Edge(v, v)); 
    }

public:
    SEARCH (const Graph &G) : G(G), cnt(0), ord(G.V(), -1)  { }

    int operator[](int v) const { return ord[v]; }
};

template <class Graph> 
class EC : public SEARCH<Graph> 
{ 
    int bcnt;
    vector <int> low; 

    void searchC(Edge e)
    { 
        int w = e.w;
        (this -> ord)[w] = (this -> cnt)++; low[w] = (this -> ord)[w];
        typename Graph::adjIterator A((this -> G), w);

        for (int t = A.beg(); !A.end(); t = A.nxt()){
            if ((this -> ord)[t] == -1) {
                searchC(Edge(w, t));
                if (low[w] > low[t]) low[w] = low[t];
                if (low[t] == (this -> ord)[t]){ 
                    bcnt++; // w-t is a bridge
                    cout << w << "-" << t << endl;
                }
            }
            else if (t != e.v){
                if (low[w] > (this -> ord)[t]) low[w] = (this -> ord)[t]; 
            }
        } 
    }

public:
    EC(const Graph &G) : SEARCH<Graph>(G), bcnt(0), low(G.V(), -1)
    { this -> search(); }

    int count() const { return bcnt+1; }
};

int main()
{
    DenseGRAPH g{13};
    g.insert(Edge(0, 1));
    g.insert(Edge(1, 2));
    g.insert(Edge(2, 6));
    g.insert(Edge(0, 6));
    g.insert(Edge(7, 6));
    g.insert(Edge(7, 8));
    g.insert(Edge(8, 10));
    g.insert(Edge(7, 10));
    g.insert(Edge(0, 5));
    g.insert(Edge(5, 3));
    g.insert(Edge(3, 4));
    g.insert(Edge(4, 5));
    g.insert(Edge(4, 9));
    g.insert(Edge(4, 11));
    g.insert(Edge(9, 11));
    g.insert(Edge(11, 12));

    show(g);
    cout << endl;

    EC m(g);
    cout << m.count() << endl;

    return 0;
}
```

```shell
# run result
 0: 1  5  6 
 1: 0  2 
 2: 1  6 
 3: 4  5 
 4: 3  5  9 11 
 5: 0  3  4 
 6: 0  2  7 
 7: 6  8 10 
 8: 7 10 
 9: 4 11 
10: 7  8 
11: 4  9 12 
12:11 

6-7
11-12
0-5
4
```

对于这段代码，应该在此之前思考几个问题：

* 如何判断一个无向图是否有环？

这个可以通过点和边的关系来判断，N个点对应N-1条边，如果边的数量超过N-1则必有环。

* 一个无向图有环的情况下，存在几个环？（环套树or基环树 算法，归属于动态规划，如BZOJ 1040）
* 无向图中的环，最大的环的边数是多少，最小的环的边数是多少？（POJ 3895）
* 面对一张无向连通图，最少添加多少条边，使得任意两点之间有两条五公共边的路（可以有公共点）POJ 3352

第八届蓝桥杯决赛 发现环<https://blog.csdn.net/CillyB/article/details/72802229>

Codeforces 11D A Simple Task 统计简单无向图中简单环的个数（状态压缩DP）

HDU 6184 Counting Stars

cf246 ENew Reform (并查集找环)

CodeForces 510B无向图找环的两种方法（搜索与并查集）

LA3644——无向图中找环，并查集

---

但是本题写的算法并不是找环，而是找可分离边，但是思路很接近，因为我们要找的是当前点的子孙通过回边（环）连接当前点的祖先：

在任何DFS树中，条件是当且仅当不存在回边将`w`的一个子孙与`w`的一个祖先相连，则`v-w`是一条可分离边。

对于程序算法的思路理解：首先最开始搜索时候，我们从下标最小的点`0`开始用DFS搜索，最开始传递的边是`(0,0)`，然后从与0相连的点开始搜索，是1；从1开始搜索的时候，首先检查的肯定是0，这时候我们要排除原路返回的情况下继续搜索，所以搜索2；以此类推到6，与6连通的最小点是0但是已经被访问过了，于是我们知道这是一个环，这时候我们比较搜索顺序的标号，用标号最小的来区分不同的环。下面考虑在执行搜索`(1,2)`的回溯过程，这时候1和2的`low`值都有了并且在同一个环中，那么仍然取最小的值统一，所以最后的结果就是所有点的访问顺序最会大于等于回边所引用的最小遍历编号。于是我们得到一个`ord[]`和`low[]`的数组，如果访问顺序和回边最小标号相同，代表找到可分离边。

多一些思考，是否可以通过此方法找环呢，应该是可以的，我们最后得到一个`low[]`数组，显然在同一个环的下标是一样的，本题是：

|       | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| `ord` | 0    | 1    | 2    | 8    | 9    | 7    | 3    | 4    | 5    | 10   | 6    | 11   | 12   |
| `low` | 0    | 0    | 0    | 7    | 7    | 7    | 0    | 4    | 4    | 9    | 4    | 9    | 12   |

我们可以统计`low[]`数组相异数字的个数来判断环的个数，显然不同的环数字不同，单独的点所拥有的数字只有一个，数字个数超过2的数字的个数就是环的个数，相比于（状态压缩DP），效率会提高很多。值得注意的是，我们可以联想到`LeetCode 26 & 80 Remove Duplicates from Sorted Array`，思路是有借鉴之处。或者我们不排序，就在进行标记的同时我们就记录环的个数（如何实施？）

也可以采用`map`的数据结构，最后统计里面数量超过1的数字的个数即可）

```c++
#include <map>
#include <iostream>

using namespace std;

//增加一个函数circleCount
int circleCount(const vector<int> &low)
{
    map<int, int> m;
    
    for (size_t i = 0; i < low.size(); ++i)
        ++m[low[i]];
    
    int num = 0;
    for (auto e : m){
        if (e.second > 1)
            ++num;
    }
    
    return num;
}
```

注意：可分离边或者边连通分量的个数和环的个数之间没有任何关系，比如`3-4-5   4-9-11`这个部分多次重复，环的数量增加，但是可分离边或者边连通分量个数不会增加。

采用邻接矩阵表示法，那么我们不妨在每次访问过一条边后就将矩阵里的数量-1。

**我们把上面的思路写成一道简单的OJ题目（原创哦）**：

```
求连通图中环的个数，边连通分量的个数，并输出可分离边

输入数据：
第一行代表case的个数n,表边的数目m
接下来m行是m条边

输出数据：
第一行边连通分量的个数
接下来输出可分离边

样例：
1 16
0 1
1 2
2 6
6 0
6 7
7 8
7 10
8 10
0 5
3 4
5 3
5 4
4 9
9 11
4 11
11 12

输出：
4
6-7
0-5
11-12
```

```c++
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<int> line(50, 0);
vector<vector<int>> denseGraph(50, line);
vector<int> order(50, -1);
vector<int> low(50, 0);
stack<int> seperateEdge;
int maxVertex = -1, edgeNum = 0, sequence = 0;

ostream & operator<<(ostream & os, stack<int> &s)
{
    while(!s.empty()){
        os << s.top();
        s.pop();
        os << "-" << s.top() << endl;
        s.pop();
    }

    return os;
}

void search(int v, int w)
{
    order[w] = sequence++;
    low[w] = order[w];

    for (int i = 0; i <= maxVertex; ++i){
        if (denseGraph[w][i]){
            if (order[i] == -1){
                search(w, i);
                if (low[w] > low[i]) low[w] = low[i];
                if (low[i] == order[i]){
                    ++edgeNum;
                    seperateEdge.push(i);
                    seperateEdge.push(w);
                    //cout << w << "-" << i << endl;
                }
            }
            else if (i != v){
                if (low[w] > order[i]) low[w] = order[i];
            }
        } 
    }
}

void output()
{
    search(0, 0);
    cout << (edgeNum + 1) << endl;
    cout << seperateEdge;
}

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; ++i){
        //input process
        for (int j = 0; j < m; ++j){
            int point1, point2;
            cin >> point1 >> point2;
            ++denseGraph[point1][point2];
            ++denseGraph[point2][point1];
            maxVertex = max(maxVertex, max(point1, point2));
        }

        output();

        //reset process
        for (int j = 0; j <= maxVertex; ++j)
            fill(denseGraph[j].begin(), denseGraph[j].begin() + maxVertex, 0);
        fill(order.begin(), order.begin() + maxVertex, -1);
        fill(low.begin(), low.begin() + maxVertex, 0);
        maxVertex = -1;
        edgeNum = sequence = 0;
    }

    return 0;
}
```

上面的程序面对此题结果还是正确的，但是考虑下面这种情况：

![1569134420746](F:\学习笔记\c++\算法总结\assets\1569134420746.png)

上面代码的求解就会出现问题，所以求环的方法还是状态压缩DP更正确，所以找可分离边和找环没有什么必然联系。



关节点和重连通图

<https://blog.csdn.net/stillxjy/article/details/52049394

**关节点**是一个特殊的顶点，如果删除这个点，将把一个连通图分解为至少两个不相交的子图，关节点也被称为**分离顶点或割点**。

如果图中每一对顶点都由两条不相交的路径连接，则称该图是**重连通**的。**重连通分量**是删除任意一个顶点时仍然保持连通。

很自然的产生以下问题：

* 如何判断一个图是不是重连通的。
* 如何找到图中的关节点（割点），如何输出重连通分量。

如果图中每对顶点之间都至少有k条顶点不相交的路径将这两个顶点连接起来，则称这个图时**k-连通**的。一个图的**顶点连通度**定义为要把一个图分解为两部分所需删除的最小顶点数。

需要参考的定理：`Mebger定理` $\Rightarrow$`Whitney定理` 。

如果图中每对顶点之间都至少有k条不相交的路径将这两个顶点连接起来，则称这个图时**k-边连通**的。**边连通度**定义为要把图分解为两部分所需删除的最小边数。

```
【1】有向图的边连通度：
这个其实就是最小割问题。以s为源点，t为汇点建立网络，原图中的每条边在网络中仍存在，容量为1，求该网络的最小割（也就是最大流）的值即为原图的边连通度。
【2】有向图的点连通度：
需要拆点。建立一个网络，原图中的每个点i在网络中拆成i'与i''，有一条边<i', i''>，容量为1 （<s', s''>和<t', t''>例外，容量为正无穷）。原图中的每条边<i, j>在网络中为边<i'', j'>， 
容量为正无穷。以s'为源点、t''为汇点求最大流，最大流的值即为原图的点连通度。 
说明：最大流对应的是最小割。显然，容量为正无穷的边不可能通过最小割，也就是原图中的边和s、t两个点不能删去；若边<i, i''>通过最小割，则表示将原图中的点i删去。
【3】无向图的边连通度：
将图中的每条边(i, j)拆成<i, j>和<j, i>两条边，再按照有向图的办法（【1】）处理；
【4】无向图的点连通度：
将图中的每条边(i, j)拆成<i, j>和<j, i>两条边，再按照有向图的办法（【2】）处理。
```

==这部分按理说应放在网络流部分==

**S-T连通性问题**：一个给定图中，把两个顶点s和t分开，所需删除的最小边数和顶点数分贝是多少？

**一般连通性问题**：一个给定图时k-连通的嘛？时k-边连通的嘛？点连通度和边连通度各是多少？

典型题目：

<https://blog.csdn.net/u013480600/article/details/44831553>

<https://blog.csdn.net/u013480600/article/details/44835827>

- [ ] POJ 1144 Network(简单求无向图割顶数)：直接求割顶数。
- [ ] POJ 2117 Electricity(无向图割点)：问删除一点能增加几个连通分量
- [ ] POJ 1523 SPF(割点所割连通分量数): 问删除一点能增加几个连通分量。
- [ ] HDU 4587 TWO NODES(无向图割点)：还是关于删除一个点能剩余几个连通分量的问题。
- [ ] HDU 3849 By Recognizing…(求无向图的桥数目):如何在dfs完之后判断一条边是否是桥？
- [ ] HDU 4738 Caocao's Bridges(重边无向图求桥)：有重边的无向图如何求桥边.
- [ ] POJ 3352Road Construction(边双连通分量)：求添加最少的边数，使得图变成边双连通。
- [ ] POJ 3177Redundant Paths(边双连通分量+缩点)：求添加最少的边数，使得图变成边双连通。
- [ ] HDU 3749Financial Crisis(点-双连通分量)：输出两点间路径条数

## 2.7 BFS算法

```c++
#include <queue>
#include <vector>

using namespace std;

template <class Graph> 
class BFS : public SEARCH<Graph> 
{ 
    vector<int> st;

    void searchC(Edge e)
    { 
        queue<Edge> Q;  
        Q.push(e);
        while (!Q.empty()){
            if (ord[(e = Q.front()).w] == -1) {
                int v = e.v, w = e.w;
                ord[w] = cnt++; st[w] = v; 
                typename Graph::adjIterator A(G, w);

                for (int t = A.beg(); !A.end(); t = A.nxt()) 
                    if (ord[t] == -1) Q.put(Edge(w, t));
            }
            Q.pop();
        }   
    }

public:
    BFS(Graph &G) : SEARCH<Graph>(G), st(G.V(), -1) 
    { search(); }

    int ST(int v) const { return st[v]; }
};
```



# 第三章 有向图和无环有向图

## 3.2 有向图的DFS

![1569653543299](F:\学习笔记\c++\算法总结\assets\1569653543299.png)

书中所写的“树边”、 “回边” 、“下边”、“跨边”和《算法导论》里面的树边、后向边、前向边和横向边概念对应。

书中所给的程序里`pre[] post[]`的概念对应算法导论里面的时间戳，算法导论里面的显然更符合思维习惯。我们可以用下面的图来展示《算法导论》里关于DFS森林相关的概念。

![img](F:\学习笔记\c++\算法总结\assets\638419-20151128184040687-313147708.png)

书中的程序在我这里是按单文件写的，用在线编译器编译，这里出现了一点问题：

用`codingground`和`Wandbox`时候会显示`File size limit exceeded`，但是用`Coliru`又无法进行交互式输入输出。所以需要在输入上进行改进。

```c++
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Edge 
{ 
    int v, w;

    Edge(int v = -1, int w = -1) : v{v}, w{w} { }
};

class DenseGRAPH
{ 
    int Vcnt, Ecnt; 
    bool digraph;
    vector <vector<bool>> adj;

public:
    DenseGRAPH(int V, bool digraph = false) : Vcnt(V), Ecnt(0), digraph(digraph), adj(V)
    { 
        for (int i = 0; i < V; i++) 
            adj[i].assign(V, false);
    }

    int V() const { return Vcnt; }

    int E() const { return Ecnt; }

    bool directed() const { return digraph; }

    void insert(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == false) Ecnt++;
        adj[v][w] = true;
        if (!digraph) adj[w][v] = true; 
    } 

    void remove(Edge e)
    { 
        int v = e.v, w = e.w;
        if (adj[v][w] == true) Ecnt--;
        adj[v][w] = false;
        if (!digraph) adj[w][v] = false; 
    } 

    bool edge(int v, int w) const 
    { return adj[v][w]; }
    
    class adjIterator;
    friend class adjIterator;
};

class DenseGRAPH::adjIterator
{ 
    const DenseGRAPH &G;
    int i, v;
    
public:
    adjIterator(const DenseGRAPH &G, int v) : G{G}, i{-1}, v{v} { }
  
    int beg()
    { 
        i = -1; 
        return nxt(); 
    }

    int nxt()
    {
        for (i++; i < G.V(); i++)
            if (G.adj[v][i] == true) return i;
        return -1;
    }

    bool end()
    { return i >= G.V(); }
};

template <class Graph> 
void show(const Graph &G)
{ 
    for (int s = 0; s < G.V(); s++) 
    {
        cout.width(2); cout << s << ":";

        typename Graph::adjIterator A(G, s);

        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            cout.width(2); cout << t << " "; 
        }

        cout << endl;
    }
}

template <class Graph> 
class DFS
{ 
    const Graph &G;
    int depth, cnt, cntP;
    vector<int> findTime, finishTime;

    void show(string s, Edge e)
    { 
        for (int i = 0; i < depth; i++) cout << "  ";
        cout << e.v << "-" << e.w << s << endl; 
    }

    void dfsR(Edge e)
    { 
        int w = e.w; show(string(" tree"), e);
        findTime[w] = cnt++; depth++;

        typename Graph::adjIterator A(G, w);
        for (int t = A.beg(); !A.end(); t = A.nxt()){ 
            Edge x(w, t);

            if (findTime[t] == -1) dfsR(x);
            else if (finishTime[t] == -1) show(string(" back"), x);
            else if (findTime[t] > findTime[w]) show(string(" down"), x);
            else show(string(" cross"), x);
        }
        finishTime[w] = cntP++; depth--;
    }

public:
  DFS(const Graph &G) : G(G), cnt(0), cntP(0), findTime(G.V(), -1), finishTime(G.V(), -1)
    { 
        for (int v = 0; v < G.V(); v++) 
            if (findTime[v] == -1) dfsR(Edge(v, v)); 
    }
};


int main()
{
    int vertexNum = 13;
    //cin >> vertexNum;
    DenseGRAPH g(vertexNum, true);

    g.insert(Edge(0, 1));
    g.insert(Edge(0, 5));
    g.insert(Edge(0, 6));
    g.insert(Edge(2, 0));
    g.insert(Edge(2, 3));
    g.insert(Edge(3, 2));
    g.insert(Edge(3, 5));
    g.insert(Edge(4, 3));
    g.insert(Edge(4, 2));
    g.insert(Edge(4, 1));
    g.insert(Edge(5, 4));
    g.insert(Edge(6, 4));
    g.insert(Edge(6, 9));
    g.insert(Edge(7, 6));
    g.insert(Edge(7, 8));
    g.insert(Edge(8, 7));
    g.insert(Edge(8, 9));
    g.insert(Edge(9, 10));
    g.insert(Edge(9, 11));
    g.insert(Edge(10, 12));
    g.insert(Edge(11, 12));
    g.insert(Edge(12, 9));
    
   DFS<DenseGRAPH> m(g);

    return 0;
}

/*
定义输入格式：
第一行：点的个数（从0开始计数）
接下来n行代表有向边
13
0 1
0 5
0 6
2 0
2 3
3 2
3 5
4 3
4 2
4 1
5 4
6 4
6 9
7 6
7 8
8 7
8 9
9 10
9 11
10 12
11 12
12 9
 */
```

```shell
# run result
0-0 tree
  0-1 tree
  0-5 tree
    5-4 tree
      4-1 cross
      4-2 tree
        2-0 back
        2-3 tree
          3-2 back
          3-5 back
      4-3 down
  0-6 tree
    6-4 cross
    6-9 tree
      9-10 tree
        10-12 tree
          12-9 back
      9-11 tree
        11-12 cross
7-7 tree
  7-6 cross
  7-8 tree
    8-7 back
    8-9 cross
```

程序143-164行显然一句一句写会略显麻烦，所以不妨利用`codingground`生成代码：

```c++
int main()
{
    int vertexNum;
    cin >> vertexNum;

    int point1, point2;
    while(cin >> point1 >> point2)
    {
        cout << "g.insert(Edge(" << point1 << ", " << point2 << "));" << endl;
    }
    
    return 0;
}
```

```shell
# run result
g.insert(Edge(0, 1));
g.insert(Edge(0, 5));
g.insert(Edge(0, 6));
g.insert(Edge(2, 0));
g.insert(Edge(2, 3));
g.insert(Edge(3, 2));
g.insert(Edge(3, 5));
g.insert(Edge(4, 3));
g.insert(Edge(4, 2));
g.insert(Edge(4, 1));
g.insert(Edge(5, 4));
g.insert(Edge(6, 4));
g.insert(Edge(6, 9));
g.insert(Edge(7, 6));
g.insert(Edge(7, 8));
g.insert(Edge(8, 7));
g.insert(Edge(8, 9));
g.insert(Edge(9, 10));
g.insert(Edge(9, 11));
g.insert(Edge(10, 12));
g.insert(Edge(11, 12));
g.insert(Edge(12, 9));
```

针对OJ类题目的简单写法：

```c++
#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<int> line(13, 0);
vector<vector<int>> denseGraph(13, line);
vector<int> findTime(13, -1), finishTime(13, -1);
int depth = 0, cnt = 0, cntP = 0;

void show(string s, int v, int w)
{
    for (int i = 0; i < depth; i++) cout << "  ";
    cout << v << "-" << w << s << endl; 
}

void dfs(int v, int w)
{
    show(string(" tree"), v, w);
    findTime[w] = cnt++; depth++;

    for (int i = 0; i < 13; ++i){
        if (denseGraph[w][i]){
            if (findTime[i] == -1) dfs(w, i);
            else if (finishTime[i] == -1) show(string(" back"), w, i);
            else if (findTime[i] > findTime[w]) show(string(" down"), w, i);
            else show(string(" cross"), w, i);
        }
    }

    finishTime[w] = cntP++; depth--;
}


int main()
{
    int point1, point2;
    while(cin >> point1 >>point2){
        denseGraph[point1][point2] = 1;
    }

    for (int i = 0; i < 13; ++i){
        if (findTime[i] == -1) dfs(i, i);
    }
}
/*
输入：
0 1
0 5
0 6
2 0
2 3
3 2
3 5
4 3
4 2
4 1
5 4
6 4
6 9
7 6
7 8
8 7
8 9
9 10
9 11
10 12
11 12
12 9
*/
```

```shell
# run result
0-0 tree
  0-1 tree
  0-5 tree
    5-4 tree
      4-1 cross
      4-2 tree
        2-0 back
        2-3 tree
          3-2 back
          3-5 back
      4-3 down
  0-6 tree
    6-4 cross
    6-9 tree
      9-10 tree
        10-12 tree
          12-9 back
      9-11 tree
        11-12 cross
7-7 tree
  7-6 cross
  7-8 tree
    8-7 back
    8-9 cross
```

## 3.3 可达性和传递闭包

典型题目：POJ 1932（SPFA+判断正环+Floyd求传递闭包）

POJ 3660（Floyd求传递闭包）

此部分更好的写法出现在《算法设计与分析基础》的8.4 Warshall算法和Floyd算法



## 3.5 无环有向图

书中P156讲到的二叉DAG和二叉树压缩甚至可以扩展为一本书或一个专题，涉及到一个数据结构“ST表”。

可以参考的书有《有序二叉决策图及应用》





# 第四章 最小生成树

最小生成树（Minimum spanning tree）可以参考《数据结构：思想与实现》，CP-Algorithm，OI WIKI或者《C++图算法》的内容。

## 4.3 Prim算法和优先级搜索

 **Dense graphs: O(n^2)**

对于一个无向图G有n个节点和m条边，找到一个图连接所有节点，任意节点到其他节点只有一条简单路径，并且所有边的权重之和最小，这棵生成树就是最小生成树。

![Random graph](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/MST_before.png)

![MST of this graph](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/MST_after.png)

**Input**

```
6
0 1 2
0 3 1
0 4 4
1 3 3
1 5 7
1 2 3
2 3 5
2 5 8
3 4 9
```

**Program**

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x0fffffff; // weight INF means there is no edge
int n = 6;
vector<vector<int>> adj(n, vector<int>(n, INF)); // adjacency matrix of graph

struct Edge {
    int w = INF, to = -1;
};

void prim() {
    int total_weight = 0;
    vector<bool> selected(n, false);
    vector<Edge> min_e(n);
    min_e[0].w = 0;

    for (int i=0; i<n; ++i) {
        int v = -1;
        for (int j = 0; j < n; ++j) {
            if (!selected[j] && (v == -1 || min_e[j].w < min_e[v].w))
                v = j;
        }

        if (min_e[v].w == INF) {
            cout << "No MST!" << endl;
            exit(0);
        }

        selected[v] = true;
        total_weight += min_e[v].w;
        if (min_e[v].to != -1)
            cout << (v + 1) << " - " << (min_e[v].to + 1) << ": " << min_e[v].w << endl;

        for (int to = 0; to < n; ++to) {
            if (adj[v][to] < min_e[to].w)
                min_e[to] = {adj[v][to], v};
        }
    }

    cout << total_weight << endl;
}

int main()
{
    int v, w, weight;
    cin >> n;
    while(cin >> v >> w >> weight){
        adj[v][w] = weight;
        adj[w][v] = weight;
    }
    prim();
}
```

**Output**

```shell
4 - 1: 1
2 - 1: 2
3 - 2: 3
5 - 1: 4
6 - 2: 7
17
```

算法思路：

最外层的循环起到的作用是确保把每个点都要加入到最小生成树里面来，每次最开始都是先从没有被访问的点里面选一个交叉边权值最小的（程序22-27行），然后此点被加入到已经访问过的节点（标记访问过），这时候用到动态规划的思想，也就是需要理解数组`min_e[i]`的意思，我们用数组来存储未被访问过的节点`i`到所有已经访问过的节点的最小权值，也就是说，这个数组保存了上一轮的最小权值，这次如果遇到更小的，那么就更新，否则不更新。这样就避免了每次都去重新算一遍交叉边的最小权值。



**Sparse graphs O(m log n)**

```c++
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 0x0fffffff; // weight INF means there is no edge

struct Edge {
    int w = INF, to = -1;

    bool operator<(Edge const& other) const 
    {
        return w < other.w;
    }
};

int n = 6;
vector<vector<Edge>> adj(n); // adjacency matrix of graph

void prim() {
    int total_weight = 0;
    vector<Edge> min_e(n);
    min_e[0].w = 0;
    set<Edge> q;
    q.insert({0, 0});
    vector<bool> selected(n, false);
    for (int i = 0; i < n; ++i) {
        if (q.empty()) {
            cout << "No MST!" << endl;
            exit(0);
        }

        int v = q.begin()->to;
        selected[v] = true;
        total_weight += q.begin()->w;
        q.erase(q.begin());

        if (min_e[v].to != -1)
            cout << v << " " << min_e[v].to << endl;

        for (Edge e : adj[v]) {
            if (!selected[e.to] && e.w < min_e[e.to].w) {
                q.erase({min_e[e.to].w, e.to});
                min_e[e.to] = {e.w, v};
                q.insert({e.w, e.to});
            }
        }
    }

    cout << total_weight << endl;
}

int main()
{
    int v, w, weight;
    cin >> n;
    while(cin >> v >> w >> weight){
        adj[v].push_back({weight, w}); 
        adj[w].push_back({weight, v});
    }
    prim();

    return 0;
}
```

思路和用邻接矩阵表示的方法相差无几，区别在于适用对象是稠密图还是稀疏图。



## 4.4 Kruskal算法

Kruskal算法和Prim算法的区别在于，先加入n个点，逐次加入n-1条边，每次选一个权值最小的边加入，如果不会出现回边则加入，否则不加，对于回边的判断可以用并查集来实现。

```c++
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v, weight;

    bool operator<(Edge const& other) 
    {
        return weight < other.weight;
    }
};

int n = 6, total_weight = 0;
vector<Edge> edges, result;
vector<int> parent(n), setRank(n);

void make_set(int v) {
    parent[v] = v;
    setRank[v] = 0;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (setRank[a] < setRank[b])
            swap(a, b);
        parent[b] = a;
        if (setRank[a] == setRank[b])
            setRank[a]++;
    }
}

void kruskal()
{
    for (int i = 0; i < n; i++)
        make_set(i);

    sort(edges.begin(), edges.end());

    int num = 0;
    for (Edge e : edges) {
        if (find_set(e.u) != find_set(e.v)) {
            total_weight += e.weight;
            result.push_back(e);
            union_sets(e.u, e.v);
            ++num;
            if (num == n - 1) return; //already insert n-1 edges
        }
    }
}

ostream & operator<<(ostream & os, vector<Edge> & edges)
{
    for (auto e : edges)
        os << e.u << " - " << e.v << ": " << e.weight << endl;

    return os;
}

int main()
{
    int v, w, weight;
    cin >> n;
    while(cin >> v >> w >> weight){
        edges.push_back({v, w, weight});
    }
    kruskal();
    cout << total_weight << endl;
    cout << result;

    return 0;
}
```

其中`setRank`相当于按秩（或者理解为树的高度）进行的路径压缩。通过并查集的数据结构来区分访问过的点和没访问过的点。



## 4.5 Boruvka算法

此种算法和Kruskal算法比较接近，使用的情景并不多，不做展开了。



## 4.6 欧几里得MST

给定平面上的n个点，找出连接所有这些点的最短线段的集合。



#第五章 最短路径

加权有向图中的每条路径都有相关的“路径权”，其值为该路径上边的权值之和。找出两个给定顶点间的权值最小的路径是最短路径问题。

**源点-汇点最短路径** ： 给定一个起始顶点s和一个结束定点t，在图中找到从s到t的一条最短路径。

**单源最短路径**：给定一个起始顶点s，找出从s到图中其他各个顶点的最短路径

**全源最短路径**：找出连接图中各对顶点的最短路径。

**公路路线图**：给出各个主要城市之间的距离的表，一般是给出一个无向图

**航班路线问题**：航班或运输系统的路线图，比如飞机在两个城市间飞行，可能希望花费的时间最少，或者旅行的成本最低。比如两个城市之间的飞行，往往一个方向比另一个方向需要花费更多的时间，主要因为风向的影响，所以返回采取迂回路线也许比直达更便宜。

## 5.1 基本原则

* 边松弛：检查沿着一条给定的边是否可以给出到达其目的顶点的一条新的最短路径。
* 路径松弛：检查通过一个给定顶点是否可以给出连接另外两个给定顶点的一条新的最短路径。

## 5.2 Dijkstra算法





# 第六章 网络流

最小割模型汇总：<https://blog.csdn.net/qq_35649707/article/details/77482691>

网络流的典型练习：网络流24题