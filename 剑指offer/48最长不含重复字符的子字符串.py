'''
Description: 
Author: Tjg
Date: 2021-10-15 20:40:12
LastEditTime: 2021-10-16 10:51:45
LastEditors: Please set LastEditors
'''
# 滑动窗口 
# 时间复杂度O(n^2) 空间复杂度O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        left = 0
        right = 0
        maxSum = 0

        while right < len(s):
            while right < len(s) and s[right] not in s[left:right]:
                right += 1
            maxSum = max(maxSum, right - left)

            if right != len(s):
                while s[right] in s[left:right]:
                    left += 1
                right += 1

        return maxSum

# 滑动窗口 哈希表
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        numSet = set()
        left = 0
        right = 0
        maxSum = 0

        while right < len(s):
            while right < len(s) and s[right] not in numSet:
                numSet.add(s[right])
                right += 1
            maxSum = max(maxSum, right - left)

            # right没越界，但是s[right]在之前的集合中，此时要紧缩
            if right != len(s):
                while s[right] in numSet:
                    numSet.remove(s[left])
                    left += 1
                numSet.add(s[right])
                right += 1

        return maxSum

# 动态规划 无法通过 因为力扣上有其他字符
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if s.count(' ') == len(s):
            return 1

        curLength = 0
        maxLength = 0
        position = [-1] * 26
        
        for i in range(0, len(s)):
            prevIndex = position[ord(s[i]) - ord('a')]
            if prevIndex < 0 or i - prevIndex > curLength:
                curLength += 1
            else:
                maxLength = max(maxLength, curLength)
                curLength = i - prevIndex
            position[ord(s[i]) - ord('a')] = i
        
        maxLength = max(maxLength, curLength)
        
        return maxLength

s = "  "
s1 = Solution()
ans = s1.lengthOfLongestSubstring(s)
print(ans)