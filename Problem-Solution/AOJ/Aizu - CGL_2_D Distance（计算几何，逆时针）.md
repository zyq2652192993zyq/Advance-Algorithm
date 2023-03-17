> # Aizu - CGL_2_D Distance（计算几何，逆时针）

# Description

![img](F:\Project\Advanced-Algorithm\Problem Solution\19fe6a8e407a242c7b2f1ebce5e2169a)

For given three points p0, p1, p2, print

```
COUNTER_CLOCKWISE
```

if p0, p1, p2 make a counterclockwise turn (1),

```
CLOCKWISE
```

if p0, p1, p2 make a clockwise turn (2),

```
ONLINE_BACK
```

if p2 is on a line p2, p0, p1 in this order (3),

```
ONLINE_FRONT
```

if p2 is on a line p0, p1, p2 in this order (4),

```
ON_SEGMENT
```

if p2 is on a segment p0p1 (5).

# Input

```
xp0 yp0 xp1 yp1
q
xp20 yp20
xp21 yp21
...
xp2q-1 yp2q-1
```

In the first line, integer coordinates of p0 and p1 are given. Then, q queries are given for integer coordinates of p2.

# Output

For each query, print the above mentioned status.

# Constrains

- 1 ≤ q ≤ 1000
- -10000 ≤ xi, yi ≤ 10000
- p0 and p1 are not identical.

# Sample Input

```
0 0 2 0
2
-1 1
-1 -1
```

# Sample Output

```
COUNTER_CLOCKWISE
CLOCKWISE
```

-----

```c++
#include <bits/stdc++.h>

using namespace std;

const double EPS = 1e-7;
inline bool equals(double a, double b) { return fabs(a - b) < EPS; }

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

    bool operator==(const Point & p) const 
    { return fabs(x - p.x) < EPS && fabs(y - p.y) < EPS; }
};

typedef Point Vector;

double cross(const Vector & a, const Vector & b)
{
    return a.x * b.y - a.y * b.x;
}

double dot(const Vector & a, const Vector & b)
{
    return a.x * b.x + a.y * b.y;
}

int main()
{   
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
    Vector a(x2 - x1, y2 - y1);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        double x0, y0; cin >> x0 >> y0;
        Vector b(x0 - x1, y0 - y1);
        if (cross(a, b) > EPS) cout << "COUNTER_CLOCKWISE" << endl;
        else if (cross(a, b) < -EPS) cout << "CLOCKWISE" << endl;
        else {
            if (dot(a, b) < -EPS) {
                cout << "ONLINE_BACK" << endl;
            }
            else if (a.norm() < b.norm()) cout << "ONLINE_FRONT" << endl;
            else cout << "ON_SEGMENT" << endl;
        }
    }   

    return 0;
}
```

`p2`与`p0`和`p1`之间的关系有上图5种情况（根据叉乘符合右手螺旋法则）。

1. `p2`位于逆时针方向；
2. `p2`位于顺时针方向；
3. `p2`位于直线`p0p1`上，顺序为`p2 -> p0 -> p1`；
4. `p2`位于直线`p0p1`上，顺序为`p0 -> p1 -> p2`；
5. `p2`位于直线`p0p1`上，顺序为`p0 -> p2 -> p1`。

设向量`p0p1`为`a`，向量`p0p2`为`b`，则判断方法是：（对应标号）

1. 外积$a \times b$为正，则`b`在`a`的逆时针位置。
2. 外积$a \times b$为负，则`b`在`a`的顺时针位置。
3. 上述两条都不符合，表示`p2`位于`p0p1`的直线上，当内积$a \cdot b$为负的时候，顺序为`p2 -> p0 -> p1`。
4. 上述三条都不符合，如果`b`的大小大于`a`，那么顺序为`p0 -> p1 -> p2`。
5. 如果`b`的大小小于`a`，那么顺序为`p0 -> p2 -> p1`。

这道题思路不难，但是在C++计算浮点数的时候，尤其要注意与`EPS`的比较，负数的时候是小于`-EPS`。