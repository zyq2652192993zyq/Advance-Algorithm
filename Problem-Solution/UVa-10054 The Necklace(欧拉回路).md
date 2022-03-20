> # UVa-10054 The Necklace(欧拉回路)

# Description

My little sister had a beautiful necklace made of colorful beads. Two successive beads in the necklace shared a common color at their meeting point. The figure below shows a segment of the necklace:

But, alas! One day, the necklace was torn and the beads were all scattered over the floor. My sister did her best to recollect all the beads from the floor, but she is not sure whether she was able to collect all of them. Now, she has come to me for help. She wants to know whether it is possible to make a necklace using all the beads she has in the same way her original necklace was made and if so in which order the bids must be put.

Please help me write a program to solve the problem.

# Input

The input contains T test cases. The first line of the input contains the integer T.
The first line of each test case contains an integer N(5≤N≤1000) giving the number of beads my sister was able to collect. Each of the next N lines contains two integers describing the colors of a bead.
Colors are represented by integers ranging from 1 to 50.

# Output

For each test case in the input first output the test case number as shown in the sample output. Then if you apprehend that some beads may be lost just print the sentence "some beads may be lost"on a line byitself. Otherwise, print N lines with a single bead description on each line. Each bead description consists of two integers giving the colors of its two ends. For 1si≤Vi, the second integer on line i must be the same as the first integer on line i+ 1. Additionally, the second integer on line N must be equal to the first integer on line 1. Since there are many solutions, any one of them is acceptable.
Print a blank line between two successive test cases.

# Sample Input

```
2
5
1 2
2 3
3 4
4 5
5 6
5
2 1
2 2
3 4
3 1
2 4
```

# Sample Output

```
Case#1
some beads may be lost

Case #2
2 1
1 3
3 4
4 2
2 2
```

---

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> degree(51, 0);
vector<bool> vertexVisited(51, false);
vector<vector<int>> denseGraph(51, degree);
int maxVertex = 0, start = 0;

void EulerPath(int s)
{
    for (int i = 1; i <= maxVertex; ++i){
        if (denseGraph[s][i]){
            //小技巧，既有visit功能，又有解决自环
            --denseGraph[s][i];
            --denseGraph[i][s];
            EulerPath(i);
            cout << i << " " << s << endl; //输出注意下顺序
        }
    }
}

void DFS(int s)
{
    vertexVisited[s] = true;

    for (int i = 1; i <= maxVertex; ++i){
        if (!vertexVisited[i] && denseGraph[s][i]){
            DFS(i);
        }
    }
}

bool connectCheck()
{
    DFS(start);

    for (int i = 1; i <= maxVertex; ++i){
        if (!vertexVisited[i]) 
            return false;
    }

    return true;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    
    int caseNum = 0;
    bool gap = false;
    cin >> caseNum;

    for (int i = 1; i <= caseNum; ++i){
        bool flag = true;
        int edgeNum;
        cin >> edgeNum;

        for (int j = 1; j <= edgeNum; ++j){
            int point1, point2;
            cin >> point1 >> point2;

            if (flag){
                start = max(point1, point2);
                flag = false;
            }

            ++degree[point1];
            ++degree[point2];
            ++denseGraph[point1][point2];
            ++denseGraph[point2][point1];

            maxVertex = max(maxVertex, max(point1, point2));
        }

        //检查是否是连通图，比如每个都是自环则度数满足但无回路
        //bool connect = connectCheck();

        //检查节点度数
        bool exist = true; 
        for (int j = 1; j <= maxVertex; ++j){
            if (degree[j] % 2 != 0) 
                exist = false;
        }

        if (gap) cout << endl;
        gap = true;
        cout << "Case #" << i << endl;
        if (exist ){
            EulerPath(start);
        }
        else cout << "some beads may be lost" << endl;

        //reset process
        fill(degree.begin() + 1, degree.begin() + 1 + maxVertex, 0);
        fill(vertexVisited.begin() + 1, vertexVisited.begin() + 1 + maxVertex, false);
        for(int j = 1; j <= maxVertex; ++j)
            fill(denseGraph[j].begin() + 1, denseGraph[j].begin() + 1 + maxVertex, 0);
        maxVertex = start = 0;
    }

    return 0;
}
```

此题还是存在些疑惑：

进行连通性检查反而会得到`wrong answer`，特殊的反例，如所有的点全是自环，显然满足奇偶性检查，但是显然不能组成在一起。



