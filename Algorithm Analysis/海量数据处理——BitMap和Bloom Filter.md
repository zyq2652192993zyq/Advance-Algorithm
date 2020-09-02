> # 海量数据处理——BitMap和Bloom Filter

参考资料：

* [Bloom Filter概念和原理](https://blog.csdn.net/jiaomeng/article/details/1495500)
* [使用BloomFilter布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param)

* [布隆过滤器(BloomFilter)原理 实现和性能测试](https://blog.csdn.net/xindoo/article/details/103183445)
* 《编程之法：面试和算法心得》

## 基本概念

Bloom Filter是一种空间效率很高的随机数据结构，它利用位数组很简洁地表示一个集合，并能判断一个元素是否属于这个集合。Bloom Filter的这种高效是有一定代价的：在判断一个元素是否属于某个集合时，有可能会把不属于这个集合的元素误认为属于这个集合（false positive）。因此，Bloom Filter不适合那些“零错误”的应用场合。而在能容忍低错误率的应用场合下，Bloom Filter通过极少的错误换取了存储空间的极大节省。

典型应用场景：

* 网页爬虫对URL的去重，避免爬取相同的URL地址；
* 反垃圾邮件，从数十亿个垃圾邮件列表中判断某邮箱是否垃圾邮箱（同理，垃圾短信）；
* 缓存击穿，将已存在的缓存放到布隆过滤器中。查询一个在缓存内必然不存在的数据，导致每次请求都要去存储层去查询，这样缓存就失去了意义。如果在大流量下数据库可能挂掉。缓存击穿是黑客攻击系统的常用手段。（[缓存穿透、缓存击穿、缓存雪崩区别和解决方案](https://blog.csdn.net/kongtiao5/article/details/82771694)）

经常与Bloom Filter一起提及的还有MD5算法：

* [MD5算法详解](https://blog.csdn.net/goodnameused/article/details/81068697)
* [MD5算法原理及其实现](https://blog.csdn.net/u012611878/article/details/54000607)

## BitMap

> 参考了《编程之法：面试和算法心得》的6.6节。

位图就是用一个`bit`来标记某个元素对应的值，某个`bit`对应的索引就是对应元素实际的数字。

### 典型应用1：数据排序

利用`BitMap`来进行排序类似于桶排序，数值对应的标记为1，比如排序`[4,7,2,5,3]`。

### 典型应用2：电话号码统计

某个文件内包含一些电话号码，每个号码8位数字，统计不同号码的个数。

分析：电话号码的最大可能值为`999999999`，也就是每个位是9，所以最多需要`99999999`位来存储，折合下来需要的内存约为99M。

### 典型应用3：2.5亿数字去重

（1）在2.5亿个数字中找出不重复的数字。

（2）统计2.5亿中不重复的数字个数。假设内存是2G。

分析（1）：假设我们直接在内存里面存储这2.5亿数字，最坏的情况，这2.5亿数字全都不重复，每个`int`类型占32位，相当于4个字节，所以需要$2^{32} \times 2^5 \div 8= 16\text{G}$，很显然内存无法承受。此时对于每个数字让其对应2位，如果没有出现过就是`00`，出现过是`01`，第二次出现标记为`10`，`11`无意义。所以第一次先遍历所有数据进行标记，第二次再遍历一遍位图，把标记是`01`的提取出来进行存储即可。

计算使用位图的内存，存储每个标记占用`1/4`个字节，所以需要$2^{32} \times \frac{1}{4}=1\text{G}$字节。

分析（2）：对于只关心不同的数字的个数，只需要`512M`的内存，因为我们可以设置一个变量`count`来进行计数，并且只需要一个标记位。对于每个数字，如果对应标记位为0，则设置标记位为1，计数器`count`加1；如果标记位为1，则忽略。此时需要的内存$2^{32} \times \frac{1}{8}=512\text{M}$。

### 典型应用4：整数的快速查询

给定40亿个不重复的没排过序的`unsigned int`整数，给定一个`unsigned int`整数，快速判断其是否在这40亿个数里面。

分析：`unsigned int`总共的数据是$2^{32}$个，每个用一个标记位，则需要的内存$2^{32} \times \frac{1}{8}=512\text{M}$。

## Bloom Filter

`Bloom Filter`可以看成是BitMap的扩展，初始状态结构长度为`m`，每一位初始设置为0.

![img](https://p-blog.csdn.net/images/p_blog_csdn_net/jiaomeng/275417/o_bf1.jpg)

当一个元素被加入到集合中时，通过`k`个散列函数将这元素映射到数组中的`k`个点，也就是每个散列函数（`Hash Function`）对于元素映射一个点，`k`个散列函数自然是`k`个点（需要不同散列函数对于同一个元素映射到不同的点才有意义），然后将这`k`位都设置为1。

对于每个位置，如果一个位置多次被设置为1，只有第一次起作用。

![img](https://p-blog.csdn.net/images/p_blog_csdn_net/jiaomeng/275417/o_bf2.jpg)

当判断一个元素`x`是否存在于集合时，用`k`个散列函数计算出映射的位置，如果所有的映射位置全都是1，那么认为这个元素存在于集合里面，但是也可能时误判（false positive）。

### 错误率估计

假设现在有集合$S=\{x_1, x_2, x_3 \cdots ,x_n\}$，集合里面有`n`个元素，设有`k`个散列函数，位图的长度为`m`，为了简化模型，设$kn < m$。















































































