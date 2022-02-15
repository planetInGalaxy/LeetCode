'''
Description: 
设计有限阻塞队列，生产者消费者模型
Author: Tjg
Date: 2022-02-15 17:27:47
LastEditTime: 2022-02-15 18:00:07
LastEditors: Please set LastEditors
'''
# 有时候是消费者需要等待生产者生产，
# 有时候是生产者要等待消费者消费，
# 这是两个不同的“一前一后问题”，
# 因此也需要设置两个同步信号量。
import threading
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0
        # 不考虑时间效率
        self.queue = []
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(capacity)

    def enqueue(self, element: int) -> None:
        self.empty.acquire()
        if self._size < self.capacity:
            self.queue.append(element)
            self._size += 1
        self.full.release()


    def dequeue(self) -> int:
        self.full.acquire()
        if self._size > 0:
            data = self.queue.pop(0)
            self._size -= 1
        self.empty.release()
        return data


    def size(self) -> int:
        return self._size