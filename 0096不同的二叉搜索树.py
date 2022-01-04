'''
Description: 
Author: Tjg
Date: 2021-12-04 23:36:23
LastEditTime: 2021-12-04 23:49:50
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(1)
# 开塔兰数：给定一个栈的入栈序列，出栈序列的种类数
# C[2n, n] / (n + 1)
from functools import reduce
import operator
class Solution:
    def numTrees(self, n: int) -> int:
        def fact(m):
            return reduce(operator.mul, range(1, m + 1))

        res = fact(2 * n) / fact(n) ** 2 / (n + 1)
        return int(res)