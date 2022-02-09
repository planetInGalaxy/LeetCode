'''
Description: 
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组
(该子数组中至少包含一个数字)，并返回该子数组所对应的乘积。
Author: Tjg
Date: 2022-02-09 22:04:21
LastEditTime: 2022-02-09 23:14:44
LastEditors: Please set LastEditors
'''
# 官方
# 动态规划
# 时间复杂度O(n)
# 考虑当前位置如果是一个负数的话，那么我们希望
# 以它前一个位置结尾的某个段的积也是个负数，
# 这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，
# 即尽可能小。如果当前位置是一个正数的话，
# 我们更希望以它前一个位置结尾的某个段的积也是个正数，
# 并且希望它尽可能地大。
# 因此同时维护min和max

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return 0

        ans = minF = maxF = nums[0]
        for i in range(1, len(nums)):
            mx = maxF
            mn = minF
            maxF = max(mx * nums[i], mn * nums[i], nums[i])
            minF = min(mx * nums[i], mn * nums[i], nums[i])
            ans = max(maxF, ans)
        return ans
