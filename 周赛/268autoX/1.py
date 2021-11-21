'''
Description: 
Author: Tjg
Date: 2021-11-21 10:30:09
LastEditTime: 2021-11-21 10:33:46
LastEditors: Please set LastEditors
'''
class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        maxDistance = 0
        for i in range(0, len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    maxDistance = max(maxDistance, j - i)
        return maxDistance