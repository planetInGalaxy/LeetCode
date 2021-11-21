'''
Description: 
Author: Tjg
Date: 2021-11-20 10:20:01
LastEditTime: 2021-11-20 12:52:39
LastEditors: Please set LastEditors
'''
# 未解决
class Solution:
    class block:
        def __init__(self) -> None:
            self.left = -1
            self.top = -1
            self.otherBlock = set()
            
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        maxArea = 0
        # Python创建二维数组
        dp = [[set() for j in range(n)] for i in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i != 0 and matrix[i - 1][j] == '1':
                        for k in dp[i - 1][j]:
                            if k[1] == j:
                                dp[i][j].add(k)
                    if j != 0 and matrix[i][j - 1] == '1':
                        for k in dp[i][j - 1]:
                            if k[0] == i:
                                dp[i][j].add(k)
                    
                    if i != 0 and j != 0:
                        common = dp[i - 1][j].union(dp[i][j - 1])
                    elif i != 0:
                        common = dp[i - 1][j]
                    elif j != 0:
                        common = dp[i][j - 1]
                    else:
                        common = set()
                    
                    dp[i][j].union(common)
                        
                    
                    if len(dp[i][j]) == 0:
                        dp[i][j].add((i, j)) 
                print(i,j,id(dp[i][j]),dp[i][j])
                # print(dp)
            

                    # area1 = (i -dp[i][j][0][0] + 1) * (j - dp[i][j][0][1] + 1)
                    # area2 = (i -dp[i][j][1][0] + 1) * (j - dp[i][j][1][1] + 1)
                    # maxArea = max(maxArea, area1, area2)
        
        return maxArea

                    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s1 = Solution()
ans = s1.maximalRectangle(matrix)
print(ans)