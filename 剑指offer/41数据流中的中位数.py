'''
Description: 
Author: Tjg
Date: 2021-10-14 22:01:49
LastEditTime: 2021-10-14 22:38:31
LastEditors: Please set LastEditors
'''
#  双堆 时间复杂度 Add O(logn) Get O(1) 空间复杂度O(1)
import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.MaxHeap = []
        self.MinHeap = []
        heapq.heapify(self.MaxHeap)
        heapq.heapify(self.MinHeap)
        self.add2MaxHeap = True

    def addNum(self, num: int) -> None:
        if self.add2MaxHeap is True:
            if self.MinHeap != [] and num > self.MinHeap[0]:
                heapq.heappush(self.MinHeap, num)
                maxInMaxHeap = heapq.heappop(self.MinHeap)
                heapq.heappush(self.MaxHeap, -maxInMaxHeap)
            else:
                heapq.heappush(self.MaxHeap, -num)
            self.add2MaxHeap = False
        else:
            if self.MaxHeap != [] and num < -self.MaxHeap[0]:
                heapq.heappush(self.MaxHeap, -num)
                minInMinHeap = -heapq.heappop(self.MaxHeap)
                heapq.heappush(self.MinHeap, minInMinHeap)
            else:
                heapq.heappush(self.MinHeap, num)
            self.add2MaxHeap = True
        # print(self.MaxHeap, self.MinHeap)

    def findMedian(self) -> float:
        count = len(self.MaxHeap) + len(self.MinHeap)
        if count == 0:
            return None
        if count & 0b1 == 1:
            return -self.MaxHeap[0]
        else:
            return (self.MinHeap[0] - self.MaxHeap[0]) / 2

