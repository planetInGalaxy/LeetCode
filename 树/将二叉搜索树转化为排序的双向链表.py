'''
Description: 
Author: Tjg
Date: 2021-08-29 08:40:45
LastEditTime: 2021-08-29 09:24:08
LastEditors: Please set LastEditors
'''
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树递归框架
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        first, last = None, None
        def travel(node):
            if node == None:
                return None

            travel(node.left)

            nonlocal first,last
            # 将目前最后一个节点与当前节点建立连接
            if last:
                last.right = node
                node.left = last
            else:
                # 寻找第一个节点
                first = node
            # 不断更新最后一个节点
            last = node
            
            travel(node.right)

        if not root:
            return None
        travel(root)
        last.right = first
        first.left = last
        return first