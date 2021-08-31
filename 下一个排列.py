'''
Description: 
Author: Tjg
Date: 2021-06-30 10:42:25
LastEditTime: 2021-06-30 11:22:46
LastEditors: Please set LastEditors
'''
# 贪心
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                min = i
                j = i + 1
                while j < len(nums):
                    if nums[j] > nums[i - 1] and nums[j] < nums[min]:
                        min = j
                    j += 1
                nums[i - 1],nums[min] = nums[min],nums[i - 1]
                # 这里应该直接逆序，而不是用排序
                print(nums)
                for k in range(len(nums) -  1, i, -1):
                    print(k)
                    for l in range(i,k):
                        if nums[l] > nums[l + 1]:
                            nums[l],nums[l + 1] = nums[l + 1],nums[l]
                print(nums)
                return
        else:
            nums.sort()
            
s1 = Solution()
nums = [1,2,5,3,2]
s1.nextPermutation(nums)
print(nums)
