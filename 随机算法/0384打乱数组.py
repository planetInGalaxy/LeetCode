'''
Description: 
给你一个整数数组nums ，设计算法来打乱一个没有重复元素的数组。
打乱后，数组的所有排列应该是等可能的。
Author: Tjg
Date: 2022-02-13 22:51:41
LastEditTime: 2022-02-13 23:04:48
LastEditors: Please set LastEditors
'''
# 官方 暴力解法
# 时间复杂度 三个函数：O(n) O(n) O(n2)
# 空间复杂度O(n)
import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.nums)
        # 随机抽取一个数并移除
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums

# 官方 Fisher-Yates 洗牌算法
# 时间复杂度 三个函数：O(n) O(n) O(n)
# 空间复杂度O(n)
import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        # 随机抽取一个数并移除
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums