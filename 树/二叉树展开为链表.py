'''
Description: 
Author: Tjg
Date: 2021-07-17 10:59:50
LastEditTime: 2021-07-26 11:02:00
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
import turtle


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def drawTree(self):
        def preorderTraversal(root, deg):
            if root == None:
                return
            if root.left:
                turtle.setheading(270)
                turtle.right(deg)
                turtle.pendown()
                turtle.forward(50)
                turtle.write(str(root.left.val))
                preorderTraversal(root.left, deg / 2)
                turtle.setheading(270)
                turtle.right(deg)
                turtle.penup()
                turtle.backward(50)

            if root.right:
                turtle.setheading(270)
                turtle.left(deg)
                turtle.pendown()
                turtle.forward(50)
                turtle.write(str(root.right.val))
                preorderTraversal(root.right, deg / 2)
                turtle.setheading(270)
                turtle.left(deg)
                turtle.penup()
                turtle.backward(50)

        if self != None:
            turtle.right(90)
            turtle.pencolor('red')
            turtle.write(self.val)
            deg = 30
            preorderTraversal(self, deg)
            turtle.down()

    def __repr__(self):
        traversal_pre = []
        traversal_in = []
        traversal_post = []
        self.preorderTraversal(self, traversal_pre)
        self.inorderTraversal(self, traversal_in)
        self.postorderTraversal(self, traversal_post)
        return "->".join((str(i) for i in traversal_pre)) \
            + '\n' + "->".join((str(i) for i in traversal_in)) \
            + '\n' + "->".join((str(i) for i in traversal_post))

    # 前序遍历
    def preorderTraversal(self, root, traversal):
        if root == None:
            return
        traversal.append(root.val)
        self.preorderTraversal(root.left, traversal)
        self.preorderTraversal(root.right, traversal)

    # 中序遍历
    def inorderTraversal(self, root, traversal):
        if root == None:
            return
        self.inorderTraversal(root.left, traversal)
        traversal.append(root.val)
        self.inorderTraversal(root.right, traversal)

    # 后序遍历
    def postorderTraversal(self, root, traversal):
        if root == None:
            return
        self.postorderTraversal(root.left, traversal)
        self.postorderTraversal(root.right, traversal)
        traversal.append(root.val)

# 非原地算法


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten(root, linkedList):
            if root == None:
                return None
            linkedList.right = TreeNode(root.val)
            linkedList = linkedList.right
            if root.left:
                linkedList = flatten(root.left, linkedList)
            if root.right:
                linkedList = flatten(root.right, linkedList)
            return linkedList
        linkedList = TreeNode()
        flatten(root, linkedList)
        return linkedList.right

# 原地算法 非同步


class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

# 原地算法 同步 疑问


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr


s1 = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right = TreeNode(5)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(7)
print(t1)
# t1.drawTree()
answer = s1.flatten(t1)
print(answer)
print(t1)
t1.drawTree()
