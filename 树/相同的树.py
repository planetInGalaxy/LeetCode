'''
Description: 
Author: Tjg
Date: 2021-06-16 19:27:14
LastEditTime: 2021-06-16 20:32:56
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        traversal_pre = []
        traversal_in = []
        traversal_post = []
        self.preorderTraversal(self,traversal_pre)
        self.inorderTraversal(self,traversal_in)
        self.postorderTraversal(self,traversal_post)
        return "->".join((str(i) for i in traversal_pre)) \
        + '\n' + "->".join((str(i) for i in traversal_in)) \
        + '\n' + "->".join((str(i) for i in traversal_post))

    # 前序遍历
    def preorderTraversal(self, root,traversal):
        if root == None:
            return 
        traversal.append(root.val)
        self.preorderTraversal(root.left,traversal)
        self.preorderTraversal(root.right,traversal)

    # 中序遍历
    def inorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.inorderTraversal(root.left,traversal)
        traversal.append(root.val)
        self.inorderTraversal(root.right,traversal)

    # 后序遍历
    def postorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.postorderTraversal(root.left,traversal)
        self.postorderTraversal(root.right,traversal)
        traversal.append(root.val)

# 深度优先搜索 存于列表
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        traversal_p = []
        traversal_q = []
        self.preorderTraversal(p,traversal_p)
        self.preorderTraversal(q,traversal_q)
        if traversal_p == traversal_q:
            return True
        else:
            return False

    def preorderTraversal(self, root,traversal):
        if root == None:
            traversal.append(None)
            return 
        traversal.append(root.val)
        self.preorderTraversal(root.left,traversal)
        self.preorderTraversal(root.right,traversal)

# 深度优先搜索 不用额外存储空间
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)

t2 = TreeNode(1)
t2.right = TreeNode(2)
t2.right.left = TreeNode(3)
print(t1)
print(t2)
s1 = Solution()
answer = s1.isSameTree(t1,t2)
print(answer)