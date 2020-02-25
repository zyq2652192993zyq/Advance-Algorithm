> # 图算法——最短路--Floyd-Warshall算法

# Floyd-Warshall算法求解全源最短路

Floyd-Warshall算法是用来求解全源最短路问题。

==下面算法存在问题，过不了第一个测试用例==

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 1000000000;

int vertexNum = 3005, edgeNum = 6005;
vector<vector<long long>> d(vertexNum, vector<long long>(vertexNum));

void FloydWarshall()
{
	for (int i = 1; i <= vertexNum; ++i) {
		for (int j = 1; j <= vertexNum; ++j) {
			//不连通的设为1e9
			if (i != j && !d[i][j]) d[i][j] = INF;
		}
	}

	for (int k = 1; k <= vertexNum; ++k) {
		for (int i = 1; i <= vertexNum; ++i) {
			for (int j = 1; j <= vertexNum; ++j) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
}

bool detect()
{
	for (int i = 1; i <= vertexNum; ++i) {
		if (d[i][i] < 0) return false;
	}
	return true;
}

void outputResult()
{
	for (int i = 1; i <= vertexNum; ++i) {
		long long res = 0;
		for (int j = 1; j <= vertexNum; ++j) {
			res += j * d[i][j];
		}
		cout << res << endl;
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
	cin >> vertexNum >> edgeNum;
	for (int i = 1; i <= edgeNum; ++i) {
		int from, to, cost;
		cin >> from >> to >> cost;
		d[from][to] = cost;
	}
	FloydWarshall();
	if (detect()) outputResult();
	else cout << -1 << endl;
	
    return 0;
}
```



# Floyd-Warshall算法求解负环

只需要检测`d[i][i] < 0`是否有成立的。

# 典型题目：

- [ ] HDU 3631
- [ ] POJ 2263
- [ ] POJ 2240
- [ ] HDU 1690
- [ ] HDU 4034
- [ ] POJ 3660
- [ ] POJ 1847
- [ ] HDU 1385
- [ ] POJ 2502
- [ ] HDU 2807
- [ ] HDU 1245
- [ ] POJ 3615
- [ ] POJ 2570
- [ ] HDU 1869
- [ ] HDU 3665
- [ ] POJ 1975
- [ ] POJ 1125