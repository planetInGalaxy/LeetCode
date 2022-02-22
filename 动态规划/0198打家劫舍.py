'''
Description: 
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，
计算你不触动警报装置的情况下，
一夜之内能够偷窃到的最高金额。
Author: Tjg
Date: 2022-02-22 20:14:13
LastEditTime: 2022-02-22 20:15:14
LastEditors: Please set LastEditors
'''
# 动态规划 状态压缩
# O(n) O(1)
class Solution:
    def rob(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return None
        
        n = len(nums)
        dp_not_rob = 0
        dp_rob = nums[0]
        for i in range(1, n):
            temp = dp_not_rob
            dp_not_rob = max(dp_not_rob, dp_rob)
            dp_rob = temp + nums[i]
        
        return max(dp_not_rob, dp_rob)