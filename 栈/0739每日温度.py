'''
Description: 
给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，
其中answer[i]是指在第 i 天之后，才会有更高的温度。
如果气温在这之后都不会升高，请在该位置用0来代替。
Author: Tjg
Date: 2022-02-11 20:40:14
LastEditTime: 2022-02-11 20:49:32
LastEditors: Please set LastEditors
'''
# 单调栈
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        if temperatures is None or temperatures == []:
            return None

        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer
