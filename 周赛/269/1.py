'''
Description: 
Author: Tjg
Date: 2021-11-28 10:30:31
LastEditTime: 2021-11-28 10:33:07
LastEditors: Please set LastEditors
'''
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans