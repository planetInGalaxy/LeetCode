'''
Description: 
已知一个函数rand7()能够生成1-7的随机数，
每个数概率相等，请给出一个函数rand10()，
该函数能够生成 1-10 的随机数，每个数概率相等。
Author: Tjg
Date: 2022-02-13 20:39:43
LastEditTime: 2022-02-13 22:13:42
LastEditors: Please set LastEditors
'''
import random
import functools
rand7 = functools.partial(random.randint, 1, 7)

# 拒绝采样
# 时间复杂度平均O(1) 最坏无穷
# 调用Rand7()的期望次数约为2.5次
# 空间复杂度O(1)
class Solution:
    def rand10(self):

        while True:
            # 1234567
            # ...
            # .....(49)
            # 行下标为0 ~ n-1,列下标为1 ~ n
            # 行下标乘 n 后加列下标
            # n * (f(n) - 1) + f(n)
            row = rand7()
            col = rand7()
            num = 7 * (row - 1) + col
            if num <= 40:
                return 1 + (num - 1) % 10

# 官方 拒绝采样进阶
# 时间复杂度平均O(1) 最坏无穷
# 调用Rand7()的期望次数约为2.2
# 空间复杂度O(1)
class Solution:
    def rand10(self) -> int:
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b
            if idx <= 40:
                return 1 + (idx - 1) % 10
            a = idx - 40
            b = rand7()
            # get uniform dist from 1 - 63
            idx = (a - 1) * 7 + b
            if idx <= 60:
                return 1 + (idx - 1) % 10
            a = idx - 60
            b = rand7()
            # get uniform dist from 1 - 21
            idx = (a - 1) * 7 + b
            if idx <= 20:
                return 1 + (idx - 1) % 10
