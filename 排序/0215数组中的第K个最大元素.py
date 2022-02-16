'''
Description: 
Author: Tjg
Date: 2022-01-01 22:38:55
LastEditTime: 2022-02-16 20:50:57
LastEditors: Please set LastEditors
'''
# 快排思想
# 时间复杂度 平均 O(n) 最坏O(n2)
# 最好情况下，有 f(N) = O(N) + f(N/2)，
# 根据主定理，能够得到 f(N) = O(N)f(N) = O(N)。
# 空间复杂度 平均O(logn) 最坏O(n)
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
            # i == j
            # 此时 nums[i] >= key
            # l和i交换
            # 交换后，nums[l] >= key, nums[i] = key
            # nums[l...i-1] >= key 
            # nums[i] = key 
            # nums[i+1...r] < key
            nums[l], nums[i] = nums[i], nums[l]

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

# 堆排思想
# 时间复杂度O(nlogk)
# 空间复杂度O(k)
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

# 内置的nlargest函数，返回前n个最大的数
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k,nums)[k - 1]

s1 = Solution()
ans = s1.findKthLargest(nums, k)
print(ans)
