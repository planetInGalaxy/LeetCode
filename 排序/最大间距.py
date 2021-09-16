'''
Description: 
Author: Tjg
Date: 2021-09-07 17:29:13
LastEditTime: 2021-09-07 17:45:51
LastEditors: Please set LastEditors
'''
# 计数排序 超时
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        array = [0] * (max_num - min_num + 1)
        for i in nums:
            array[i - min_num] += 1
        ans = 0
        temp = 0
        for i in range(1,len(array)):
            if array[i] == 0:
                temp += 1
            else:
                ans = max(ans,temp + 1)
                temp = 0
        return ans

# 基数排序
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        array = [0] * (max_num - min_num + 1)
        for i in nums:
            array[i - min_num] += 1
        ans = 0
        temp = 0
        for i in range(1,len(array)):
            if array[i] == 0:
                temp += 1
            else:
                ans = max(ans,temp + 1)
                temp = 0
        return ans