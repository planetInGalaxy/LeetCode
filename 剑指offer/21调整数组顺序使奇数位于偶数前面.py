'''
Description: 
Author: Tjg
Date: 2021-10-07 17:59:08
LastEditTime: 2021-10-07 18:17:30
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n） 空间复杂度O(1) p131
# 双指针
class Solution:
    def exchange(self, nums: list[int]) -> list[int]:
        if nums == []:
            return []
        left = 0
        right = len(nums) - 1
        while left < right:
            # 用while里的left < right而不是在下面添加if的两个原因：
            # 1 防止过头，right在left的左边，交换出错
            # 2 防止下标溢出
            while nums[left] & 0b1 == 1 and left < right:
                left += 1
            while nums[right] & 0b1 == 0 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums