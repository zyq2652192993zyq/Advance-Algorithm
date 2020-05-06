> # Aizu - CGL_1_B Reflection（计算几何，映像）

# Description

For given three points p1, p2, p, find the reflection point x of p onto p1p2.

![img](F:\Project\Advanced-Algorithm\Problem Solution\ae8472f1d3e07770001735343c4bc00b)

# Input

```
xp1 yp1 xp2 yp2
q
xp0 yp0
xp1 yp1
...
xpq−1 ypq−1
```

In the first line, integer coordinates of p1 and p2 are given. Then, q queries are given for integer coordinates of p.

# Output

For each query, print the coordinate of the reflection point x. The output values should be in a decimal fraction with an error less than 0.00000001.

# Constrains

- 1 ≤ q ≤ 1000
- -10000 ≤ xi, yi ≤ 10000
- p1 and p2 are not identical.

# Sample Input

```
0 0 2 0
3
-1 1
0 1
1 1
```

# Sample Output

```
-1.0000000000 -1.0000000000
0.0000000000 -1.0000000000
1.0000000000 -1.0000000000
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

int main()
{   
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
    Point a(x1, y1), b(x2, y2);
    Vector v1(b.x - a.x, b.y - a.y);
    double len = v1.abs();

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        double x, y; cin >> x >> y;
        Point p(x, y);
        Vector v2(p.x - a.x, p.y - a.y);
        double projection = (v1.x * v2.x + v1.y * v2.y) / len;
        double tx = projection * (b.x - a.x) / len;
        double ty = projection * (b.y - a.y) / len;
        tx += a.x; ty += a.y; //垂线与直线交点
        cout << fixed << setprecision(8) << (2 * tx - x) << ' ' << fixed << setprecision(8) << (2 * ty - y) << endl;
    }

    return 0;
}
```

相当于在Projection的基础上进行变化，垂线的交点是互为对称的两个点的中点。