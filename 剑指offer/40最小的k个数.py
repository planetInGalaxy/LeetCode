'''
Description: 
Author: Tjg
Date: 2021-08-21 17:45:30
LastEditTime: 2021-10-14 21:45:31
LastEditors: Please set LastEditors
'''
# 堆
# 时间复杂度O(n+klogn) 空间复杂度O(1)
import heapq
class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        heapq.heapify(arr)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(arr))
        return ans 

# 快排原理 p210
# 时间复杂度 最好O(n) 最坏O(n^2) 空间复杂度O(1)
class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        def partition(l,r):
            i = l
            j = r
            key = arr[l]
            while i < j:
                while i < j and arr[j] > key:
                    j -= 1
                while i < j and arr[i] <= key:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            return j

        if arr == []:
            return None
        
        start = 0
        end = len(arr) - 1
        index = partition(start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
            else:
                start = index + 1
            index = partition(start, end)
        
        ans = arr[:k]
        return ans

s1 = Solution()
ls = [6,1,2,5,4,3]
ans = s1.getLeastNumbers(ls, 3)
print(ans)

