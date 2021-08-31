'''
Description: 
Author: Tjg
Date: 2021-07-29 17:00:36
LastEditTime: 2021-07-29 17:04:35
LastEditors: 
'''
# dp 状态压缩
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp_0 = nums[0]
        ans = dp_0
        for i in range(1,len(nums)):
            if dp_0 < 0:
                dp_0 = nums[i]
            else:
                dp_0 = dp_0 + nums[i]
            if dp_0 > ans:
                ans = dp_0
        return ans