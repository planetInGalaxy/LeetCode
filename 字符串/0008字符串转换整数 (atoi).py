'''
Description: 
Author: Tjg
Date: 2021-10-19 17:51:49
LastEditTime: 2021-10-19 18:17:57
LastEditors: Please set LastEditors
'''
# 同剑指offer67
class Solution:
    def myAtoi(self, s: str) -> int:
        # 检查是是否是空指针或者是空字符串
        if s is None or s == "":
            return 0
        
        # 去除空格，并再次检查字符串是否为空
        s = s.strip()
        if s == "":
            return 0
        
        # 检查第一个字符是否合法
        first = s[0]
        if first not in '+-0123456789' or first in '+-' and len(s) == 1:
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
        for i in range(start, len(s)):
            if s[i] in '0123456789':
                end += 1
            else:
                break

        # 如果没有合法的数字就return 0 否则判断number是否在int范围内
        if end == start:
            return 0
        else:
            number = sign * int(s[start:end])
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
