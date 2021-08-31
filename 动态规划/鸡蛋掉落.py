'''
Description: 
Author: Tjg
Date: 2021-08-24 09:02:25
LastEditTime: 2021-08-24 09:57:24
LastEditors: Please set LastEditors
'''
# 动态规划 递归 备忘录 二分找谷点
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()
        def dp(k,n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k,n) in memo:
                return memo[(k,n)]
            
            res = float('INF')

            # for i in range(1, n + 1):
            #     res = min(res, max(dp(k, n - i), dp(k - 1, i - 1)) + 1)

            l,r = 1,n
            while l <= r:
                mid = l + (r - l) // 2
                broken = dp(k - 1, mid - 1) + 1
                not_broken = dp(k, n - mid) + 1
                if broken > not_broken:
                    r = mid - 1
                    res = min(res, broken)
                else:
                    l = mid + 1
                    res = min(res, not_broken)
            memo[(k,n)] = res
            return res

        return dp(k, n)


s1 = Solution()
s1.superEggDrop(3,14)
