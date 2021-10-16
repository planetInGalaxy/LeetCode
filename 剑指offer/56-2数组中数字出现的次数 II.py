'''
Description: 
Author: Tjg
Date: 2021-10-16 22:00:38
LastEditTime: 2021-10-16 22:26:02
LastEditors: Please set LastEditors
'''
# p278
# 将所有数字的二进制的某一位累加起来
# 如果该位之和能被3整除，则结果的该位为0
# 反之，结果的该位为1
# 最后从右到左，累加起来
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if nums == [] or len(nums) < 3:
            return None

        bitList = [0] * 32
        for i in nums:
            bitMask = 0b01
            for j in range(31, -1, -1):
                bit = i & bitMask
                if bit != 0:
                    bitList[j] += 1
                bitMask <<= 1
        print(bitList)
        print([bin(i) for i in nums])
        
        result = 0
        for i in range(32):
            result <<= 1
            result += bitList[i] % 3
        return result

nums = [9,1,7,9,7,9,7]
s1 = Solution()
ans = s1.singleNumber(nums)
print(ans)