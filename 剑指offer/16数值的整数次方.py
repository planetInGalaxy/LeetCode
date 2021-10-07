'''
Description: 
Author: Tjg
Date: 2021-10-06 17:18:44
LastEditTime: 2021-10-06 18:47:25
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n） 空间复杂度O(1) p 111
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n == 0:
            return 0.0

        result = 1.0
        sign = True if n >= 0 else False
        abs_value = abs(n)

        for i in range(abs_value):
            result *= x
        
        if not sign:
            result = 1 / result
        
        return result

# 时间复杂度O(logn) 空间复杂度O(logn) p 113
# 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powerRecursion(base, exp):
            if exp == 0:
                return 1
            if exp == 1:
                return base
            result = powerRecursion(base, exp >> 1)
            result *= result
            if exp & 0b1 == 1:
                result *= base
            return result

        if x == 0 and n == 0:
            return 0.0

        sign = True if n >= 0 else False
        abs_value = abs(n)

        result = powerRecursion(x, abs_value)
        
        if not sign:
            result = 1 / result
        
        return result        

s1 = Solution()
ans = s1.myPow(0.00001, 2147483647)
print(ans)