'''
Description: 
Author: Tjg
Date: 2021-10-05 22:35:07
LastEditTime: 2021-10-05 23:13:38
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

# 时间复杂度O(n2) 空间复杂度O(n) p63
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def build(start1, start2, length):
            if length <= 0:
                return
            root = preorder[start1]
            node = TreeNode(root)
            left_length = 0
            for i in range(start2, start2 + length):
                if inorder[i] != root:
                    left_length += 1
                else:
                    break
            right_length = length - left_length - 1

            node.left = build(start1 + 1, start2, left_length)
            node.right = build(start1 + left_length + 1, start2 + left_length + 1, right_length)
            return node
        
        if not preorder:
            return None 
        root = build(0, 0, len(preorder))
        return root

# 利用哈希表改进
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def build(start1, start2, length):
            if length <= 0:
                return
            root = preorder[start1]
            node = TreeNode(root)
            
            root_index = index[root]
            left_length = root_index - start2
            right_length = length - left_length - 1

            node.left = build(start1 + 1, start2, left_length)
            node.right = build(start1 + left_length + 1, start2 + left_length + 1, right_length)
            return node
        
        if not preorder:
            return None
        index = {element: i for i, element in enumerate(inorder)}
        root = build(0, 0, len(preorder))
        return root

# 官方
# 利用哈希表
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s1 = Solution()
ans = s1.buildTree(preorder, inorder)
print(ans)