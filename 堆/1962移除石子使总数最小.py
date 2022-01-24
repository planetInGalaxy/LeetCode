'''
Description: 
给你一个整数数组 piles ，数组 下标从 0 开始 ，
其中 piles[i] 表示第 i 堆石子中的石子数量。另给你一个整数 k ，
请你执行下述操作 恰好 k 次：
选出任一石子堆 piles[i] ，并从中 移除 floor(piles[i] / 2) 颗石子。
Author: Tjg
Date: 2022-01-24 21:49:52
LastEditTime: 2022-01-24 22:01:57
LastEditors: Please set LastEditors
'''
# 大根堆
# 时间复杂度O(klogn) 空间复杂度O(1)
import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        if piles is None or piles == []:
            return None

        piles = [-i for i in piles]
        heapq.heapify(piles)
        for i in range(k):
            num = heapq.heappop(piles)
            # python中总是向左取整，而不是向0方向取整
            heapq.heappush(piles, num // 2)
        return -sum(piles)