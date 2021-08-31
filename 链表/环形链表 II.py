'''
Description: 用哈希也可以不过需要O（n）的额外空间
Author: Tjg
Date: 2021-07-26 09:52:56
LastEditTime: 2021-07-26 10:07:04
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# 快慢指针法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        fast = head 
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast