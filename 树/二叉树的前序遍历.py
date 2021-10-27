'''
Description: 
Author: Tjg
Date: 2021-06-16 16:51:46
LastEditTime: 2021-10-23 18:00:26
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

# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        return self.traversal(root,answer)

    def traversal(self,root,answer):
        if root == None:
            return []
        answer.append(root.val)
        self.traversal(root.left,answer)
        self.traversal(root.right,answer)
        return answer

# 迭代 双重循环
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        stack = []
        node = root
        while node or stack:
            while node:
                answer.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return answer

# 迭代 一重循环
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        answer = []
        stack = [root]
        while stack:
            node = stack.pop()
            answer.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return answer


t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)
print(t1)
s1 = Solution()
answer = s1.preorderTraversal(t1)
print(answer)