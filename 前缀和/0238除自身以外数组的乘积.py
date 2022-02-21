'''
Description: 
给你一个整数数组 nums，返回数组 answer ，
其中 answer[i] 等于 nums 中除 nums[i] 
之外其余各元素的乘积。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。
Author: Tjg
Date: 2022-02-21 22:00:29
LastEditTime: 2022-02-21 22:26:57
LastEditors: Please set LastEditors
'''
# 前缀和 遍历两遍
# 时间复杂度O(n)
# 空间复杂度O(1) (不包含输入输出)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if nums is None or len(nums) < 2:
            return None
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        pre = 1
        for i in range(n - 1, -1, -1):
            ans[i] = pre * ans[i]
            pre *= nums[i]

        return ans