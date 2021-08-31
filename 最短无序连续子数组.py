'''
Description: 
Author: Tjg
Date: 2021-08-03 08:16:01
LastEditTime: 2021-08-03 10:01:41
LastEditors: Please set LastEditors
'''
# 先排序再比较 复杂度O(nlogn)
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        def isSorted() -> bool:
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False
            return True
        
        if isSorted():
            return 0
        
        numsSorted = sorted(nums)
        left = 0
        while nums[left] == numsSorted[left]:
            left += 1

        right = n - 1
        while nums[right] == numsSorted[right]:
            right -= 1
        
        return right - left + 1

# 遍历 复杂度O（n）
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1
        if start == len(nums) - 1:
            return 0
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1
        # print(start,end)
        ptr = start
        ptr_end = end
        while ptr <= ptr_end:
            while start >= 0 and nums[ptr] < nums[start]:
                start -= 1
            while end <= len(nums) - 1 and nums[ptr] > nums[end]:
                end += 1
            ptr += 1
        return end - start - 1

# 官方 一次遍历 疑问
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        return 0 if right == -1 else right - left + 1
