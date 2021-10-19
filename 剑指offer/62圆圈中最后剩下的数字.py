'''
Description: 
Author: Tjg
Date: 2021-10-18 10:40:13
LastEditTime: 2021-10-18 11:12:19
LastEditors: Please set LastEditors
'''
# 约瑟夫环 双向环形链表 超时 p301
# 时间复杂度O(n*m) 空间复杂度O(n)
class Solution:
    class node:
        def __init__(self, val = None, next = None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev
    def lastRemaining(self, n: int, m: int) -> int:
        if n <= 0 or m <= 0:
            return None

        head = self.node(0)
        p = head
        for i in range(1, n):
            p.next = self.node(i)
            p.next.prev = p
            p = p.next
        p.next = head
        head.prev = p

        while head.next != head:
            for i in range(m):
                head = head.next
            head.prev.prev.next = head
            head.prev = head.prev.prev

        return head.val

# 数学规律 p303 疑问
# 时间复杂度O(n) 空间复杂度 递归O(n) 循环O(1)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n <= 0 or m <= 0:
            return None

        if n == 1:
            return 0

        return (self.lastRemaining(n - 1, m) + m) % n 

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n <= 0 or m <= 0:
            return None

        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        
        return last
