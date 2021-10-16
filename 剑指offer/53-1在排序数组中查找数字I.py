'''
Description: 
Author: Tjg
Date: 2021-10-16 17:53:19
LastEditTime: 2021-10-16 18:03:54
LastEditors: Please set LastEditors
'''
# 二分查找
# 时间复杂度O(logn) 空间复杂度O(1)
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums == []:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if left < len(nums) and nums[left] == target:
            start = left
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    left = mid + 1
            if right >= 0 and nums[right] == target:
                end = right
                return end - start + 1
            else:
                return 0
        else:
            return 0

nums = [5,7,7,8,8,10]
target = 8
s1 = Solution()
ans = s1.search(nums, target)
print(ans)