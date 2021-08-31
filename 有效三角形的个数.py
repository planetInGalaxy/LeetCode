'''
Description: 
Author: Tjg
Date: 2021-08-04 13:34:47
LastEditTime: 2021-08-04 14:58:35
LastEditors: Please set LastEditors
'''
# 排序 + 二分查找
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                sum = nums[i] + nums[j]
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] < sum:
                        left = mid + 1
                    elif nums[mid] >= sum:
                        right = mid - 1
                ans += left - 1 - j
        return ans    