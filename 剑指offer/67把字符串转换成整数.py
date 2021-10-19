'''
Description: 
Author: Tjg
Date: 2021-10-18 15:24:53
LastEditTime: 2021-10-18 16:03:30
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def strToInt(self, str: str) -> int:
        # 检查是是否是空指针或者是空字符串
        if str is None or str == "":
            return 0
        
        # 去除空格，并再次检查字符串是否为空
        str = str.strip()
        if str == "":
            return 0
        
        # 检查第一个字符是否合法
        first = str[0]
        if first not in '+-0123456789' or first in '+-' and len(str) == 1:
            return 0

        # 找到第一个合法的数字
        sign = 1
        start = 0
        if first == '+':
            start = 1
        elif first == '-':
            sign = -1
            start = 1
        
        # 找到最后一个合法的数字
        end = start
        for i in range(start, len(str)):
            if str[i] in '0123456789':
                end += 1
            else:
                break

        # 如果没有合法的数字就return 0 否则判断number是否在int范围内
        if end == start:
            return 0
        else:
            number = sign * int(str[start:end])
            # 2^31 - 1
            if number > 0x7fffffff:
                return 0x7fffffff
            # python中的0x80000000是正数,如果想转为32位的负数
            # 32开外的位上的0需要取反为1
            # -2^31
            elif number < ~(0x80000000 ^ 0xffffffff):
                return ~(0x80000000 ^ 0xffffffff)
            else:
                return number

s = "-12a3"
s1 = Solution()
ans = s1.strToInt(s)
print(ans)