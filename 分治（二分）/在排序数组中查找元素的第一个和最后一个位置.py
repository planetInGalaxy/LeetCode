'''
Description: 
Author: Tjg
Date: 2021-07-26 17:22:33
LastEditTime: 2021-07-26 17:43:18
LastEditors: Please set LastEditors
'''
# 最左 最右二分法 
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        answer = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return [-1,-1]
        else:
            answer.append(left)

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return [-1,-1]
        else:
            answer.append(right)
        return answer

# 合二为一的二分
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                if nums[l] == target and nums[r] == target:
                    # 直接找到了
                    return [l, r]
                if nums[l] != target:                # 没找到 左边右移一位
                    l += 1
                if nums[r] != target:                # 没找到 右边左移一位
                    r -= 1
            elif nums[mid] < target:                # l,r 都在mid右边
                l = mid + 1
            else:                                   # l,r 都在mid左边
                r = mid - 1
        return [-1, -1]
