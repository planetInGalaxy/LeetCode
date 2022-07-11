'''
Description: 
Author: Tjg
Date: 2022-07-10 21:24:58
LastEditTime: 2022-07-10 21:30:35
LastEditors: Please set LastEditors
'''
# 暴力 O(n^2)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return None

        if needle is '':
            return 0
        
        if haystack is '':
            return -1

        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    break
            else:
                return i
        else:
            return -1