'''
Description: 
Author: Tjg
Date: 2021-07-01 11:05:02
LastEditTime: 2021-07-01 11:16:26
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

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

s1 = Solution()
l1 = ListNode(0)
l2 = ListNode(1)
l1.next = l2
l2.next = l1
answer = s1.hasCycle(l1)
print(answer)
print(l1)