'''
Description: 
给定一个大小为 n 的整数数组，
找出其中所有出现超过 ⌊n/3⌋ 次的元素。
Author: Tjg
Date: 2022-02-03 19:43:11
LastEditTime: 2022-02-08 23:21:14
LastEditors: Please set LastEditors
'''

# 官方 摩尔投票
# 核心思路是对拼消耗
# 每三个不同的数可以抵消
# 从而找到出现次数最多的两个数
# 最后再遍历一遍，检验出现次数是否达到n/3
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            # 如果该元素为第一个元素，则计数加1
            if vote1 > 0 and num == element1:
                vote1 += 1
            # 如果该元素为第二个元素，则计数加1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            # 选择第一个元素
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            # 选择第二个元素
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # 如果三个元素均不相同，则相互抵消1次
            else:
                vote1 -= 1
                vote2 -= 1

        cnt = 0
        if vote1 > 0:
            for num in nums:
                if num == element1:
                    cnt += 1
            if cnt > len(nums) // 3:
                ans.append(element1)

        cnt = 0
        if vote2 > 0:
            for num in nums:
                if num == element2:
                    cnt += 1
            if cnt > len(nums) // 3:
                ans.append(element2)
        
        return ans
