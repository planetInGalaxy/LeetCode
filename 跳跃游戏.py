'''
Description: 
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
Author: Tjg
Date: 2021-01-30 15:51:58
LastEditTime: 2022-01-25 23:33:58
LastEditors: Please set LastEditors
'''
# 贪心
# 时间复杂度O(n)
class Solution:
    def canJump(self, nums):
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if max_i >= i and i+jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  # 更新最远能到达位置
        return max_i >= i

s = Solution()
ls = [2,0,0]
print(s.canJump(ls))
