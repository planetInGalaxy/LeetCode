'''
Description: 
Author: Tjg
Date: 2021-10-11 10:32:58
LastEditTime: 2021-10-11 11:32:37
LastEditors: Please set LastEditors
'''
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O(n) p193
# 二叉树递归框架
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def convert(root, lastNode):
            if root is None:
                return None
            
            if root.left:
                convert(root.left, lastNode)
            
            root.left = lastNode
            if lastNode is not None:
                lastNode.right = root
            lastNode = root
            
            if root.right:
                convert(root.right, lastNode)
        
        if root is None:
            return None
        
        head = root
        while head.left:
            head = head.left
        
        convert(root, None)
        return head

# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O(n) 力扣通过版
# 二叉树递归框架
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
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
                # 如果没有last节点，说明是第一个节点
                first = node
            # 不断更新最后一个节点
            last = node
            
            travel(node.right)

        if not root:
            return None

        first, last = None, None
        travel(root)
        
        last.right = first
        first.left = last
        
        return first