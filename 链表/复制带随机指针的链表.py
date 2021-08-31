'''
Description: 
Author: Tjg
Date: 2021-07-22 20:51:29
LastEditTime: 2021-07-22 22:59:01
LastEditors: Please set LastEditors
'''
# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# 思路 第一轮迭代 复制next并把每一个存在哈希表中 node：1 1：new_node
# 第二轮迭代 通过哈希完成random的链接
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 递归  不适合
        # def copyList(new_head,head):
        #     if head == None:
        #         return None
        #     new_head = Node(head.val)
        #     new_head.next = copyList(new_head.next,head.next)
        #     return new_head
        # new_head = None
        # new_head = copyList(new_head,head)

        dummy = Node(0)
        prev = dummy
        node2num = {None:-1} # 在第一轮迭代中 不会把None放到字典中
        num2node = {-1:None}
        node = head
        i = 0
        while node:
            prev.next = Node(node.val)
            prev.next.next = node.next
            node2num[node] = i
            num2node[i] = prev.next
            prev = prev.next
            node = node.next
            i += 1
        print(num2node,node2num)
        new_node = dummy.next
        old_node = head
        while old_node:
            num = node2num[old_node.random]
            new_node.random = num2node[num]
            old_node = old_node.next
            new_node = new_node.next
        return dummy.next

s1 = Solution()
list1 = Node(1)
list1.next = Node(2)
print(list1)
answer = s1.copyRandomList(list1)
print(answer)