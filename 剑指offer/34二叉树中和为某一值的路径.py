'''
Description: 
Author: Tjg
Date: 2021-10-10 10:24:46
LastEditTime: 2021-10-10 10:38:33
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 时间复杂度O(n) 空间复杂度 最好O(longn) 最坏O(n)
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        def getPath(node, sum):
            if node is None:
                return
            path.append(node.val)
            sum += node.val
            
            if sum == target and not node.left and not node.right:
                ans.append(path[:])
                path.pop()
                return
            
            getPath(node.left, sum)
            getPath(node.right, sum)
            path.pop()
            return
                

        ans = []
        path = []
        getPath(root, 0)
        return ans