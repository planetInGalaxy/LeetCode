'''
Description: 
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
Author: Tjg
Date: 2022-03-15 20:42:16
LastEditTime: 2022-03-15 20:52:09
LastEditors: Please set LastEditors
'''
# 进制转换 需要减一
# 时间复杂度O(log26 n)
# 空间复杂度O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            num = columnNumber % 26
            columnNumber //= 26
            ans.append(chr(ord('A') + num))
        ans = "".join(ans[::-1])
        return ans