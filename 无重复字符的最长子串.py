'''
Description: 
Author: Tjg
Date: 2021-06-01 21:55:35
LastEditTime: 2021-07-27 20:37:11
LastEditors: 
'''

# 暴力法 O（n）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max = 0
        for i in range(len(s)):
            sub_str = s[i]
            for j in s[i + 1:]:
                if j not in sub_str:
                    sub_str += j
                    # print(sub_str)
                else: # 子串后边有一个是重复的字符的情况
                    if max < len(sub_str): 
                        max = len(sub_str)
                    break
            else: # 子串在最后边的情况
                if max < len(sub_str): 
                    max = len(sub_str)
                    break

        return max

# 滑动窗口 O（n） 与算法抄不同
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, right = 0, 0
        maxn = 0
        while right < len(s):
            c = s[right]
            right += 1
            # print(c,window)
            while c in window:
                d = s[left]
                left += 1
                window.remove(d)
            # print(left,right)
            window.add(c)
            if right - left > maxn:
                maxn = right - left
        return maxn



string = "abcabcbb"
s1 = Solution()
answer = s1.lengthOfLongestSubstring(string)
print(answer)