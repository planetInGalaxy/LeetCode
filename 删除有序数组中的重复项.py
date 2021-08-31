'''
Description: 
Author: Tjg
Date: 2021-07-20 22:39:21
LastEditTime: 2021-07-20 22:55:52
LastEditors: Please set LastEditors
'''
# 原地修改
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        length = 1
        last = nums[0]
        last_left_i = 0
        for i in range(1,len(nums)):
            if nums[i] != last:
                last = nums[last_left_i + 1] = nums[i]
                last_left_i += 1
                length += 1             
        return length