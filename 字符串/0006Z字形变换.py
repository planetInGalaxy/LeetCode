'''
Description: 
Author: Tjg
Date: 2021-10-19 18:37:52
LastEditTime: 2021-10-19 18:56:35
LastEditors: Please set LastEditors
'''
# 把每行的字符串看做是一个字符串，最后输出的时候把字符串拼接起来
# 通过取余得到每行的字符串
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if str == "":
            return ""
        if numRows == 1:
            return s
        
        strList = [[] for i in range(numRows)]
        period = 2 * (numRows - 1)
        for i in range(len(s)):
            remainder = i % period
            if remainder < numRows:
                strList[remainder].append(s[i])
            else:
                strList[period - remainder].append(s[i])

        strResult = []
        for i in strList:
            strResult.extend(i)
        # print(strResult)

        string = "".join(strResult)
        return string


s = "PAYPALISHIRING"
s1 = Solution()
ans = s1.convert(s, 3)
print(ans)