'''
Description: 
Author: Tjg
Date: 2021-07-20 14:58:49
LastEditTime: 2021-07-20 15:50:12
LastEditors: Please set LastEditors
'''
# 分治 3/4
from abc import ABCMeta


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def search(x1,y1,x2,y2):
            if x1 == x2 and y1 == y2:
                return matrix[x1][y1] == target
            if x1 > x2 or y1 > y2 or target < matrix[x1][y1] or target > matrix[x2][y2]:
                return False

            mid_x = x1 + (x2 - x1) // 2
            mid_y = y1 + (y2 - y1) // 2

            if target == matrix[mid_x][mid_y]:
                return True
            elif target > matrix[mid_x][mid_y]:
                return search(mid_x + 1, mid_y + 1, x2, y2) \
                    or search(x1, mid_y + 1, mid_x, y2) \
                    or search(mid_x + 1, y1, x2, mid_y)
            else:
                return search(x1, y1, mid_x - 1, mid_y - 1) \
                    or search(x1, mid_y, mid_x - 1, y2) \
                    or search(mid_x, y1, x2, mid_y - 1)

        row = len(matrix)
        col = len(matrix[0])
        return search(0,0,row - 1,col - 1)

# 分治 2/4
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            # 判断矩阵左下角和右下角和target的值，如果 不在范围内，则剪枝
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left)//2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)

# 左下角指针迭代
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False

s1 = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 15

answer = s1.searchMatrix(matrix, target)
print(answer)