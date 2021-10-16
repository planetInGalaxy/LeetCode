'''
Description: 
Author: Tjg
Date: 2021-10-16 17:25:29
LastEditTime: 2021-10-16 17:38:24
LastEditors: Please set LastEditors
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        pA = headA
        pB = headB
        while pA != pB:
            # pA != None 需要到达None节点 否则无法判断出无公共节点的情况
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA

        return pA