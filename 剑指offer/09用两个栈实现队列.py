'''
Description: 
Author: Tjg
Date: 2021-10-06 09:28:05
LastEditTime: 2021-10-06 11:15:20
LastEditors: Please set LastEditors
'''
# 入栈 时间复杂度O（1）
# 出栈 摊销法 时间复杂度O（1）
# p70
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2 != []:
            value = self.stack2.pop()
        elif self.stack1 == []:
            value = -1
        else:
            self.stack2.extend(self.stack1[::-1])
            self.stack1.clear()
            value = self.stack2.pop()
        return value


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
val1 = obj.deleteHead()
val2 = obj.deleteHead()
val3 = obj.deleteHead()
val4 = obj.deleteHead()
print(val1, val2, val3, val4)