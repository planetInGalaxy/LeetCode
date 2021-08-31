'''
Description: 
Author: Tjg
Date: 2021-08-29 09:31:47
LastEditTime: 2021-08-29 10:18:24
LastEditors: Please set LastEditors
'''
# 异或 O（n）
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans

# 二分 O（logn）
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # print(left,right,mid)
            if mid % 2 == 0 and nums[mid] == nums[mid + 1] \
                or mid % 2 == 1 and nums[mid] == nums[mid - 1]:
                left = mid + 1
            elif mid % 2 == 0 and nums[mid] == nums[mid - 1] \
                or mid % 2 == 1 and nums[mid] == nums[mid + 1]:
                right = mid
            else:
                return nums[mid]
        print(nums[left])
        return nums[left]
        
nums = [2]
s1 = Solution()
s1.singleNonDuplicate(nums)