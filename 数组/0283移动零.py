'''
Description: 
Author: Tjg
Date: 2022-01-08 17:55:18
LastEditTime: 2022-01-08 18:18:51
LastEditors: Please set LastEditors
'''
# 通过0的个数，计算移动的位置
# 时间复杂度O(n) 空间复杂度O(n)
# 每个位置最多被遍历两遍，无0全一遍，有0全两遍
# 0越多，效率最低
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or nums == []:
            return
        
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i - zeros] = nums[i]
        
        # py易错点：zeros为0时出现问题
        if zeros != 0:
            nums[-zeros:] = [0] * zeros
        
        return 

# 官方题解
# 双指针法 
# 左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部
# 右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移
# 每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变
# 1.左指针左边均为非零数
# 2.右指针左边直到左指针处均为零
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
