'''
Description: 
Author: Tjg
Date: 2021-10-16 19:22:14
LastEditTime: 2021-10-16 20:32:15
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

# 二叉搜索树的中序遍历
# 时间复杂度O(k) 空间复杂度 最坏 O(k) 最好O(logk)
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def travel(node):
            # 设定一个返回值
            target = None

            # 先从右遍历
            if node.right:
                target = travel(node.right)

            # k是全局变量，每次遍历到一个节点，就减 1
            nonlocal k
            k -= 1
            print(k, node.val)

            # k为0说明该值是第k大的
            if k == 0:
                target = node
                
            # 如果已经找到了，k 在当前以及回来的过程中是  <= 0的
            # 此时就不要再往深处递归了，应该直接返回
            # 如果未找到则继续中序遍历
            if k > 0 and node.left:
                target = travel(node.left)
            
            # 返回目标值
            return target

        # 输入检测
        if root == None or k <= 0:
            return None

        # 需要返回节点值，而不是节点
        return travel(root).val


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.left.left = TreeNode(1)
tree.left.right = TreeNode(4)
tree.right = TreeNode(6)
'''
5
3 6
24 xx
1
'''

tree = TreeNode(0)
tree.right = TreeNode(1)
tree.right.right = TreeNode(2)
tree.right.right.right = TreeNode(3)


s1 = Solution()
ans = s1.kthLargest(tree, 2)
print(tree)
print(ans)