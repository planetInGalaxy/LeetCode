'''
Description: 
Author: Tjg
Date: 2022-02-19 21:54:07
LastEditTime: 2022-02-19 23:12:10
LastEditors: Please set LastEditors
'''
# 优先队列
# 存储值之外还存储了下标
# 用以判断是否属于窗口，不是则pop
# 时间复杂度O(nlogk) 空间复杂度O(k)（不考虑答案）
import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if nums is None or nums == [] or 0 < k > len(nums):
            return None

        q = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(q)
        n = len(nums)
        ans = []
        for i in range(k - 1, n):
            heapq.heappush(q, (-nums[i], i))
            # q[0][1]直接取得最值
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans

# 单调队列
# 单调递减的队列
# 可以保证最左边一定是最大的
# 由于需要两边出，并且右边进，用deque
# 时间复杂度O(n) 空间复杂度O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if nums is None or nums == [] or 0 < k > len(nums):
            return None

        q = deque()
        for i in range(k - 1):
            # 用 q 判断是否为空， 用q[-1]取右值
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = []
        n = len(nums)
        for i in range(k - 1, n):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans