> # 字符串算法-字符串HASH

参考资料：

* 邝斌的ACM模板新
* kuangbin专题系列
* [一本通提高篇 哈希和哈希表（一）哈希](https://blog.csdn.net/dhdhdhx/article/details/103149651?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3)

* [一本通提高篇 哈希和哈希表 （二）哈希表](https://blog.csdn.net/dhdhdhx/article/details/103192599?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

* 各种哈希函数的实现：<https://blog.csdn.net/wanglx_/article/details/40300363>

* <https://cloud.tencent.com/developer/article/1092226>

* <https://www.cnblogs.com/-clq/archive/2012/05/31/2528153.html>

* BKDR Hash实现<https://www.cnblogs.com/qq952693358/p/6034875.html>

* 《高级数据结构》林厚从第一章 哈希表
* 《算法竞赛进阶指南》Hash部分

## 哈希函数的构造

构造哈希函数的两个标准：简单和均匀

* 简单：哈希函数的计算要简单快速
* 均匀：对于关键字集合中的任一关键字，哈希函数能以等概率将其映射线性表空间的任何一个位置。

1. 直接定址法（常用）

   以关键字`key`本身或关键字加上某个数值常量C作为哈希地址的方法。$h(key) = key + C$

2. 除余法（常用）

   选择一个适当的正整数$m$，用$m$去除关键字，取余数作为地址。$h(key) = key \% m$。一般选$m$为质数。假设选$m$为合数，那么对于一个关键字$q$满足$GCD(m, q) = d > 1$ ，存在$m = a \times d, q = b \times d$，则$q \% m = q - m \times [q/m] = q - m\times[b/a]$，其中$[b/a]$的取值范围是$[0,b]$，而理想的运算是关键字可以均匀的映射到$[0,m-1]$。所以$m$的约数越多，余数不均匀的情况就越频繁，冲突的几率就越高，一般选$m$为小于某个区域长度的最大素数。

3. 数字分析法

   如果遇到关键字的位数比存储区域的地址位数多，可以对关键字的各个位进行分析，丢掉不均匀的位，适用于对所有关键字已知并且对每一位的取值情况做了统计的。

   |    key    | table |
   | :-------: | :---: |
   | 000319426 |  326  |
   | 000718309 |  709  |
   | 000629443 |  643  |
   | 000758615 |  715  |
   | 000919697 |  997  |
   | 000310329 |  329  |

4. 平方取中法

   将关键字的值平方，然后取中间的几位作为哈希地址，具体取法需要具体问题具体分析。比如

   ```
   0100    0110    1010    1001    0111
   0010000 0012100 1020100 1002001 0012321
   ```

   取表长为1000，则可以取中间的三位`(100,121,201,020,123)`。

5. 折叠法

   如果关键字的位数比存储区域的位数多，并且各位分布比较均匀，不适用于数字分析法，则可以考虑折叠法。折叠法将关键字分为几个部分，所有部分相加，如果最高位存在进位，则丢弃进位。分段取决于存储区域的位数。比如

   ```
   关键字key = 58422241，转换为3位的地址码
   5 8 4
   2 2 2
     4 1
   ------
   8 4 7
   所以h(key) = 847
   ```

6. 基数转换法

   将关键字的值看成另一个基数制的表示，然后转为原来基数制的数，使用数字分析法取其中的几位。一般选择大于原来基数的数作为转换的基数，并且两个基数要互质。另外也可以不用分析法取数字，可以转换后继续利用除余法（一本通提高篇）选数字。

   ```
   key = 236075 --- 10进制
   key' = 236075 --- 13进制 ---> 转为10进制 = 841547
   玄学选择第2，3，4，5位，所以h(key) = 4154
   ```

上面提到的方法属于理论分析，实际上在解决实际问题的时候，常用的方法是**取一固定值$P$，把字符串看成$P$进制数（基数转换法），并对每种字符分配一个大于0的数值（常用就直接利用ASCII码），求出该$P$进制数，然后对一个数$M$取模，作为字符串的哈希值**

根据经验来讲，一般$P=13331或131$，产生哈希值冲突的概率极低，如果哈希值相同，就认为原字符串是相同的。通常取模运算的效率会比较低，通常取$M = 2^{64}$，计算$P$进制数用`unsigned long long`类型，这样溢出后就相当于取模了。

假设已经知道字符串`S`的哈希值`H(S)`，在`S`后面加上一个字符`c`，设`c`分配的数值是`value[c]`，那么哈希值`H(S+c)`为：

```
H(S + c) = (H(S) * P + value[c]) % M
```

如果已经知道字符串`S`的哈希值为`H(S)`，字符串`T`的哈希值是`H(T)`，那么字符串`S+T`的哈希值为：

```
H(S + T) = (H(S) * p^(length(T)) + H(T)) % M
```

核心代码：

```c++
typedef unsigned long long ull;

ull hash[N], p[N];
ull P = 13331;

void calculate(const string & s)
{
	int n = s.size();
	p[0] = 1;

	for (int i = 1; i <= n; ++i) {
		h[i] = h[i - 1] * P + s[i - 1];
		p[i] = p[i - 1] * P;
	}
}

inline ull get(int left, int right)
{
	return h[right] - h[left - 1] * p[right - left + 1]; 
}
```

注意上述核心代码并非一成不变，需要具体问题具体分析，并作出针对性的变化，灵活应用。典型的程序形式可以参见洛谷-P3370 【模板】字符串哈希的写法。






## 冲突的处理

处理冲突的方法：

* 拉链法（Chaining）

参考：https://www.acwing.com/blog/content/404/



* 开地址法（Open Addressing）
  * 线性探查法 （POJ 1186 方程的解数）
  * 二次探查法 （PAT甲级真题1078或AcWing 1564 哈希）
  * 哈希函数探查法



## 构造数据让哈希算法失效

构造数据让哈希算法失效通常不作为一种方法，一般书中都是在冲突的处理部分举几个例子让我们理解哈希可能产生冲突的情况。让哈希失效其实是一种从反面去理解哈希的途径，做题的过程中，我们通常不需要自己构造数据，只需要写出正确的算法，但是在BZOJ的3097，3098，3099这三道题，告诉我们没有一种万能的哈希方法，需要具体问题具体分析。

- [ ] BZOJ 3097（参考了https://www.mina.moe/archives/2391）
- [ ] BZOJ 3098（参考了http://hzwer.com/1861.html）
- [ ] BZOJ 3099 （参考了http://qianxingjian.lofter.com/post/1eb4703f_f978e51）









## 典型应用

### 判断两个字符串是否相同

- [x] 洛谷-P3370 【模板】字符串哈希

给定 N个字符串（第 i 个字符串长度为 $M_i$，字符串内包含数字、大小写字母，大小写敏感），请求出 N 个字符串中共有多少个不同的字符串。

这道题不用处理冲突值，达到了完美哈希。

```c++
#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

vector<ull> hashValue(10005);
ull P = 13331;

ull calculate(const string & s)
{
	int n = s.size();
	ull res = 0;
	for (int i = 0; i < n; ++i) res = res * P + (ull)s[i];

	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int strNum; cin >> strNum;
	string s;

	for (int i = 1; i <= strNum; ++i) {
		cin >> s;
		hashValue[i] = calculate(s);
	}

	sort(hashValue.begin() + 1, hashValue.begin() + 1 + strNum);

	int cnt = 1;
	for (int i = 2; i <= strNum; ++i) {
		if (hashValue[i] != hashValue[i - 1]) ++cnt;
	}

	cout << cnt << endl;

	return 0;
}
```

### 求区间不相同子串个数

- [ ] HDU 4622 Reincarnation

参考链接：https://www.cnblogs.com/liuweimingcprogram/p/5724152.html

最初发现这道题是在《邝斌的ACM模板（新）》字符串哈希一节，其代码里的`head`和`next`数组没有注释可能较难理解，下面做一个解释：

![字符串哈希.png](https://i.loli.net/2020/06/22/iglxELBfuVXZ8vA.png)

一般采用字符串哈希的时候，我们使用`unsigned long long`类型，这是一个很大的范围，当我们又得到一个哈希值的时候，想知道之前是否存在了。一个简单直接的想法是采用直接映射的办法，将得到的哈希值映射到数组的下标，这样如果映射到的数组下标已经有值存在，那么就知道存在重复了。但是这样做很明显，对于很多问题我们无法开那么大的数组，所以一个改进的策略是用一个适当大小的数组来存储，这时候就用哈希值对数组长度取模。

举个例子，比如数组长度是13，我们得到两个不同的哈希值1和14，但是对数组长度取模后都是1，假如先插入1，在插入14的时候发现1所在的位置已经被占据，那么首先比较两个数字是否相等，发现不等，那么如何解决14的插入问题？

一种办法就是模拟拉链法，用数组`s`按顺序接受依次得到哈希值，也就是图中中间的序列，假设哈希值是`val`，让数组`head[val]`指向`val`在数组`s`存储的下标1，`next[1] = 0`代表和`val`对数组长度取模后相同的哈希值不存在。当插入14的时候，我们让`head[14]`指向14存储的下标5，`next`表示的是和他值相同的下一个节点，那么`next[5] = 1`，其他插入以此类推。

起始还存在一个更简单的写法，就是直接使用二维数组，两者思路基本一致。

>  另外这道题的解法不止字符串哈希一种，还可以用后缀数组或者后缀自动机来解决。



### 出现次数大于等于`k`的最长子串

- [ ] HDU-4080 Stammering Aliens



### 求最长回文串

- [ ] POJ-3974 Palindrome



### 二维字符串哈希

一个矩阵只包含0和1，判断一个矩阵是否是另一个矩阵的子矩阵。





### 构建后缀数组

- [ ]   来源《算法竞赛进阶指南》



## 典型问题

- [x] POJ 1186 方程的解数（手写哈希）
- [x] 洛谷-P3370 【模板】字符串哈希
- [x] HDU 2609（最小表示法  + 字符串哈希）
- [ ] HDU 4622 Reincarnation（求区间不相同子串个数）
- [ ] HDU 4080 Stammering Aliens
- [ ] HDU 6208
- [ ] 洛谷-P1275 魔板
- [ ] 「BZOJ2351」 Matrix
- [ ] 「BZOJ3555」[Ctsc2014] 企鹅QQ
- [ ] 「BZOJ4754」独特的树叶
- [ ] 「BZOJ4892」[Tjoi2017]dna
- [ ] 洛谷-P5043 树的同构
- [ ] 洛谷-P2761 程序补丁
- [ ] 洛谷-P1381 单词背诵
- [ ] 洛谷-P3396 
- [ ] 洛谷-P1117 优秀的拆分
- [ ] 洛谷-P2957 谷仓里的回声
- [ ] https://www.cnblogs.com/henry-1202/category/1200785.html
- [ ] 牛客：https://www.nowcoder.com/discuss/178326?type=101
- [ ] POJ 2752
- [ ] POJ 3461
- [ ] POJ 2406
- [ ] POJ 2503
- [ ] POJ 3461
- [ ] HDU 4300
- [ ] HDU 1800
- [ ] HDU 4886
- [ ] HDU 1880
- [ ] HDU 4821