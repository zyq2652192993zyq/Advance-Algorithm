> # ALGOSPORT-CLOCKSYNC （暴力枚举）

Links: https://algospot.com/judge/problem/read/CLOCKSYNC

----

#### Problem



![judge-attachments/d3428bd7a9a425b85c9d3c042b674728/clocks.PNG](http://algospot.com/media/judge-attachments/d3428bd7a9a425b85c9d3c042b674728/clocks.PNG)

As shown in the figure, there are 16 clocks arranged in a 4 x 4 grid. These clocks all indicate 12, 3, 6, or 9 o'clock. I want to change these clocks to all point to 12 o'clock.

The only way to manipulate the clock's time is to operate all 10 switches, each of which is connected to as few as 3 to as many as 5 clocks. Each time a switch is pressed, the time of the clocks connected to that switch moves forward by 3 hours. Here is a list of switches and the clocks to which they are connected.

| 0    | 0, 1, 2         |
| ---- | --------------- |
| 1    | 3, 7, 9, 11     |
| 2    | 4, 10, 14, 15   |
| 3    | 0, 4, 5, 6, 7   |
| 4    | 6, 7, 8, 10, 12 |
| 5    | 0, 2, 14, 15    |
| 6    | 3, 14, 15       |
| 7    | 4, 5, 7, 14, 15 |
| 8    | 1, 2, 3, 4, 5   |
| 9    | 3, 4, 5, 9, 13  |

Assume that the clocks are numbered sequentially from the top row, from left to right. Write a program that counts the number of switches that must be pressed at least to set all clocks to 12 o'clock, given the times currently indicated by the clocks.

#### input

The first line gives the number of test cases C (<= 30).
Each test case is given as 16 integers per line, and each integer represents the time indicated by each clock from 0 to 15 as one of 12, 3, 6, or 9.

#### Print

Print one line for each test case. Prints the minimum number of switches that must be pressed to return all clocks to 12 o'clock. If this is not possible, -1 is output.

#### example input

```
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6
```

#### example output

```
2
9
```

------

对于每个开关，旋转4次和不旋转的效果是一样的，所以其实旋转的次数只会是0-3，于是对于每个开关，总共有四种选择，一共10个开关，总的时间复杂度为$4^{10}$，可以接受。

记得每次旋转完成后需要恢复之前的状态，以及中途就发现已经满足条件，可以提前停止。

```c++
#include <bits/stdc++.h>

using namespace std;

vector<int> seq(16);


unordered_map<int, vector<int>> um {
    {0, {0, 1, 2}},
    {1, {3, 7, 9, 11}},
    {2, {4, 10, 14, 15}}, 
    {3, {0, 4, 5, 6, 7}},
    {4, {6, 7, 8, 10, 12}},
    {5, {0, 2, 14, 15}},
    {6, {3, 14, 15}},
    {7, {4, 5, 7, 14, 15}},
    {8, {1, 2, 3, 4, 5}},
    {9, {3, 4, 5, 9, 13}}
};


int DFS(int changeNum, int times, int step) {
    if (changeNum >= 10) {
        for (auto & e : seq) {
            if (e != 12) return -1;
        }

        return step;
    }

    auto & vec = um[changeNum];
    for (auto & e : vec) {
        seq[e] += 3 * times;
        seq[e] %= 12;
        if (seq[e] == 0) seq[e] = 12;
    }
    if (accumulate(seq.begin(), seq.end(), 0) == 16 * 12) return step + times;

    int res = INT_MAX;
    for (int i = 0; i < 4; ++i) {
        int tmp = DFS(changeNum + 1, i, step + times);
        if (tmp == -1) continue;
        res = min(res, tmp);
    }

    for (auto & e : vec) {
        seq[e] -= 3 * times;
        if (seq[e] < 0) seq[e] += 12;
        seq[e] %= 12;
        if (seq[e] == 0) seq[e] = 12;
    }    

    return res == INT_MAX ? -1 : res;
}


int solve() {
    int res = INT_MAX;
    for (int i = 0; i < 4; ++i) {
        int tmp = DFS(0, i, 0);
        if (tmp == -1) continue;
        res = min(res, tmp);
    }

    return res == INT_MAX ? -1 : res;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        for (int i = 0; i < 16; i++) {
            cin >> seq[i];
        }

        cout << solve() << endl;
    }

    return 0;
}
```

上面的方法需要进行状态恢复，另外一种不需要进行状态恢复的方法：

```c++
#include <bits/stdc++.h>

using namespace std;

vector<int> seq(16);


unordered_map<int, vector<int>> um {
    {0, {0, 1, 2}},
    {1, {3, 7, 9, 11}},
    {2, {4, 10, 14, 15}}, 
    {3, {0, 4, 5, 6, 7}},
    {4, {6, 7, 8, 10, 12}},
    {5, {0, 2, 14, 15}},
    {6, {3, 14, 15}},
    {7, {4, 5, 7, 14, 15}},
    {8, {1, 2, 3, 4, 5}},
    {9, {3, 4, 5, 9, 13}}
};

const int MAX = 100;


void push(int changNum) {
    for (auto & e : um[changNum]) {
        seq[e] += 3;
        seq[e] %= 12;
        if (seq[e] == 0) seq[e] = 12;
    }
}

int solve(int changNum) {
    if (changNum >= 10) {
        for (auto & e : seq) {
            if (e != 12) return MAX;
        }

        return 0;
    }

    int res = MAX;
    for (int i = 0; i < 4; ++i) {      
        res = min(res, i + solve(changNum + 1));
        push(changNum);
    }

    return res;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        for (int i = 0; i < 16; i++) {
            cin >> seq[i];
        }

        int res = solve(0);
        cout << (res >= MAX ? -1 : res) << endl;
    }

    return 0;
}
```

注意这里push的时候每次增加的数量是3，所以需要在计算res的后面，这样才能描述没有修改的状态。