'''
Description: 
Author: Tjg
Date: 2021-10-06 19:07:29
LastEditTime: 2021-10-06 19:37:18
LastEditors: Please set LastEditors
'''
# 时间复杂度O(10^n) 空间复杂度O(10^n) p114
# 该解法用C++做会溢出
class Solution:
    def printNumbers(self, n: int) -> list[int]:
        return list(range(1, 10**n))

# 时间复杂度O(10^n) 空间复杂度O(10^n) p116
# 大数问题
# 全排列 回溯
class Solution:
    def printNumbers(self, n: int) -> list[int]:
        def dfs(length):
            if length == n:
                if num != []:
                    res.append("".join(num))
                return
            for i in range(10):
                if num == [] and i == 0:
                    dfs(length + 1)
                    continue
                num.append(str(i))
                dfs(length + 1)
                num.pop()

        res = []
        num = []
        dfs(0)
        return [int(i) for i in res]

s1 = Solution()
ans = s1.printNumbers(3)
print(ans)