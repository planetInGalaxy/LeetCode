'''
Description: 
Author: Tjg
Date: 2021-08-27 18:35:58
LastEditTime: 2021-08-28 11:00:01
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

# 非原地合并，一起合并，需要额外空间（不符合题意）
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode(0,None)
        node = dummy
        while lists:
            for i in range(len(lists)):
                if i == 0 or lists[i].val < lists[min_index].val:
                    min_index = i
            node.next = ListNode(lists[min_index].val)
            node = node.next
            lists[min_index] = lists[min_index].next
            if lists[min_index] == None:
                lists.pop(min_index)
        print(dummy.next)
        return dummy.next

# 原地合并，一起合并，无需额外空间
# 超时
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # 先排除[]空列表的特殊情况
        n = 0 
        while n < len(lists):
            if not lists[n]:
                lists.pop(n)
            else:
                n += 1
        if not lists:
            return None

        # 获得头指针并弹出
        for i in range(len(lists)):
            if i == 0 or lists[i].val < lists[min_index].val:
                min_index = i 
        head = lists.pop(min_index)
        node = head
        
        # 每轮添加一个节点
        while lists:
            # 先寻找到链表数组中最下的值
            for i in range(len(lists)):
                if i == 0 or lists[i].val < lists[min_index].val:
                    min_index = i
            # 如果最小值小于头链表下一位的值，则插入
            if node.next == None or lists[min_index].val <= node.next.val:
                temp = lists[min_index].next
                lists[min_index].next = node.next
                node.next = lists[min_index]
                lists[min_index] = temp
            # 头链表的node指针往后移动
            node = node.next
            # 如果lists中的链表到底了，就剔除它
            if lists[min_index] == None:
                lists.pop(min_index)
        print(head)
        return head

# 分治合并，递归会使用到 O(logk) 空间代价的栈空间
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        def merge(headA, headB):
            dummy = ListNode()
            prev = dummy
            while headA and headB:
                if headA.val <= headB.val:
                    prev.next = headA
                    prev = prev.next
                    headA = headA.next
                else:
                    prev.next = headB
                    prev = prev.next
                    headB = headB.next
            if headA == None:
                prev.next = headB
            else:
                prev.next = headA
            return dummy.next

        def divide(l,r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = l + (r - l) // 2
            l1 = divide(l,mid)
            l2 = divide(mid + 1, r)
            return merge(l1,l2)

        ans = divide(0,len(lists) - 1)
        return ans
        



l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

s1 = Solution()
ans = s1.mergeKLists([l1,l2,l3])
print(ans)