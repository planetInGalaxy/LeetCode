'''
Description: 
Author: Tjg
Date: 2021-07-26 10:11:18
LastEditTime: 2021-10-07 18:28:55
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 时间复杂度O(n) 空间复杂度O(1)
# 鲁棒性问题：
# 1 空指针
# 2 节点小于k个
# 3 k为0
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return None
        fast = slow = head
        while k != 1:
            if fast == None:
                return None
            fast = fast.next
            k -= 1
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow