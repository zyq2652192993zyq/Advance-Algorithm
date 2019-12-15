> # HDU-3849 By Recognizing These Guys, We Find Social Networks Useful(桥，Tarjan算法)

# Problem Description

Social Network is popular these days.The Network helps us know about those guys who we are following intensely and makes us keep up our pace with the trend of modern times.
But how?
By what method can we know the infomation we wanna?In some websites,maybe Renren,based on social network,we mostly get the infomation by some relations with those "popular leaders".It seems that they know every lately news and are always online.They are alway publishing breaking news and by our relations with them we are informed of "almost everything".
(Aha,"almost everything",what an impulsive society!)
Now,it's time to know what our problem is.We want to know which are the key relations make us related with other ones in the social network.
Well,what is the so-called key relation?
It means if the relation is cancelled or does not exist anymore,we will permanently lose the relations with some guys in the social network.Apparently,we don't wanna lose relations with those guys.We must know which are these key relations so that we can maintain these relations better.
We will give you a relation description map and you should find the key relations in it.
We all know that the relation bewteen two guys is mutual,because this relation description map doesn't describe the relations in twitter or google+.For example,in the situation of this problem,if I know you,you know me,too.

# Input

The input is a relation description map.
In the first line,an integer t,represents the number of cases(t <= 5).
In the second line,an integer n,represents the number of guys(1 <= n <= 10000) and an integer m,represents the number of relations between those guys(0 <= m <= 100000).
From the second to the (m + 1)the line,in each line,there are two strings A and B(1 <= length[a],length[b] <= 15,assuming that only lowercase letters exist).
We guanrantee that in the relation description map,no one has relations with himself(herself),and there won't be identical relations(namely,if "aaa bbb" has already exists in one line,in the following lines,there won't be any more "aaa bbb" or "bbb aaa").
We won't guarantee that all these guys have relations with each other(no matter directly or indirectly),so of course,maybe there are no key relations in the relation description map.

# Output

In the first line,output an integer n,represents the number of key relations in the relation description map.
From the second line to the (n + 1)th line,output these key relations according to the order and format of the input.

# Sample Input

```
1
4 4
saerdna aswmtjdsj
aswmtjdsj mabodx
mabodx biribiri
aswmtjdsj biribiri
```

# Sample Output

```
1
saerdna aswmtjdsj
```

----

```c++
#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
const int maxn=10000+10;
const int maxm=100000+10;
int n,m;
struct node
{
    char s[20];
    bool operator <(const node& rhs)const
    {
        return strcmp(s,rhs.s)<0;
    }
};
map<node,int> mp;//将字符串node映射成节点编号
struct Edge
{
    node u,v;
    bool flag;//标记该边是不是桥
}e[maxm];
vector<int> G[maxn];
int pre[maxn],low[maxn];
int dfs_clock;
void tarjan(int u,int fa)
{
    low[u]=pre[u]=++dfs_clock;
    for(size_t i=0;i<G[u].size();i++)
    {
        int v=G[u][i];
        if(v==fa) continue;
        if(!pre[v])
        {
            tarjan(v,u);
            low[u]=min(low[u],low[v]);
        }
        else low[u] = min(low[u],pre[v]);
    }
}
int main()
{
    int T; scanf("%d",&T);
    while(T--)
    {
        int id=0;
        scanf("%d%d",&n,&m);
        mp.clear();
        dfs_clock=0;
        memset(pre,0,sizeof(pre));
        for(int i=1;i<=n;i++) G[i].clear();
        for(int i=0;i<m;i++)
        {
            e[i].flag=false;
            scanf("%s%s",e[i].u.s,e[i].v.s);
            if(mp.find(e[i].u)==mp.end()) mp[e[i].u]= ++id;
            if(mp.find(e[i].v)==mp.end()) mp[e[i].v]= ++id;
            int x = mp[e[i].u], y=mp[e[i].v];
            G[x].push_back(y);
            G[y].push_back(x);
        }
        tarjan(1,-1);
        bool ok=true;//判断是否连通图
        for(int i=1;i<=n;i++)if(!pre[i])
        {
            ok=false;
            break;
        }
        if(!ok) printf("0\n");
        else
        {
            int ans=0;//计数桥总数
            for(int i=0;i<m;i++)
            {
                int u=mp[e[i].u], v=mp[e[i].v];
                if(low[u]>pre[v]||low[v]>pre[u]) e[i].flag=true,ans++;
            }
            printf("%d\n",ans);
            for(int i=0;i<m;i++)if(e[i].flag)
                printf("%s %s\n",e[i].u.s,e[i].v.s);
        }
    }
    return 0;
}
```

