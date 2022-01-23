'''
Description: 
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
Author: Tjg
Date: 2022-01-23 22:15:37
LastEditTime: 2022-01-23 22:17:26
LastEditors: Please set LastEditors
'''
# 数学
# 时间复杂度O(1) 空间复杂度O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def count(num):
            return (num + 1) // 2
        return count(high) - count(low - 1)