'''
Description: 
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。
返回该列名称对应的列序号 。
Author: Tjg
Date: 2022-03-15 20:37:51
LastEditTime: 2022-03-15 20:56:18
LastEditors: Please set LastEditors
'''
# 进制转换
# 时间复杂度O(len)
# 空间复杂度O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = 26 * ans + (ord(ch) - ord('A') + 1)
        return ans