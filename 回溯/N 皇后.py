'''
Description:
Author: Tjg
Date: 2021-02-01 09:11:04
LastEditTime: 2021-02-01 10:20:47
LastEditors: Please set LastEditors
'''

# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         def check(temp_test):
#             for i in range(n):
#                 for j in range(i + 1, n):
#                     if abs(j - i) == abs(int(temp_test[j]) - int(temp_test[i])):
#                         return False
#             return True

#         def trackback(temp_test, m):
#             if m == 0:
#                 if check(temp_test):
#                     result.append(temp_test)
#                 return
#             for i in range(n):
#                 if str(i) not in temp_test:  # 剪枝
#                     trackback(temp_test + str(i), m - 1)
#             return

#         result=[]
#         trackback("", n)
#         finalResult=[]
#         for i in range(len(result)):
#             finalResult.append([])
#             for j in result[i]:
#                 temp='.' * n
#                 temp=list(temp)
#                 temp[int(j)]='Q'
#                 temp="".join(temp)
#                 finalResult[i].append(temp)
#         return finalResult

# s=Solution()
# print(s.solveNQueens(4))


class Solution:
    def solveNQueens(self, n: int):
        def generateBoard():
            board = list()
            temp = ['.'] * n
            for i in range(n):
                temp[queens[i]] = "Q"
                board.append("".join(temp))
                temp[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrack(0)
        return solutions

s=Solution()

print(s.solveNQueens(4))
