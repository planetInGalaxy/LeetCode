'''
Description: 
Author: Tjg
Date: 2021-07-20 21:49:52
LastEditTime: 2021-07-20 21:54:31
LastEditors: Please set LastEditors
'''
# 排序 + 贪心 O（nlogn）
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max = 0
        for i in range(len(nums) // 2):
            sum = nums[i] + nums[-(i + 1)]
            if max < sum:
                max = sum
        return max