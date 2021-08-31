'''
Description: 
Author: Tjg
Date: 2021-07-16 09:28:18
LastEditTime: 2021-07-21 17:41:34
LastEditors: Please set LastEditors
'''
# 原地哈希
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # 数据预处理 全部变为范围外的n+1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] >= n + 1:
                nums[i] = n + 1
        # 将出现的数字映射到列表中的元素中
        for i in range(len(nums)):
            if abs(nums[i]) != n + 1:
                nums[abs(nums[i]) - 1] *= (-1 if nums[abs(nums[i]) - 1] > 0 else 1)
        print(nums)
        # 寻找最小的未被标记的正整数
        for i in range(len(nums)):
             if nums[i] > 0:
                 return i + 1
        return n + 1

s1 = Solution()
nums = [3,4,-1,1]
answer = s1.firstMissingPositive(nums)
print(answer)