'''
Description: 
Author: Tjg
Date: 2021-10-24 10:29:34
LastEditTime: 2021-10-24 10:45:35
LastEditors: Please set LastEditors
'''
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def isValid(s: str):
            if s.count('-') > 1 or s.count('!') + s.count(',') + \
                s.count('.') > 1:
                return False
                
            for i in range(len(s)):
                if s[i] in '0123456789' or \
                    i != len(s) - 1 and s[i] in '!,.':
                    return False
                if s[i] == '-':
                    if i == 0 or i == len(s) - 1 or i == len(s) - 2 and s[-1] in '!,.':
                        return False
        
            return True
            pass
        sentenceList = sentence.split()
        ans = 0
        for i in sentenceList:
            if isValid(i):
                ans += 1
        
        return ans

s = "!this  ans-a b8d!"
s1 = Solution()
ans = s1.countValidWords(s)
print(ans)