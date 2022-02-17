'''
Description: 
Author: Tjg
Date: 2021-09-07 17:29:13
LastEditTime: 2022-02-17 21:11:33
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
class Bucket: # 自己定义一个桶
    def __init__(self):
        self.empty = True
        self.max = float('-inf')
        self.min = float('inf')

    def put(self, num):
        self.max = max(self.max, num)
        self.min = min(self.min, num)
        self.empty = False

    def isEmpty(self):
        return self.empty
        
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if nums is None or len(nums) < 2:
            return 0

        n = len(nums)
        # 分成 n + 1 个桶 
        buckets = [Bucket() for _ in range(n + 1)]  
        min_value = min(nums)
        max_value = max(nums)
        # 桶涵盖的范围，前闭后开
        diff = max_value - min_value
        if diff == 0:
            return 0
        d = diff / n
        # 放入桶中
        for num in nums:
            buckets[int((num - min_value) / d)].put(num)  

        ans = 0
        start = buckets[0].max
        # 第一个桶和最后一个桶永远都是有数字的
        for i in range(1, len(buckets)):  
            if not buckets[i].isEmpty():
                ans = max(ans, buckets[i].min - start)
                start = buckets[i].max

        return ans

    