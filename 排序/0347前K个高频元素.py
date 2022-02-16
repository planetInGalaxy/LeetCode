'''
Description: 
给你一个整数数组 nums 和一个整数 k ，
请你返回其中出现频率前 k 高的元素。
你可以按任意顺序返回答案。
Author: Tjg
Date: 2022-02-16 20:02:28
LastEditTime: 2022-02-16 21:43:02
LastEditors: Please set LastEditors
'''
# 计数排序思想
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if nums is None or nums == []:
            return None
        
        n = len(nums)
        map = {}
        sort = [None] * ( n + 1)
        ans = []
        
        for i in nums:
            map[i] = map.get(i, 0) + 1
        
        for key, value in map.items():
            if sort[value] is None:
                sort[value] = []
            sort[value].append(key)

        
        for i in range(n, 0, -1):
            if sort[i] is not None:
                ans.extend(sort[i])
                # print(len(ans))
            if len(ans) == k:
               return ans
        
        