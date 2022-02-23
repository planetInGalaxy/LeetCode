'''
Description: 
给你一个整数数组 nums 和两个整数 k 和 t 。
请你判断是否存在 两个不同下标 i 和 j，
使得 abs(nums[i] - nums[j]) <= t ，
同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。
Author: Tjg
Date: 2022-02-19 14:01:01
LastEditTime: 2022-02-23 22:33:38
LastEditors: Please set LastEditors
'''
# 桶排序
# 时间复杂度O(n) 空间复杂度O(min(n, k))
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size

        map = {}
        size = t + 1
        for i, u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为k
            if i >= k:
                map.pop(getIdx(nums[i - k]))

        return False
