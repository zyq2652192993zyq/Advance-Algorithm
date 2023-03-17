> #POJ-2049 Finding Nemo(BFS最短路径)

# Description

Nemo is a naughty boy. One day he went into the deep sea all by himself. Unfortunately, he became lost and couldn't find his way home. Therefore, he sent a signal to his father, Marlin, to ask for help.
After checking the map, Marlin found that the sea is like a labyrinth with walls and doors. All the walls are parallel to the X-axis or to the Y-axis. The thickness of the walls are assumed to be zero.
All the doors are opened on the walls and have a length of 1. Marlin cannot go through a wall unless there is a door on the wall. Because going through a door is dangerous (there may be some virulent medusas near the doors), Marlin wants to go through as few doors as he could to find Nemo.
Figure-1 shows an example of the labyrinth and the path Marlin went through to find Nemo.
![img](https://vj.z180.cn/6f22e4b0e6545e9f66d0871df89b552f?v=1577889440)
We assume Marlin's initial position is at (0, 0). Given the position of Nemo and the configuration of walls and doors, please write a program to calculate the minimum number of doors Marlin has to go through in order to reach Nemo.

# Input

The input consists of several test cases. Each test case is started by two non-negative integers M and N. M represents the number of walls in the labyrinth and N represents the number of doors.
Then follow M lines, each containing four integers that describe a wall in the following format:
x y d t
(x, y) indicates the lower-left point of the wall, d is the direction of the wall -- 0 means it's parallel to the X-axis and 1 means that it's parallel to the Y-axis, and t gives the length of the wall.
The coordinates of two ends of any wall will be in the range of [1,199].
Then there are N lines that give the description of the doors:
x y d
x, y, d have the same meaning as the walls. As the doors have fixed length of 1, t is omitted.
The last line of each case contains two positive float numbers:
f1 f2
(f1, f2) gives the position of Nemo. And it will not lie within any wall or door.
A test case of M = -1 and N = -1 indicates the end of input, and should not be processed.

# Output

For each test case, in a separate line, please output the minimum number of doors Marlin has to go through in order to rescue his son. If he can't reach Nemo, output -1.

# Sample Input

```
8 9
1 1 1 3
2 1 1 3
3 1 1 3
4 1 1 3
1 1 0 3
1 2 0 3
1 3 0 3
1 4 0 3
2 1 1
2 2 1
2 3 1
3 1 1
3 2 1
3 3 1
1 2 0
3 3 0
4 3 1
1.5 1.5
4 0
1 1 0 1
1 1 1 1
2 1 1 1
1 2 0 1
1.5 1.7
-1 -1
```

# Sample Output

```
5
-1
```

---

```c++
#include<iostream>
#include<queue>
#include <cstring>
using namespace std;
 
#define MAXV 210
#define INF 1<<29
#define Empty 0
#define Door 1
#define Wall INF
 
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
 
int xa[MAXV][MAXV],ya[MAXV][MAXV];
int dis[MAXV][MAXV];
int dt[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
int xmax,ymax;
 
bool pd(int x,int y){
    if(x>0&&x<=xmax&&y>0&&y<=ymax)  return 1;
    return 0;
}
 
int getvalue(int x,int y,int i){
    if(i == 0)  return ya[x-1][y];
    if(i == 1)  return ya[x][y];
    if(i == 2)  return xa[x][y-1];
    return xa[x][y];
}
 
int bfs(int tx,int ty){
    int i,j,vx,vy,dx,dy,tmp;
    queue<int>q;
    for(i=1;i<=ymax;i++){
        for(j=1;j<=xmax;j++)
            dis[i][j] = INF;
    }
    dis[1][1] = 0;
    q.push(1);
    q.push(1);
    while(!q.empty()){
        vx = q.front(); q.pop();
        vy = q.front(); q.pop();
        for(i=0;i<4;i++){
            dx = vx + dt[i][0];
            dy = vy + dt[i][1];
            tmp = getvalue(vx,vy,i);
            if(pd(dx,dy)&&dis[dx][dy]>dis[vx][vy]+tmp){
                dis[dx][dy] = dis[vx][vy] + tmp;
                q.push(dx);
                q.push(dy);
            }
        }
    }
    return (dis[tx][ty] == INF?-1:dis[tx][ty]);
}
 
int main(){
    int n,m,i,j;
    int x,y,d,t;
    double sx,sy;
    while(cin>>m>>n){
        if(m==-1&&n==-1)    break;
        ymax = xmax = -1;
        memset(xa,Empty,sizeof(xa));
        memset(ya,Empty,sizeof(ya));
        for(i=0;i<m;i++){
            cin>>x>>y>>d>>t;
            if(d == 1){
                for(j=0;j<t;j++)
                    ya[x][y+j+1] = Wall;
                ymax = max(y+t+1,ymax);
                xmax = max(x+1,xmax);
            }
            else{
                for(j=0;j<t;j++)
                    xa[x+j+1][y] = Wall;
                ymax = max(y+1,ymax);
                xmax = max(x+t+1,xmax);
            }
        }
        for(i=0;i<n;i++){
            cin>>x>>y>>d;
            if(d == 1)  ya[x][y+1] = Door;
            else xa[x+1][y] = Door;
        }
        cin>>sx>>sy;
        if(!(sx>=1&&sx<=199&&sy>=1&&sy<=199))
            cout<<0<<endl;
        else{
            cout<<bfs((int)sx+1,(int)sy+1)<<endl;
        }
    }
    return 0;
}
```

题目的一个难点是如何去表示墙壁，这是第一个需要转化的问题。