'''
Description: 
Author: Tjg
Date: 2021-07-21 16:57:31
LastEditTime: 2021-07-21 17:29:34
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        print_string = []
        
        print_string.append(str(self.val))
        p = self.next
        while p != None:
            print_string.append(str(p.val))
            p = p.next
        return "->".join(print_string)

# 迭代法
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if head == None:
        #     return None
        dummy = ListNode(0,head)
        prev = dummy
        while prev.next and prev.next.next:
            curr = prev.next
            prev.next = prev.next.next
            curr.next = prev.next.next
            prev.next.next = curr
            prev = curr
        return dummy.next

# 递归法
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
