'''
Description: 
Author: Tjg
Date: 2021-08-21 17:50:14
LastEditTime: 2021-08-21 17:57:49
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def traverse(root,sum):
            if root == None:
                return False
            sum = sum + root.val
            if sum == targetSum and not root.left and not root.right:
                return True
            return traverse(root.left,sum) or traverse(root.right,sum)
        return traverse(root,0)