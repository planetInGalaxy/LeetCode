'''
Description: 
Author: Tjg
Date: 2021-10-08 15:31:15
LastEditTime: 2021-10-08 15:45:26
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O（n）
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compareLeftAndRright(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return compareLeftAndRright(root1.left, root2.right) \
                and compareLeftAndRright(root1.right, root2.left)

        # if root is None:
        #     return True
        # return compareLeftAndRright(root.left, root.right)
        return compareLeftAndRright(root, root)