'''
Description: 
Author: Tjg
Date: 2021-07-17 09:45:00
LastEditTime: 2021-07-17 10:36:38
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
# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# BFS
import queue
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = queue.Queue()
        q.put(root)
        depth = 1
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1

s1 = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)
answer = s1.minDepth(TreeNode(1))
print(answer)