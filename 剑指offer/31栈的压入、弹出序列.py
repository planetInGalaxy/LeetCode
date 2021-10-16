'''
Description: 
Author: Tjg
Date: 2021-10-08 16:22:06
LastEditTime: 2021-10-08 17:02:55
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(n) p169
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        if pushed == [] and popped == []:
            return True
        if len(pushed) != len(popped):
            return False
        p1 = 0
        p2 = 0
        stack = []
        while p1 < len(pushed):
            # 下标不能溢出 
            while p1 < len(pushed) and pushed[p1] != popped[p2]:
                stack.append(pushed[p1])
                p1 += 1
            # 如果不是因为下标溢出，即二者相等，则跳过，否则不符合题意
            if p1 < len(pushed):
                p1 += 1
                p2 += 1
            else:
                return False

            while p2 < len(popped) and stack != [] and stack[-1] == popped[p2]:
                stack.pop()
                p2 += 1
        if p1 == p2:
            return True
        else:
            return False