'''
Description: 
# 相关 0543 二叉树的直径
路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，
达到任意节点的序列。同一个节点在一条路径序列中至多出现一次。
该路径至少包含一个节点，且不一定经过根节点。
路径和是路径中各节点值的总和。
给你一个二叉树的根节点root，返回其最大路径和。
Author: Tjg
Date: 2022-02-03 16:03:42
LastEditTime: 2022-02-03 16:26:21
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 后序遍历
# 注意不一定到叶子节点
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def posterReverse(root):    
            if root is None:
                return 0
            nonlocal maxSum
            left_value = posterReverse(root.left)
            right_value = posterReverse(root.right)
            single_sum = max(left_value, right_value)
            double_sum = left_value + right_value
            # 一共有三种情况，只有一个子树，有两个子树，无子树
            maxSum = max(maxSum, single_sum + root.val, 
                double_sum + root.val, root.val)
            return root.val + (single_sum if single_sum > 0 else 0)

        maxSum = float("-inf")
        posterReverse(root)
        return maxSum

# 官方
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
        
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)
   
        maxGain(root)
        return self.maxSum
