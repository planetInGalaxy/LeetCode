'''
Description: 
Author: Tjg
Date: 2021-08-27 16:47:23
LastEditTime: 2021-08-27 17:04:02
LastEditors: Please set LastEditors
'''
# 删除的时间复杂度是O(n) 其余是O(1)
# 额外空间复杂度 O（1）
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('INF')
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        pop_num = self.stack.pop()
        if pop_num == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = float("INF")
        return pop_num

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
# 辅助栈
# 删除的时间复杂度是O(1)
# 额外空间复杂度O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float('INF')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()