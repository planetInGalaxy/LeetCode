'''
Description: 
Author: Tjg
Date: 2021-06-01 19:44:57
LastEditTime: 2021-06-08 20:14:10
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
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1 = []
        ls2 = []
        ls3 = []
        while l1 != None:
            ls1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            ls2.append(l2.val)
            l2 = l2.next
        # print(ls1,ls2)
        temp = 0
        if len(ls2) < len(ls1):
            ls1, ls2 = ls2, ls1
  
        for i in range(len(ls2)):
            if i < len(ls1):
                ls3.append((temp + ls1[i] + ls2[i]) % 10)
                temp = (temp + ls1[i] + ls2[i]) // 10
            else:
                ls3.append((temp + ls2[i]) % 10)
                temp = (temp + ls2[i]) // 10
                
        if temp > 0:
            ls3.append(temp)
        # print(ls3)
        l3 = ListNode()
        p = l3
        for i in range(len(ls3)):
            p.val = ls3[i]
            if i != len(ls3) - 1:
                p.next = ListNode() # 改变对象的值
                p = p.next # 重新指向一个对象
        return l3


l1 = ListNode()
l2 = ListNode()
p = l1
for i in [9,9,9,9,9,9]:
    p.val = i
    p.next = ListNode() # 改变对象的值
    p = p.next # 重新指向一个对象
p.val = 9

p = l2
for i in [9,9,9]:
    p.val = i
    p.next = ListNode() # 改变对象的值
    p = p.next # 重新指向一个对象
p.val = 9

s1 = Solution()
anwser = s1.addTwoNumbers(l1,l2)
print(l1)
print(l2)
print(anwser)
