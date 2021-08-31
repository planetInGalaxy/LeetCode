'''
Description: 
Author: Tjg
Date: 2021-08-31 11:20:02
LastEditTime: 2021-08-31 11:45:45
LastEditors: Please set LastEditors
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前序遍历 + 回溯记录路径
# 时间复杂度O（n） 空间复杂度 最坏O（n） 平衡二叉树 O（logn）
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        path = []
        def travel(root):
            path.append(root)
            if root == p or root == q:
                paths.append(path[:])
            if root.left:
                travel(root.left)
                path.pop()
            if root.right:
                travel(root.right)
                path.pop()
        travel(root)
        print(paths)
        i = 0
        while i < len(paths[0]) and i < len(paths[1]):
            if paths[0][i] != paths[1][i]:
                break
            i += 1
        return paths[0][i - 1]

# 后序遍历
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left == None and right == None:
            return None
        elif left != None and right != None:
            return root
        elif left != None:
            return left
        elif right != None:
            return right
        