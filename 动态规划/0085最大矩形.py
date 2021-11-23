'''
Description: 
Author: Tjg
Date: 2021-11-20 10:20:01
LastEditTime: 2021-11-23 14:09:02
LastEditors: Please set LastEditors
'''
# https://blog.csdn.net/charlie_jilei/article/details/78668843
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0

        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        # print(n, m)
        le = [[0] * m for _ in range(n)]
        ri = [[m - 1] * (m + 1) for _ in range(n)]
        l = [[0] * m for _ in range(n)]
        r = [[m - 1] * m for _ in range(n)]
        h = [[0] * m for _ in range(n)]

        # 左闭
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i - 1][j - 1] == '0':
                    le[i][j] = j
                else:
                    # if j == 1:
                    #     le[i][j] = 0
                    # else:
                    le[i][j] = le[i][j - 1]
        # 右开
        for i in range(1, n):
            for j in range(m - 1, 0, -1):
                if matrix[i - 1][j - 1] == '0':
                    ri[i][j] = j - 1
                else:
                    # if j == m - 1:
                    #     ri[i][j] = m - 1
                    # else:
                    ri[i][j] = ri[i][j + 1]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i - 1][j - 1] == '1':
                    # h[i][j] = 0
                    # l[i][j] = 0
                    # r[i][j] = m - 1
                # else:
                    # if i == 1:
                    #     l[i - 1][j] = 0
                    #     r[i - 1][j] = m - 1
                    h[i][j] = h[i - 1][j] + 1
                    l[i][j] = max(l[i - 1][j], le[i][j])
                    r[i][j] = min(r[i - 1][j], ri[i][j])

        ans = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i - 1][j - 1] == '1':
                    ans = max(ans, h[i][j] * (r[i][j] - l[i][j]))
                    # print(i - 1, j - 1, l[i][j], r[i][j], h[i][j] * (r[i][j] - l[i][j] - 1))

        return ans


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
s1 = Solution()
ans = s1.maximalRectangle(matrix)
print(ans)
