'''
Description: 
Author: Tjg
Date: 2021-11-28 10:50:00
LastEditTime: 2021-11-28 11:13:22
LastEditors: Please set LastEditors
'''
class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        maxIndex = nums.index(max(nums))
        minIndex = nums.index(min(nums))
        n = len(nums)
        ans = 0
        if min(minIndex + 1, n - minIndex) < min(maxIndex + 1, n - maxIndex):
            if minIndex + 1 <= n - minIndex:
                ans += (minIndex + 1)
                maxIndex -= (minIndex + 1)
                n -= (minIndex + 1)
            else:
                ans += (n - minIndex)
                n = minIndex
            ans += min(maxIndex + 1, n - maxIndex)
        else:
            if maxIndex + 1 <= n - maxIndex:
                ans += (maxIndex + 1)
                minIndex -= (maxIndex + 1)
                n -= (maxIndex + 1)
            else:
                ans += (n - maxIndex)
                n = maxIndex
            ans += min(minIndex + 1, n - minIndex)

        return ans

nums = [0,-4,19,1,8,-2,-3,5]
s1 = Solution()
ans = s1.minimumDeletions(nums)
print(ans)