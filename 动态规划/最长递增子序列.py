'''
Description: 
Author: Tjg
Date: 2021-07-29 14:43:12
LastEditTime: 2021-07-29 14:43:19
LastEditors: 
'''
# 贪心 + 二分
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            if not ans or i > ans[-1]:
                ans.append(i)
            else:
                l,r = 0, len(ans) - 1
                loc = -1
                while l <= r:
                    mid = l + (r - l) // 2
                    if ans[mid] > i:
                        r = mid - 1
                    elif ans[mid] < i:
                        l = mid + 1
                    else:
                        break
                else:
                    loc = l
                    ans[loc] = i
            # print(ans)
        return l
        
# 动态规划 o（n2）
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        ans = max(dp)
        return ans

s1 = Solution()
ls1 = [4,10,4,3,8,9]
ans = s1.lengthOfLIS(ls1)
print(ans)