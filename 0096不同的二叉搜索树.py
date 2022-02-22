'''
Description: 
给你一个整数 n ，
求恰由 n 个节点组成且节点值从 1 到 n 
互不相同的二叉搜索树有多少种？
返回满足题意的二叉搜索树的种数。
Author: Tjg
Date: 2021-12-04 23:36:23
LastEditTime: 2022-02-22 22:17:56
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(1)
# 开塔兰数：给定一个栈的入栈序列，出栈序列的种类数
# C[2n, n] / (n + 1)
from functools import lru_cache, reduce
import operator
class Solution:
    def numTrees(self, n: int) -> int:
        def fact(m):
            return reduce(operator.mul, range(1, m + 1))

        res = fact(2 * n) / fact(n) ** 2 / (n + 1)
        return int(res)

# 动态规划（记忆化搜索）
# 时间复杂度O(n2) 空间复杂度O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(n)
        def dp(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            
            ans = 0
            for i in range(n):
                sum1 = dp(i)
                sum2 = dp(n - i - 1)
                if sum1 != 0 and sum2 != 0:
                    ans += sum1 * sum2
                elif sum1 == 0:
                    ans += sum2
                elif sum2 == 0:
                    ans += sum1
            
            # print(n, ans)
            return ans
        
        return dp(n)

# 非递归的动态规划
# 时间复杂度O(n2) 空间复杂度O(n)
class Solution:
    def numTrees(self, n):

        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]

n = 3
s1 = Solution()
ans = s1.numTrees(n)
print(ans)

