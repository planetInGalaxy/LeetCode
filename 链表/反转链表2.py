'''
Description: 疑问
Author: Tjg
Date: 2021-06-09 14:48:25
LastEditTime: 2021-09-10 11:49:51
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


# 一次遍历
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1,head)
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        # pre是前一半链表最后一个节点，不用变
        # cur是正在反转的链表中最后一个节点，也不用变
        # next是即将加入反转链表的节点
        cur = pre.next
        for _ in range(right - left):
            # 获取即将加入反转链表的节点
            next = cur.next
            # 将反转链表中最后一个节点指向新加入节点的下一个节点
            cur.next = next.next
            # 新加入的节点指向反转链表中第一个节点
            next.next = pre.next
            # 前一半链表最后一个节点指向新加入节点
            pre.next = next

        return dummy_node.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
print(l1)
s1 = Solution()
ans = s1.reverseBetween(l1,1,3)
print(ans)
