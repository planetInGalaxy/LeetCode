'''
Description: 
Author: Tjg
Date: 2022-02-19 20:08:08
LastEditTime: 2022-02-19 20:59:42
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 动态规划 后序遍历
# 时间复杂度O(n) 空间复杂度O(n)
# 因为父节点取决于子节点是否选择
# 所以设立每个节点都有两个状态
# 后面的节点根据左右节点的选择和未选择递推即可
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0, 0

            selected_left, unselected_left = dfs(root.left)
            selected_right, unselected_right = dfs(root.right)

            selected = unselected_left + unselected_right + root.val
            unselected = max(selected_left + selected_right, \
                selected_left + unselected_right, \
                    unselected_left + selected_right, \
                        unselected_left + unselected_right)
            
            return selected, unselected

        selected, unselected = dfs(root)
        return max(selected, unselected)