'''
Description: 
Author: Tjg
Date: 2021-06-09 12:05:35
LastEditTime: 2022-01-22 11:43:40
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
import time


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


# 递归 用递归函数返回最终的指针
class Solution(object):
    def reverseList(self, head):
        # 递归终止条件是当前为空(头指针为空)，或者下一个节点为空
        if(head is None or head.next is None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


s1 = Solution()
start = time.time()
for i in range(10000):
    l1 = ListNode(0)
    cur = l1
    for i in range(1, i // 100):
        cur.next = ListNode(i)
        cur = cur.next
    ans = s1.reverseList(l1)
end = time.time()
print(end - start)

node = ans
while node:
    print(node.val)
    node = node.next
