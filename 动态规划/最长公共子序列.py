'''
Description: 
Author: Tjg
Date: 2021-07-29 14:54:32
LastEditTime: 2021-07-29 14:55:24
LastEditors: 
'''
# 动态规划
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        for i in range(1,len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text2[j - 1] == text1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
