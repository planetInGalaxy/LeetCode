'''
Description: 
给你一个 只包含正整数的非空数组 nums 。
请你判断是否可以将这个数组分割成两个子集，
使得两个子集的元素和相等。
Author: Tjg
Date: 2022-02-19 15:08:59
LastEditTime: 2022-02-19 16:12:31
LastEditors: Please set LastEditors
'''
# 动态规划
# 时间复杂度O(n*target) 空间复杂度O(n*target)
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if nums is None or len(nums) < 2:
            return False

        s = sum(nums)
        if s % 2 == 1:
            return False
            
        half = s // 2
        n = len(nums)
        # 行数和数组长度有关 列数和target(half)有关
        # 在遍历每一个数字的时候，
        # 状态为在num[0..i]中有无子序列的和为j
        # 根据前面的状态递推出包含该数字时或者不包含该数字时的状态
        dp = [[False] * (half + 1) for _ in range(n)]
        dp[0][0] = True
        if nums[0] <= half:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(half + 1):
                if j == 0:
                    dp[i][j] = True
                elif dp[i - 1][j] is True or \
                    nums[i] <= j and dp[i - 1][j - nums[i]] is True:
                    dp[i][j] = True
        
        return dp[-1][-1]
