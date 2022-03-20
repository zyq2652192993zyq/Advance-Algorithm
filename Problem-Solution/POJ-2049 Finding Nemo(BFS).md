> # POJ-2049 Finding Nemo(BFS)

# Description

Nemo is a naughty boy. One day he went into the deep sea all by himself. Unfortunately, he became lost and couldn't find his way home. Therefore, he sent a signal to his father, Marlin, to ask for help.
After checking the map, Marlin found that the sea is like a labyrinth with walls and doors. All the walls are parallel to the X-axis or to the Y-axis. The thickness of the walls are assumed to be zero.
All the doors are opened on the walls and have a length of 1. Marlin cannot go through a wall unless there is a door on the wall. Because going through a door is dangerous (there may be some virulent medusas near the doors), Marlin wants to go through as few doors as he could to find Nemo.
Figure-1 shows an example of the labyrinth and the path Marlin went through to find Nemo.

![img](http://poj.org/images/2049_1.jpg)

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
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define Max 210 
#define Inf 10000010 //无穷大
int dir[4][2]={{1,0},{-1,0},{0,-1},{0,1}}; //四个搜索方向，上、下、左、右
 
int tran_top[Max][Max];
int tran_low[Max][Max];
int tran_left[Max][Max];
int tran_right[Max][Max];
 
int pos[Max][Max][2];
bool flag[Max][Max];  //记录格点是否搜索
int lowx,lowy,topx,topy; // 迷宫坐下点(lowx,lowy) 右下点(topx,topy)
int tx,ty; //转化后的终点坐标
int Sum; //最终结果
int n,m; 
int h,w; //转化后的方格规格
int get_tran(int x,int y,int index){ // 得到从点（x,y）分别向上、下、左、右方向时遇到的是wall、door还是空
    if(index==0)
        return tran_top[x][y];
    else if(index==1)
        return tran_low[x][y];
    else if(index==2)
        return tran_left[x][y];
    else
        return tran_right[x][y];
}
void dfs(int x,int y,int num){ // dfs搜索最小值
    if(num>=Sum) // 剪枝，若大于最小值，则直接返回
        return ;
    if(x==1 || x==h || y==1 || y==w){ //终点判定，若能到达迷宫外，说明可以找到，逆向搜索
        Sum=num;
        return ;
    }
    for(int i=0;i<4;i++){ //分别搜索四个方向
        int tempx=x+dir[i][0],tempy=y+dir[i][1];
        if(get_tran(x,y,i)==0 && !flag[tempx][tempy]){ //若为door，并且下一步方格没有搜索，则往该方向继续搜索
            flag[tempx][tempy]=true;//设置为已经搜索
            dfs(tempx,tempy,num+1);//继续深搜
            flag[tempx][tempy]=false;//回溯
        }
        else if(get_tran(x,y,i)==-1 && !flag[tempx][tempy]){//若为空，则同上
            flag[tempx][tempy]=true;
            dfs(tempx,tempy,num);
            flag[tempx][tempy]=false;
        }
    }
}
    
int main(){
    while(scanf("%d%d",&n,&m),n!=-1){
        int i,j,tex,tey,ted,tet;
        memset(pos,-1,sizeof(pos)); //初始化为-1
        lowx=lowy=Inf; // 初始化左下点坐标，右上点坐标
        topx=topy=-1;
        for(i=1;i<=n;i++){
            scanf("%d%d%d%d",&tex,&tey,&ted,&tet);
            if(tex<lowx) lowx=tex; //求左下角坐标
            if(tey<lowy) lowy=tey;
            if(!ted){
                if(tex+tet>topx) topx=tex+tet; //右上点坐标
                if(tey>topy) topy=tey;
                for(j=tex;j<tex+tet;j++)  // 设置横向pos
                    pos[j][tey][0]=1;
            }
            else{
                if(tex>topx) topx=tex;
                if(tey+tet>topy) topy=tey+tet;
                for(j=tey;j<tey+tet;j++) //设置纵向pos
                    pos[tex][j][1]=1;
            }
        }
        for(i=1;i<=m;i++){
            scanf("%d%d%d",&tex,&tey,&ted);
            if(tex<lowx) lowx=tex;
            if(tey<lowy) lowy=tey;
            if(!ted){
                if(tex+1>topx) topx=tex+1; 
                if(tey>topy) topy=tey;
                pos[tex][tey][0]=0; //设置横向pos
            }
            else{
                if(tex>topx) topx=tex;
                if(tey+1>topy) topy=tey+1;
                pos[tex][tey][1]=0; // 设置纵向pos
            }
        }
        int ix,iy;
        for(i=lowy;i<topy;i++){ //利用pos将迷宫转化为熟悉的二维方格
            ix=i-lowy+1;
            for(j=lowx;j<topx;j++){
                iy=j-lowx+2;
                tran_top[ix][iy]=tran_low[ix+1][iy]=pos[j][i][0];
                tran_right[ix+1][iy-1]=tran_left[ix+1][iy]=pos[j][i][1];
            }
        }
        h=topy-lowy+2,w=topx-lowx+2; //方格规模
        for(i=lowx;i<topx;i++) // 单独转化特殊情况pos
            tran_top[h-1][i-lowx+2]=tran_low[h][i-lowx+2]=pos[i][topy][0];//=trans[h][i-lowx+2][h-1][i-lowx+2]=pos[i][topy][0];
        for(i=lowy;i<topy;i++)// 单独转化特殊情况pos
            tran_right[i-lowy+2][w-1]=tran_left[i-lowy+2][w]=pos[topx][i][1];//=trans[i-lowy+2][w][i-lowy+2][w-1]=pos[topx][i][1];
        float tempx,tempy;
        scanf("%f%f",&tempx,&tempy);
        if(tempx<=lowx || tempx>=topx || tempy<=lowy || tempy>=topy){ //判断点是否在迷宫内
            printf("0\n");
            continue;
        }
        tx=int(tempy-lowy)+2;
        ty=int(tempx-lowx)+2;
        memset(flag,0,sizeof(flag));
        flag[tx][ty]=1;
        Sum=Inf;
        dfs(tx,ty,0);
        if(Sum==Inf) //若达不到终点
            printf("-1\n");//输出-1
        else //否则输出最小值
            printf("%d\n",Sum);
    }
    return 0;
}
```

给定一个迷宫，给定迷宫的状态，即迷宫的每条单位边可能是wall，也可能是door，也可能是空。这些状态以点加方向加长度的形式给出。并给定搜索的起点和终点。要求出从起点到终点所必须经过的最少door数量。简单的搜索题。

主要是题目中迷宫的状态转化为常规的二维矩阵比较伤脑筋，也比较麻烦，其余的都好解决。

这里转化思路如下:

边分为横向和纵向两种方向，分别用0和1表示。可以事先创建一个三维矩阵pos[i][j][0]表示坐标（i,j）点横向一个单位的迷宫状态，用pos[i][j][1]表示坐标（i,j）点纵向一个单位的迷宫状态。用-1、0、1分别表示是空、door和wall。由于输入中只是输入door和wall的情况，所以可以事先将pos数字设为-1即均为空状态。然后根据输入依次填充pos数组。同时在输入的过程中将迷宫左下点（lowx,lowy)和右上点(topx,topy)的坐标求出来（通过比较，这个容易实现）。接着就进入转化了。转化过程如下：

事先设置四个二维数组，分别为tran_left、tran_right、tran_top、tran_low。设h=topy-lowy+2,w=topx-lowx。转化后的方格为h*w规格（不难想象）。用tran_left数组表示相邻点从左边一个方格到右边一个方格中间的边是wall、door、还是空。依次类推：right、top、low分别表示从右边到左边、从下到上、从上到下中间的边是wall、door、还是空。这个转化通过pos数组进行（不难实现），转化结束。

这里要注意几个问题：

1）由于终点可能并不再迷宫内，故要实现判定终点是否在迷宫内部，如果不再则输出0，否则根据转化后的矩阵dfs或bfs搜索最少值即可

2）根据dfs或bfs搜索最小值，若无法到大终点，则要输出-1，否则输出最小值

3）转化后的矩阵搜索起点应该在终点比较合适（已判定在迷宫内）