'''
Description: 
Author: Tjg
Date: 2021-10-18 16:20:05
LastEditTime: 2021-10-18 17:46:54
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

# 剑指offer 330
# 先遍历二叉树求出两条路径，在求最后公共节点
# 时间复杂度 最好O(logn) 最坏O(n) 空间复杂度同
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getCommonNode(path1, path2):
            index = 0
            while index < len(path1) and index < len(path2) \
                and path1[index] == path2[index]:
                index += 1
            return path1[index - 1]
            
        def getPath(root, node):
            if root is None:
                return False

            path.append(root)
            # print(path)
            
            if root == node:
                paths.append(path[:])
                path.pop()
                return True
            
            found = False
            if root.left is not None:
                found = getPath(root.left, node)
                # 因为最多有两个节点非None，所以需要分别pop
                # 根节点和带寻找点抵消
                # 最后正好是空列表
                path.pop()

            # 判断是否找到，找到则提前退出
            if found:
                return True

            if root.right is not None:
                getPath(root.right, node)
                path.pop()

            return found

        if root is None or p is None or q is None:
            return None

        paths = []
        path = []
        getPath(root, p)
        getPath(root, q)

        # print(paths)
        return getCommonNode(paths[0], paths[1])

# labuladong
# 不需要额外的列表存储路径节点
# 时间复杂度 最好O(logn) 最坏O(n) 空间复杂度同
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:# or p is None or q is None:
            return None
        if root == p or root == q:
            return root

        node1 = self.lowestCommonAncestor(root.left, p, q)
        node2 = self.lowestCommonAncestor(root.right, p, q)

        if node1 is None and node2 is None:
            return None
        elif node1 is not None and node2 is not None:
            return root
        elif node1 is not None:
            return node1
        else:
            return node2

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right = TreeNode(1)
p = root.left.left
q = root.right
s1 = Solution()
ans = s1.lowestCommonAncestor(root, p, q)
print(ans)