'''
Description: 
Author: Tjg
Date: 2021-10-21 10:03:10
LastEditTime: 2021-10-21 10:45:03
LastEditors: Please set LastEditors
'''
# 思想同剑指offer29
# 由外向内逐层转移矩阵
# 一共 n // 2层需要旋转
# 每层要旋转 n - 2*i -1 组数据
# 一组数据有上下左右四种情况
# 时间复杂度O(n^2) 空间复杂度O(1)
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == [] or matrix == [[]]:
            return []

        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
        
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s1 = Solution()
ans = s1.rotate(matrix)
print(ans)
        
