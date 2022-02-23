'''
Description: 
给你二叉树的根节点 root 和一个整数目标和 targetSum ，
找出所有从根节点到叶子节点路径总和等于给定目标和的路径。
叶子节点是指没有子节点的节点。
Author: Tjg
Date: 2022-02-23 22:35:00
LastEditTime: 2022-02-23 22:48:28
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 前序遍历 回溯
# 时间复杂度O(n2) 空间复杂度O(n)
# 在最坏情况下，树的上半部分为链状，
# 下半部分为完全二叉树，并且从根节点
# 到每一个叶子节点的路径都符合题目要求。
# 此时，路径的数目为 O(N)，
# 并且每一条路径的节点个数也为 O(N)，
# 因此要将这些路径全部添加进答案中，时间复杂度为 O(N^2)。
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def preorder(root):
            if root is None:
                return

            path.append(root.val)
            nonlocal sum
            sum += root.val
            if not root.left and not root.right:
                if sum == targetSum:
                    ans.append(path[:])
                
            preorder(root.left)
            preorder(root.right)
            path.pop()
            sum -= root.val
        
        ans = []
        path = []
        sum = 0
        preorder(root)
        return ans