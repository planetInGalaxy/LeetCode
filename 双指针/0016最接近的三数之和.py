'''
Description: 
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在恰好一个解。
Author: Tjg
Date: 2022-02-25 22:40:04
LastEditTime: 2022-02-25 22:56:50
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n2) 空间复杂度O(logn)（排序栈空间）
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        def update(cur):
            nonlocal ans
            if abs(cur - target) < abs(ans - target):
                ans = cur
        
        if nums is None or nums == []:
            return None
        
        nums.sort()
        n = len(nums)
        ans = float("inf")

        for i in range(n - 2):
            # 确保和上次枚举的元素不一样，剪枝
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举第二和第三个数
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于0，移动右指针
                    new_k = k - 1
                    # 移动到下一个不相等的元素，剪枝
                    while j < new_k and nums[new_k] == nums[k]:
                        new_k -= 1
                    k = new_k
                else:
                    # 如果和小于0，移动左指针
                    new_j = j + 1
                    # 移动到下一个不相等的元素，剪枝
                    while new_j < k and nums[new_j] == nums[j]:
                        new_j += 1
                    j = new_j
        
        return ans