'''
Description: 
Author: Tjg
Date: 2022-01-01 22:38:55
LastEditTime: 2022-01-01 23:23:37
LastEditors: Please set LastEditors
'''
# 快排思想
# 时间复杂度O(n) 空间复杂度O(logn)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(l, r):
            i = l
            j = r
            key = nums[i]
            while i < j:
                while i < j and nums[j] < key:
                    j -= 1
                while i < j and nums[i] >= key:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            # print(i)
            # print(nums)
            return i

        def find(l, r):
            _k = partition(l, r)
            if _k < k:
                l = _k + 1
            elif _k > k:
                r = _k - 1
            elif _k == k:
                return nums[k]
            return find(l, r)

        k -= 1
        return find(0, len(nums) - 1)

nums = [3,2,1,5,6,4] 
k = 2

s1 = Solution()
ans = s1.findKthLargest(nums, k)
print(ans)

# 堆排思想
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # return heapq.nlargest(k,nums)[k - 1]
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            popNum = heapq.heappushpop(heap, num)
            # print(popNum)

        # return heapq.heappop(heap)
        return heap[0]

nums = [3,2,1,5,6,4] 
k = 2

s1 = Solution()
ans = s1.findKthLargest(nums, k)
print(ans)
