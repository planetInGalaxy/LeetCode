'''
Description: 
Author: Tjg
Date: 2021-08-27 15:47:31
LastEditTime: 2021-08-27 16:10:19
LastEditors: Please set LastEditors
'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 递归
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def travel(root):
            if root == None:
                return 0
            depth = 0
            for i in root.children:
                depth = max(depth,travel(i))
            return depth + 1
        return travel(root)

# 迭代 元组 拆包
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 1
        stack = [(1,root),]
        while stack:
            current_depth, node = stack.pop()
            depth = max(depth, current_depth)
            if node.children:
                stack.extend(zip(
                    [current_depth + 1 ] * len(node.children), node.children[::-1]))
            
        return depth
        

