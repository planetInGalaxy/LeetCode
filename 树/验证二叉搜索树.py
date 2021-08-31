'''
Description: 
Author: Tjg
Date: 2021-07-16 18:08:06
LastEditTime: 2021-07-16 18:17:59
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
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBST(root,min,max):
            if root == None:
                return True
            if min != None and min.val >= root.val:
                return False
            if max != None and max.val <= root.val:
                return False
            return isValidBST(root.left,min,root) and isValidBST(root.right,root,max)
        return isValidBST(root,None,None)
        
tree = TreeNode(2.5)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

s1 = Solution()
answer = s1.isValidBST(tree)
print(answer)
