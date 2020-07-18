> # 典型问题——第K大问题

参考资料：

* https://www.cnblogs.com/zhjp11/archive/2010/02/26/1674227.html
* 可持久化数据结构研究，陈立杰

经常遇到一类问题：求一个数组里的第K大的数。衍生的问题，二维有序数组查找第K大的数；动态区间查找第K大的数。

典型题目：

- [x] LeetCode 215  数组中的第K个最大元素
- [x] LeetCode 230 二叉搜索树中第K小的元素  
- [x] LeetCode  347 前 K 个高频元素  （桶排序）
- [ ] LeetCode  373 查找和最小的K对数字
- [x] LeetCode 378 有序矩阵中第K小的元素
- [ ] LeetCode 440 字典序的第K小数字  
- [x] LeetCode  658 找到 K 个最接近的元素  
- [x] LeetCode  668 乘法表中第k小的数（二分查找）  
- [ ] LeetCode  692 前K个高频单词   
- [x] LeetCode  703 数据流中的第K大元素（堆）
- [x] LeetCode  719 找出第 k 小的距离对
- [ ] LeetCode  779 第K个语法符号
- [ ] LeetCode  973 最接近原点的 K 个点  
- [x] LeetCode  1471 数组中的 k 个最强值  （排序）
- [x] LeetCode1483 树节点的第 K 个祖先  （倍增优化）
- [x]  LeetCode  1492 n 的第 k 个因子



## 基本方法

比如`LeetCode 215  数组中的第K个最大元素`，就是一个很典型的对于整个数组进行查找，需要返回的是前`K`个数，方法有很多，但是数据范围不同，可以应用的方法也不同。



### 堆排序

把数据放入优先级队列中，取出K个数即可。时间复杂度$O(k \log n)$。

```c++
//LeetCode 215
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        priority_queue<int> pq(nums.begin(), nums.end());
        int cnt = 0;
        while (cnt++ < k - 1) pq.pop();

        return pq.top();        
    }
};
```

### 快速排序

所有数据排序，通过下标直接求得第K大/小的数。时间复杂度$O(n \log n)$。

```c++
//LeetCode 215
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        sort(nums.begin(), nums.end());
        int n = nums.size();
        return nums[n - k];       
    }
};
```

### 快速选择法

实际上就是修改版的快排。先用枢纽元将数据分割成两部分，然后判断从枢纽元到数组末尾的元素个数：

* 恰好为K，则输出枢纽元
* 大于K，则对右半部分数据递归继续划分
* 小于K，对左半部分找$K - (n - pos)$，`pos`是枢纽元的下标位置。

```c++
//LeetCode 215
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int n = nums.size();
        quickSort(nums, 0, n - 1, k);
        return nums[n - k];     
    }

    void quickSort(vector<int> & nums, int start, int end, int k)
    {
        if (start < end) {
            int pos = partition(nums, start, end);
            int cnt = end - pos + 1;
            if (cnt == k) return;
            else if (cnt < k) quickSort(nums, start, pos - 1, k - cnt);
            else quickSort(nums, pos + 1, end, k);
        }
    }

    int partition(vector<int> & nums, int start, int end)
    {
        int pivot = nums[end];
        int pos = start - 1;
        for (int i = start; i <= end - 1; ++i) {
            if (nums[i] <= pivot) {
                ++pos;
                std::swap(nums[pos], nums[i]);
            }
        }
        std::swap(nums[pos + 1], nums[end]);
        return pos + 1;
    }
};
```

另外还有进一步晚上的BFPRT算法：https://zhuanlan.zhihu.com/p/31498036

### 分桶法

《挑战程序设计竞赛》

- [ ] POJ 2104

* https://blog.csdn.net/yukizzz/article/details/50667752

### 平方割法





### 块状链表

解决动态区间第K大

- [ ] ZOJ 2112 Dynamic Rankings（动态区间第K大）



### 线段树

- [ ] HDU 2852
- [ ] POJ 2985

### 树状数组

能用线段树解决第K大问题，自然会联想到与之关联的树状数组。

### 主席树

* https://blog.csdn.net/DancingZ/article/details/82667957?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2

解决静态区间第K大问题，数据不能动态变化。

### 伸展树（splay tree）

- [x] 洛谷-P1801 黑匣子



### 线性基（第K大异或和）

第K大问题与位运算的结合



### 海量数据top K

在《典型问题——海量数据》里总结。



## 划分树

参考资料：https://www.cnblogs.com/GoldenFingers/archive/2018/08/17/9475172.html















