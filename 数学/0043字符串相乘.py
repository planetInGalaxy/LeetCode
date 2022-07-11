'''
Description: 
给定两个以字符串形式表示的非负整数 num1 和 num2，
返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
Author: Tjg
Date: 2022-07-11 23:20:11
LastEditTime: 2022-07-11 23:38:22
LastEditors: Please set LastEditors
'''
# 使用数组存放乘积的每位数字
# 时间复杂度O(nm)
# 空间复杂度O(n+m)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        n = len(num1)
        m = len(num2)
        ansArr = [0] * (n + m)
        for i in range(n - 1, -1 , -1):
            for j in range(m - 1, -1, -1):
                ansArr[i + j + 1] += int(num1[i]) * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        ansArr = ansArr if ansArr[0] != 0 else ansArr[1:]
        ansStr = "".join(map(str,ansArr))
        return ansStr