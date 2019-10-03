> # POJ-1041 John's trip(欧拉回路)

# Description

Little Johnny has got a new car. He decided to drive around the town to visit his friends. Johnny wanted to visit all his friends, but there was many of them. In each street he had one friend. He started thinking how to make his trip as short as possible. Very soon he realized that the best way to do it was to travel through each street of town only once. Naturally, he wanted to finish his trip at the same place he started, at his parents' house.

The streets in Johnny's town were named by integer numbers from 1 to n, n < 1995. The junctions were independently named by integer numbers from 1 to m, m <= 44. No junction connects more than 44 streets. All junctions in the town had different numbers. Each street was connecting exactly two junctions. No two streets in the town had the same number. He immediately started to plan his round trip. If there was more than one such round trip, he would have chosen the one which, when written down as a sequence of street numbers is lexicographically the smallest. But Johnny was not able to find even one such round trip.

Help Johnny and write a program which finds the desired shortest round trip. If the round trip does not exist the program should write a message. Assume that Johnny lives at the junction ending the street appears first in the input with smaller number. All streets in the town are two way. There exists a way from each street to another street in the town. The streets in the town are very narrow and there is no possibility to turn back the car once he is in the street

# Input

Input file consists of several blocks. Each block describes one town. Each line in the block contains three integers x; y; z, where x > 0 and y > 0 are the numbers of junctions which are connected by the street number z. The end of the block is marked by the line containing x = y = 0. At the end of the input file there is an empty block, x = y = 0.

# Output

Output one line of each block contains the sequence of street numbers (single members of the sequence are separated by space) describing Johnny's round trip. If the round trip cannot be found the corresponding output block contains the message "Round trip does not exist."

# Sample Input

```
1 2 1
2 3 2
3 1 6
1 2 5
2 3 3
3 1 4
0 0
1 2 1
2 3 2
1 3 3
2 4 4
0 0
0 0
```

# Sample Output

```
1 2 3 5 4 6 
Round trip does not exist.
```

---

```c++
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<int> STREET(1996, 0);
vector<vector<int>> matrix(45, STREET); //存储 matrix[点][边] = 点 的矩阵 
vector<bool> edgeVisited(1996, false); //边是否访问
vector<int> degree(45, 0); //点的度数
stack<int> s;
int max_junction = 0, max_street = 0, start = 0;

ostream & operator<<(ostream & os, stack<int> &s)
{
    while (!s.empty()){
        os << s.top() << " ";
        s.pop();
    }

    return os;
}

void EulerPath(int start)
{
    for (int i = 1; i <= max_street; ++i){
        if (!edgeVisited[i] && matrix[start][i]){
            edgeVisited[i] = true;
            EulerPath(matrix[start][i]);
            s.push(i);
        }
    }
}

int main()
{
    bool flag = true, next = true;

    int junction1 = 0, junction2 = 0, street = 0; 
    while(cin >> junction1 >> junction2){
        if (junction1 == 0 && junction2 == 0){
            if (next){
                bool exist = true;
                for (int i = 1; i <= max_junction; ++i){
                    if (degree[i] % 2 != 0) 
                        exist = false;
                }

                if (exist){
                    EulerPath(start);
                    cout << s << endl;
                }
                else{
                    cout << "Round trip does not exist." << endl;
                }
                
                //清理工作
                fill(STREET.begin() + 1, STREET.begin() + max_street + 1, 0);
                fill(edgeVisited.begin() + 1, edgeVisited.begin() + max_street + 1, false);
                fill(degree.begin() + 1, degree.begin() + max_junction + 1, 0);
                for (int i = 1; i <= max_junction; ++i)
                    fill(matrix[i].begin() + 1, matrix[i].begin() + 1 + max_street, 0);
                max_junction = max_street = start = 0; 
                flag = true;
                junction1 = junction2 = street = 0;
                next = false;
            }
            else break;
        }
        else{
            cin >> street;

            matrix[junction1][street] = junction2;
            matrix[junction2][street] = junction1;
            ++degree[junction1];
            ++degree[junction2];

            if (flag) {
                start = min(junction1, junction2); //确定欧拉路径的起始点
                flag = false;
            }

            max_junction = max(max_junction, max(max_junction, junction2)); //确定点的数量
            max_street = max(max_street, street); //确定边的数量
            next = true;
        }
    }

    return 0;
}
```

无向图的欧拉路径，并且要求回到原点，依次检查的是连通性和度数。本题没有检查连通性，和普通路径搜索需要记录步数不同，本体不需要额外变量记录步数，因为出发点是确定的，那么必须回到出发点才能保证点的度数是偶数。此题额外使用了栈来存储访问的节点。试问如果要找字典序最大的路径呢？只需要在遍历路径的向量时候，从末尾向前遍历即可。