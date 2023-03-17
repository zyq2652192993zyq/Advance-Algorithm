> # UVa-110901 / 10004 Bicoloring（二部图着色）

# Description

In 1976 the"Four Color Map Theorem"was proven with the assistance of a computer. This theorem states that every map can be colored using only four colors, in such a way that no region is colored using the same color as a neighbor region.
Here you are asked to solve a simpler similar problem. You have to decide whether a given arbitrary connected graph can be bicolored. That is, if one can assign colors(from a palette of two) to the nodes in such a way that no two adjacent nodes have the same color. To simplify the problem you can assume:

* no node will have an edge to itself.
* the graph is nondirected. That is, if a node a is said to be connected to a node b, then you must assume that b is connected to a.
* the graph will be strongly connected. That is, there will be at least one path from any node to any other node.

# Input

The input consists of several test cases. Each test case starts with a line containing the number n(1<n<200) of different nodes. The second line contains the number of edges 1. After this,I lines will follow, each containing two numbers that specify an edge between the two nodes that they represent.
A node in the graph will be labeled using a number a(0<a<n).
An input with n=0 will mark the end of the input and is not to be processed.

# Output

You have to decide whether the input graph can be bicolored or not, and print it as shown below.

# Sample Input

```
3
3
0 1
1 2
2 0
3
2
0 1
1 2
9
8
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0
```

# Sample Output

```
NOT BICOLORABLE.
BICOLORABLE.
BICOLORABLE.
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> color(200, -1);
vector<vector<int>> denseGraph(200, vector<int>(200));
int vertexNum, edgeNum;

bool DFS(int v, int c)
{
    color[v] = (c + 1) % 2; //给当前点着色

    for (int i = 0; i < vertexNum; ++i){
        if(denseGraph[v][i]){ //给所有与v相连的点染色
            if (color[i] == -1){
                if (!DFS(i, color[v])) return false;
            }
            else if (color[i] != c) return false; //染色出现矛盾
        }
    }
    
    return true;
}

int main()
{
    while ((cin >> vertexNum) && vertexNum){
        cin >> edgeNum;
        for (int i = 0; i < edgeNum; ++i){
            int point1, point2;
            cin >> point1 >> point2;
            denseGraph[point1][point2] = 1;
            denseGraph[point2][point1] = 1;
        }

        bool flag = true;
        for (int i = 0; i < vertexNum; ++i){
            if (color[i] == -1){ //当前点还没有被染色
                if (!DFS(i, 0)){
                    flag = false;
                    break;
                }
            }
        }

        if (flag) cout << "BICOLORABLE."  << endl;
        else cout << "NOT BICOLORABLE." << endl;

        //reset process
        fill(color.begin(), color.begin() + vertexNum, -1);
        for (int i = 0; i < vertexNum; ++i)
            fill(denseGraph[i].begin(),  denseGraph[i].begin() + vertexNum, 0);
    }

    return 0;
}
```

按照点的大小顺序，从最小的点开始搜索，用一个和节点数目相同的数组来存储着色，由于是只有两种颜色，所以就用1，0来区分即可，如果这个图用其他颜色来区分，我们就用0，1，2，3来区分，需要改动的有14和21行的程序。