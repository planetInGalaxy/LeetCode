'''
Description: 
Author: Tjg
Date: 2021-07-16 12:54:40
LastEditTime: 2021-07-16 13:46:40
LastEditors: Please set LastEditors
'''
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while right > left:
            print(left,right,len(nums))
            while nums[left] == 0 and left < len(nums):
                left += 1
                if left == len(nums) - 1:
                    return
            while nums[right] == 2 and right > -1:
                right -= 1
                if right == 0:
                    return
            if not (nums[left] == 1 and nums[right] == 1):
                nums[left],nums[right] = nums[right],nums[left]
            else:
                p = left + 1
                while p < right:
                    if nums[p] == 0:
                        nums[left],nums[p] = nums[p],nums[left]
                        break
                    elif nums[p] == 2:
                        nums[right],nums[p] = nums[p],nums[right]
                        break
                    p += 1
                else:
                    break

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
            print(p0,p2,i,nums)

s1 = Solution()
nums = [2,1,2,1,0,1,0]
answer = s1.sortColors(nums)
print(nums)
