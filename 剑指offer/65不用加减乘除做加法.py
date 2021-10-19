'''
Description: 
Author: Tjg
Date: 2021-10-18 11:57:11
LastEditTime: 2021-10-18 14:44:57
LastEditors: Please set LastEditors
'''
# 剑指offer p311
# 整体
# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
# 时间复杂度O(1) 空间复杂度O(1)
class Solution:
    def add(self, a: int, b: int) -> int:
        # 0b11111111111111111111111111111111 -1 用于截取后32位数
        # 0b01111111111111111111111111111111 最大32位正数 用于判断是否是32位正数
        x = 0xffffffff
        y = 0x7fffffff
        print(bin(x), bin(-1), bin(y))
        sum = 0
        carry = 0
        # python中整数不止32位，需要截取后32位数,针对负数的情况
        a &= x
        b &= x
        print(bin(a), bin(b))
        while b != 0:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum
            # 这里进位可能超过32位，需要处理
            b = carry & x
            print(bin(a), bin(b))
        print(bin(~(a ^ x)))
        # python中负数的表示方式不一样
        # 需要把32位数还原为python的存储格式
        # 将 32 位以上的位取反，1 至 32 位不变
        return a if a <= y else ~(a ^ x)

s1 = Solution()
ans = s1.add(1,-2)
print(ans)

# test
# for i in range(100):
#     for j in range(100, 300, 3):
#         if i + j != s1.add(i, j):
#             print("wrong")
# print('right')
