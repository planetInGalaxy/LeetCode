'''
Description: 
Author: Tjg
Date: 2021-10-06 17:03:31
LastEditTime: 2021-10-06 17:14:22
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 循环32次 空间复杂度O(1) p 100
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        flag = 1
        max = 2 **32
        while flag <= max:
            if n & flag:
                count += 1
            flag <<= 1
        return count

# 时间复杂度O(n) 循环0b1的个数次 空间复杂度O(1) p 102
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count