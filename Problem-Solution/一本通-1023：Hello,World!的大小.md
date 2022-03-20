> # 一本通-1023：Hello,World!的大小

【题目描述】
我们曾经输出过的“Hello, World!”吗？它虽然不是本章所涉及的基本数据类型的数据，但我们同样可以用sizeof函数获得它所占用的空间大小。

【输入】
(无)

【输出】
一个整数，即“Hello, World!”的大小。

【输入样例】
(无)

【输出样例】
(无)

-----

```c
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main()
{
	char ch[] = "Hello, World!";
	printf("%d\n", (int)sizeof(ch));

	return 0;
}
```

