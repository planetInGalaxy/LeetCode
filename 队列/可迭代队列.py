'''
Description: 
Author: Tjg
Date: 2022-02-12 13:49:46
LastEditTime: 2022-02-12 13:49:47
LastEditors: Please set LastEditors
'''
# from queue import Queue

# class IterableQueue(Queue): 

#     _sentinel = object()

#     def __iter__(self):
#         return self

#     def __init__(self):
#         super(IterableQueue, self).__init__()
#         self.put(self._sentinel)
        
#     def __next__(self):
#         item = self.get()
#         if item is self._sentinel:
#             raise StopIteration
#         else:
#             return item
    
#     def __repr__(self):
#         return str(self.__iter__())

class LinkedQueue():
    class _Node():
        def __init__(self, val=0, next=None) -> None:
            self.val = val
            self.next = next
    def __init__(self) -> None:
        self.head = self.tail = self._Node()
        self._qsize = 0
    
    def get(self):
        if self.qsize != 0:
            val = self.head.next.val
        self.head = self.head.next
        self._qsize -= 1
        return val

    def put(self, val):
        self.tail.next = self._Node(val=val)
        self.tail = self.tail.next
        self._qsize += 1
        return

    def has(self, val):
        cur = self.head.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        else:
            return False

    def qsize(self):
        return self._qsize

    def __repr__(self):
        print_string = []
        p = self.head.next
        while p != None:
            print_string.append(str(p.val))
            p = p.next
        return "->".join(print_string)
