'''
Description: 
Author: Tjg
Date: 2021-07-27 18:05:52
LastEditTime: 2021-07-27 18:28:07
LastEditors: 
'''

# 新知识 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window ={}
        for i in t:
            need[i] = need.get(i, 0) + 1

        left, right = 0, 0
        valid = 0
        start, end = 0, 100000
        while right < len(s):
            c = s[right]
            right += 1
            if need.get(c, 0) != 0:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < end - start:
                    start, end = left, right
                d = s[left]
                left += 1
                if need.get(d, 0) != 0:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if end == 100000 else s[start:end]

