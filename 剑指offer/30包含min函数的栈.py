'''
Description: 
Author: Tjg
Date: 2021-10-08 15:11:28
LastEditTime: 2021-10-08 16:56:00
LastEditors: Please set LastEditors
'''
# 时间复杂度O(1) 空间复杂度O(n) p167
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stackHelper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stackHelper == [] or self.stackHelper[-1] > x:
            self.stackHelper.append(x)
        else:
            self.stackHelper.append(self.stackHelper[-1])

    def pop(self) -> None:
        if self.stack != []:
            self.stack.pop()
            self.stackHelper.pop()
        else:
            print('error')

    def top(self) -> int:
        if self.stack != []: 
            return self.stack[-1]
        else:
            print('error')

    def min(self) -> int:
        if self.stackHelper != []:
            return self.stackHelper[-1]
        else:
            print('error')

# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.min()
minStack.pop()
minStack.top()
minStack.min()

