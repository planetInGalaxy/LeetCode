'''
Description: 
Author: Tjg
Date: 2021-10-07 19:29:13
LastEditTime: 2021-10-07 19:57:09
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 时间复杂度O(nm) 空间复杂度O(n+m) p150
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def compare(headA, headB):
            if headB is None:
                return True

            if headA and headA.val == headB.val:
                return compare(headA.left, headB.left) and compare(headA.right, headB.right)
            return False

        def travel(head):
            if head is None:
                return False

            hasCommonStruct = False
            if head.val == B.val:
                hasCommonStruct = compare(head, B)
            if not hasCommonStruct:
                hasCommonStruct = travel(head.left) or travel(head.right)
            return hasCommonStruct
        
        if A is None or B is None:
            return False
        return travel(A)