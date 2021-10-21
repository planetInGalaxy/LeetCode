'''
Description: 
Author: Tjg
Date: 2021-10-21 08:51:01
LastEditTime: 2021-10-21 09:47:25
LastEditors: Please set LastEditors
'''
# 回溯 当前的数字可选可不选
# 先逆向排序，但是没啥用，没有减少搜索空间
# 时间复杂度O(n*2^n) 空间复杂度O(target)
import time
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(n, sum):
            if n == len(candidates) or sum > target:
                return
            if sum == target:
                ans.append(comb[:])
                return

            dfs(n + 1, sum)
            comb.append(candidates[n])
            dfs(n, sum + candidates[n])
            comb.pop()

        comb = []
        ans = []
        candidates.sort(reverse=True)
        dfs(0, 0)
        return ans

candidates = [8] + [1 for i in range(15)]
target = 8
s1 = Solution()
start = time.time()
ans = s1.combinationSum(candidates, target)
end = time.time()
# print(ans)
print(end - start)