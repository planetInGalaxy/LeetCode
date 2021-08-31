'''
Description: 链表是传引用
Author: Tjg
Date: 2021-06-08 20:04:12
LastEditTime: 2021-06-09 08:28:03
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
        
# 双指针法     
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head # 双指针
        p2 = head
        while n - 1: # 第一个指针移动n - 1位
            n-=1
            p1=p1.next
        while p1.next and p1.next.next: # 检查快指针有没有到底，p1.next是删除头结点的特殊情况
            p1 = p1.next
            p2 = p2.next
        if p1.next == None: # 检查是否删除头结点
            return head.next
        p2.next = p2.next.next
        return head

# 双指针法 头节点前面设置一个哑结点，避免讨论
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

# 栈 list的append与pop构成栈 使用了哑结点 
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next


l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(3)
print(l1)
s1 = Solution()
ans = s1.removeNthFromEnd(l1,1)
print(ans)
