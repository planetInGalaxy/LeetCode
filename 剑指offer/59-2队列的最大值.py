'''
Description: 
Author: Tjg
Date: 2021-10-17 19:13:29
LastEditTime: 2021-10-17 19:57:19
LastEditors: Please set LastEditors
'''
# 思想同上题
# 时间复杂度都是O(1) 空间复杂度O(n)（用了一个辅助队列）
from collections import deque
class MaxQueue:

    def __init__(self):
        self.data = deque()
        self.max = deque()

    def max_value(self) -> int:
        if len(self.max) > 0:
            return self.max[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.data.append(value)
        # ！ 这里是while
        while len(self.max) > 0 and self.max[-1] < value:
            self.max.pop()
        self.max.append(value)

    def pop_front(self) -> int:
        if len(self.data) > 0:
            value = self.data.popleft()
            if value == self.max[0]:
                self.max.popleft()
            return value
        else:
            return -1

# 剑指offer 稍慢 疑问 p292
# 时间复杂度都是O(1) 空间复杂度O(n)（用了一个辅助队列，以及额外的n个对象）
from collections import deque
class MaxQueue:
    class InternalData:
        def __init__(self, number, index):
            self.number = number
            self.index = index

        def __repr__(self):
            return str(self.index) + " : " + str(self.number)

    def __init__(self):
        self.data = deque()
        self.max = deque()
        self.currentIndex = 0

    def max_value(self) -> int:
        if len(self.max) > 0:
            return self.max[0].number
        else:
            return -1

    def push_back(self, value: int) -> None:
        
        while len(self.max) > 0 and self.max[-1].number <= value:
            self.max.pop()
        internalData = self.InternalData(value, self.currentIndex)
        self.data.append(internalData)
        self.max.append(internalData)
        self.currentIndex += 1

    def pop_front(self) -> int:
        if len(self.data) > 0:
            if self.data[0].index == self.max[0].index:
                self.max.popleft()
            value = self.data.popleft().number
            return value
        else:
            return -1

s1 = MaxQueue()
ans = []
ans.append(s1.push_back(1))
ans.append(s1.push_back(2))
ans.append(s1.max_value())
ans.append(s1.pop_front())
ans.append(s1.max_value())
ans.append(s1.pop_front())
ans.append(s1.max_value())
# ans.append()
# ans.append()
# ans.append()


print(ans)