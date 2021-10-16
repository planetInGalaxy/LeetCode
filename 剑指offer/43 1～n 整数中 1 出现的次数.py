'''
Description: 
Author: Tjg
Date: 2021-10-15 14:15:50
LastEditTime: 2021-10-15 15:00:09
LastEditors: Please set LastEditors
'''
# 统计每一个数的每一位 超时 p221
# 时间复杂度O(nlogn) 空间复杂度O(1)
class Solution:
    def countDigitOne(self, n: int) -> int:
        def countOf(num):
            count = 0
            while num > 0:
                if num % 10 == 1:
                    count += 1
                # 这里一定要用整数除法！
                num //= 10
            return count

        countSum = 0
        for i in range(1, n + 1):
            countSum += countOf(i)
        return countSum

# 统计第一位 统计整n个数字的其余位 递归统计剩余数字 p223
# 时间复杂度O(logn*logn) 空间复杂度O(1)
class Solution:
    def countDigitOne(self, n: int) -> int:
        numString = str(n) 
        
        if len(numString) == 1:
            if numString == '0':
                return 0
            else:
                return 1

        if int(numString[0]) > 1:
            numFirstDigit = 10 ** (len(numString) - 1)
        else:
            numFirstDigit = n - 10 ** (len(numString) - 1) + 1

        numOtherDigit = int(numString[0]) * (len(numString) - 1) \
                        * 10 ** (len(numString) - 2)

        numRecurisive = self.countDigitOne(int(numString[1:]))

        return numFirstDigit + numOtherDigit + numRecurisive

s1 = Solution()
ans = s1.countDigitOne(12)
print(ans)