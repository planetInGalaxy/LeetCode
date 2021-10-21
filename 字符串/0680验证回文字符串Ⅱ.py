'''
Description: 
Author: Tjg
Date: 2021-10-20 09:25:40
LastEditTime: 2021-10-20 09:33:43
LastEditors: Please set LastEditors
'''
# 双指针，找到第一个不相同的字符，
# 然后判断去掉左边或者右边的字符后是否为回文串
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(left, right, flag):
            while left < right:
                if s[left] != s[right]:
                    if flag is True:
                        return isValid(left, right - 1, False)\
                            or isValid(left + 1, right, False)
                    else:
                        return False
                left += 1
                right -= 1 
            else:
                return True
        
        if s == "" or len(s) == 1:
            return True
        return isValid(0, len(s) - 1, True)

s = "abba"
s1 = Solution()
ans = s1.validPalindrome(s)
print(ans)