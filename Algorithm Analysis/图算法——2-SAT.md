> # 图算法——2-SAT

k-SAT问题大概就是多个0101变量之间存在k元限制求合法解的问题。其中，k元限制指的是:
$$
x_{p_{1}} \oplus x_{p_{2}} \oplus x_{p_{3}} \cdots \oplus x_{p_{k}}=a
$$
其中a是0或者1，而$\oplus$是一种二元bool操作。

k>2的情况已被证明是NP问题，目前只能够暴力枚举来解决。
而当k=2时，存在O（nm）和O（n+m）两种常用做法。O（nm）的做法可以用来解决关于最小字典序解的问题。因为无法通过此题，所以在此只描述O（n+m）的算法。

```c++
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int maxn=10000+10;

struct TwoSAT
{
    int n;
    vector<int> G[maxn*2];
    bool mark[maxn*2];
    int S[maxn*2],c;
 
    bool dfs(int x)
    {
        if(mark[x]) return true;
        if(mark[x^1]) return false;
        mark[x]=true;
        S[c++]=x;
        for(int i=0;i<G[x].size();i++)
            if(!dfs(G[x][i])) return false;
        return true;
    }
 
    void init(int n)
    {
        this->n = n;
        for(int i=0;i<2*n;i++) G[i].clear();
        memset(mark,0,sizeof(mark));
    }
 
    void add_clause(int x,int xval,int y,int yval)
    {
        x=x*2+xval;
        y=y*2+yval;
        G[x^1].push_back(y);
        G[y^1].push_back(x);
    }
 
    bool solve()
    {
        for(int i=0;i<2*n;i+=2)
        if(!mark[i] && !mark[i+1])
        {
            c=0;
            if(!dfs(i))
            {
                while(c>0) mark[S[--c]]=false;
                if(!dfs(i+1)) return false;
            }
        }
        return true;
    }
};
```

典型题目：

- [ ] 洛谷 P4782模板 2-SAT
- [ ] POJ 3207 Ikki's Story IV - Panda's Trick(2-SAT)：圆内外连线问题。
- [ ] POJ 3678 Katu Puzzle(2-SAT)：与或非判断数值。
- [ ] POJ 3683 Priest John's Busiest Day(2-SAT输出方案)：判断区间是否重叠。
- [ ] POJ 3648 Wedding(2-SAT)：婚礼座位安排。
- [ ] POJ 2723 Get Luffy Out(2-SAT)：钥匙开门问题。
- [ ] POJ 2749 Building roads(2-SAT)：如何构建道路。
- [ ] POJ 2296 Map Labeler(2-SAT)：放置正方形。
- [ ] HDU 3062 Party(2-SAT简单题)：夫妻选择出席聚会
- [ ] HDU 1814 Peaceful Commission(2-SAT:最小字典序)：代表参加会议。
- [ ] HDU 3622 Bomb Game(2-SAT+二分)：放置炸弹问题。
- [ ] HDU 3715 Go Deeper(2-SAT)：程序递归深度问题
- [ ] HDU 1824 Let's go home(2-SAT)：队员去留问题。
- [ ] POJ 3905 Perfect Election(简单2-SAT)：选举问题
- [ ] HDU 4115 Eliminate the Conflict (2-SAT)：出拳问题。
- [ ] UVA rectangles
- [ ] code forces the door problem
- [ ] code forces Radio Stations

