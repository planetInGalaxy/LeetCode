'''
Description: 
给定一个包含 n + 1 个整数的数组 nums ，
其数字都在 [1, n] 范围内包括 1 和 n，
可知至少存在一个重复的整数。
假设 nums 只有一个重复的整数 ，返回这个重复的数 。
你设计的解决方案必须不修改数组 nums且只用常量级 O(1) 的额外空间。
Author: Tjg
Date: 2022-02-22 20:12:02
LastEditTime: 2022-02-22 20:15:31
LastEditors: Please set LastEditors
'''
# 修改 O(n) O(1)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return None
        n = len(nums) - 1
        for i in range(n + 1):
            if nums[nums[i] % (n + 1)] < n + 1:
                nums[nums[i] % (n + 1)] += n + 1
            else:
                return nums[i] % (n + 1)


# 双指针 Floyd判圈算法
# 不修改 O(n) O(1)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return None
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow