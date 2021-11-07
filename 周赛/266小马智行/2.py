'''
Description: 
Author: Tjg
Date: 2021-11-07 11:13:36
LastEditTime: 2021-11-07 11:26:44
LastEditors: Please set LastEditors
'''
class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        basic = 'aeiou'
        for i in range(len(word)):
            if word[i] in basic:
                count += (i + 1) * (len(word) - i)
        
        return count


word = "aba"
s1 = Solution()
ans = s1.countVowels(word)
print(ans)