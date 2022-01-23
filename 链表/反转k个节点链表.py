'''
Description: 
Author: Tjg
Date: 2022-01-22 11:45:01
LastEditTime: 2022-01-22 11:46:32
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

# 根据节点数来反转
class Solution:
    def  reverseList(self, head: ListNode, k: int) -> ListNode:
        new_head = None
        for _ in range(k):
            temp = head
            head = head.next
            temp.next = new_head
            new_head = temp
        return new_head

l1 = ListNode(0)
l1.next = ListNode(1)
tail = l1.next.next = ListNode(2)
print(l1)
s1 = Solution()
ans = s1.reverseList(l1, 3)
print(ans)
print(tail)