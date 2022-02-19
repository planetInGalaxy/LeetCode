'''
Description: 
给定一个字符串 s ，找到它的第一个不重复的字符，
并返回它的索引 。如果不存在，则返回 -1 。
Author: Tjg
Date: 2022-02-19 14:06:18
LastEditTime: 2022-02-19 14:07:41
LastEditors: Please set LastEditors
'''
# 哈希
# 时间复杂度O(n) 空间复杂度O(n)
# 由于存储的是-1和下标，第二次遍历只需要遍历哈希表
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None or s == "":
            return -1
        
        map = {}
        for idx, ch in enumerate(s):
            if ch in map:
                map[ch] = -1
            else:
                map[ch] = idx

        for v in map.values():
            if v != -1:
                return v
        else:
            return -1
