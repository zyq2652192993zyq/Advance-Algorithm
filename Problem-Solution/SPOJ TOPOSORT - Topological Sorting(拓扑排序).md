> # SPOJ TOPOSORT - Topological Sorting(拓扑排序)

Sandro is a well organised person. Every day he makes a list of things which need to be done and enumerates them from 1 to n. However, some things need to be done before others. In this task you have to find out whether Sandro can solve all his duties and if so, print the correct order.

# Input

In the first line you are given an integer n and m (1<=n<=10000, 1<=m<=1000000). On the next m lines there are two distinct integers x and y, (1<=x,y<=10000) describing that job x needs to be done before job y.

# Output

Print "Sandro fails." if Sandro cannot complete all his duties on the list. If there is a solution print the correct ordering, the jobs to be done separated by a whitespace. If there are multiple solutions print the one, whose first number is smallest, if there are still multiple solutions, print the one whose second number is smallest, and so on.

# Sample Input & Output

```
Input
8 9
1 4
1 2
4 2
4 3
3 2
5 2
3 5
8 2
8 6
```

```
Ouptut
1 4 3 5 7 8 2 6 
```

```
Input
2 2
1 2
2 1
```

```
Output
Sandro fails.
```

---

```c++
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

size_t vertexNum, edgeNum;
vector<vector<int>> adj(10001);
vector<int> result, inDegree;
priority_queue<int, vector<int>, greater<int>> q;

ostream & operator<<(ostream & os, const vector<int> & v)
{
    for (size_t i = 0; i < v.size(); ++i){
        os << v[i];
        if (i != v.size() - 1) os << " ";
    }
    return os;
}

void topologicalSort()
{
    for (size_t i = 1; i <= vertexNum; ++i){
        if (inDegree[i] == 0)
            q.push(i);
    }

    while (!q.empty()) {
        int tmp = q.top();
        q.pop();
        result.push_back(tmp);
        for (auto i = adj[tmp].begin(); i != adj[tmp].end(); ++i){
            if (--inDegree[*i] == 0)
                q.push(*i);
        }
    }
    if (result.size() < vertexNum) cout << "Sandro fails." << endl;
    else cout << result << endl;
}


int main()
{
    cin >> vertexNum >> edgeNum;
    inDegree.assign(vertexNum + 1, 0);
    while (edgeNum--) {
        int point1, point2;
        cin >> point1 >> point2;
        adj[point1].push_back(point2);
        ++inDegree[point2];
    }
    topologicalSort();

    return 0;
}
```

这里应用了一个`priority_queue<int, vector<int>, greater<int>>`来保证每次按字典序最小的输出。