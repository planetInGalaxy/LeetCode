'''
Description: 
Author: Tjg
Date: 2021-10-06 09:59:43
LastEditTime: 2021-10-06 11:16:21
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n） 空间复杂度O(1) p76
class Solution:
    def numWays(self, n: int) -> int:
        fib0 = 1
        fib1 = 1
        for i in range(n):
            # 可以同时赋值
            fib0, fib1 = fib1, fib0 + fib1
        return fib0 % int(1e9+7)
        