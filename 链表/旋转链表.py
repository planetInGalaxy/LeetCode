'''
Description: 
Author: Tjg
Date: 2021-06-09 08:19:58
LastEditTime: 2021-06-09 12:07:22
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        k = k % n
        delta = n - k
        if k == 0:
            return head
        rear = head
        while delta - 1:
            delta = delta - 1
            rear = rear.next
            
        new_head = rear.next
        rear.next = None
        p = new_head
        while p.next:
            p = p.next
        p.next = head
        return new_head
        
# 闭合为环
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        if (add := n - k % n) == n:
            return head
        
        cur.next = head
        while add:
            cur = cur.next
            add -= 1
        
        ret = cur.next
        cur.next = None
        return ret


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
print(l1)
s1 = Solution()
ans = s1.rotateRight(l1,2)
print(ans)
