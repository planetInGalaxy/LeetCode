'''
Description: 
Author: Tjg
Date: 2021-10-21 09:52:04
LastEditTime: 2021-10-21 10:48:09
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 前序遍历 
# 时间复杂度 最坏O(n) 平均O(n) 最好O(1) 
# 空间复杂度 最坏O(n) 平均O(logn) 最好O(1)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        found = self.searchBST(root.left, val)
        if found:
            return found
        else:
            found = self.searchBST(root.right, val)
        return found