'''
Description: 
Author: Tjg
Date: 2021-10-16 19:00:00
LastEditTime: 2021-10-16 19:18:14
LastEditors: Please set LastEditors
'''
# 二分查找 p266
# 时间复杂度O(logn) 空间复杂度O(1)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if nums == []:
            return None
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        # 循环条件带等号 退出时有 right = left - 1
        # 本体要寻找第一个不符合 == 的值，这个值是 == 的值的右边第一个
        # 由于left = mid + 1 所以left会趋近该值
        # 由于right = mid - 1 所以right会趋近于最后一个 == 的值
        return left

ls = [1,2]
s1 = Solution()
ans = s1.missingNumber(ls)
print(ans)