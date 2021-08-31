'''
Description: 
Author: Tjg
Date: 2021-08-31 11:20:02
LastEditTime: 2021-08-31 12:33:34
LastEditors: Please set LastEditors
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代查找
# 满足二叉搜索树规律
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
