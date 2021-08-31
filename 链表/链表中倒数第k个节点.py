'''
Description: 
Author: Tjg
Date: 2021-07-26 10:11:18
LastEditTime: 2021-07-26 10:14:53
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        while k != 0:
            fast = fast.next
            k -= 1
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow