'''
Description: 
Author: Tjg
Date: 2021-06-25 16:08:28
LastEditTime: 2021-06-25 16:26:48
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        traversal_pre = []
        traversal_in = []
        traversal_post = []
        self.preorderTraversal(self,traversal_pre)
        self.inorderTraversal(self,traversal_in)
        self.postorderTraversal(self,traversal_post)
        return "->".join((str(i) for i in traversal_pre)) \
        + '\n' + "->".join((str(i) for i in traversal_in)) \
        + '\n' + "->".join((str(i) for i in traversal_post))

    # 前序遍历
    def preorderTraversal(self, root,traversal):
        if root == None:
            return 
        traversal.append(root.val)
        self.preorderTraversal(root.left,traversal)
        self.preorderTraversal(root.right,traversal)

    # 中序遍历
    def inorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.inorderTraversal(root.left,traversal)
        traversal.append(root.val)
        self.inorderTraversal(root.right,traversal)

    # 后序遍历
    def postorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.postorderTraversal(root.left,traversal)
        self.postorderTraversal(root.right,traversal)
        traversal.append(root.val)

# 贪心算法 每次选取最中间的作为根节点 递归调用
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def build(l,r):
            mid = l + (r- l) // 2
            node = TreeNode(nums[mid])
            if l <= mid - 1:
                node.left = build(l, mid - 1)
            if r >= mid + 1:
                node.right = build(mid + 1, r)
            return node
        return build(0, len(nums) - 1)
