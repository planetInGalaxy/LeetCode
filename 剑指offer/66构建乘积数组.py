'''
Description: 
Author: Tjg
Date: 2021-10-18 14:55:08
LastEditTime: 2021-10-18 15:13:11
LastEditors: Please set LastEditors
'''
# 先想象一个矩阵，然后逐行从上往下，再从下往上递乘 p313
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def constructArr(self, a: list[int]) -> list[int]:
        if len(a) < 2:
            return []
        b = [1] * len(a)
        
        product = 1
        for i in range(1, len(b)):
            product *= a[i - 1]
            b[i] *= product

        product = 1
        for i in range(len(b) - 2, -1, -1):
            product *= a[i + 1]
            b[i] *= product
        
        return b

s1 = Solution()
ls = [1,2,3,4,5]
ans = s1.constructArr(ls)
print(ans)
