> # 字符串算法-字符串HASH

https://blog.csdn.net/dhdhdhx/article/details/103149651?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3

选自“邝斌的ACM模板（新）” 

- [ ] POJ 2752
- [ ] POJ 3461
- [ ] POJ 2406
- [ ] POJ 2503
- [ ] POJ 3461
- [ ] HDU 4622
- [ ] HDU 4300
- [ ] HDU 1800
- [ ] HDU 4886
- [ ] HDU 1880
- [ ] HDU 4821

各种哈希函数的实现：<https://blog.csdn.net/wanglx_/article/details/40300363>

<https://cloud.tencent.com/developer/article/1092226>

<https://www.cnblogs.com/-clq/archive/2012/05/31/2528153.html>

BKDR Hash实现<https://www.cnblogs.com/qq952693358/p/6034875.html>

《算法》一书部分内容：

<https://www.cnblogs.com/cjyyb/p/9242149.html>

## 5.1 字符串排序

第一类方法会从右到左检查键中的字符。这种方法一般被称为**低位优先（LSD）**的字符串排序。使用数字（digit）代替字符（character）的原因要追溯到相同方法在各种数字类型中的应用。如果将一个字符串看作一个256进制的数字，那么从右向左检查字符串就等价于先检查数字的最位。这种方法最适合用于键的长度都相同的字符串排序应用。

第二类方法会从左到右检查键中的字符，首先查看的是最高位的字符。这些方法通常称为**高位优先（MSD）**的字符串排序——本节将会学习两种此类算法。高位优先的字符串排序的吸引人之处在于，它们不一定需要检查所有的输入就能够完成排序。高位优先的字符串排序和快速排序类似，因为它们都会将需要排序的数组切分为独立的部分并递归地用相同的方法处理子数组来完成排序。

### 5.1.1 索引计数法

适用于小整数键

**Input**

```
Anderson 2
Brown 3
Davis 3
Garcia 4
Harris 1
Jackson 3
Johnson 4
Jones 3
Martin 1
Martinez 2
Miller 2
Moore 1
Robinson 2
Smith 4
Taylor 3
Thomas 4
Thompson 4
White 2
Williams 3
Wilson 4
```

**Program**

```c++
#include <iostream>
#include <vector>
#include <iomanip>
#include <string>

using namespace std;

struct student{
    string name;
    int group;
    
    student(): name(""), group(0) {}
};

vector<student> a(20), aux(20);
vector<int> cnt(6, 0);

ostream & operator<<(ostream & os, vector<student> & v)
{
    for (auto e : v){ //格式化输出
       os << setiosflags(ios::left) << setw(8) << e.name << "  " << setw(2) << e.group << endl;
    }
   
   return os;
}

int main()
{
    string studentName;
    int studentGroup;
    int i = 0;
   
    while (cin >> studentName >> studentGroup){
        a[i].name = studentName;
        a[i++].group = studentGroup;
        ++cnt[studentGroup + 1]; //输入的同时进行频率统计
    }
   
    for (int i = 1; i <= 5; ++i) //频率转换为索引
        cnt[i] += cnt[i - 1];
        
    for (int i = 0; i < 20; ++i) //数据分类，聚集元素的相对位置无变化
        aux[cnt[a[i].group]++] = a[i];
    
    for (int i = 0; i < 20; ++i) //回写
        a[i] = aux[i];
        
    cout << a;
   
   
   
   return 0;
}
```

```shell
# run result
Harris    1 
Martin    1 
Moore     1 
Anderson  2 
Martinez  2 
Miller    2 
Robinson  2 
White     2 
Brown     3 
Davis     3 
Jackson   3 
Jones     3 
Taylor    3 
Williams  3 
Garcia    4 
Johnson   4 
Smith     4 
Thomas    4 
Thompson  4 
Wilson    4 
```

### 5.1.2 低位优先的字符串排序

这种方法其实和基数排序原理是一致的。

**Input**

```
4PGC938
2IYE230
3CIO720
1ICK750
1OHV845
4JZY524
1ICK750
3CIO720
1OHV845
1OHV845
2RLA629
2RLA629
3ATW723
```

**Program**

```c++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void LSD(vector<string> &a)
{
    int n = a.size();
    vector<string> aux(n);
    
    for (int i = n - 1; i >= 0; --i){
        vector<int> cnt(256 + 1, 0);
        
        for (auto e : a)  //统计频率
            ++cnt[e[i] + 1];
            
        for (int j = 1; j <= 256; ++j)  //频率转为索引
            cnt[j] += cnt[j - 1];
            
        for (auto e : a) //数据分类
            aux[cnt[e[i]]++] = e;
            
        for (int j = 0; j < n; ++j)  //回写
            a[i] = aux[i];
    }
}

ostream & operator<<(ostream & os, vector<string> & a)
{
    for (auto e : a)
        os << e << endl;
        
    return os;
}

int main()
{
    vector<string> a(13);
    string tmp;
    int i = 0;
    
    while (cin >> tmp){
        a[i++] = tmp;
    }
    
    LSD(a);
    
    cout << a;
   
    return 0;
}
```

```shell
# run result
1ICK750
1ICK750
1OHV845
1OHV845
1OHV845
2IYE230
2RLA629
2RLA629
3ATW723
3CIO720
3CIO720
4JZY524
4PGC938
```

### 5.1.3 高位优先的字符串排序（MSD）

高位优先排序其实和普通的排序几乎无差别，所以直接用`STL`版本的排序即可。

**Input**

```
she
sells
seashells
by
the
seashore
the
shells
she
sells
are
surely
seashells
```

**Program**

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

ostream & operator<<(ostream & os, vector<string> & a)
{
    for (auto e : a)
        os << e << endl;
        
    return os;
}

int main()
{
    vector<string> a;
    string tmp;
    
    while (cin >> tmp){
        a.push_back(tmp);
    }
    sort(a.begin(), a.end());
    
    cout << a;
   
    return 0;
}
```

```shell
# run result
are
by
seashells
seashells
seashore
sells
sells
she
she
shells
surely
the
the
```

### 5.1.4 三向字符串快速排序

作为三向字符串快速排序鹤立鸡群的一个示例，我们来考察一个现代系统中的典型数据处理任务。假设你架设了一个网站并希望分析它产生的流量。你可以从系统管理员那里得到网站的所有活动，每项活动的信息中都含有发起者的域名。例如，本书网站上的web.log.txt文件中包含的就是该网站一个星期中的所有活动。为什么三向字符串快速排序能够有效处理这种文件呢？因为排序结果中许多字符串都有**很长的公共前缀**，而这种算法不会重复检查它们。

**Input**

```
edu.princeton.cs 
com.apple 
edu.princeton.cs 
com.cnn 
com.google 
edu.uva.cs 
edu.princeton.cs 
edu.princeton.cs.www
edu.uva.cs 
edu.uva.cs 
edu.uva.cs 
com.adobe 
edu.princeton.ee
```

**Program**

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void sort(vector<string> & a, int lo, int hi, int d)
{
    if (hi <= lo) return;
    int lt = lo, gt = hi;
    int v = a[lo][d];
    int i = lo + 1;
    
    while (i <= gt)
    {
        int t = a[i][d];
        if ( t < v) swap(a[lt++], a[i++]);
        else if (t > v) swap(a[i], a[gt--]);
        else ++i;
    }
    
    sort(a, lo, lt - 1, d);
    //当做为比较值的字符串长度不满足处理时，cmpKey为-1，即该
    //字符串查找已经到了末尾，此时必须加此限制，否则会出现死
    //循环的情况，如下示例所示，如果比较的两个字符串是相同的，
    //会出现i值不断后向移动，当i移动到字符c之后时，两个字符串
    //的之后cmpKey永远恒等于-1。
    if (v >= 0) sort(a, lt, gt, d + 1);
    sort(a, gt + 1, hi, d);
}

void quick3StringSort(vector<string> & a)
{
    sort(a, 0, a.size() - 1, 0);
}

ostream & operator<<(ostream & os, vector<string> & a)
{
    for (auto e : a)
        os << e << endl;
        
    return os;
}

int main()
{
    vector<string> a;
    string tmp;
    
    while (cin >> tmp){
        a.push_back(tmp);
    }
    
    quick3StringSort(a);

    cout << a;
   
    return 0;
}
```

```shell
# run result
com.adobe
com.apple
com.cnn
com.google
edu.princeton.cs
edu.princeton.cs
edu.princeton.cs
edu.princeton.cs.www
edu.princeton.ee
edu.uva.cs
edu.uva.cs
edu.uva.cs
edu.uva.cs
```

在将字符串数组a[]排序时，根据它们的首字母进行三向切分，然后（递归地）将得到的三个子数组排序：一个含有所有首字母小于切分字符的字符串子数组，一个含有所有首字母等于切分字符的字符串的子数组（排序时忽略它们的首字母），一个含有所有首字母大于切分字符的字符串的子数组。