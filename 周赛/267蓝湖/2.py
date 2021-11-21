'''
Description: 
Author: Tjg
Date: 2021-11-14 10:39:15
LastEditTime: 2021-11-20 10:10:59
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
from typing import Optional
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

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head,tail):
            # print(head, tail)
            if head.next == tail:
                return head
            
            node = reverse(head.next, tail)
            head.next.next = head
            head.next = tail
            return node

        length = 1
        dummy = ListNode(-1,head)

        while dummy is not None and dummy.next is not None:
            if length % 2 == 0:
                left = dummy
            i = 0 
            while i < length and dummy.next != None:
                print(length, head)
                dummy = dummy.next
                i += 1
            
            if length % 2 == 0:
                right = dummy.next
                dummy = left
                left.next = reverse(left.next,right)
                
            length += 1
        
        return head



dummy = ListNode(-1)
head = dummy
for i in range(0, 20):
    head.next = ListNode(i)
    head = head.next
head = dummy.next
print(head)

s1 = Solution()
ans = s1.reverseEvenLengthGroups(head)
print(ans)