'''
Description: 
Author: Tjg
Date: 2021-07-26 22:42:25
LastEditTime: 2021-07-26 23:04:14
LastEditors: Please set LastEditors
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
            # 新知识 可以输出 但是输出超限算错
        return len(ans)

s1 = Solution()
ls1 = [4,10,4,3,8,9]
ans = s1.lengthOfLIS(ls1)
print(ans)