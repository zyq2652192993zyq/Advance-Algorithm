> # 数学——复变函数--快速傅里叶变换（FFT）

参考资料：

* [十分简明易懂的FFT（快速傅里叶变换）](https://blog.csdn.net/enjoy_pascal/article/details/81478582)
* [浅谈FFT、NTT和MTT](https://www.cnblogs.com/Paulliant/p/10254037.html)
* [从多项式乘法到快速傅里叶变换](http://blog.miskcoo.com/2015/04/polynomial-multiplication-and-fast-fourier-transform)
* 《信息学奥赛数学一本通》7.5 快速傅里叶变换

典型题目：

- [ ] CodeForces 444B DZY Loves FFT
- [ ] 洛谷-P4721 [模板] 分治FFT
- [ ] 洛谷-P3803 [模板] 多项式乘法（FFT）
- [ ] 洛谷-P1919 [模板] A*B Problem升级版（FFT快速傅里叶）

## 离散傅里叶变换（DFT）



## 快速傅里叶变换（FFT）

快速傅里叶变换（Fast Fourier Transform）主要作用是用来求卷积（多项式乘法）。朴素多项式乘法为各系数相乘，时间复杂度为$O(n^2)$，使用FFT可以优化到$O(n \log n)$。

### 朴素FFT



### 分治FFT



### 精度优化的FFT（MTT）

对FFT精度进行优化的是毛神仙，所以也叫MTT。



## 快速傅里叶逆变换（IFT）

