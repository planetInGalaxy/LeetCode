'''
Description: 
Author: Tjg
Date: 2021-08-23 08:53:01
LastEditTime: 2021-08-23 09:21:01
LastEditors: Please set LastEditors
'''
# 动态规划 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(i,j):
            # print(i,j)
            if j == n:
                return i == m
            if i == m:
                if (n - j) % 2 == 1:
                    return False
                for k in range(j + 1, n, 2):
                    if p[k] != '*':
                        return False
                return True
            
            key = (i,j)
            if key in memo:
                return memo[key]
            
            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < n - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    res = dp(i + 1, j + 1)
            else:
                if j < n - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2)
                else:
                    res = False
            
            memo[key] = res
            return res

        m = len(s)
        n = len(p)
        memo = {}
        dp(0,0)
        # print(memo)
        return memo[(0,0)]

s = 'aa'
p = '.*'
s1 = Solution()
s1.isMatch(s,p)