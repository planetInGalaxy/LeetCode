'''
Description: 
Author: Tjg
Date: 2021-12-22 10:11:14
LastEditTime: 2021-12-22 10:22:51
LastEditors: Please set LastEditors
'''
# 回溯
# 时间复杂度O(n) 空间复杂度O(n)
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '0'
                    dfs(x - 1, y)
                    dfs(x + 1, y)
                    dfs(x, y - 1)
                    dfs(x, y + 1) 
    
        m = len(grid)
        n = len(grid[0])
        sum = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    sum += 1
        return sum

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s1 = Solution()
ans = s1.numIslands(grid)
print(ans)