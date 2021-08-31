'''
Description: 
Author: Tjg
Date: 2021-06-17 10:58:39
LastEditTime: 2021-06-17 11:40:17
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

# 广搜--一个列表存储--力扣上无法通过
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        answer = []
        if root == None:
            return answer
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            answer.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return answer

# 广搜--层次存储--力扣上可以通过
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        answer = []
        if root == None:
            return answer
        q = queue.Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            floor = []
            for _ in range(size):
                node = q.get()
                floor.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            answer.append(floor)
        return answer


t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)
print(t1)
s1 = Solution()
answer = s1.levelOrder(t1)
print(answer)