'''
Description: 
给你一个整数数组nums和一个整数k，
请你统计并返回该数组中和为k的连续子数组的个数。
Author: Tjg
Date: 2022-02-10 23:51:00
LastEditTime: 2022-02-11 00:24:12
LastEditors: Please set LastEditors
'''
# 官方 前缀和 
# 超时
# 时间复杂度O(n2) 空间复杂度O(1)
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if nums is None or nums == []:
            return 0

        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        
        return count

# 官方 前缀和+哈希表优化
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if nums is None or nums == []:
            return 0

        count = 0
        pre = 0
        map = {}
        map[0] = 1
        # 我们考虑以i结尾的和为k的连续子数组个数时
        # 只要统计有多少个前缀和为pre[i]−k的pre[j]即可
        # 因为此时子数组subNums[j...i]的和就是k
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in map:
                count += map[pre - k]
            map[pre] = map.get(pre, 0) + 1
        
        return count