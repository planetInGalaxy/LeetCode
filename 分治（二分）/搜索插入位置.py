'''
Description: 
Author: Tjg
Date: 2021-07-21 19:07:23
LastEditTime: 2021-07-21 19:14:45
LastEditors: Please set LastEditors
'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return left