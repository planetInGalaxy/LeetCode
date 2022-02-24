'''
Description: 
给出二叉搜索树的根节点，该树的节点值各不相同，
请你将其转换为累加树(Greater Sum Tree)，
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
Author: Tjg
Date: 2022-02-24 20:35:52
LastEditTime: 2022-02-24 20:38:09
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 右节点先的中序遍历
# 时间复杂度O(n) 空间复杂度O(n)
from typing import Optional
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rinorder(root): 
            if root is None:
                return None

            rinorder(root.right)
            nonlocal sum
            sum += root.val
            root.val = sum
            rinorder(root.left)

        sum = 0
        rinorder(root)
        return root