'''
Description: 
Author: Tjg
Date: 2022-01-08 17:10:34
LastEditTime: 2022-01-08 17:14:51
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 后序遍历：从最底层开始翻转
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def postTravel(node):
            if node is None:
                return None
            postTravel(node.left)
            postTravel(node.right)
            node.left, node.right = node.right, node.left
        
        postTravel(root)
        return root