'''
Description: 
Author: Tjg
Date: 2021-07-27 18:29:01
LastEditTime: 2021-07-27 18:29:23
LastEditors: 
'''
# 滑动窗口 与算法小抄不同
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        for i in s1:
            need[i] = need.get(i, 0) + 1
        left, right = 0, 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1
            if need.get(c, 0) != 0:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(s1):
                    return True
                d = s2[left]
                left += 1
                if need.get(d, 0) != 0:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        else:
            return False