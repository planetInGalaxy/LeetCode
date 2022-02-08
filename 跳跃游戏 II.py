'''
Description: 
Author: Tjg
Date: 2021-01-30 16:38:41
LastEditTime: 2022-01-26 00:17:55
LastEditors: Please set LastEditors
'''
# 贪心
# 时间复杂度O(n)
class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        count = 0
        i = 0
        while i < len(nums) - 1:
            max_step = 0
            max_index = i
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums) - 1:
                    count += 1
                    return count
                if max_step <= j - i + nums[j]:
                    max_step = j - i + nums[j]
                    max_index = j
            i = max_index
            count += 1
        return count

# 贪心
# 时间复杂度O(n)
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


s = Solution()
ls = [2,3,1,1,4]
print(s.jump(ls))
