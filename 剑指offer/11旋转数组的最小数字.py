'''
Description: 
Author: Tjg
Date: 2021-10-06 10:57:00
LastEditTime: 2021-10-06 11:14:30
LastEditors: Please set LastEditors
'''
# 时间复杂度O（logn + n） 空间复杂度O（1） p86
class Solution:
    def minArray(self, numbers: list[int]) -> int:
        if not numbers:
            return None
        # 只有一/两个元素的特殊情况
        if len(numbers) <= 2:
            return min(numbers)

        left = 0
        right = len(numbers) - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            # 旋转度为0的情况
            if numbers[left] < numbers[right]:
                return numbers[left]
            # 三数相同的情况
            if numbers[mid] == numbers[left] and \
                numbers[mid] == numbers[right]:
                return min(numbers)
            # 正常情况
            if numbers[mid] >= numbers[left]:
                left = mid
            elif numbers[mid] <= numbers[right]:
                right = mid
        # left是最大的数，right是最小的数
        return numbers[right]