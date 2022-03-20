> # HDU-1062 Text Reverse（split函数）

# Problem Description

```
Ignatius likes to write words in reverse way. Given a single line of text which is written by Ignatius, you should reverse all the words and then output them.
```

# Input

```
The input contains several test cases. The first line of the input is a single integer T which is the number of test cases. T test cases follow.
Each test case contains a single line with several words. There will be at most 1000 characters in a line.
```

# Output

```
For each test case, you should output the text which is processed.
```

# Sample Input

```
3
olleh !dlrow
m'I morf .udh
I ekil .mca
```

# Sample Output

```
hello world!
I'm from hdu.
I like acm.

Hint

Remember to use getchar() to read '\n' after the interger T, then you may use gets() to read a line and process it.
```

---

```c++
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
int main(void)
{
    int t,loc;
    cin>>t;
    getchar();
    string s1;    
    while (t--)
    {
        getline(cin,s1);
        loc=0;
        while (s1.find(" ",loc)!=string::npos)//反转前n-1个单词
        {
            reverse( s1.begin()+loc , s1.begin()+s1.find(" ",loc) );
            loc=s1.find(" ",loc)+1;//更新每次反转的begin位置
        }
        reverse( s1.begin()+s1.find_last_of(" ")+1 , s1.end() );//反转最后一个单词
        cout<<s1<<endl;
    }
    return 0;
}

```

相似问题：split函数的实现。拓展点，reverse函数的STL代码。