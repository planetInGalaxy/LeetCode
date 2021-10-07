'''
Description: 
Author: Tjg
Date: 2021-10-06 11:35:29
LastEditTime: 2021-10-06 12:10:39
LastEditors: Please set LastEditors
'''
# 时间复杂度O（mxn） 空间复杂度O（mxn） p90
# 回溯法
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def search(row, col, length):
            if row >= 0 and row < rows and \
                col >= 0 and col < cols and \
                visited[row][col] == False and \
                board[row][col] == word[length]:
                length += 1
                visited[row][col] = True
                # print(visited,length,length_Max)
                if length == length_Max:
                    return True
                else:
                    hasPath =  search(row + 1, col, length) or \
                        search(row - 1, col, length) or \
                        search(row, col + 1, length) or \
                        search(row, col - 1, length)
                    if hasPath:
                        return True
                    else:
                        length -= 1
                        visited[row][col] = False
                        return False
            else:
                return False
        

        if board is None or len(board) * len(board[0]) < len(word):
            return False

        rows = len(board)
        cols = len(board[0])
        length_Max = len(word)
        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and search(row, col, 0):
                        return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
s1 = Solution()
ans = s1.exist(board, word)
print(ans)