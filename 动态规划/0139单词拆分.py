'''
Description: 
给你一个字符串s和一个字符串列表wordDict作为字典。
请你判断是否可以利用字典中出现的单词拼接出s。
注意：不要求字典中出现的单词全部都使用，
并且字典中的单词可以重复使用。
Author: Tjg
Date: 2022-02-09 20:46:35
LastEditTime: 2022-02-09 21:41:18
LastEditors: Please set LastEditors
'''
# 暴力解法 DFS
# 时间复杂度O(n!xm) 单词数n，平均长度m
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def dfs(i):
            # print(i, len(s))
            if i == len(s):
                return True
            for word in wordDict:
                # print(word)
                for j in range(len(word)):
                    if i + j >= len(s) or s[i + j] != word[j]:
                        break
                else:
                    # print(i, j, i + j + 1)
                    # 这里不能直接return dfs()
                    # 否则return之后直接跳出当前函数调用栈的循环
                    # 导致漏算
                    ans = dfs(i + j + 1)
                    if ans is True:
                        return True
            return False
 
        return dfs(0)

# 官方
# 动态规划
# 时间复杂度O(n2)
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[-1]
        
s = "cars"
wordDict = ["car","ca","rs"]
s1 = Solution()
ans = s1.wordBreak(s, wordDict)
print(ans)