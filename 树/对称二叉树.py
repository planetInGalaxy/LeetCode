'''
Description: 
Author: Tjg
Date: 2021-06-16 20:24:18
LastEditTime: 2021-06-16 20:36:06
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

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None or root.left == None and root.right == None:
            return True
        else:
            return self.preorderTraversal(root.left,root.right)
        
    def preorderTraversal(self, root_l,root_r):
        if root_l == None and root_r == None:
            return True
        elif root_l == None or root_r == None:
            return False
        elif root_l.val != root_r.val:
            return False
        else:
            return self.preorderTraversal(root_l.left,root_r.right) \
                and self.preorderTraversal(root_l.right,root_r.left)

t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.left = TreeNode(3)
print(t1)
s1 = Solution()
answer = s1.isSymmetric(t1)
print(answer)