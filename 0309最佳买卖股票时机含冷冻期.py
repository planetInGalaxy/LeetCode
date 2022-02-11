'''
Description: 
Author: Tjg
Date: 2022-02-11 22:01:06
LastEditTime: 2022-02-11 23:06:19
LastEditors: Please set LastEditors
'''
# 官方
# 动态规划
# 时间复杂度O(n) 空间复杂度O(n)
# 对于每一日，一共只有三种状态，持有，不持有，不持有且冷冻，
# 对于所有交易日，一共3n种状态
# 每种状态的收益由一个dp数组来定义，表示当天结束后的状态
# 状态转移方程根据规则，并利用之前的三种状态来定义
# max(f[i - 1][1], f[i - 1][2])是当前最优子结构
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] \
            + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            # 之前已经持有，或者在今天（非冷冻期）买入
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            # 前一天一定要持有股票，然后今天卖出
            f[i][1] = f[i - 1][0] + prices[i]   
            # 股票是昨天卖出，或者很久之前卖出
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        
        return max(f[n - 1][1], f[n - 1][2])
