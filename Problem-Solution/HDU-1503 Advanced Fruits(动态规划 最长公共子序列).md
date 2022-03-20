> # HDU-1503 Advanced Fruits(动态规划 最长公共子序列)

# Problem Description

The company "21st Century Fruits" has specialized in creating new sorts of fruits by transferring genes from one fruit into the genome of another one. Most times this method doesn't work, but sometimes, in very rare cases, a new fruit emerges that tastes like a mixture between both of them.
A big topic of discussion inside the company is "How should the new creations be called?" A mixture between an apple and a pear could be called an apple-pear, of course, but this doesn't sound very interesting. The boss finally decides to use the shortest string that contains both names of the original fruits as sub-strings as the new name. For instance, "applear" contains "apple" and "pear" (APPLEar and apPlEAR), and there is no shorter string that has the same property.

A combination of a cranberry and a boysenberry would therefore be called a "boysecranberry" or a "craboysenberry", for example.

Your job is to write a program that computes such a shortest name for a combination of two given fruits. Your algorithm should be efficient, otherwise it is unlikely that it will execute in the alloted time for long fruit names.

# Input

Each line of the input contains two strings that represent the names of the fruits that should be combined. All names have a maximum length of 100 and only consist of alphabetic characters.

Input is terminated by end of file.

# Output

For each test case, output the shortest name of the resulting fruit on one line. If more than one shortest name is possible, any one is acceptable.

# Sample Input

```
apple peach
ananas banana
pear peach
```

# Sample Output

```
appleach
bananas
pearch
```

---

```c++
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string s1, s2;

    while (cin >> s1 >> s2){
        vector<string> line(101);
        vector<vector<string>> d(101, line);

        d[0][0] = "";
        for (size_t i = 1; i <= s1.size(); ++i) d[i][0] = s1.substr(0, i);
        for (size_t i = 1; i <= s2.size(); ++i) d[0][i] = s2.substr(0, i);

        for (size_t i = 1; i <= s1.size(); ++i){
            for (size_t j = 1; j <= s2.size(); ++j){
                if (s1[i-1] == s2[j-1]){
                    d[i][j] = d[i-1][j-1];
                    d[i][j].push_back(s1[i-1]);
                } 
                else{
                    if (d[i-1][j].size() < d[i][j-1].size()){
                        d[i][j] = d[i-1][j];
                        d[i][j].push_back(s1[i-1]);
                    } 
                    else{
                        d[i][j] = d[i][j-1];
                        d[i][j].push_back(s2[j-1]);
                    } 
                }
            }
        }

        cout << d[s1.size()][s2.size()] << endl;
    }

    return 0;
}
```

$d[i][j]$表示包含$s1[i], s2[j]$的最短字符串，注意的一点是，在计算$d[i][j]$时，不能直接写`d[i][j] = d[i][j-1].push_back(s1[i-1])`，因为这样$d[i][j-1]$就变了。