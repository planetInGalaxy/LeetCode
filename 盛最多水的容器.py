'''
Description: 
Author: Tjg
Date: 2021-06-02 18:05:55
LastEditTime: 2021-08-25 10:19:48
LastEditors: Please set LastEditors
'''
# 双指针 + 贪心
class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
