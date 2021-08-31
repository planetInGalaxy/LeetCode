'''
Description: 
Author: Tjg
Date: 2021-01-30 15:51:58
LastEditTime: 2021-01-30 16:38:29
LastEditors: Please set LastEditors
'''
class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        i = 0
        while True:
            if i + nums[i] >= len(nums) - 1:
                return True
            elif nums[i] == 0:
                return False
            max_step = 0
            max_index = 0
            for j in range(i + 1, i + nums[i] + 1):
                if max_step <= j - i + nums[j]:
                    max_step = j - i + nums[j]
                    max_index = j
            i = max_index

s = Solution()
ls = [2,0,0]
print(s.canJump(ls))
