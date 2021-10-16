'''
Description: 
Author: Tjg
Date: 2021-10-10 11:07:06
LastEditTime: 2021-10-10 11:36:46
LastEditors: Please set LastEditors
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        print_string = []
        
        print_string.append(str(self.val))
        p = self.next
        while p != None:
            print_string.append(str(p.val))
            p = p.next
        return "->".join(print_string)

# 时间复杂度O(n) 空间复杂度O(n)
# 哈希表
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        newNode = dummy
        oldNode = head
        
        while oldNode:
            newNode.next = Node(oldNode.val)
        
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        # 先把new节点插入old链表中
        node = head
        while node:
            copyNode = Node(node.val, node.next)
            node.next = copyNode
            node = node.next.next
        
        # 把new节点的random指针指向对应的new节点或者None
        node = head
        while node:
            if node.random is not None:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next
        # print(head)

        # 分离old new节点
        oldHeadDummy = Node(0)
        oldNode = oldHeadDummy
        newHeadDummy = Node(0)
        newNode = newHeadDummy
        node = head
        while node:
            # print(oldHeadDummy.next, newHeadDummy.next)
            oldNode.next = node
            oldNode = oldNode.next
            newNode.next = node.next
            newNode = newNode.next
            node = node.next.next
            oldNode.next = None
        # print(oldHeadDummy.next)
        return newHeadDummy.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.random = None
l1.next.random = l1
l1.next.next.random = l1.next

print(l1)
s1 = Solution()
ans = s1.copyRandomList(l1)
print(ans)