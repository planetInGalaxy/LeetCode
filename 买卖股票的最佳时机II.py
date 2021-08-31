'''
Description: 
Author: Tjg
Date: 2021-01-30 15:27:28
LastEditTime: 2021-01-30 15:33:45
LastEditors: Please set LastEditors
'''
class Solution(object):
    def maxProfit(self, prices):
        left_min = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] <= left_min:
                left_min = prices[i]
            else:
                profit += prices[i] - left_min
                left_min = prices[i]

        return profit

s = Solution()
ls = [7,6,4,3,1]
print(s.maxProfit(ls))
