'''
Description: 
Author: Tjg
Date: 2021-10-06 16:21:41
LastEditTime: 2021-10-06 16:52:48
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n2） 空间复杂度O（n） p 96
# 动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[j] * dp[i - j], dp[i])
        return dp[n]

# 贪心
# 时间复杂度O(1) 空间复杂度O(1) p98
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        timesOf3 = n // 3
        if n == timesOf3 * 3 + 1:
            timesOf3 -= 1
            timesOf2 = 2
        elif n == timesOf3 * 3 + 2:
            timesOf2 = 1
        else:
            timesOf2 = 0
        return pow(3, timesOf3) * pow(2, timesOf2) % int(1e9+7)

