'''
Description: 
Author: Tjg
Date: 2021-08-23 08:26:06
LastEditTime: 2021-08-23 21:10:42
LastEditors: Please set LastEditors
'''
# 动态规划 贪心
class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        print(dp)
        return dp [n]

s1 = Solution()
s1.maxA(7)