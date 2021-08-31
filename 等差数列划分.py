'''
Description: 
Author: Tjg
Date: 2021-08-10 20:54:53
LastEditTime: 2021-08-10 22:05:56
LastEditors: Please set LastEditors
'''
# 差分 计数
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        
        d, t = nums[0] - nums[1], 0
        ans = 0
        
        # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t
        
        return ans
