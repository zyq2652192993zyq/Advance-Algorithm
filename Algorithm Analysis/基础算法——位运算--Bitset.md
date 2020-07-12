> # 基础算法——位运算--Bitset

`bitset`是C++的一种类型，在头文件`<bitset>`里。

* 解决4维及以上的高维偏序问题
* 《算法竞赛入门经典》里的集合生成问题
* OI wiki：https://oi-wiki.org/lang/csl/bitset/
* 《C++ Primer》17.2 `bitset`类型

## 基础知识

### `bitset`类型

通常位运算可以应用于子集生成等场景，可以极大的提高程序的效率，`bitset`类型通过头文件`<bitset>`调用。

内存是按照字节寻址，而不是`bit`，一个`bool`类型的数据，虽然只是表示`0/1`，但是也要占据一个字节。对于4字节的`int`类型，如果只存储`0/1`，那么`bitset`占据的空间只是`int`l类型的`1 / 32`，在某些情况下，可以优化常数。

#### 定义和初始化`bitset`

三种初始化方式：默认初始化，使用`unsigned`值初始化，使用`string`初始化。

`bitset`具有固定的大小，定义时需要声明含有多少个二进制位。在`bitset`对象中，编号为0的位是**低位（lower-order）**，编号最大的（`n - 1`）的是**高位**。

```c++
#include <bits/stdc++.h>

using namespace std;


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    bitset<10> bitvec1;
    cout << bitvec1 << endl; //默认初始化，所有位全是0

    bitset<10> bitvec2(5U);
    cout << bitvec2 << endl; //使用一个unsigned值初始化

    bitset<10> bitvec3("1100");
    cout << bitvec3 << endl;

    string s = "1111";
    bitset<10> bitvec4(s);
    cout << bitvec4 << endl;

    return 0;
}
```

```
# result
0000000000
0000000101
0000001100
0000001111
```

使用字符串初始化需要多注意一些，需要保证字符串里的字符是`0 / 1`，另外就是字符串的下标0对应的是`bitset`的最高位，初始化并不一定需要用整个字符串，使用方法类似于`string`的`substr`。

```c++
//从字符串下标pos开始的len个字符用来初始化
bitset<n> bitvec(string s, int pos, int len);

//从字符串下标pos开始到字符串末尾的字符初始化
bitset<n> bitvec(string s, int pos);
```

#### `bitset`操作

 `count, size, all, any, none`操作不接受参数，`set, reset,flip`比较特殊，不接受参数就是对每一位操作，接收参数`int pos`就是对指定位操作。`all`是C++11新标准的内容。

```c++
#include <bits/stdc++.h>

using namespace std;


int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    bitset<10> bitvec("1100");
    cout << "initial : " << bitvec << endl;

    cout << bitvec.any() << endl; //ture，因为存在是1的位

    cout << bitvec.none() << endl; //false，因为存在是1的位

    cout << bitvec.all() << endl; //false，并不是所有位都使用了,C++11

    cout << bitvec.count() << endl; //设置为1的位数

    cout << bitvec.size() << endl; //bitvec的大小

    cout << bitvec.set() << endl; //所有位设为1，默认是true

    cout << bitvec.reset() << endl; //所有位设为0

    cout << bitvec.set(0) << endl; //最低位设为1

    cout << bitvec.flip() << endl; //所有位取反

    cout << bitvec.to_ulong() << endl; //转换为一个unsigned long类型

    cout << bitvec.to_ullong() << endl; //C++11

    cout << bitvec.to_string() << endl;

    return 0;
}
```

```
initial : 0000001100
1
0
0
2
10
1111111111
0000000000
0000000001
1111111110
1022
1022
1111111110
```

注意到，标准库已经为我们重载了输入输出运算符，所以可以直接`cout`输出`bitset`的值。



## 树分块与`bitset`



## 莫队配合`bitset`



## 解决4维以上的高维偏序



