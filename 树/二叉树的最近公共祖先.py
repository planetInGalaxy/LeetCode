'''
Description: 
Author: Tjg
Date: 2021-08-31 11:50:24
LastEditTime: 2021-10-18 17:32:17
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
        # 只会遇到一次，就是最近的那个公共祖先
        elif left != None and right != None:
            return root
        # 如果只符合一个条件，有两种情况
        # 第一种情况是在找到LCA前，这时候我们返回相应节点表示在该子树中有其中一个节点
        # 第二章情况是在找到LCA后，这时候我们返回相应的公共祖先节点
        elif left != None:
            return left
        elif right != None:
            return right

# 哈希存储父节点