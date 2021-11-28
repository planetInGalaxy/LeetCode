'''
Description: 
Author: Tjg
Date: 2021-11-23 19:39:04
LastEditTime: 2021-11-24 09:39:18
LastEditors: Please set LastEditors
'''
# 单调栈 数据复杂度O(nm) 空间复杂度O(nm)
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        stick = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    stick[i][j] = stick[i][j - 1] + 1 if j > 0 else 1
                else:
                    stick[i][j] = 0

        maxAns = 0
        # 对每一列进行求解
        for j in range(m):        
            right = [n] * n
            left = [-1] * n

            monoStack = []
            for i in range(n):
                while monoStack and stick[i][j] < stick[monoStack[-1]][j]:
                    peek = monoStack.pop()
                    right[peek] = i
                monoStack.append(i)

            monoStack.clear()
            for i in range(n - 1, -1, -1):
                while monoStack and stick[i][j] < stick[monoStack[-1]][j]:
                    peek = monoStack.pop()
                    left[peek] = i
                monoStack.append(i)

            ans = max((right[i] - left[i] - 1) * stick[i][j] for i in range(n))
            maxAns = max(maxAns, ans)
        return maxAns


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

s1 = Solution()
ans = s1.maximalRectangle(matrix)
print(ans)
