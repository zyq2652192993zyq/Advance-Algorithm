> # 分治法- CDQ

典型题目：

<https://www.cnblogs.com/flashhu/p/9381075.html>

<https://zhuanlan.zhihu.com/p/55322598> CDQ与整体二分

https://www.bilibili.com/video/BV1y4411k7qk

https://www.luogu.com.cn/training/2971

cdq 分治是一种重要的分治思路，例如归并排序求逆序对就是 cdq 分治的思想。

二维数点即在给定的二维区间中对点进行统计，可以用 cdq 分治或主席树来实现，待修的则有对应的 cdq 套 cdq，cdq 套树，以及树套树的做法。

P3810 【模板】三维偏序（陌上花开）（三维偏序模板，可用 cdq 套树状数组或 cdq 套 cdq）

P5621 [DbOI2019] 德丽莎世界第一可爱（四维偏序模板，可用 cdq 套 cdq 套树状数组或 cdq 套树状数组套线段树等解决）

P5445 [APIO2019] 路灯（区间修改的二维数点，注意差分可以让你直接用树状数组套权值线段树维护）

P5044 [IOI2018] meetings 会议（笛卡尔树上的 DP，用线段树优化）

P4899 [IOI2018] werewolf 狼人（建最小最大两个点 Kruskal 重构树后转化成二维数点）