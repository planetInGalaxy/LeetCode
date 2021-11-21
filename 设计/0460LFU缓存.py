'''
Description: 
Author: Tjg
Date: 2021-11-15 10:50:42
LastEditTime: 2021-11-16 11:09:43
LastEditors: Please set LastEditors
'''
# labuladon p227
# 三个哈希表 
# keyToValue，用于取值 
# LFU的freqToKey类似于LRU中的哈希链表，但是只用存key即可
# keyToFreq，用于反向映射 快速获得freqToKey中所有的key
from collections import deque
class LFUCache:
    class LinkedHashSet:
        class Node:
            def __init__(self, key=None, next=None, prev=None) -> None:
                self.key = key
                self.next = next
                self.prev = prev
            def __repr__(self):
                return "<" + str(self.key) + ">"

        def __init__(self):
            self.map = {}
            self.head = self.Node(-1)
            self.tail = self.Node(-1)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0

        def append(self, k):
            node = self.Node(k)
            self.map[k] = node
            node.prev = self.tail.prev
            node.prev.next = node
            node.next = self.tail
            self.tail.prev = node
            self.size += 1

        def remove(self, k):
            # print(k,self.map)
            node = self.map[k]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.map.pop(k)
            self.size -= 1
        
        def firstKey(self):
            return self.head.next.key

        def isEmpty(self):
            return self.size == 0
        
        def __repr__(self):
            print_string = []            
            p = self.head
            while p != None:
                print_string.append(str(p.key))
                p = p.next
            return "->".join(print_string)


    def __init__(self, capacity: int):
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freqToKey = {}
        self.cap = capacity
        self.minFreq = 0

    def increaseFreq(self, key):
        freq = self.keyToFreq[key]
        self.keyToFreq[key] = freq + 1

        self.freqToKey[freq].remove(key)
        if self.freqToKey[freq].isEmpty():
            self.freqToKey.pop(freq)
            if freq == self.minFreq:
                self.minFreq += 1
                 
        if freq + 1 not in self.freqToKey:
            self.freqToKey[freq + 1] = self.LinkedHashSet()
        self.freqToKey[freq + 1].append(key)


    def removeMinFreqKey(self):
        keyList = self.freqToKey[self.minFreq]
        deletedKey = keyList.firstKey()
        keyList.remove(deletedKey)
        # 因为是有新加入的，所以minFreq一定为1，不用手动更新了
        if keyList.isEmpty():
            # print(self.freqToKey)
            self.freqToKey.pop(self.minFreq)
        
        self.keyToVal.pop(deletedKey)
        self.keyToFreq.pop(deletedKey)

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.increaseFreq(key)
            return
        if self.cap <= len(self.keyToVal):
            self.removeMinFreqKey()

        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        
        if 1 not in self.freqToKey:
            self.freqToKey[1] = self.LinkedHashSet()
        self.freqToKey[1].append(key)
        self.minFreq = 1

lFUCache = LFUCache(2)
lFUCache.put(1, 1)   # cache=[1,_], cnt(1)=1
lFUCache.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lFUCache.get(1))      # 返回 1
                      # cache=[1,2], cnt(2)=1, cnt(1)=2
lFUCache.put(3, 3)   # 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                      # cache=[3,1], cnt(3)=1, cnt(1)=2
print(lFUCache.get(2))      # 返回 -1（未找到）
print(lFUCache.get(3))      # 返回 3
                      # cache=[3,1], cnt(3)=2, cnt(1)=2
lFUCache.put(4, 4)   # 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                      # cache=[4,3], cnt(4)=1, cnt(3)=2
print(lFUCache.get(1))      # 返回 -1（未找到）
print(lFUCache.get(3))      # 返回 3
                      # cache=[3,4], cnt(4)=1, cnt(3)=3
print(lFUCache.get(4))      # 返回 4
                      # cache=[3,4], cnt(4)=2, cnt(3)=3

