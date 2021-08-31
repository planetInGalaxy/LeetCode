'''
Description: 
Author: Tjg
Date: 2021-07-20 20:44:16
LastEditTime: 2021-07-20 21:20:06
LastEditors: Please set LastEditors
'''
# 纵向比较法 O（mn）
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs == []:
            return ""
        prefix = ""
        n = 0
        while True:
            if n < len(strs[0]):
                temp = strs[0][n]
            else:
                return prefix
            for i in strs:
                if n >= len(i) or temp != i[n]:
                    return prefix
            else:
                prefix = prefix + temp
            n += 1
        return prefix

# 简洁版本
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sub=strs[0]
        for index,m in enumerate(sub):
            for i in strs:
                if index>=len(i) or i[index]!=m:
                    return sub[0:index]
        return sub
        
# 先找出max和min  再比较 O（n）
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1