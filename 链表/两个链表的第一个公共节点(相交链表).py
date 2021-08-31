'''
Description: 
Author: Tjg
Date: 2021-07-21 16:52:54
LastEditTime: 2021-08-12 08:03:11
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 双指针 记录差值
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def listLength(head):
            length = 0
            node = head
            while node:
                node = node.next
                length += 1
            return length
        len_A = listLength(headA)
        len_B = listLength(headB)
        if len_A < len_B:
            len_A, len_B = len_B, len_A
            headA, headB = headB, headA

        delta = len_A - len_B
        # print(delta)
        while delta:
            headA = headA.next
            delta -= 1
        # print(headA.val,headB.val)
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        else:
            return None

# 双指针 互换跑道
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      if headA == None or headB == None:
        return None
      
      pa = headA
      pb = headB
      while pa != pb:
        pa = pa.next if pa != None else headB
        pb = pb.next if pb != None else headA
      
      return pa