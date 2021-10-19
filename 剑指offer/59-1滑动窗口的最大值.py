'''
Description: 
Author: Tjg
Date: 2021-10-17 16:16:25
LastEditTime: 2021-10-17 17:20:52
LastEditors: Please set LastEditors
'''
# 官方题解
# 使用一个大根堆保存数值及其下标
# 遍历数组将其加入队列中，并且检验最大值的下标
# 弹出下标不在窗口范围内的最大值
# 获得有效的最大值作为答案
# 时间复杂度O(nlogn) 空间复杂度O(n)
import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if nums == [] or len(nums) < k:
            return []

        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(q)

        ans = []
        for i in range(k - 1, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            # 由于我们已经记录了下标，当队列中的下标距离现在下标超过k - 1则无效并弹出
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans

# 剑指offer p291 
# 双端队列 既能移除最左边的最大值 也能移除右边的较小值
# 将当前值从后插入队列中，同时移除比它小的所有值
# 在获取最大值的过程中，先判断最大值所在位置是否在有效区间内
# 如果超过区间则，从左端删除它
# 如果没有，就是该窗口区间要找的最大值
# 时间复杂度O(n) 空间复杂度O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if nums == [] or len(nums) < k:
            return []

        indexDeque = deque()
        for i in range(k - 1):
            while len(indexDeque) != 0 and nums[i] >= nums[indexDeque[-1]]:
               indexDeque.pop()
            indexDeque.append(i)

        ans = []
        for i in range(k - 1, len(nums)):
            print([nums[i] for i in indexDeque], indexDeque)
            while len(indexDeque) != 0 and nums[i] >= nums[indexDeque[-1]]:
               indexDeque.pop()

            # 后值一定比前值的下标大，所以一定在区间内，不用判断
            #  这里用 == i - k，因为不会遇到更旧的值，旧值已经被移除了(左&右)
            if len(indexDeque) != 0 and indexDeque[0] == i - k:
                indexDeque.popleft()
            indexDeque.append(i)

            ans.append(nums[indexDeque[0]])

        return ans

nums = [1,3,-1,-3,-5,3,6,7]
s1 = Solution()
ans = s1.maxSlidingWindow(nums, 3)
print(ans)