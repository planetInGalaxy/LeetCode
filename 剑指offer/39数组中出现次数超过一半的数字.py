'''
Description: 
Author: Tjg
Date: 2021-10-14 20:21:17
LastEditTime: 2021-10-14 21:24:50
LastEditors: Please set LastEditors
'''

# 快排原理 需要改动原数组 超时 p206
# 时间复杂度 最好O(n) 最坏O(n^2) 空间复杂度O(1)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def partition(l,r):
            i = l
            j = r
            key = nums[l]
            while i < j:
                while i < j and nums[j] > key:
                    j -= 1
                while i < j and nums[i] <= key:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j

        if nums == []:
            return None

        mid = len(nums) >> 1
        start = 0
        end = len(nums) - 1

        index = partition(start, end)
        while index != mid:
            # print(start,index, mid, nums)
            if index > mid:
                end = index - 1
            else:
                start = index + 1
            index = partition(start, end)

        result = nums[mid]
        return result

# 不需改动数组 p207
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if nums == []:
            return None
        
        times = 0
        result = -1
        for i in nums:
            if times == 0:
                times = 1
                result = i
            elif result == i:
                times += 1
            else:
                times -= 1
        return result
        
s1 = Solution()
ls = [2,2,1,1,1,2,2]
ans = s1.majorityElement(ls)
print(ans)