'''
Description: 
Author: Tjg
Date: 2021-10-16 11:23:52
LastEditTime: 2021-10-16 11:59:45
LastEditors: Please set LastEditors
'''
# 剑指offer第二种思路 p242
# 只求丑数，而不是对每个数进行丑数判断
# 丑数都是由1乘上不同数量的2 3 5得来的，任何一个丑乘上2 3 5 还是一个丑数
# 所以我们对之前的丑数不断乘2 3 5即可得到所有的丑数
# 时间复杂度O(n） 空间复杂度O(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 0:
            return None
        if n == 1:
            return 1
        
        uglyNumber = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(1, n):
            minNumber = min(uglyNumber[index2] * 2, uglyNumber[index3] * 3, \
                uglyNumber[index5] * 5)
            uglyNumber.append(minNumber)
            if uglyNumber[index2] * 2 == minNumber:
                index2 += 1
            if uglyNumber[index3] * 3 == minNumber:
                index3 += 1
            if uglyNumber[index5] * 5 == minNumber:
                index5 += 1
        #     print(uglyNumber, index2, index3, index5)
        # print(uglyNumber)
        return uglyNumber[-1]

s1 = Solution()
ans = s1.nthUglyNumber(12)
print(ans)