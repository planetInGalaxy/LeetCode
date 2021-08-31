'''
Description: 
Author: Tjg
Date: 2021-08-21 17:45:30
LastEditTime: 2021-08-21 17:47:56
LastEditors: Please set LastEditors
'''
import heapq
class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        heapq.heapify(arr)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(arr))
        
        return ans 