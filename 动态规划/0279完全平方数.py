'''
Description: 
给你一个整数 n ，返回和为 n 的完全平方数的最少数量。
完全平方数是一个整数，其值等于另一个整数的平方；
换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
Author: Tjg
Date: 2022-02-23 19:49:58
LastEditTime: 2022-02-23 22:50:40
LastEditors: Please set LastEditors
'''
# 记忆化搜索
# 时间复杂度O(n^3/2) 空间复杂度O(n)
from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        # count = 0
        @lru_cache(n)
        def dp(n):
            if n == 0:
                return 0
            ans = float("inf")
            for square_num in squares:
                if square_num <= n:
                    ans = min(ans, dp(n - square_num) + 1)
            # nonlocal count
            # count += 1
            # print(n, count, ans)
            return ans
        
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        squares = []
        for i in range(1, int(n ** (1/2)) + 1):
            squares.append(i ** 2)
        
        ans = dp(n)
        return ans
