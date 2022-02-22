'''
Description: 
给你两个单词 word1 和 word2，
请返回将 word1 转换成 word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
Author: Tjg
Date: 2022-02-22 20:47:57
LastEditTime: 2022-02-22 21:51:02
LastEditors: Please set LastEditors
'''
# 动态规划
# 时间复杂度O(nm) 空间复杂度O(nm)
from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # 注意需要给定缓存大小
        @lru_cache(n * m)
        def dp(i, j):
            if i == n and j == m:
                return 0
            elif i == n:
                return abs(m - j)
            elif j == m:
                return abs(n - i)
            
            if word1[i] == word2[j]:
                ans = dp(i + 1, j + 1)
            # 定义不同 
            # elif i != n - 1 and j != m - 1 and \
            #     word1[i] == word2[j + 1] and word1[i + 1] == word2[j]:
            #     ans = min(dp(i, j + 1), dp(i + 1, j), dp(i + 2, j + 2)) + 1
            # elif word1[i] != word2[j]:
            else:
                ans = min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1)) + 1

            return ans

        return dp(0, 0)

word1 = "intention"
word2 = "execution"
s1 = Solution()
ans = s1.minDistance(word1, word2)
print(ans)