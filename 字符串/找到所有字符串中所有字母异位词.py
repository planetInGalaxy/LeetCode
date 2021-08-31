'''
Description: 
Author: Tjg
Date: 2021-07-27 19:57:36
LastEditTime: 2021-07-27 19:57:37
LastEditors: 
'''
# 滑动窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need = {}
        window = {}
        for i in p:
            need[i] = need.get(i, 0) + 1
        left, right = 0,0
        invalid = 0
        ans = []
        while right < len(s):
            c = s[right]
            right += 1
            if need.get(c, 0) != 0:
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    invalid += 1

            while invalid == len(need):
                if right - left == len(p):
                    ans.append(left)
                d = s[left]
                left += 1
                if need.get(d, 0) != 0:
                    if need[d] == window[d]:
                        invalid -= 1
                    window[d] -= 1
        return ans