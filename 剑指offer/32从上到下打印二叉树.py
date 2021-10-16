'''
Description: 
Author: Tjg
Date: 2021-10-08 17:38:46
LastEditTime: 2021-10-08 18:19:48
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# I        
# 时间复杂度O(n) 空间复杂度O(n) p172
import queue
from typing import FrozenSet
class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        ans = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            ans.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return ans

# II
# 时间复杂度O(n) 空间复杂度O(n)
# 低效
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            rows = []

            while not q.empty():
                rows.append(q.get())
            ans.append([node.val for node in rows])

            for node in rows:
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
        return ans
        
# 时间复杂度O(n) 空间复杂度O(n) p174
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        rows = []
        q = queue.Queue()
        q.put(root)
        toBePrinted = 1
        nextLevel = 0

        while not q.empty():
            node = q.get()
            rows.append(node.val)
            toBePrinted -= 1

            if node.left is not None:
                q.put(node.left)
                nextLevel += 1
            if node.right is not None:
                q.put(node.right) 
                nextLevel += 1
            if toBePrinted == 0:
                ans.append(rows[:])
                rows.clear()
                toBePrinted = nextLevel
                nextLevel = 0
        return ans

# III
# 时间复杂度O(n) 空间复杂度O(n)
# 低效
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        q = queue.Queue()
        q.put(root)
        isOdd = True

        while not q.empty():
            rows = []

            while not q.empty():
                rows.append(q.get())
            
            if isOdd:
                ans.append([node.val for node in rows])
                isOdd = False
            else:
                ans.append([rows[i].val for i in range(len(rows) - 1, -1, -1)])
                isOdd = True

            for node in rows:
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
        return ans

# 时间复杂度O(n) 空间复杂度O(n)
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        rows = []
        q = queue.Queue()
        q.put(root)
        toBePrinted = 1
        nextLevel = 0
        isOdd = True

        while not q.empty():
            node = q.get()
            rows.append(node.val)
            toBePrinted -= 1

            if node.left is not None:
                q.put(node.left)
                nextLevel += 1
            if node.right is not None:
                q.put(node.right) 
                nextLevel += 1
            if toBePrinted == 0:
                if isOdd:
                    ans.append(rows[:])
                    isOdd = False
                else:
                    ans.append(rows[::-1])
                    isOdd = True
                rows.clear()
                toBePrinted = nextLevel
                nextLevel = 0
        return ans