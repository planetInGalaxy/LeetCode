'''
Description: 
Author: Tjg
Date: 2021-10-16 21:28:05
LastEditTime: 2021-10-16 21:59:51
LastEditors: Please set LastEditors
'''
# p277
# 先全部异或得到一个二者异或的值
# 由于二值不想同，异或值一定不为0
# 找到右起第一个1的index，用来把数组划分为两类
# 遍历数组，如果index位为1，与其中一个num进行异或，否则与另外一个num异或
# 最终得到两个num，即为结果
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def singleNumbers(self, nums: list[int]) -> list[int]:
        if nums == [] or len(nums) < 2:
            return None
        
        xorValue = 0
        for i in nums:
            xorValue ^= i

        index = 0
        while xorValue & 0b01 == 0:
            xorValue >>= 1
            index += 1

        num1 = 0
        num2 = 0
        for i in nums:
            # == 0 或 1 << index 而不是 == 1
            if i & (1 << index) == 0:
                num1 ^= i
            else:
                num2 ^= i
        return [num1, num2]


ls = [1,2,5,2]
s1 = Solution()
ans = s1.singleNumbers(ls)
print(ans)