'''
Description: 
Author: Tjg
Date: 2021-06-16 20:38:32
LastEditTime: 2021-06-17 16:09:17
LastEditors: Please set LastEditors
'''
'''
1000000007 比 1e9 + 7更好
因为前者是int 后者是float 会有误差
'''

# 2^n 超时
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return int(self.fib(n - 1) + self.fib(n - 2) % (1e9+7))

# 线性递归 O（n）
class Solution:
    def fib(self, n: int) -> int:
        return self.good_fib(n)[0]
    def good_fib(self,n):
        if n <= 1:
            return (n,0)
        else:
            (a, b) = self.good_fib(n - 1)
            return (int((a + b) % (1e9 + 7)), a)


# 动态规划 O（n）
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return n
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp[i])
        return dp[-1] % 1000000007

# 动态规划 迭代 O（n） 最优
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            print(a)
        return a % 1000000007


s1 = Solution()
answer = s1.fib(81)
print(answer)