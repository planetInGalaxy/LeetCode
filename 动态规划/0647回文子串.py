'''
Description: 
Author: Tjg
Date: 2022-02-11 21:01:05
LastEditTime: 2022-02-11 21:11:18
LastEditors: Please set LastEditors
'''
# 动态规划
# 时间复杂度O(n2) 空间复杂度O(n2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None or s == "":
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # 一个字母为回文串
        for i in range(n):
            dp[i][i] = 1

        ans = n
        # 因为是从左下到右上递推，
        # 所以i由大到小，j由小到大迭代
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 左下角无递推来源，特殊处理
                if i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        ans += 1
                # 左下角有递推来源
                else:
                    if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                        dp[i][j] = 1
                        ans += 1

        return ans 
        