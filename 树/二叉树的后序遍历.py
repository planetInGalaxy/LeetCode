'''
Description: 
Author: Tjg
Date: 2021-06-16 16:57:09
LastEditTime: 2021-07-17 11:00:20
LastEditors: Please set LastEditors
'''
'''
Description: 
Author: Tjg
Date: 2021-06-16 16:51:46
LastEditTime: 2021-06-16 16:55:34
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

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        return self.traversal(root,answer)

    def traversal(self,root,answer):
        if root == None:
            return []
        self.traversal(root.left,answer)
        self.traversal(root.right,answer)
        answer.append(root.val)
        return answer

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        stack = []
        node = root
        prev = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev: # 到底了或者从右子树回溯到这儿了
                answer.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return answer


t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)
print(t1)
s1 = Solution()
answer = s1.postorderTraversal(t1)
print(answer)