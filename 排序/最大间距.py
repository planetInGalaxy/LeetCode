'''
Description: 
Author: Tjg
Date: 2021-09-07 17:29:13
LastEditTime: 2022-01-01 20:34:30
LastEditors: Please set LastEditors
'''
# 计数排序 超时
# 时间复杂度O(max(n, maxVal - minVal)) 空间复杂度O(maxVal - minVal)
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        array = [0] * (max_num - min_num + 1)
        for i in nums:
            array[i - min_num] += 1
        ans = 0
        temp = 0
        for i in range(1,len(array)):
            if array[i] == 0:
                temp += 1
            else:
                ans = max(ans,temp + 1)
                temp = 0
        return ans

# 桶排序
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        minVal = min(nums)
        maxVal = max(nums)
        d = max(1, (maxVal - minVal) // (n - 1))
        bucketSize = (maxVal - minVal) // d + 1
        
        buckets = [[-1,-1] for _ in range(bucketSize)]
        for num in nums:
            idx = (num - minVal) // d 
            if buckets[idx][0] == -1:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        result = 0
        prev = -1
        for i in range(bucketSize):
            if buckets[i][0] != -1:
                if prev != -1:
                    result = max(result, buckets[i][0] - buckets[prev][1])
                prev = i
        
        return result