'''
Description: 
Author: Tjg
Date: 2022-01-23 21:58:40
LastEditTime: 2022-01-23 22:10:09
LastEditors: Please set LastEditors
'''
# 贪心
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        if target is None or target == []:
            return None
        
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(target[i] - target[i - 1], 0)
        return ans
            