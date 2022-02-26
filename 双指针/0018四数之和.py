'''
Description: 
给你一个由 n 个整数组成的数组 nums ，
和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 :
(若两个四元组元素一一对应，则认为两个四元组重复)
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
Date: 2022-02-26 21:55:23
LastEditTime: 2022-02-26 22:45:16
LastEditors: Please set LastEditors
'''
# 双指针
# 时间复杂度O(n3) 空间复杂度O(logn)
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None or len(nums) < 4:
            return []
        
        nums.sort()
        # print(nums)
        # 利用哈希去重
        ans = set()
        n = len(nums)
        for i in range(n - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n- 2):
                # 一共四处，都可以剪枝，但对于非同一变量
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        # 找到一组答案之后还要继续寻找
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                    else:
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    # print(i,j,k,l)
        # 花费时间 < O(4*C(n,4))
        return [list(i) for i in ans]
                
nums = [i for i in range(-10, 11)]
target = 0
s1 = Solution()
ans = s1.fourSum(nums, target)
print(ans)
print(len(ans))