'''
Description: 
给你一个整数数组 coins ，表示不同面额的硬币；
以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1 。
每种硬币的数量是无限的。
Author: Tjg
Date: 2022-02-21 20:42:08
LastEditTime: 2022-02-21 22:46:25
LastEditors: Please set LastEditors
'''
# 记忆化搜索 
# 时间复杂度O(amount/min(coins) * len(coins)) 
# 空间复杂度O(amount/min(coins))
import functools
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # lru_cache可以缓存函数的结果
        @functools.lru_cache(amount)
        def dp(sum):
            if sum in coins:
                return 1

            ans = float("INF")
            for i in coins:
                if sum >= i:
                    ans = min(ans, dp(sum - i) + 1)
    
            return ans
        
        if amount == 0:
            return 0
        
        # 排序与否，影响不大
        coins.sort()
        ans = dp(amount)
        return ans if ans != float("INF") else -1

# 动态规划
# 时间复杂度O(amount * len(coins)) 
# 空间复杂度O(amount)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i - coin] + 1)
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1 



coins = [186,419,83,408]
amount = 6249
s1 = Solution()
ans = s1.coinChange(coins, amount)
print(ans)