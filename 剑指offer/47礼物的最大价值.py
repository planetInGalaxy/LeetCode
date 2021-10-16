'''
Description: 
Author: Tjg
Date: 2021-10-15 20:12:19
LastEditTime: 2021-10-15 20:37:25
LastEditors: Please set LastEditors
'''
# 动态规划 状态压缩 p234
# 时间复杂度O(m*n) 空间复杂度O(m*n)
class Solution:
    def maxValue(self, grid: list[list[int]]) -> int:
        if grid == [] or grid == [[]]:
            return None

        m = len(grid)
        n = len(grid[0])
        # dp = [[0] * (n + 1)] * (m + 1)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
                dp[j] = max(dp[j], dp[j - 1]) + grid[i - 1][j - 1]
        # return dp[m][n]
        return dp[n]

ls = [[1,3,1],[1,5,1],[4,2,1]]
s1 = Solution()
ans = s1.maxValue([[1],[2]])
print(ans)