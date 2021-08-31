'''
Description: 
Author: Tjg
Date: 2021-08-08 08:54:54
LastEditTime: 2021-08-08 08:58:42
LastEditors: Please set LastEditors
'''
# 动态规划 状态压缩
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        t0,t1,t2 = 0,1,1
        for _ in range(n-2):
            t0,t1,t2 = t1,t2,t0+t1+t2

        return t2