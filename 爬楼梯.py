'''
Description: 
Author: Tjg
Date: 2021-07-16 12:39:22
LastEditTime: 2021-07-16 12:46:06
LastEditors: Please set LastEditors
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 0,1
        while n:
            a,b = b, a+b
            n -= 1
            print(a,b)
        return b

s1 = Solution()
answer = s1.climbStairs(2)
print(answer)