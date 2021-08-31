'''
Description: 
Author: Tjg
Date: 2021-08-28 11:07:15
LastEditTime: 2021-08-28 12:39:38
LastEditors: Please set LastEditors
'''
# No
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [[[0,0,0]] * n for _ in range(n)]
        for i in range(n):
            if s[i] == '(':
                dp[i][i] = [1,0,0]
            else:
                dp[i][i] = [0,1,0]
        print(dp)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[j] == '(':
                        dp[i][j - 1][1] += 1
                if s[j] == ')':
                    if dp[i][j - 1][0] > 0:
                        dp[i][j - 1][0] -= 1
                        dp[i][j - 1][2] += 1
                    else:
                        break
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if dp[i][j][0] == 0 and dp[i][j][1] == 0 and ans < dp[i][j][2] * 2:
                    ans = dp[i][j][2] * 2
        for i in dp:
            print(i)
        print(ans)                        

# 动态规划 O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                if s[i - 1] == ')':
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0) + 2
        return max(dp)
        
s = "(()))())("          
s1 = Solution()
ans = s1.longestValidParentheses(s)
print(ans)