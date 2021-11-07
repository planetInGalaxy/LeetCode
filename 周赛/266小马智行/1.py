'''
Description: 
Author: Tjg
Date: 2021-11-07 10:29:55
LastEditTime: 2021-11-07 11:13:30
LastEditors: Please set LastEditors
'''
# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         def judge(current):
#             return current['a'] >= 1 and current['b'] >= 1 and current['c'] >= 1 \
#                 and current['d'] >= 1 and current['e'] >= 1
#         left = 0
#         right = 0
#         basic = ('a', 'e', 'i', 'o', 'u')
#         count = 0

#         current = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
#         while left < len(word) and right < len(word):
#             while word[left] not in basic:
#                 left += 1
#             if left >= len(word) - 4:
#                 break

#             right = left
#             while right < len(word) and word[right] in basic:
#                 current[right] += 1
#                 if judge(current):
#                     count += 1
#                 right += 1

#             if right >= len(word) - 5:
#                 break
#             left = right + 1

#         return count
# O(n^2)
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def judge(string):
            basic = {'a', 'e', 'i', 'o', 'u'}
            alphaSet = set()
            for i in string:
                alphaSet.add(i)
            # print(basic, alphaSet)
            if alphaSet == basic:
                return True
            else:
                return False

            
        
        count = 0
        for i in range(len(word) - 4):
            for j in range(i + 4, len(word)):
                # print(word[i:j + 1])
                if judge(word[i:j + 1]):
                    count += 1
        
        return count

word = "cuaieuouac"
s1 = Solution()
ans = s1.countVowelSubstrings(word)
print(ans)