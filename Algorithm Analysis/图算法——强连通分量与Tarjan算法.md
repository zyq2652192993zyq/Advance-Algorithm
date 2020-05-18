# 图算法——强连通分量与Tarjan算法

Tarjan算法的典型例子：洛谷 P3387

典型题目可参考：邝斌带你飞系列

两种典型算法：Kosaraju算法（刘汝佳训练指南P319），第二种tarjan算法

Kosaraju算法的代码实现参考了[CP-Algorithm](https://cp-algorithms.com/graph/strongly-connected-components.html)：



```c++
#include <iostream>
#include <vector>

using namespace std;

vector < vector<int> > g, gr; //g:邻接表, gr：逆向图的邻接表
vector<bool> used; //记录当前节点是否被访问过
vector<int> order, component; //order：记录访问顺序 component：存储强连通分量

void dfs1(int v) 
{
    used[v] = true;
    for (size_t i = 0; i < g[v].size(); ++i)
        if (!used[ g[v][i] ])
            dfs1(g[v][i]);
    order.push_back(v);
}

void dfs2(int v) 
{
    used[v] = true;
    component.push_back(v);
    for (size_t i = 0; i < gr[v].size(); ++i)
        if (!used[ gr[v][i] ])
            dfs2(gr[v][i]);
}

int main() 
{
    int n;
    //reading in n
    for (;;) {
        int a, b;
        //... reading next edge (a,b) ...
        g[a].push_back (b);
        gr[b].push_back (a);
    }

    used.assign(n, false);
    for (int i = 0; i < n; ++i)
        if (!used[i])
            dfs1(i);
    used.assign(n, false);
    for (int i =0; i < n; ++i) {
        int v = order[n-1-i];
        if (!used[v]) {
            dfs2(v);
            //... printing next component ...
            component.clear();
        }
    }
}
```

![1572701992769](F:\学习笔记\c++\算法总结\assets\1572701992769.png)

Tarjan算法：

**Input:**

第一行n, m，分别代表顶点个数和有向边的个数

接下来m行，每行两个整数，代表有向边的起点和终点。

```
12 17
0 1
1 2
1 3
1 4
4 1
2 5
5 2
4 5
4 6
5 7
6 7
8 6
6 9
9 8
7 10
10 11
11 9

```

```c++
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

const int maxn = 1000+10;
int n,m;
vector<vector<int>> G(maxn);
vector<int> pre(maxn, 0), low(maxn), sccno(maxn, 0); //sccno: i所在的SCC编号
int timer, scc_cnt;
stack<int> S;

void dfs(int u)
{
    pre[u] = low[u] = ++timer;
    S.push(u);
    for(auto v : G[u]) {
        if(!pre[v]) {
            dfs(v);
            low[u] = min(low[u], low[v]);
        }
        else if(!sccno[v])
        {
            low[u] = min(low[u], pre[v]);
        }
    }

    if(low[u] == pre[u])
    {
        scc_cnt++; //SCC编号计数器
        while(!S.empty())
        {
            int x = S.top(); 
            S.pop();
            sccno[x] = scc_cnt;
        }
    }
}

void find_scc(int n)
{
    scc_cnt = timer = 0;
    for(int i = 0; i < n; ++i)
        if(!pre[i]) 
            dfs(i);
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    while((cin >> n >> m) && n)
    {
        for(int i = 0; i < n; ++i) G[i].clear();
        while(m--)
        {
            int u,v;
            cin >> u >> v;
            G[u].push_back(v);
        }
        find_scc(n);
        for(int i = 0; i < n; ++i)
            cout << i << "号点属于" << sccno[i] << "分量" << endl;
    }
}
```

```shell
# run result
0号点属于5分量
1号点属于4分量
2号点属于2分量
3号点属于3分量
4号点属于4分量
5号点属于2分量
6号点属于1分量
7号点属于1分量
8号点属于1分量
9号点属于1分量
10号点属于1分量
11号点属于1分量
```

Tarjan算法相比于Kosaraju不需要两次DFS，只需要一次。算法思想和寻找桥或割点思路很接近。用一个栈S来存储当前SCC中的节点。pre用来记录对某个节点开始访问的时间，low用来记录一个SCC中最先被访问节点的标号。sscno数组用来记录所有点属于哪个SCC，scc_cnt对不同SCC标号，用来区分。



典型题目：

- [ ] HDU 2767 Proving Equivalences(强连通分量)：一个图最少添加几条边能使得该图强连通？
- [ ] POJ 1236 Network of Schools(强连通分量)：类似于前一题。
- [ ] POJ 2762 Going from u to v …(强连通分量+拓扑排序)：问你图中任意两点间是否至少有1条路？
- [ ] POJ 2186 Popular Cows(强连通分量+缩点)：求出所有其他点都可达的点数目。
- [ ] POJ 2553 The Bottom of a Graph(强连通分量)：求强连通分量+缩点DAG+处理。
- [ ] HDU 1269 迷宫城堡(强连通分量)：强连通图判定。
- [ ] HDU 3639 Hawk-and-Chicken(强连通分量+缩点)：最终需要DAG的逆图进行dfs。
- [ ] HDU 4635 Strongly connected(强连通分量)：一个图最多能添加多少条边依然不是强连通的？
- [ ] HDU 3836 Equivalent Sets(强连通分量)：最少添加边，使得图变成强连通。
- [ ] HDU 1827 Summer Holiday(强连通分量)：求强连通分量+缩点DAG+处理。
- [ ] HDU 3072 Intelligence System(强连通分量)：求强连通分量+缩点DAG+处理。
- [ ] SPOJ-Submerging Islands
- [ ] SPOJ-Good Travels
- [ ] SPOJ-Lego
- [ ] Codechef-Chef and Round Run
- [ ] Dev Skills -A Song of Fire and Ice
- [ ] UVA-11838-Come and Go
- [ ] UVA 247-Calling Circles
- [ ] UVA 13057-Prove Them All
- [ ] UVA 12645-Water Supply
- [ ] UVA 11770-Lighting Away
- [ ] UVA 12926-Trouble in Terrorist Town
- [ ] UVA 11324-The Largest Clique(最大团)
- [ ] UVA 11709-Trust groups
- [ ] UVA 12745-Wishmaster
- [ ] SPOJ-True Friends
- [ ] SPOJ-Capital City
- [ ] Codeforces-Scheme
- [ ] SPOJ-Ada and Panels

