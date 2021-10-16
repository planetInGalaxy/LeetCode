'''
Description: 
Author: Tjg
Date: 2021-10-15 14:11:03
LastEditTime: 2021-10-15 14:16:28
LastEditors: Please set LastEditors
'''
# 动态规划 状态压缩 p220
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if nums == []:
            return None
        
        dp = nums[0]
        maxSum = dp
        for i in range(1, len(nums)):
            if dp < 0:
                dp = nums[i]
            else:
                dp += nums[i]
            maxSum = max(maxSum, dp)
        return maxSum