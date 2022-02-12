'''
Description: 
Author: Tjg
Date: 2022-02-12 17:05:16
LastEditTime: 2022-02-12 17:46:09
LastEditors: Please set LastEditors
'''
# 动态规划
# dp[i][j]表示以i,j为右下角顶点的最大正方形面积
# 时间复杂度O(nm*(n + m)) 空间复杂度O(nm)
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if matrix is None or matrix == [] or \
            matrix[0] is None or matrix == []:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] != '0':
                    side = int(dp[i - 1][j - 1] ** (1/2))
                    x_length = 1
                    for x in range(i - 1, i - side - 1, -1):
                        if matrix[x][j] == '1':
                            x_length += 1
                        else:
                            break
                    y_length = 1
                    for y in range(j - 1, j - side - 1, -1):
                        if matrix[i][y] == '1':
                            y_length += 1
                        else:
                            break
                    dp[i][j] = min(x_length, y_length) ** 2
                ans = max(ans, dp[i][j])
        # print(dp)
        
        return ans

# 官方 动态规划
# dp[i][j]表示以i,j为右下角顶点的最大正方形的边长
# 时间复杂度O(nm) 空间复杂度O(nm)
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 当前最大正方形的边长取决于左上，左，上的最大正方形边长
                        # 因为边长可以由递推得来，故无需重新计算
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare



matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

s1 = Solution()
ans = s1.maximalSquare(matrix)
print(ans)