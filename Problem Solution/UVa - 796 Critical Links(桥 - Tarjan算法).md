> #UVa - 796 Critical Links(桥 - Tarjan算法)

# Description

In a computer network a link L, which interconnects two servers, is considered critical if there are at least two servers A and B such that all network interconnection paths between A and B pass through L.
Removing a critical link generates two disjoint sub–networks such that any two servers of a sub–network are interconnected. For example, the network shown in figure 1 has three critical links that are marked bold: 0 -1, 3 - 4 and 6 - 7.

![1572276807268](F:\学习笔记\c++\藏经阁\assets\1572276807268.png)

It is known that:

1. the connection links are bi–directional;
2. a server is not directly connected to itself;
3. two servers are interconnected if they are directly connected or if they are interconnected with
  the same server;
4. the network can have stand–alone sub–networks.
  Write a program that finds all critical links of a given computer network.

# Input

The program reads sets of data from a text file. Each data set specifies the structure of a network and has the format:
no of servers
server0 (no of direct connections) connected server . . . connected server
. . .
serverno of servers (no of direct connections) connected server . . . connected server
The first line contains a positive integer no of servers(possibly 0) which is the number of network servers. The next no of servers lines, one for each server in the network, are randomly ordered and show the way servers are connected. The line corresponding to server k, 0 ≤ k ≤ no of servers − 1, specifies the number of direct connections of server k and the servers which are directly connected to server k. Servers are represented by integers from 0 to no of servers − 1. Input data are correct. The first data set from sample input below corresponds to the network in figure 1, while the second data set specifies an empty network.

# Output

The result of the program is on standard output. For each data set the program prints the number of critical links and the critical links, one link per line, starting from the beginning of the line, as shown in the sample output below. The links are listed in ascending order according to their first element. The output for the data set is followed by an empty line.

#Sample Input

```
8
0 (1) 1
1 (3) 2 0 3
2 (2) 1 3
3 (3) 1 2 4
4 (1) 3
7 (1) 6
6 (1) 7
5 (0)

0
```

# Sample Output

```
3 critical links
0 - 1
3 - 4
6 - 7

0 critical links
```

---

```c++
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int n, timer;
vector<vector<int>> adj(1001);
vector<bool> visit;
vector<int> low, order;
vector<pair<int, int>> result;

void DFS(int v, int parent = -1)
{
	visit[v] = true;
	order[v] = low[v] = timer++;
	for (auto e : adj[v]){
		if (e == parent) continue;
		if (visit[e]){
			low[v] = min(low[v], order[e]);
		}
		else{
			DFS(e, v);
			low[v] = min(low[v], low[e]);
			if (low[e] > order[v]){
				if (v < e) result.push_back(make_pair(v, e));
				else result.push_back(make_pair(e, v));
			}
		}
	}
}

void findBridge()
{
	for (int i = 0; i < n; ++i){
		if (!visit[i]){
			DFS(i);
		}
	}
	sort(result.begin(), result.end());
	cout << result.size() << " critical links" << endl;
	for (auto e : result)
		cout << e.first << " - " << e.second << endl;
	cout << endl;
}

void init()
{
	timer = 0;
	result.clear();
	low.assign(n, -1);
	order.assign(n, -1);
	visit.assign(n, false);
}

int getVertexNum(string & str)
{
	int length = str.size();
	string tmp = str.substr(1, length - 2);

	return stoi(tmp);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	while (cin >> n) {
		init();
		for (int i = 0; i < n; ++i){
			int point1, vertexNum;
			string str;
            cin >> point1 >> str;
			vertexNum = getVertexNum(str);
			for (int j = 0; j < vertexNum; ++j){
				int point2;
				cin >> point2;
				adj[point1].push_back(point2);
			}
		}
		findBridge();
		for(int i = 0; i < n; ++i)
			adj[i].clear();
	}

	return 0;
}
```

题目本质其实很容易就想到是寻找桥，但是本题细节很多，一个是输入的格式很奇怪，需要一步转化，另一个是输出边的顶点顺序要升序，所有边也要按升序输出，并且结果还要空一行。