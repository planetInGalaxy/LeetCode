'''
Description: 
Author: Tjg
Date: 2021-08-25 22:11:41
LastEditTime: 2021-08-25 22:57:13
LastEditors: Please set LastEditors
'''
# dfs 回溯 列表转字符串
# 时间复杂度 
# 遍历加拷贝 链表情况 O（n） 平衡二叉树 O（nlogn）
# 转换格式 链表情况O（n） 平衡二叉树 O（nlogn）
# 空间复杂度 链表情况O（n） 平衡二叉树 O（nlogn）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        def dfs(root):
            if not root:
                return 
            path.append(str(root.val))
            # print(path)
            if not root.left and not root.right:
                ans.append(path[:])
                return
            if root.left:
                dfs(root.left)
                path.pop()
            if root.right:
                dfs(root.right)
                path.pop()

        ans = []
        path = []
        dfs(root)
        for i in range(len(ans)):
            ans[i] = "->".join(ans[i])
        return ans
