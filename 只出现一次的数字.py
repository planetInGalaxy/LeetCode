'''
Description: 
Author: Tjg
Date: 2021-06-29 16:30:01
LastEditTime: 2021-06-30 10:04:05
LastEditors: Please set LastEditors
'''
# 哈希 n n
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        record = dict(zip(nums,[0] * len(nums)))
        for i in nums:
            record[i] += 1
        for i in record.items():
            if i[1] == 1:
                return i[0]

# 异或
from functools import reduce
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
