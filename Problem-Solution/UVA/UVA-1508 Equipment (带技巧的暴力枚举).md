> # UVA-1508 Equipment (带技巧的暴力枚举)

Links: https://vjudge.net/problem/UVA-1508

----

## Description

The Korea Defense and Science Institute, shortly KDSI, has been putting constant effort into new equipment for individual soldiers for recent years, and at last released N new types of equipment. KDSI has already done evaluation of each of the N types of equipment, finally resulting in scores in five categories: attack improvement, defense improvement, vision improvement, portability, and easiness of usage. The score in each category is quantified as an integer in the range 0 to 10,000, and the rating of each type of equipment is thus represented as a sequence of five integers.

In consideration of costs and capability of average individual soldiers, KDSI also reported that each soldier will be able to install at most K types of equipment on his body to extend his ability. If a single type is installed on a soldier, then his ability in each category is extended by the specified score of that type. Moreover, if a soldier installs more than one type of equipment, then his ability in each category is extended by the maximum score of the chosen types in that category. For example, if the vision improvement scores of type a and type b are 10 and 15, respectively, then installing a combination of two types a and b will result in a vision improvement by their maximum score 15. We call the maximum score 15 the extension score of a category; so, the extension score of vision improvement for combination {a, b} is 15 in this example.

KDSI now started devising a way of finding an optimal combination of K types of equipment for best performance of individual soldiers. While a force can sometimes be of a special purpose so that a certain category would be more important than the others, every single category is, however, regarded equally important in general. For this general purpose, KDSI defined the objective score of a combination of equipment to be the sum of the extension scores of the five categories for the combination. KDSI thus wants to find a best combination of K types of equipment such that its objective score is maximized among all possible combinations of K types. You are asked by KDSI to devise and write a computer program that finds the objective score of a best combination of K types of equipment, that is, the maximum possible objective score for all possible combinations of K types among the given N types of equipment.

Put differently, you are given N types of equipment {1, . . . , N} and their ratings Ri represented by five integers Ri = (ri,1, ri,2, ri,3, ri,4, ri,5) with 0 ≤ ri,j ≤ 10, 000 for each i = 1, . . . , N and j = 1, . . . , 5. Given another natural number K (1 ≤ K ≤ N), your program has to compute the objective score of a best combination of K types of equipment.

For example, consider an input instance in which N = 4, K = 2, and each Ri is given as below:

R1 = (30, 30, 30, 30, 0) 

R2 = (50, 0, 0, 0, 0) 

R3 = (0, 50, 0, 50, 10) 

R4 = (0, 0, 50, 0, 20).

Then, choosing R1 and R3 forms a best combination of two types {1, 3} and yields the objective score 30 + 50 + 30 + 50 + 10 = 170, which will be the answer of a correct program.

## Input

Your program is to read from standard input. The input consists of T test cases. The number T of test cases is given in the first line of the input. From the second line, each test case is given in order, consisting of the following: a test case contains two integers N (1 ≤ N ≤ 10, 000) and K (1 ≤ K ≤ N) in its first line, and is followed by N lines each of which consists of five integers inclusively between 0 and 10,000, representing the five scores ri,1, ri,2, ri,3, ri,4, and ri,5 of each type i of equipment for i = 1, . . . , N in order. Two consecutive integers in one line are separated by a single space and there is no empty line between two consecutive test cases.

## Output

Your program is to write to standard output. Print exactly one line for each test case. The line should contain a single integer that is the objective score of a best combination of K types of equipment; the maximum possible objective score for all possible combinations of K types among the given N types of equipment for the corresponding test case. The following shows sample input and output for two test cases

## Sample Input

```
2
4 2
30 30 30 30 0
50 0 0 0 0
0 50 0 50 10
0 0 50 0 20
5 1
10 20 60 0 0
0 0 20 50 30
30 50 20 20 0
10 10 10 20 30
30 0 20 10 20
```

## Sample Output

```
170
120
```

-----

这道题首先应该判断出，如果`k = 1` 时，选出总和最大的元组即可，如果`k > 5`，那么只需要选出元组每个位置上的最大值，问题的难点在于当`k = 2,3,4,5`的时候，如果直接组合数暴力运算肯定会超时，所以需要换一种思路。

对于每一个元组，可以得到的组合的数量是$2^5 - 1$种，而最后的结果只是得到最大值，所以可以用位运算表示选择的状态，用`11111`表示最初的状态，用`step`表示当前选择的元组的个数，用`state`表示剩余可选的状态。时间复杂度$2^5 \times n$。

```c++
#include <bits/stdc++.h>

using namespace std;


int n, k;

const int INF = 5e8 + 5;
vector<int> seq(5);
vector<int> sum(1 << 5, 0);


int DFS(int step, int state) {
    if (step == k) {
        return state == 0 ? 0 : -INF;
    }

    int res = 0;
    for (int s = state; s > 0; s = (s - 1) & state) {
        res = max(res, DFS(step + 1, state ^ s) + sum[s]);
    }

    return res;
}


void init() {
    fill(sum.begin(), sum.end(), 0);
}


int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int caseNum; cin >> caseNum;
    while (caseNum--) {
        init();

        cin >> n >> k;
        k = min(k, 5);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < 5; ++j) {
                cin >> seq[j];
            }

            for (int s = 0; s < (1 << 5); ++s) {
                int tmp = 0;
                for (int j = 0; j < 5; ++j) {
                    if (s & (1 << j)) {
                        tmp += seq[j];
                    }
                }

                sum[s] = max(sum[s], tmp);
            }
        }

        int res = DFS(0, (1 << 5) - 1);
        cout << res << endl;
    }

    return 0;
}
```

