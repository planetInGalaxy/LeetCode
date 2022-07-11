'''
Description: 
给你一个数组 nums 和一个值 val，
你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
Author: Tjg
Date: 2022-07-10 20:41:14
LastEditTime: 2022-07-10 21:22:34
LastEditors: Please set LastEditors
'''
# 计数法 略
# 双指针法
# left最终的位置 -> 数组大小
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return None

        left = 0
        right = len(nums)
        # 左闭右开
        # 可以保证只有一个元素的时候，进入循环
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                nums[left] = nums[right - 1]
                right -= 1

        return left
        