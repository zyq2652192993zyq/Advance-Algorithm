> #POJ-1129 Channel Allocation(四色问题的DFS)

# Description

When a radio station is broadcasting over a very large area, repeaters are used to retransmit the signal so that every receiver has a strong signal. However, the channels used by each repeater must be carefully chosen so that nearby repeaters do not interfere with one another. This condition is satisfied if adjacent repeaters use different channels.

Since the radio frequency spectrum is a precious resource, the number of channels required by a given network of repeaters should be minimised. You have to write a program that reads in a description of a repeater network and determines the minimum number of channels required.

# Input

The input consists of a number of maps of repeater networks. Each map begins with a line containing the number of repeaters. This is between 1 and 26, and the repeaters are referred to by consecutive upper-case letters of the alphabet starting with A. For example, ten repeaters would have the names A,B,C,...,I and J. A network with zero repeaters indicates the end of input.

Following the number of repeaters is a list of adjacency relationships. Each line has the form:

A:BCDH

which indicates that the repeaters B, C, D and H are adjacent to the repeater A. The first line describes those adjacent to repeater A, the second those adjacent to B, and so on for all of the repeaters. If a repeater is not adjacent to any other, its line has the form

A:

The repeaters are listed in alphabetical order.

Note that the adjacency is a symmetric relationship; if A is adjacent to B, then B is necessarily adjacent to A. Also, since the repeaters lie in a plane, the graph formed by connecting adjacent repeaters does not have any line segments that cross.

# Output

For each map (except the final one with no repeaters), print a line containing the minumum number of channels needed so that no adjacent channels interfere. The sample output shows the format of this line. Take care that channels is in the singular form when only one channel is required.

# Sample Input

```
2
A:
B:
4
A:BC
B:ACD
C:ABD
D:BC
4
A:BCD
B:ACD
C:ABD
D:ABC
0
```

# Sample Output

```
1 channel needed.
3 channels needed.
4 channels needed. 
```

---

```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<vector<int> > denseGraph(26, vector<int>(26));
vector<int> history(26, 0);
int pointNum, channelNum, cnt = 0;

void DFS(int p)
{
    if (p == pointNum){
        ++cnt;
        return;
    } 

    for (int c = 1; c <= channelNum; ++c){
        bool flag = true;
        for (int i = 0; i < p; ++i){
            if (denseGraph[i][p] && c == history[i]){
                flag = false;
                break;
            }
        }
        if (flag){
            history[p] = c;
            DFS(p + 1);
        }
    }
}

int main()
{
    while ((cin >> pointNum) && pointNum){
        string sline;
        getline(cin, sline);

        for (int i = 0; i < pointNum; ++i){
            getline(cin, sline);
            int point1 = sline[0] - 'A';
            for (size_t j = 2; j < sline.size(); ++j){
                int point2 = sline[j] - 'A';
                denseGraph[point1][point2] = 1;
                denseGraph[point2][point1] = 1;
            }
        }

        for (int i = 1; i <= 4; ++i){
            channelNum = i;
            DFS(0);
            if (cnt != 0){
                if (i == 1) cout << channelNum << " channel needed." << endl;
                else cout << channelNum << " channels needed." << endl;
                break;
            }
            fill(history.begin(), history.begin() + pointNum, 0);
            cnt = 0;
        }

        fill(history.begin(), history.begin() + pointNum, 0);
        for (int i = 0; i < pointNum; ++i)
            fill(denseGraph[i].begin(), denseGraph[i].begin() + pointNum, 0);
        cnt = 0;
    }

    return 0;
}
```

可以看成是四色问题的变种问题，首先任何图都可以用四色覆盖，所以只需检查1-4的情况。代码其实还可以改进，第四次不需要检查直接输出。

注意点是`getline`函数会把数字末尾的`\n`读取，所以需要多读取一次。输出时候注意单复数的区别。