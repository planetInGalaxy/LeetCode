'''
Description: 
Author: Tjg
Date: 2021-11-16 14:59:12
LastEditTime: 2021-11-16 15:47:08
LastEditors: Please set LastEditors
'''
# 回溯
# 使用一个visited数组，记录目前有无被访问到
# 搜索的时候置为True，回溯的时候置回为False
# 判断当前的x，y有无溢出，溢出直接返回False
# 搜索成功的条件是i达到word字符串的长度（说明之前i-1个字符都是True）

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if 0 <= x < m and 0 <= y < n:
                if visited[x][y] is True:
                    return False                    

                if board[x][y] == word[i]:
                    visited[x][y] = True
                    isExisted = dfs(x - 1, y, i + 1) or dfs(x + 1, y, i + 1) or \
                        dfs(x, y - 1, i + 1) or dfs(x, y + 1, i + 1) 
                    visited[x][y] = False
                    return isExisted
                else:
                    return False
            else:
                return False

        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    isExisted = dfs(i, j, 0)
                    if isExisted:
                        return True
        
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCFS"

s1 = Solution()
ans = s1.exist(board, word)
print(ans)