> # 图算法——LCA

# 二叉搜索树中的LCA

LeetCode 235: 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

 ![img](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

**Example 1:**

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

**Example 2:**

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

 

**Note:**

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the BST.

----

由于**二叉搜索树的特点是左<根<右**，所以根节点的值一直都是中间值，大于左子树的所有节点值，小于右子树的所有节点值，那么我们可以做如下的判断，如果根节点的值大于p和q之间的较大值，说明p和q都在左子树中，那么此时我们就进入根节点的左子节点继续递归，如果根节点小于p和q之间的较小值，说明p和q都在右子树中，那么此时我们就进入根节点的右子节点继续递归，如果都不是，则说明当前根节点就是最小共同父节点，直接返回即可

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        if (root -> val > p -> val && root -> val > q -> val)
            return lowestCommonAncestor(root -> left, p, q);
        else if (root -> val < p -> val && root -> val < q -> val)
            return lowestCommonAncestor(root -> right, p, q);
        return root;
    }
};
```

# 二叉树上的LCA

LeetCode 236:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

 

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

 

**Note:**

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.

------

受到235的启发，虽然变成了二叉树，不再满足左 < 根 < 右的规律，但是核心思想仍然是判断两个节点是在同侧（都在左子树或者都在右子树）。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        bool inLeft1 = findNode(root -> left, p -> val);
        bool inLeft2 = findNode(root -> left, q -> val);
        if (inLeft1 && inLeft2) 
            return lowestCommonAncestor(root -> left, p, q);
        else if (!inLeft1 && !inLeft2 && root -> val != p -> val && root -> val != q -> val) 
            return lowestCommonAncestor(root -> right, p, q);
        return root;
    }

    bool findNode(TreeNode *root, int num)
    {
        if (!root) return false;
        if (root -> val == num) return true;
        return findNode(root -> left, num) || findNode(root -> right, num);
    }
};
```

额外写了个查找函数。发现性能不是太理想：

```
Runtime: 560 ms, faster than 5.10% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 16.7 MB, less than 89.09% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
```

写完发现其实可以不用额外写一个查找函数，直接递归即可。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		cout.tie(NULL);

        if (!root || root == p || root == q) return root;
        TreeNode *l = lowestCommonAncestor(root -> left, p, q);
        TreeNode *r = lowestCommonAncestor(root -> right, p ,q);
        if (l && r) return root;
        return l ? l : r;
    }
};
```

性能立刻提高很多：

```
Runtime: 16 ms, faster than 94.71% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 16.3 MB, less than 100.00% of C++ online submissions for Lowest Common Ancestor of a Binary Tree.
```

