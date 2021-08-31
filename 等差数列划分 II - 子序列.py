'''
Description: 
Author: Tjg
Date: 2021-08-11 21:13:40
LastEditTime: 2021-08-11 21:46:09
LastEditors: Please set LastEditors
'''
# 动态规划 + 哈希
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        # 字典列表
        f = [defaultdict(int) for _ in nums]
        # 遍历每两个数
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans
