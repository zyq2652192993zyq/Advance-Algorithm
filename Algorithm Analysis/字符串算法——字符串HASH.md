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

1. 直接定址法

   以关键字`key`本身或关键字加上某个数值常量C作为哈希地址的方法。$h(key) = key + C$

2. 除余法

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

   将关键字的值看成另一个基数制的表示，然后转为原来基数制的数，使用数字分析法取其中的几位。一般选择大于原来基数的数作为转换的基数，并且两个基数要互质。

   ```
   key = 236075 --- 10进制
   key' = 236075 --- 13进制 ---> 转为10进制 = 841547
   玄学选择第2，3，4，5位，所以h(key) = 4154
   ```

## 冲突的处理

处理冲突的方法：

* 拉链法（Chaining）
* 开地址法（Open Addressing）
  * 线性探查法
  * 二次探查法
  * 哈希函数探查法













## 典型应用

- [x] POJ 1186 方程的解数
- [ ] 洛谷-P1275 魔板
- [ ] 一本通-提高篇 哈希与哈希表
- [ ] 「BZOJ2351」 Matrix
- [ ] 「BZOJ3555」[Ctsc2014] 企鹅QQ
- [ ] 「BZOJ4754」独特的树叶
- [ ] 「BZOJ4892」[Tjoi2017]dna
- [ ] 洛谷-P3370 【模板】字符串哈希
- [ ] 洛谷-P5043 树的同构
- [ ] 洛谷-P2761 程序补丁
- [ ] 洛谷-P1381 单词背诵
- [ ] 洛谷-P3396 
- [ ] 洛谷-P1117 优秀的拆分
- [ ] https://www.cnblogs.com/henry-1202/category/1200785.html
- [ ] 牛客：https://www.nowcoder.com/discuss/178326?type=101

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