'''
Description: 
Author: Tjg
Date: 2021-07-28 21:47:22
LastEditTime: 2021-07-28 22:09:13
LastEditors: 
'''

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        def findParents(root):
            if root.left:
                parents[root.left.val] = root
                findParents(root.left)
            if root.right:
                parents[root.right.val] = root
                findParents(root.right)

        def findAns(root,from_,depth):
            if root == None:
                return
            if depth == k:
                ans.append(root.val)
            if root.left != from_:
                findAns(root.left,root,depth+1)
            if root.right != from_:
                findAns(root.right,root,depth+1)
            if parents[root.val] != from_: # 根节点无父节点
                findAns(parents[root.val],root,depth+1)

        parents = {root.val:None}
        ans = []
        findParents(root)
        findAns(target,None,0)
        return ans

s1 = Solution()
t1 = TreeNode(0)
t1.left = TreeNode(1)
t1.right = TreeNode(2)
answer = s1.distanceK(t1,t1,1)
print(answer)