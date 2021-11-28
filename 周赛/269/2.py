'''
Description: 
Author: Tjg
Date: 2021-11-28 10:33:50
LastEditTime: 2021-11-28 10:48:49
LastEditors: Please set LastEditors
'''
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * len(nums)
        sumNum = -1
        count = 2 * k + 1
        for i in range(len(nums)):
            if i < k or i >= len(nums) - k:
                ans[i] = -1
            else:
                if sumNum == -1:
                    sumNum = sum(nums[i - k : i + k + 1])
                    ans[i] = sumNum // count
                else:
                    sumNum = sumNum + nums[i + k] - nums[i - k -1] 
                    ans[i] = sumNum // count
                print(sumNum)
        return ans 

nums = [7,4,3,9,1,8,5,2,6]
k = 3

s1 = Solution()
ans = s1.getAverages(nums, k)
print(ans)