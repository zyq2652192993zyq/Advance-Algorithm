> # 数学——Zeller公式

Zeller公式是快速将任意日期转为星期数，在$O(1)$时间内完成。

参考链接：<https://www.cnblogs.com/faterazer/p/11393521.html>
$$
\begin{aligned}
&D=\left[\frac{c}{4}\right]-2 c+y+\left[\frac{y}{4}\right]+\left[\frac{13(m+1)}{5}\right]+d-1\\
&W=D \bmod 7
\end{aligned}
$$

* W是星期数
* c是世纪数减1，也就是年份的前两位
* y 是年份的后两位。
* m 是月份。m 的取值范围是 3 至 14，因为某年的 1、2 月要看作上一年的 13、14月，比如 2019 年的 1 月 1 日要看作 2018 年的 13 月 1 日来计算。
* d 是日数。
* [] 是取整运算。
* mod 是求余运算。