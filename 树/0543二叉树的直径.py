'''
Description: 
Author: Tjg
Date: 2022-01-09 16:55:49
LastEditTime: 2022-01-09 17:08:34
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 后序遍历
# 先求左右子节点的深度值，radis即为各个节点的左右子节点深度之和的最大值
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def postOrderTravel(node):
            if node is None:
                return 0
            
            leftDepth = postOrderTravel(node.left)
            rightDepth = postOrderTravel(node.right)
            depth = max(leftDepth, rightDepth) + 1
            currentRadis = leftDepth + rightDepth
            nonlocal radis
            radis = max(radis, currentRadis)
            return depth

        radis = 0
        postOrderTravel(root)
        return radis