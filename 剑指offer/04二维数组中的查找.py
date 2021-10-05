'''
Description: 
Author: Tjg
Date: 2021-10-05 21:01:29
LastEditTime: 2021-10-05 21:18:28
LastEditors: Please set LastEditors
'''
# 时间复杂度O（m+n）空间复杂度O（1） p47
# 主站240题
class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        # 注意要减 1
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        row = 0
        col = cols
        while row <= rows and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False    