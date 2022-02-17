'''
Description: 
Author: Tjg
Date: 2022-02-17 21:18:25
LastEditTime: 2022-02-17 23:33:51
LastEditors: Please set LastEditors
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BFS
# 时间复杂度O(n) 空间复杂度O(n)
import queue
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return None

        q = queue.Queue()
        q.put((root, 1))
        last_pos = 0
        while not q.empty():
            node, pos = q.get()
            # print(last_pos, pos)
            if last_pos != pos - 1:
                return False
            else:
                last_pos = pos
                
            if node.left is not None:
                q.put((node.left, pos * 2))
            if node.right is not None:
                q.put((node.right, pos * 2 + 1))

        return True
