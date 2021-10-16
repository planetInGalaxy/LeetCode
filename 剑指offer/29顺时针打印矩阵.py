'''
Description: 
Author: Tjg
Date: 2021-10-08 14:28:11
LastEditTime: 2021-10-08 14:52:19
LastEditors: Please set LastEditors
'''
# 时间复杂度O(mn) 空间复杂度O(mn)
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        def printLine(start):
            endX = rows - 1 - start
            endY = cols - 1 - start

            for i in range(start, endY + 1):
                ans.append(matrix[start][i])
            
            for i in range(start + 1, endX + 1):
                ans.append(matrix[i][endY])

            if start < endX:
                for i in range(endY - 1, start - 1, -1):
                    ans.append(matrix[endX][i])
            if start < endY:
                for i in range(endX - 1, start, -1):
                    ans.append(matrix[i][start])

        if matrix == [] or matrix == [[]]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        ans = []

        while 2 * start < rows and 2 * start < cols:
            printLine(start)
            start += 1
        
        return ans

# ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# s1 = Solution()
# ans= s1.spiralOrder(ls)
# print(ans)