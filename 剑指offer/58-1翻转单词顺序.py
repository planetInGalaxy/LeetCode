'''
Description: 
Author: Tjg
Date: 2021-10-17 15:09:31
LastEditTime: 2021-10-17 15:26:13
LastEditors: Please set LastEditors
'''
# 先把整个字符串进行翻转 再对单词逐个翻转 p285
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s[::-1]
        strList = s.split()

        for i in range(len(strList)):
            strList[i] = strList[i][::-1]

        reversedResult = " ".join(strList)
        return reversedResult
        
# 直接将每个单词逆置
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        strList = s.split()
        reversedList = strList[::-1]
        reversedResult = " ".join(reversedList)
        return reversedResult

s = "  hello world!  "
s1 = Solution()
ans = s1.reverseWords(s)
print(ans)