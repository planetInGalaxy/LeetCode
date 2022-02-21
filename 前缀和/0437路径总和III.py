'''
Description: 
给定一个二叉树的根节点 root ，和一个整数 targetSum ，
求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，
但是路径方向必须是向下的，只能从父节点到子节点。
Author: Tjg
Date: 2022-02-21 19:44:46
LastEditTime: 2022-02-21 20:39:09
LastEditors: Please set LastEditors
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 前缀和
# 时间复杂度O(n) 空间复杂度O(n)
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root, pre_sum):
            if root is None:
                return 

            pre_sum += root.val
            diff = pre_sum - targetSum
            # print(root.val, pre_sum, diff, pre_sum_map)
            nonlocal ans
            ans += pre_sum_map[diff]
            pre_sum_map[pre_sum] += 1
            
            dfs(root.left, pre_sum)
            dfs(root.right, pre_sum)

            pre_sum_map[pre_sum] -= 1

        ans = 0
        pre_sum_map = defaultdict(int)
        pre_sum_map[0] = 1
        dfs(root, 0)
        return ans
