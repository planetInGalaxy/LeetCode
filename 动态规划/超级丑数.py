'''
Description: 第n+1个丑数一定是前n个丑数里面的某个丑数乘上质因数之积，
但没有必要每次都对前n个丑数一一乘上质因数，复杂度会达到n2m。
设置pointers数组，记录primes[i]用了多少次
Author: Tjg
Date: 2021-08-09 16:44:16
LastEditTime: 2021-08-09 17:34:40
LastEditors: Please set LastEditors
'''
# 动态规划 疑问
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m =  len(primes)
        pointers = [1] * m

        for i in range(2, n + 1):
            min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
            print(pointers)
            dp[i] = min_num
            for j in range(m):
                if dp[pointers[j]] * primes[j] == min_num:
                    pointers[j] += 1
            
            print(dp)
            print(primes)
            
        
        
        return dp[n]


s1 = Solution()
primes = [2,7,13,19]
n = 12
answer = s1.nthSuperUglyNumber(n,primes)
print(answer)