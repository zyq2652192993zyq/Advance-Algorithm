> #HDU-1003 Max Sum(动态规划 最大连续子序列和)

# Problem Description

Given a sequence a[1],a[2],a[3]......a[n], your job is to calculate the max sum of a sub-sequence. For example, given (6,-1,5,4,-7), the max sum in this sequence is 6 + (-1) + 5 + 4 = 14.

# Input

The first line of the input contains an integer T(1<=T<=20) which means the number of test cases. Then T lines follow, each line starts with a number N(1<=N<=100000), then N integers followed(all the integers are between -1000 and 1000).

# Output

For each test case, you should output two lines. The first line is "Case #:", # means the number of the test case. The second line contains three integers, the Max Sum in the sequence, the start position of the sub-sequence, the end position of the sub-sequence. If there are more than one result, output the first one. Output a blank line between two cases.

# Sample Input

```
2
5 6 -1 5 4 -7
7 0 6 -1 1 -6 7 -5
```

# Sample Output

```
Case 1:
14 1 4

Case 2:
7 1 6
```

---

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int maxSum(vector<int> &nums, int &start, int &end)
{
    int thisSum = nums[0], sum = nums[0];
    int begin = 0, final = 0;

    for (size_t i = 1; i < nums.size(); ++i){
        if (thisSum + nums[i] >= nums[i]){
            thisSum = thisSum + nums[i];
            ++final;
        }
        else{
            thisSum = nums[i];
            begin = final = i;
        }
        
        if (thisSum >= sum){
            sum = thisSum;
            start = begin;
            end = final;
        }
    }

    return sum;
}

int main()
{
    int caseNum;
    cin >> caseNum;
    for (int i = 1; i <= caseNum; ++i){
        int size;
        cin >> size;

        vector<int> nums(size);
        for (int j = 0; j < size; ++j)
            cin >> nums[j];

        int start = 0, end = 0;
        int result = maxSum(nums, start, end);

        cout << "Case " << i << ":" << endl;
        cout << result << " " << (start + 1) << " " << (end + 1) << endl;
        if (i != caseNum) cout << endl;
    }

    return 0;
}
```

动态规划里最大连续子序列和问题，用`begin, final`来记录`thisSum`的起始点和终止点，始终通过`start, end`来记录截至到当前位置的最大连续子序列和的起始点和终止点。注意的是因为下标是从0开始计算，所以输出位置结果需要+1.