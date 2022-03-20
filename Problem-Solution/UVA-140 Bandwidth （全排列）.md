> # UVA-140 Bandwidth （全排列）

Given a graph (V, E) where V is a set of nodes and E is a set of arcs in V ×V , and an ordering on the elements in V , then the bandwidth of a node v is defined as the maximum distance in the ordering between v and any node to which it is connected in the graph. The bandwidth of the ordering is then defined as the maximum of the individual bandwidths. For example, consider the graph on the right: This can be ordered in many ways, two of which are illustrated below:

![image-20220108234621356](/Users/yzhang68/Documents/Yuqi/project/Advance-Algorithm/Problem Solution/UVA-140 Bandwidth （全排列）.assets/image-20220108234621356.png)

This can be ordered in many ways, two of which are illustrated below:

![image-20220108234637716](/Users/yzhang68/Documents/Yuqi/project/Advance-Algorithm/Problem Solution/UVA-140 Bandwidth （全排列）.assets/image-20220108234637716.png)

For these orderings, the bandwidths of the nodes (in order) are 6, 6, 1, 4, 1, 1, 6, 6 giving an ordering bandwidth of 6, and 5, 3, 1, 4, 3, 5, 1, 4 giving an ordering bandwidth of 5. Write a program that will find the ordering of a graph that minimises the bandwidth.

## Input

Input will consist of a series of graphs. Each graph will appear on a line by itself. The entire file will be terminated by a line consisting of a single ‘#’. For each graph, the input will consist of a series of records separated by ‘;’. Each record will consist of a node name (a single upper case character in the the range ‘A’ to ‘Z’), followed by a ‘:’ and at least one of its neighbours. The graph will contain no more than 8 nodes.

## Output

Output will consist of one line for each graph, listing the ordering of the nodes followed by an arrow (->) and the bandwidth for that ordering. All items must be separated from their neighbours by exactly one space. If more than one ordering produces the same bandwidth, then choose the smallest in lexicographic ordering, that is the one that would appear first in an alphabetic listing.

## Sample Input

```
A:FB;B:GC;D:GC;F:AGH;E:HD
#
```

## Sample Output

```
A B C F G D H E -> 3
```

-----

提取出所有不重复的字符，然后next_permetation进行全排列。

```c++
#include <bits/stdc++.h>

using namespace std;


string line;
string target;
int res = 8;
unordered_map<char, vector<char>> um;


int cal() {
    int ans = 0;
    for (auto & e : um) {
        char s = e.first;
        int left = find(line.begin(), line.end(), s) - line.begin();
        for (auto & ele : e.second) {
            int right = find(line.begin(), line.end(), ele) - line.begin();
            ans = max(ans, abs(right - left));
        }
    }
    
    return ans;
}


void solve() {
    res = 8;

    unordered_set<char> us;
    for (auto & e : line) {
        if ('A' <= e && e <= 'Z') us.insert(e);
    }

    for (int i = 0; i < line.size(); ++i) {
        int pos = i;
        auto & seq = um[line[i]];
        pos += 2;
        while (pos < line.size() && line[pos] != ';') {
            seq.push_back(line[pos]);
            ++pos;
        }
        i = pos;
    }


    line = string(us.begin(), us.end());
    sort(line.begin(), line.end());

    do {
        int tmp = cal();
        if (tmp < res) {
            res = tmp;
            target = line;
            cout << "res = " << res << endl;
            for (auto & e : target) cout << e << " ";
            cout << endl;
        }
    } while (next_permutation(line.begin(), line.end()));

    for (auto & e : target) {
        cout << e << " ";
    }

    cout << "-> " << res << endl;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (cin >> line) {
        if (line[0] == '#') break;
        solve();
    }

    return 0;
}
```













