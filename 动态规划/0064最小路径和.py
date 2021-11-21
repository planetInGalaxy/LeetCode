'''
Description: 
Author: Tjg
Date: 2021-11-16 14:45:49
LastEditTime: 2021-11-16 14:58:29
LastEditors: Please set LastEditors
'''
# 解决List报错问题
# typing常用类型：
# int,long,float: 整型,长整形,浮点型;
# bool,str: 布尔型，字符串类型；
# List, Tuple, Dict, Set:列表，元组，字典, 集合;
# Iterable,Iterator:可迭代类型，迭代器类型；
# Generator：生成器类型；
from typing import List

# dp
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i != 0:
                    dp[i][j] = dp[i - 1][0] + grid[i][0]
                elif j != 0:
                    dp[i][j] = dp[0][j - 1] + grid[0][j]


        return dp[m - 1][n - 1]