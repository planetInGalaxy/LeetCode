'''
Description: 
给定两个整数数组 preorder 和 inorder ，
其中 preorder 是二叉树的先序遍历，
inorder 是同一棵树的中序遍历，
请构造二叉树并返回其根节点。
Author: Tjg
Date: 2022-02-23 21:13:46
LastEditTime: 2022-02-23 22:45:09
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


# 前序遍历
# 传入相应的preorder和inorder序列
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def generate(preorder, inorder):
            # print(preorder)
            if preorder == []:
                return None
            if isinstance(preorder, int):
                return TreeNode(preorder)
            
            root_val = preorder[0]
            root = TreeNode(root_val)
            # list查找是index 
            # str查找是find(无则-1) indx(无则error)  
            # 都是找到的第一个子串的首字符下标
            # 还有rfind和rindex，从右开始查找
            idx = inorder.index(root_val)
            root.left = generate(preorder[1:idx + 1], inorder[:idx])
            root.right = generate(preorder[idx + 1:], inorder[idx + 1:])
            
            return root
        
        return generate(preorder, inorder)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s1 = Solution()
ans = s1.buildTree(preorder, inorder)
print(ans)