'''
Description: 
Author: Tjg
Date: 2021-08-12 20:11:35
LastEditTime: 2021-08-12 20:45:58
LastEditors: Please set LastEditors
'''
# 动态规划 二维 反向遍历
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

# 状态压缩 一维
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            pre = 0
            for j in range(i, n):
                if i == j:
                    dp[j] = 1
                    continue
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp    
        return dp[n - 1]