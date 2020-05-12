> # 一本通-1001：Hello,World!

### 【题目描述】

编写一个能够输出“`Hello,World!`”的程序，这个程序常常作为一个初学者接触一门新的编程语言所写的第一个程序，也经常用来测试开发、编译环境是否能够正常工作。

提示：“`Hello,World!`”中间没空格。

### 【输入】

无

### 【输出】

Hello,World!

### 【输入样例】

`（无）`【输出样例】`Hello,World!`

----

```c
#include <stdlib.h>
#include <stdio.h>

int main()
{
	char str[] = "Hello,World!";
	printf("%s\n", str);

	return 0;
}
```

