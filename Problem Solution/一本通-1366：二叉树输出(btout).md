> # 一本通-1366：二叉树输出(btout)

【题目描述】
树的凹入表示法主要用于树的屏幕或打印输出，其表示的基本思想是兄弟间等长，一个结点的长度要不小于其子结点的长度。二叉树也可以这样表示，假设叶结点的长度为1，一个非叶结点的长度等于它的左右子树的长度之和。

一棵二叉树的一个结点用一个字母表示（无重复），输出时从根结点开始：

每行输出若干个结点字符（相同字符的个数等于该结点长度），如果该结点有左子树就递归输出左子树；如果该结点有右子树就递归输出右子树。

假定一棵二叉树一个结点用一个字符描述，现在给出先序和中序遍历的字符串，用树的凹入表示法输出该二叉树。

【输入】
两行，每行是由字母组成的字符串（一行的每个字符都是唯一的），分别表示二叉树的先序遍历和中序遍历的序列。

【输出】
行数等于该树的结点数，每行的字母相同。

【输入样例】
ABCDEFG
CBDAFEG

【输出样例】
AAAA
BB
C
D
EE
F
G

-----

题目的意思是要根据每个节点的长度然后前序遍历输出，关键点在于如何确定节点长度。在二叉树的每个节点额外保存一个频率信息`freq`，首先是根据前序和中序遍历结果建树，然后递归的去计算节点的频率信息，最后递归实现前序遍历即可。

```c++
#include <bits/stdc++.h>

using namespace std;

string preorder, inorder;

struct TreeNode
{
	char ch;
	int freq;
	TreeNode *left, *right;
	TreeNode(char x): ch(x), freq(0), left(NULL), right(NULL) {}
};


TreeNode *build(int pre_start, int pre_end, int in_start, int in_end)
{
	if (pre_start == pre_end || in_start == in_end) return NULL;

	TreeNode *root = new TreeNode(preorder[pre_start]);
	int pos = inorder.find(preorder[pre_start]);
	int leftSize = pos - in_start;

	root -> left = build(pre_start + 1, pre_start + 1 + leftSize, in_start, pos);
	root -> right = build(pre_start + 1 + leftSize, pre_end, pos + 1, in_end);

	return root;
}


void makeEmpty(TreeNode *&root)
{
	if (root) {
		makeEmpty(root -> left);
		makeEmpty(root -> right);
		delete root;
		root = NULL;
	}
}

void calculateFreq(TreeNode *root)
{
	if (!root) return;
	if (!root -> left && !root -> right) {
		root -> freq = 1;
		return;
	}

	calculateFreq(root -> left); 
	calculateFreq(root -> right);
	root -> freq = (root -> left ? root -> left -> freq : 0) 
		+ (root -> right ? root -> right -> freq : 0);
}

void preorderTraversal(TreeNode *root)
{
	if (!root) return;

	for (int i = 0; i < root -> freq; ++i) {
		cout << root -> ch;
	}
	cout << endl;
	preorderTraversal(root -> left);
	preorderTraversal(root -> right);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> preorder >> inorder;

	TreeNode *root = build(0, preorder.size(), 0, inorder.size());
	calculateFreq(root);

	preorderTraversal(root);

	makeEmpty(root);

	return 0;
}
```

