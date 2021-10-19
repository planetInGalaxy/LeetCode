'''
Description: 
Author: Tjg
Date: 2021-10-17 12:26:39
LastEditTime: 2021-10-17 12:33:49
LastEditors: Please set LastEditors
'''
# 双指针 本质是不断缩小范围，将大问题逐步化简为小问题 p281
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if nums == [] or len(nums) < 2:
            return None
        
        left = 0
        right = len(nums) - 1
        while True:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [nums[left], nums[right]]
