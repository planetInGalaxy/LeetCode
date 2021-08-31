'''
Description: 
Author: Tjg
Date: 2021-06-01 22:26:52
LastEditTime: 2021-06-02 18:50:26
LastEditors: Please set LastEditors
'''
# 超时
class Solution:
    def is_palindrome(self,s):
        s_re = s[::-1]
        # print("s_re "+ s_re + " s " + s)
        if s == s_re:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_str = ""
        s = list(s)
        # print(s)
        for i in range(len(s)):
            sub_s = s[i:]
            sub_sub_s = s[i]
            if max_str == "":
                max_str = sub_sub_s
            # print("ss ",sub_s)
            for j in range(len(sub_s) - 1):
                sub_sub_s +=sub_s[j + 1]
                # print("sss ",sub_sub_s,j,self.is_palindrome(sub_sub_s))
                if self.is_palindrome(sub_sub_s) and len(sub_sub_s) > len(max_str):
                    max_str = sub_sub_s
        return str(max_str)

# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

s = "ac"
s1 = Solution()
answer = s1.longestPalindrome(s)
print(answer)
