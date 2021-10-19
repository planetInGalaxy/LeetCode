'''
Description: 
Author: Tjg
Date: 2021-10-18 09:38:55
LastEditTime: 2021-10-18 09:45:34
LastEditors: Please set LastEditors
'''
# 时间复杂度O(nlogn) 空间复杂度O(1)
class Solution:
    def isStraight(self, nums: list[int]) -> bool:
        if nums == [] or len(nums) < 5:
            return None
        
        nums.sort()
        countOf0 = nums.count(0)
        start = countOf0
        for i in range(start, len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff == 0:
                return False
            elif diff > 1:
                countOf0 -= (diff - 1)
                if countOf0 < 0:
                    return False
            else:
                pass
        else:
            return True

