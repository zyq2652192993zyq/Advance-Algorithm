> # GPA

# Problem Description

```
Each course grade is one of the following five letters: A, B, C, D, and F. (Note that there is no grade E.) The grade A indicates superior achievement , whereas F stands for failure. In order to calculate the GPA, the letter grades A, B, C, D, and F are assigned the following grade points, respectively: 4, 3, 2, 1, and 0.
```

# Input

```
The input file will contain data for one or more test cases, one test case per line. On each line there will be one or more upper case letters, separated by blank spaces.
```

# Output

```
Each line of input will result in exactly one line of output. If all upper case letters on a particular line of input came from the set {A, B, C, D, F} then the output will consist of the GPA, displayed with a precision of two decimal places. Otherwise, the message "Unknown letter grade in input" will be printed.
```

# Sample Input

```
A B C D F
B F F C C A
D C E F
```

# Sample Output

```
2.00
1.83
Unknown letter grade in input
```

---

```c++
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    string line;
    while(getline(cin, line)){
        double sum = 0; int cnt = 0;
        bool rule = false;
        for (size_t i = 0; i < line.size(); ++i){
            bool flag = false;
            switch(line[i]){
                case 'A': sum += 4.0; ++cnt; break;
                case 'B': sum += 3.0; ++cnt; break;
                case 'C': sum += 2.0; ++cnt; break;
                case 'D': sum += 1.0; ++cnt; break;
                case 'F': ++cnt; break;
                case ' ': break;
                default:
                    flag = true;
                    rule = true;
                    break;
            }
            if (flag) break;
        }

        if (rule) cout << "Unknown letter grade in input" << endl;
        else{
            cout << fixed << setprecision(2) << sum / cnt << endl;
        }
    }

    return 0;
}
```

注意点：输出保留两位小数，即` cout << fixed << setprecision(2) `的用法。