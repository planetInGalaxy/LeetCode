'''
Description: 
Author: Tjg
Date: 2021-10-15 18:51:53
LastEditTime: 2021-10-15 20:05:58
LastEditors: Please set LastEditors
'''
# 动态规划 类似斐波那契 p232
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 0:
            return None 
            
        s = str(num)
        a = 1
        b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a

s1 = Solution()
ans = s1.translateNum(624)
print(ans)