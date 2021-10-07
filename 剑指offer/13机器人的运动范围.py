'''
Description: 
Author: Tjg
Date: 2021-10-06 15:37:02
LastEditTime: 2021-10-06 16:13:24
LastEditors: Please set LastEditors
'''
# 时间复杂度O（mxn）空间复杂度O（mxn） p93
# 回溯法
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def getDigitSum(num):
            # sum2不行
            # sum2 = sum([int(i) for i in str(num).split()])
            sum1 = 0
            while num > 0:
                sum1 += num % 10
                num //= 10
            return sum1

        def check(row, col):
            isValid = row >= 0 and row < m and \
                col >= 0 and col < n and \
                visited[row][col] is False and \
                getDigitSum(row) + getDigitSum(col) <= k
            return isValid
                
        def search(row, col):
            if check(row,col):
                visited[row][col] = True
                nonlocal count
                count += 1
                search(row + 1, col)
                search(row - 1, col)
                search(row, col + 1)
                search(row, col - 1)
            else:
                return
            
        count = 0
        visited = [[False] * n for _ in range(m)]
        search(0, 0)
        return count

s1 = Solution()
ans = s1.movingCount(11, 8, 16)
print(ans)