'''
Description: 
Author: Tjg
Date: 2021-06-08 20:48:32
LastEditTime: 2021-06-08 22:21:18
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

# 迭代法 不对称
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0,l1)
        prev = dummy
        while l1 != None and l2 != None:
            # print("pre",dummy.next,prev,l1,l2)
            if l1.val >= l2.val:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
                prev.next = l1
            else:
                l1 = l1.next
                prev = prev.next
            # print("pas",dummy.next)

        if l1 == None: 
# 是prev.next 而不是l1,因为l1只是个指针，仅仅是l1指针指向
# 新的地址，而没有把l1，l2连接起来
            prev.next= l2 
        return dummy.next

# 迭代法 对称
class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

# 递归法
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

l1 = ListNode(3)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)

l2 = ListNode(2)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)
print(l1,l2)
s1 = Solution()
ans = s1.mergeTwoLists(l1,l2)
print(ans)
