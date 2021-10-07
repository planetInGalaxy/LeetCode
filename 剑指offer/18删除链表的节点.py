'''
Description: 
Author: Tjg
Date: 2021-10-06 20:26:28
LastEditTime: 2021-10-06 20:34:52
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 时间复杂度O(n) 空间复杂度O(1) p121
# 与书上不同
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return dummy.next