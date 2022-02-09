'''
Description: 
Author: Tjg
Date: 2022-01-24 21:37:52
LastEditTime: 2022-02-09 20:25:47
LastEditors: Please set LastEditors
'''
# list代替字符串
# 时间复杂度O(mn) 空间复杂度O(n)
class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        if words is None or words == [] or s == "":
            return None
        s = list(s)
        now = []
        for i in words:
            now.extend(list(i))
            if now == s:
                return True
            if len(now) >= len(s):
                return False
        else:
            return False