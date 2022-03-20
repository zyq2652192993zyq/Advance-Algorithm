> # SPOJ SUBMERGE - Submerging Islands

Vice City is built over a group of islands, with bridges connecting them. As anyone in Vice City knows, the biggest fear of vice-citiers is that some day the islands will submerge. The big problem with this is that once the islands submerge, some of the other islands could get disconnected. You have been hired by the mayor of Vice city to tell him how many islands, when submerged, will disconnect parts of Vice City. You should know that initially all the islands of the city are connected.

# Input

The input will consist of a series of test cases. Each test case will start with the number N (1 ≤ N ≤ 10^4) of islands, and the number M of bridges (1 ≤ M ≤ 10^5). Following there will be M lines each describing a bridge. Each of these M lines will contain two integers Ui, Vi (1 ≤ Ui,Vi ≤ N), indicating that there is a bridge connecting islands Ui and Vi. The input ends with a case where N = M = 0.

# Output

For each case on the input you must print a line indicating the number of islands that, when submerged, will disconnect parts of the city.

# Sample Input

```
3 3
1 2
2 3
1 3
6 8
1 3
6 1
6 3
4 1
6 4
5 2
3 2
3 5
0 0
```

# Sample Output

```
0
1
```

---

```c++
#include <iostream>
#include <vector>

using namespace std;

int n; // number of nodes
vector<vector<int>> adj(10001); // adjacency list of graph
vector<bool> visited(10001, false);
vector<int> order(10001, -1), low(10001, -1);
int timer, num = 0;

void DFS(int v, int parent = -1) {
    visited[v] = true;
    order[v] = low[v] = timer++;
    int children=0;
    for (int to : adj[v]) {
        if (to == parent) continue;
        if (visited[to]) {
            low[v] = min(low[v], order[to]);
        } else {
            DFS(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] >= order[v] && parent!=-1)
                ++num;
            ++children;
        }
    }
    if(parent == -1 && children > 1)
        ++num;
}

void findArticulationPoint() {
    timer = 0;num = 0;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i])
            DFS(i);
    }
}

void init()
{
    for (int i = 1; i <= n; ++i){
        adj[i].clear();
        visited[i] = false;
        order[i] = -1;
        low[i] = -1;
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    while ((cin >> n >> m) && n && m) {
        for (int i = 0; i < m; ++i) {
            int point1, point2;
            cin >> point1 >> point2;
            adj[point1].push_back(point2);
            adj[point2].push_back(point1);
        }
        findArticulationPoint();
        cout << num << endl;
        init();
    }   

    return 0;
}
```

模板类题目：找连通图的割点。