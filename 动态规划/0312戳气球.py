'''
Description: 
Author: Tjg
Date: 2021-10-22 15:44:52
LastEditTime: 2021-10-22 15:52:03
LastEditors: Please set LastEditors
'''
# labuladong p187 
# 动态规划
# 时间复杂度O(n^3) 空间复杂度O(n^2)
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        if nums is None:
            return 0

        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        
        dp = [[0] * (n + 2)for _ in range(n + 2)]
        for i in range(n , -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], \
                        dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        
        return dp[0][n + 1]
