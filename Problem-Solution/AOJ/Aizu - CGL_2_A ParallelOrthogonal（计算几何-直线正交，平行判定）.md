> # Aizu - CGL_2_A Parallel/Orthogonal（计算几何-直线正交，平行判定）

# Description

For given two lines s1 and s2, print "2" if they are parallel, "1" if they are orthogonal, or "0" otherwise.

s1 crosses points p0 and p1, and s2 crosses points p2 and p3.

# Input

The entire input looks like:

```
q (the number of queries)
1st query
2nd query
...
qth query
```

Each query consists of integer coordinates of the points p0, p1, p2, p3 in the following format:

```
xp0 yp0 xp1 yp1 xp2 yp2 xp3 yp3
```

# Output

For each query, print "2", "1" or "0".

# Sample Input

```
3
0 0 3 0 0 2 3 2
0 0 3 0 1 1 1 4
0 0 3 0 1 1 2 2
```

# Sample Output

```
2
1
0
```

-----

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

const double EPS = 1e-7;

class Point
{
public:
	double x, y;

	Point(double x = 0, double y = 0): x(x), y(y) {}

	Point operator+(Point & p) { return Point(x + p.x, y + p.y); }
	Point operator-(Point & p) { return Point(x - p.x, y - p.y); }
	Point operator*(double k) { return Point(x * k, y * k); }
	Point operator/(double k) { return Point(x / k, y / k); }

	double abs() { return sqrt(norm()); }
	double norm() { return x * x + y * y; }

	bool operator<(const Point & p) const { return x != p.x ? x < p.x : y < p.y; }
	bool operator==(const Point & p) const { return fabs(x - p.x) < EPS && fabs(y - p.y) < EPS; }
};

typedef Point Vector;

ostream & operator<<(ostream & os, const Point & p)
{
	os << "("<< p.x << ", " << p.y << ")" << endl;
	return os;
}

double dot(const Vector & a, const Vector & b)
{
	return a.x * b.x + a.y * b.y;
}

double cross(const Vector & a, const Vector & b)
{
	return a.x * b.y - a.y * b.x;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int queryNum;
    cin >> queryNum;
    while (queryNum--) {
    	int a1, b1, a2, b2, a3, b3, a4, b4;
    	cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3 >> a4 >> b4;
    	Vector v1(a2 - a1, b2 - b1), v2(a4 - a3, b4 - b3);
    	int dorRes = dot(v1, v2);
    	int crossRes = cross(v1, v2);
    	if (!dorRes) cout << 1 << endl;
    	else if (!crossRes) cout << 2 << endl;
    	else cout << 0 << endl;
    }	

	return 0;
}
```

直线平行叉积（外积）为0，正交点积（内积）为0。