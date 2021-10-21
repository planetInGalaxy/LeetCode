'''
Description: 
Author: Tjg
Date: 2021-10-20 19:19:30
LastEditTime: 2021-10-20 19:25:22
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n*2^n)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(n):
            if n == len(nums):
                ans.append(subSet[:])
                return
            subSet.append(nums[n])
            dfs(n + 1)
            subSet.pop()
            dfs(n + 1)

        ans = []
        subSet = []
        dfs(0)
        return ans