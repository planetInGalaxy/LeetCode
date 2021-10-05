'''
Description: 
Author: Tjg
Date: 2021-10-05 22:05:07
LastEditTime: 2021-10-05 22:13:40
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 非递归 
# 时间复杂度O(n) 空间复杂度O(n) p59
class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

# 递归(慢)
# 时间复杂度O(n) 空间复杂度O(n) p59
class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        answer = []
        def reverse(node):
            if node == None:
                return 
            reverse(node.next)
            answer.append(node.val)
        reverse(head)
        return answer
