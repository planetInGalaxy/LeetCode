'''
Description: 
Author: Tjg
Date: 2021-10-18 21:50:44
LastEditTime: 2021-10-22 15:58:54
LastEditors: Please set LastEditors
'''
# labuladong
# 动态规划 自顶向下 
# 剑指offer题的数据有 空字符串 需要额外判断
# 时间复杂度O(m*n) 空间复杂度O(m*n)
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
        
        # 因为可能有空串，所以需要额外判断，判断方式与递归终止条件类似
        if n == 0:
            return m == 0

        if m == 0:
            if n % 2 == 1:
                return False
            for i in range(1, n, 2):
                if p[i] != '*':
                    return False
            else:
                return True
  
        memo = {}
        dp(0,0)
        # print(memo)
        return memo[(0,0)]

s = ''
p = '.*'
s1 = Solution()
ans = s1.isMatch(s,p)
print(ans)