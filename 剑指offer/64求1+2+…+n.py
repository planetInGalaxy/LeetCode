'''
Description: 
Author: Tjg
Date: 2021-10-18 11:32:24
LastEditTime: 2021-10-18 11:54:05
LastEditors: Please set LastEditors
'''
# 官方题解
# 因为题目特殊，只能先设立一个全局变量
# 在递归中累加变量
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def sumNums(self, n: int) -> int:
        def getSum(n):
            nonlocal sum
            sum += n

            n and getSum(n - 1)
            return

        sum = 0
        getSum(n)
        return sum 


s1 = Solution()
ans = s1.sumNums(3)
print(ans)