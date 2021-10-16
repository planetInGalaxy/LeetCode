'''
Description: 
Author: Tjg
Date: 2021-10-15 15:18:40
LastEditTime: 2021-10-15 16:29:20
LastEditors: Please set LastEditors
'''
# 字符串表示完整的数字 超时
# 时间复杂度O(n) 空间复杂度O(nlogn)
class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = []
        for i in range(n + 1):
            nums.append(str(i))
        numString = "".join(nums)
        return int(numString[n])

# 迭代计算1位2位...n位数字占的索引，最后在相应区间内计算出result p225
# 时间复杂度O(logn) 空间复杂度O(1)
class Solution:
    def findNthDigit(self, n: int) -> int:
        def countOfIntergers(digits):
            if digits == 1:
                return 10
            else:
                return 9 * 10 ** (digits - 1)

        def getNumber(index, digits):
            if digits == 1:
                number = index // digits
            else:
                number = 10 ** (digits - 1) + index // digits
            numString = str(number)
            return int(numString[index % digits])
            
        if n < 0:
            return None
        digits = 1

        while True:
            count = countOfIntergers(digits)
            if n < count * digits:
                return getNumber(n, digits)
            n -= count * digits
            digits += 1

s1 = Solution()
ans = s1.findNthDigit(3)
print(ans)