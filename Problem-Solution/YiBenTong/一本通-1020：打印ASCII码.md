> # 一本通-1020：打印ASCII码

### 【题目描述】

输入一个除空格以外的可见字符（保证在函数scanf中可使用格式说明符%c读入），输出其ASCII码。

### 【输入】

一个除空格以外的可见字符。

### 【输出】

一个十进制整数，即该字符的ASCII码。

### 【输入样例】

A

### 【输出样例】

65

------

```c
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main()
{
	char ch;
	scanf("%c", &ch);
	printf("%d\n", (int)ch);

	return 0;
}
```

