'''
Description: 
Author: Tjg
Date: 2021-06-16 16:26:44
LastEditTime: 2021-08-27 16:42:17
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
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        return self.traversal(root,answer)

    def traversal(self,root,answer):
        if root == None:
            return []
        self.traversal(root.left,answer)
        answer.append(root.val)
        self.traversal(root.right,answer)
        return answer

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        stack = []
        node = root
        # 当栈空或节点为None则停止
        while node or stack:
            # 节点一直沿着左子树迭代，每走一步保存节点到栈中，直至叶子节点
            while node:
                stack.append(node)
                node = node.left
            # 取出栈中最后一个节点，即最左节点
            # 保存过的节点已经从栈中pop了，所以不会重复遍历
            node = stack.pop()
            answer.append(node.val)
            # 来到右节点上重复以上迭代流程
            node = node.right
        return answer

t1 = TreeNode(1)
t1.left = TreeNode(4)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)
print(t1)
s1 = Solution()
answer = s1.inorderTraversal(t1)
print(answer)