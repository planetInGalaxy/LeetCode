'''
Description: 
Author: Tjg
Date: 2021-08-21 17:59:51
LastEditTime: 2021-08-21 18:10:11
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
            

        