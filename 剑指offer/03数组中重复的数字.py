'''
Description: 
Author: Tjg
Date: 2021-10-05 20:23:53
LastEditTime: 2021-10-05 20:41:31
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n） 空间复杂度O（1） p40
class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # print(nums)
                # 交换顺序不能错，否则nums[i]变化后nums[nums[i]]也变化
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
        return -1

ls = [2,3,1,0,2,5,3]
s1 = Solution()
answer = s1.findRepeatNumber(ls)
print(answer)