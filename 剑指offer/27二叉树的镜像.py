'''
Description: 
Author: Tjg
Date: 2021-10-08 14:15:25
LastEditTime: 2021-10-08 14:41:27
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 时间复杂度O(n) 空间复杂度 最坏O（n） 最好O(logn)
# 镜像就是每个节点交换其左右节点
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root