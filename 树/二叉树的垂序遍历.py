'''
Description: 
Author: Tjg
Date: 2021-07-31 09:12:03
LastEditTime: 2021-07-31 12:16:04
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先按列 行 值 排序，再通过列分组
class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        def traverse(row,col,root):
            if root == None:
                return
            nodes.append((col,row,root.val))
            traverse(row + 1, col - 1, root.left)
            traverse(row + 1, col + 1, root.right)
            
        nodes = []
        traverse(0,0,root)
        nodes.sort()
        print(nodes)
        ans = []
        c_0 = nodes[0][0]
        for i in range(len(nodes)):
            if i ==0 or nodes[i][0] != nodes[i-1][0]:
                ans.append([])
            ans[-1].append(nodes[i][2])
        return ans

s1 = Solution()
t1 = TreeNode(0)
t1.right = TreeNode(1)
t1.right.left = TreeNode(2)
answer = s1.verticalTraversal(t1) 
print(answer)