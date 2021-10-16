'''
Description: 
Author: Tjg
Date: 2021-10-11 11:38:25
LastEditTime: 2021-10-16 21:16:25
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

import collections
class Codec:
    def serialize(self, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        print('[' + ','.join(res) + ']')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]":
            return

        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


root = "[1,2,3,null,null,4,5,null,null,null,null]"
s1 = Codec()
tree = s1.deserialize(root)
print(tree)
ls = s1.serialize(tree)
print(ls)

# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/
