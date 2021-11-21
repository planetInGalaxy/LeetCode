'''
Description: 
Author: Tjg
Date: 2021-11-16 11:14:45
LastEditTime: 2021-11-16 11:31:40
LastEditors: Please set LastEditors
'''
# dp
# 注意dp数组的行列分别是哪个
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

        
