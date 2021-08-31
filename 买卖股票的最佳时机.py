'''
Description: 
Author: Tjg
Date: 2021-01-30 15:44:24
LastEditTime: 2021-01-30 15:48:08
LastEditors: Please set LastEditors
'''
class Solution(object):
    def maxProfit(self, prices):
        left_min = prices[0]
        profit_max = 0
        for i in range(1, len(prices)):
            if prices[i] <= left_min:
                left_min = prices[i]
            elif profit_max <= prices[i] - left_min:
                profit_max = prices[i] - left_min

        return profit_max

s = Solution()
ls = [7,6,4,3,1]
print(s.maxProfit(ls))