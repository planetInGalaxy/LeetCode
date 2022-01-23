'''
Description: 
Author: Tjg
Date: 2022-01-08 17:16:19
LastEditTime: 2022-01-08 17:52:41
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

# 先求出链表的长度（也可以直接用快慢指针，快指针的后一个节点即可）
# 然后反转链表的后半部分（向下取整）
# 将前半部分函数和翻转后的后半函数一一比较（后半部分作为循环条件）
# 原链表未修改回来
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            if head is None:
                return None
            node = head.next
            head.next = None
            while node is not None:
                next = node.next
                node.next = head
                head = node
                node = next 
            return head
        
        if head is None:
            return None

        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        
        step = (length + 1) // 2
        right_head = head
        while step != 0:
            right_head = right_head.next
            step -= 1
        right_head = reverse(right_head)

        while right_head is not None:
            if head.val != right_head.val:
                return False
            head = head.next
            right_head = right_head.next
        else:
            return True

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(0)
s1 = Solution()
ans = s1.isPalindrome(head)
print(ans)