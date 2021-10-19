'''
Description: 
Author: Tjg
Date: 2021-10-18 11:15:14
LastEditTime: 2021-10-18 11:22:28
LastEditors: Please set LastEditors
'''
# p305
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 因为返回值是int，所以无效的情况下利润为0
        if len(prices) < 2:
            return 0

        buy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - buy
            if diff > 0:
                maxProfit = max(maxProfit, diff)
            else:
                buy = prices[i]
        
        return maxProfit