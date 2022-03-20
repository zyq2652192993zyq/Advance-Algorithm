> # SPOJ CCOMPS - Count Components(无向图的连通性)

Given an undirected graph of N nodes (numbered from 1 to N) and M edges, find the number of its connected components.

# Input

The first line of input consists of two integers, N and M, the number of nodes and the number of edges respectively. (N ≤ 100000, M ≤ 200000)

The next M lines of input contain a pair of integers (x, y) representing anedge between nodes x and y. (1 ≤ x, y ≤ N)

# Output

To the first and only line of output, print a single integer: the number of connected components.

# Sample Input

```
5 2
1 2
3 4
```

# Sample Output

```
3
```

---

```c++
#include <iostream>
#include <vector>

using namespace std;

int n; //顶点的数目
vector<vector<int>> adj(100001); //链表存储图，用数组模拟
vector<bool> used(100001, false); //记录数组是否被访问果
vector<int> comp; 

ostream & operator<<(ostream & os, vector<int> & v)
{
    for (auto e : v)
        os << e << " ";
    return os;
}

void DFS(int v)
{
    used[v] = true;
    comp.push_back(v);
    for (auto e : adj[v]){
        if (!used[e]){
            DFS(e);
        }
    }

}

int findComponents()
{
    int result = 0;
    for (int i = 0; i < n; ++i){
        if (!used[i]){
            comp.clear();
            DFS(i);
            ++result;
        }
    }

    return result;
}


int main()
{
    int m;
    cin >> n >> m;
    for (int i = 0; i < m; ++i){
        int point1, point2;
        cin >> point1 >> point2;
        adj[point1].push_back(point2);
        adj[point2].push_back(point1);
    }
    cout << findComponents() << endl;
    
    return 0;
}
```



