> # Aizu - CGL_2_B Intersection (计算几何，判断直线相交)

# Description

For given two segments s1 and s2, print "1" if they are intersect, "0" otherwise.

s1 is formed by end points p0 and p1, and s2 is formed by end points p2 and p3.

# Input

The entire input looks like:

```
q (the number of queries)
1st query
2nd query
...
qth query
```

Each query consists of integer coordinates of end points of s1 and s2 in the following format:

```
xp0 yp0 xp1 yp1 xp2 yp2 xp3 yp3
```

# Output

For each query, print "1" or "0".

# Constrains

- 1 ≤ q ≤ 1000
- -10000 ≤ xpi, ypi ≤ 10000
- p0 ≠ p1 and p2 ≠ p3.

# Sample Input

```
3
0 0 3 0 1 1 2 -1
0 0 3 0 3 1 3 -1
0 0 3 0 3 -2 5 0
```

# Sample Output

```
1
1
0
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

int ccw(Point & p0, Point & p1, Point & p2)
{
    Vector a = p1 - p0;
    Vector b = p2 - p0;
    if (cross(a, b) > EPS) return -1;
    else if (cross(a, b) < -EPS) return 1;
    else {
        if (dot(a, b) < -EPS) return 2;
        else if (a.norm() < b.norm()) return -2;
        else return 0;
    }
}

bool intersection(Point & p1, Point & p2, Point & p3, Point & p4)
{
    return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 
        && ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0;
}

int main()
{   
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        double x0, y0, x1, y1, x2, y2, x3, y3;
        cin >> x0 >> y0 >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        Point p1(x0, y0), p2(x1, y1), p3(x2, y2), p4(x3, y3);
        if (intersection(p1, p2, p3, p4)) cout << 1 << endl;
        else cout << 0 << endl;
    }   

    return 0;
}
```

