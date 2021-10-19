'''
Description: 
Author: Tjg
Date: 2021-10-17 12:38:25
LastEditTime: 2021-10-17 12:59:46
LastEditors: Please set LastEditors
'''
# 双指针 都从左边出发 p283
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def findContinuousSequence(self, target: int) -> list[list[int]]:
        if target < 3:
            return None

        left = 1
        right = 2
        # 1 奇数的一半需要 +1  
        # 2 range左闭右开需要 +1  
        # 3 left和right从1开始计数，多一个0元素
        nums = [i for i in range(target // 2 + 3)]
        ans = []
        while left <= target // 2:
            # 求和公式比sum函数快
            intervalSum = int((right + left) * (right - left + 1) / 2)
            if  intervalSum < target:
                right += 1
            elif intervalSum > target:
                left += 1
            else:
                # 这里也可以用 range生成器
                ans.append(nums[left:right + 1])
                left += 1
        return ans