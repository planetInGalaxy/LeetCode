'''
Description: 
Author: Tjg
Date: 2021-01-30 16:38:41
LastEditTime: 2021-01-30 16:48:40
LastEditors: Please set LastEditors
'''
class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        count = 1
        i = 0
        while i + nums[i] < len(nums) - 1:
            max_step = 0
            max_index = 0
            for j in range(i + 1, i + nums[i] + 1):
                if max_step <= j - i + nums[j]:
                    max_step = j - i + nums[j]
                    max_index = j
            i = max_index
            count += 1
        return count

s = Solution()
ls = [2,3,1,1,4]
print(s.jump(ls))
