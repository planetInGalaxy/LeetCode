'''
Description: 
Author: Tjg
Date: 2021-08-13 23:16:11
LastEditTime: 2021-08-13 23:28:29
LastEditors: Please set LastEditors
'''
# 动态规划 二维 保存最大值
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_l = 0
        max_r = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if dp[i + 1][j - 1] != -1 and s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_r - max_l + 1:
                        max_l = i
                        max_r = j
                else:
                    dp[i][j] = -1
        return s[max_l:max_r + 1]

s1 = Solution()
s = "babad"
answer = s1.longestPalindrome(s)
print(answer)