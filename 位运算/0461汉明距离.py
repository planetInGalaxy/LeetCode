'''
Description: 
Author: Tjg
Date: 2022-01-08 16:43:27
LastEditTime: 2022-01-08 16:45:08
LastEditors: Please set LastEditors
'''
# 异或
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        result = 0
        while xor > 0:
            result += xor & 0b1
            xor >>= 1
        return result