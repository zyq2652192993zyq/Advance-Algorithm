> # 一本通-1364：二叉树遍历(flist)

【题目描述】
树和二叉树基本上都有先序、中序、后序、按层遍历等遍历顺序，给定中序和其它一种遍历的序列就可以确定一棵二叉树的结构。

假定一棵二叉树一个结点用一个字符描述，现在给出中序和按层遍历的字符串，求该树的先序遍历字符串。

【输入】
两行，每行是由字母组成的字符串（一行的每个字符都是唯一的），分别表示二叉树的中序遍历和按层遍历的序列。

【输出】
一行，表示二叉树的先序序列。

【输入样例】
DBEAC
ABCDE

【输出样例】

ABDEC

-----

```c++
#include <bits/stdc++.h>

using namespace std;

string inorder, levelorder;
int n;

void solve(int pos, int start, int end)
{
	bool flag = false;
	int j;
	for (int i = pos; i < n; ++i) {
		for (j = start; j <= end; ++j) {
			if (inorder[j] == levelorder[i]) {
				cout << levelorder[i];
				flag = true; break;
			}
		}
		if (flag) break;
	}

	if (start < j) solve(pos + 1, start, j - 1);
	if (j < end) solve(pos + 1, j + 1, end);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> inorder >> levelorder;
	n = inorder.size();
	solve(0, 0, n - 1);

	return 0;
}
```

层序遍历的每一层的节点都是下一层的根节点，以测试用例为例：

首先根据层序遍历的第一个元素可知，A是根节点，然后在中序遍历里找到A，那么A的左边的元素就是左子树的元素，右边的元素是右子树的元素。这里我们判断左右两边是否存在元素，因为如果不存在元素的话，层序遍历的结果里是不会出现的。更确切的讲，比如A的右边无元素，那么意味着层序遍历的结果里第二层只有B一个元素。

用变量`pos`记录上一个根节点的位置，只需要从根节点往后开始寻找即可，比如到了B，位于左子树，只需要从DBE中查找，因为层序遍历是按照每一层元素出现的先后顺序显示的，那么最先匹配的就是先序遍历的根，所以直接输出即可。