'''
Description: 
Author: Tjg
Date: 2021-10-17 10:55:10
LastEditTime: 2021-10-17 11:11:02
LastEditors: Please set LastEditors
'''
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        def OR(nums):
            orResult = 0
            for i in nums:
                orResult = orResult | i
            nonlocal maxResult
            maxResult = max(maxResult, orResult)
            orResults[orResult] = orResults.get(orResult, 0) + 1

        def getSubSet(n):
            if n == len(nums):
                OR(subSet)
                return

            subSet.append(nums[n])
            getSubSet(n + 1)
            subSet.pop()

            getSubSet(n + 1)


        orResults = {}
        maxResult = 0
        subSet = []
        getSubSet(0)

        return orResults[maxResult]

nums = [3,2,1,5]
s1 = Solution()
ans = s1.countMaxOrSubsets(nums)
print(ans)