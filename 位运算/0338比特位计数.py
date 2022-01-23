'''
Description: 
Author: Tjg
Date: 2022-01-08 22:19:11
LastEditTime: 2022-01-08 22:35:47
LastEditors: Please set LastEditors
'''
# 动态规划 + 位运算
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def countBits(self, n: int) -> list[int]:
        if n < 0:
            return None
        if n == 0:
            return [0]

        bitsCount = [0]
        power = 1
        for i in range(1, n + 1):
            # 可以用这个方法判断是不是2的整数幂
            # if i & i - 1 == 0:
            if i == power:
                bitsCount.append(1)
                power *= 2
            else:
                bitsCount.append(1 + bitsCount[i - power])
        
        return bitsCount

s1 = Solution()
ans = s1.countBits(100)
print(ans)