> # 树——k-d树

参考资料：

* https://oi-wiki.org/ds/kdt/
* 《挑战程序设计竞赛2-算法和数据结构》

## 基础知识

涉及的知识点，范围搜索，area 搜索。

构建KD tree的时候，用到了替罪羊树，快速选择算法，优化的时候涉及启发式搜索。









## 典型应用

### 平面最近点对

- [x] 洛谷-P1429 平面最近点对（加强版）

这道题不涉及点的增加和删除，所有可以静态构建树。对于节点的设计，维护以当前节点为根的子树中横纵坐标的最小值和最大值`maintain`，如果一个点不在这个范围内，并且距离已经大于目前的最优解，那么其对应的子树也没有必要搜索了。

```c++
#include <bits/stdc++.h>

using namespace std;

enum axis {X, Y};


struct Node {
    double x, y;
    double xMin, xMax, yMin, yMax;
    int left, right;
    axis a;
};


int n;
vector<Node> tree(2e5 + 5);
double res = 2e18;

bool cmpX(Node & a, Node & b) {
    return a.x < b.x;
}

bool cmpY(Node & a, Node & b) {
    return a.y < b.y;
}

void maintain(int root) {
    tree[root].xMin = tree[root].xMax = tree[root].x;
    tree[root].yMin = tree[root].yMax = tree[root].y;
    if (tree[root].left) {
        tree[root].xMin = min(tree[root].xMin, tree[tree[root].left].xMin);
        tree[root].xMax = max(tree[root].xMax, tree[tree[root].left].xMax);
        tree[root].yMin = min(tree[root].yMin, tree[tree[root].left].yMin);
        tree[root].yMax = max(tree[root].yMax, tree[tree[root].left].yMax);
    }
    if (tree[root].right) {
        tree[root].xMin = min(tree[root].xMin, tree[tree[root].right].xMin);
        tree[root].xMax = max(tree[root].xMax, tree[tree[root].right].xMax);
        tree[root].yMin = min(tree[root].yMin, tree[tree[root].right].yMin);
        tree[root].yMax = max(tree[root].yMax, tree[tree[root].right].yMax);
    }
}


int build(int l, int r) {
    if (l >= r) return 0;
    int mid = l + ((r - l) >> 1);
    double averageX = 0, averageY = 0, varX = 0, varY = 0;
    for (int i = l; i <= r; ++i) {
        averageX += tree[i].x;
        averageY += tree[i].y;  
    }
    averageX = averageX / (r - l + 1);
    averageY = averageY / (r - l + 1);
    for (int i = l; i <= r; ++i) {
        varX += (tree[i].x - averageX) * (tree[i].x - averageX);
        varY += (tree[i].y - averageY) * (tree[i].y - averageY);
    }

    if (varX > varY) {
        tree[mid].a = X;
        nth_element(tree.begin() + l, tree.begin() + mid, tree.begin() + r + 1, cmpX);
    }
    else {
        tree[mid].a = Y;
        nth_element(tree.begin() + l, tree.begin() + mid, tree.begin() + r + 1, cmpY);
    }

    tree[mid].left = build(l, mid - 1);
    tree[mid].right = build(mid + 1, r);

    maintain(mid);

    return mid;
}

double dist(int a, int b) {
    return (tree[a].x - tree[b].x) * (tree[a].x - tree[b].x) +
           (tree[a].y - tree[b].y) * (tree[a].y - tree[b].y);
}

double calculateDist(int a, int b) {
    double ans = 0;
    if (tree[b].xMin > tree[a].x) ans += (tree[b].xMin - tree[a].x) * (tree[b].xMin - tree[a].x);
    if (tree[b].xMax < tree[a].x) ans += (tree[b].xMax - tree[a].x) * (tree[b].xMax - tree[a].x);
    if (tree[b].yMin > tree[a].y) ans += (tree[b].yMin - tree[a].y) * (tree[b].yMin - tree[a].y);
    if (tree[b].yMax < tree[a].y) ans += (tree[b].yMax - tree[a].y) * (tree[b].yMax - tree[a].y);
    return ans;
}

void query(int l, int r, int pos) {
    if (l > r) return;

    int mid = l + ((r - l) >> 1);
    if (mid != pos) res = min(res, dist(mid, pos));
    if (l == r) return;

    double leftDist = calculateDist(pos, tree[mid].left);
    double rightDist = calculateDist(pos, tree[mid].right);
    if (leftDist < res) query(l, mid - 1, pos);
    if (rightDist < res) query(mid + 1, r, pos);
}



int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> tree[i].x >> tree[i].y;
    build(1, n);
    for (int i = 1; i <= n; ++i) query(1, n, i);
    cout << fixed << setprecision(4) << sqrt(res) << endl;
    
    return 0;
}
```



### 范围搜索

- [x] AOJ-DSL_2_C: Range Search(KD Tree)

对于某个二维平面上点的集合，列举出给定范围内的点。另外，给定的点集合无法进行点的添加和删除操作。









## 典型题目

- [x] AOJ-DSL_2_C: Range Search(KD Tree)

