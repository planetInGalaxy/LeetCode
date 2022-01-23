'''
Description: 
Author: Tjg
Date: 2022-01-08 16:47:13
LastEditTime: 2022-01-08 16:56:16
LastEditors: Please set LastEditors
'''
# 摩尔投票法
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return None
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = nums[i]
                    count = 1
        return majority