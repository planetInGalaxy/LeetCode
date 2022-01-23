'''
Description: 
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
http://c.biancheng.net/view/8105.html
Author: Tjg
Date: 2022-01-22 10:12:47
LastEditTime: 2022-01-22 17:36:36
LastEditors: Please set LastEditors
'''
from typing import Optional
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 翻转一个子链表，并且返回新的头与尾
        def reverse(head: ListNode, tail: ListNode):
            prev = None # 或者tail.next
            p = head
            while prev != tail:
                next = p.next
                p.next = prev
                prev = p
                p = next
            return tail, head
        
        if head is None or head.next is None or k == 1:
            return head

        dummy = ListNode(0, head)
        pre = tail = dummy
        while head:
            # 查看剩余部分长度是是否 >= k
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return dummy.next
            # 保存后面链表的第一个节点
            next = tail.next
            # 翻转子链表
            head, tail = reverse(head, tail)
            # 把子链表首尾接回原链表
            pre.next = head
            tail.next = next
            # 迭代更新pre和head
            pre = tail
            head = tail.next
        
        return dummy.next




l1 = ListNode(0)
l1.next = ListNode(1)
tail = l1.next.next = ListNode(2)
print("l1 ", l1)
s1 = Solution()
ans = s1.reverseKGroup(l1, 2)
print("ans ", ans)
print("tail ", tail)