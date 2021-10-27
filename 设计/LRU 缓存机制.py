'''
Description: 
Author: Tjg
Date: 2021-07-18 11:51:59
LastEditTime: 2021-10-22 16:07:53
LastEditors: Please set LastEditors
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 链表结点


class Node:
    def __init__(self, key=None, val=None, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

# 双向链表
class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def adddLast(self, x: Node):
        x.prev = self.tail.prev
        x.prev.next = x
        x.next = self.tail
        self.tail.prev = x
        self.size += 1

    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.size == 0:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.cache = DoubleList()

    def makeRecently(self, key: int):
        x = self.map.get(key)
        self.cache.remove(x)
        self.cache.adddLast(x)

    def addRecently(self, key: int, val: int):
        x = Node(key, val)
        self.cache.adddLast(x)
        self.map.update({key:x})

    def deleteKey(self, key: int):
        x = self.map.pop(key)
        self.cache.remove(x)

    def removeLeastRecently(self):
        deleteNode = self.cache.removeFirst()
        # print(deleteNode.key,self.map)
        self.map.pop(deleteNode.key)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map.get(key).val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.cap == self.cache.size:
                self.removeLeastRecently()
        else:
            self.deleteKey(key)

        self.addRecently(key, value)  # 是value 不是val

# 自带的双端队列（双向链表）结构 慢 
# size存储不存储没太大必要 运行速度都慢 可以用len(self.map)替代
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cache = deque(maxlen=capacity)
        self.size = 0

    def makeRecently(self, key: int):
        x = self.map.get(key)
        self.cache.remove(x)
        self.cache.append(x)

    def addRecently(self, key: int, val: int):
        x = Node(key, val)
        self.cache.append(x)
        self.map.update({key:x})
        self.size += 1

    def deleteKey(self, key: int):
        x = self.map.pop(key)
        self.cache.remove(x)
        self.size -= 1

    def removeLeastRecently(self):
        deleteNode = self.cache.popleft()
        self.map.pop(deleteNode.key)
        self.size -= 1
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map.get(key).val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.size == self.cache.maxlen:
                self.removeLeastRecently()
        else:
            self.deleteKey(key)
        self.addRecently(key, value)  # 是value 不是val

lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # 缓存是 {1=1}
lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
print(lRUCache.get(1))    # 返回 1
lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
print(lRUCache.get(2))    # 返回 -1 (未找到)
lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
print(lRUCache.get(1))    # 返回 -1 (未找到)
print(lRUCache.get(3))   # 返回 3
print(lRUCache.get(4))    # 返回 4
