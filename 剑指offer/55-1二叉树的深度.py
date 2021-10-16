'''
Description: 
Author: Tjg
Date: 2021-10-16 20:57:36
LastEditTime: 2021-10-16 21:00:03
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的后序遍历 p 272
# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))