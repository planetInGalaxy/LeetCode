'''
Description: 
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
Author: Tjg
Date: 2022-07-11 21:58:41
LastEditTime: 2022-07-11 22:17:02
LastEditors: Please set LastEditors
'''
# 使用map存储，一次遍历
# 时间复杂度O(n^2)
# 空间复杂度O(n^2)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def getIndex(i, j):
            m = i // 3
            n = j // 3
            martixIndex = m * 3 + n
            return martixIndex

        if board is None:
            return None
        
        # 因为set是可变类型，所以需要用列表生成式而不是*
        cols = [set() for _ in range(9)]
        matrix = [set() for _ in range(9)]
        # print(id(cols[0]), id(cols[1]))
        for i in range(9):
            row = set()
            for j in range(9):
                martixIndex = getIndex(i, j)
                if board[i][j] == '.':
                    continue
                if board[i][j] in row \
                    or board[i][j] in cols[j] \
                    or board[i][j] in matrix[martixIndex]:
                    print(i, j)
                    return False
                else:
                    row.add(board[i][j])
                    cols[j].add(board[i][j])
                    matrix[martixIndex].add(board[i][j])
        else:
            return True