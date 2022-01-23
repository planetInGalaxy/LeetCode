'''
Description: 
Author: Tjg
Date: 2022-01-08 22:48:46
LastEditTime: 2022-01-08 23:15:45
LastEditors: Please set LastEditors
'''
# 官方题解
# 原地哈希
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for num in nums:
            # 既能影响到index值，又不会使其失去信息
            index = (num - 1) % n
            nums[index] += n
        
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret

nums = [4,3,2,7,8,2,3,1]
s1 = Solution()
ans = s1.findDisappearedNumbers(nums)
print(ans)
