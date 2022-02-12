'''
Description: 
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，
可以构造一个表达式：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，
在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于target的不同表达式的数目。
Author: Tjg
Date: 2022-02-12 22:21:14
LastEditTime: 2022-02-12 23:57:54
LastEditors: Please set LastEditors
'''
# 回溯 -> 动态规划 状态压缩 哈希
# 时间复杂度O(n*2^n) 空间复杂度O(2^n)
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if nums is None or nums == []:
            return 0

        last_map = {0:1}
        for num in nums:
            cur_map = {}
            for key in list(last_map.keys()):
                cur_map[key + num] = cur_map.get(key + num, 0) + last_map[key]
                cur_map[key - num] = cur_map.get(key - num, 0) + last_map[key]
            last_map = cur_map
            print(cur_map)
        return cur_map.get(target, 0)
        


# 官方 
# 动态规划 + 数学
# 记数组的元素和为sum，添加-号的元素之和为neg，
# 则其余添加+的元素之和为sum − neg
# (sum - neg) - neg = sum - 2 * neg = target
# neg = (sum - target) / 2
# 由于数组nums中的元素都是非负整数，neg也必须是非负整数，
# 所以上式成立的前提是sum − target是非负偶数
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if nums is None or nums == []:
            return 0

        # 必须先判断是否有解
        diff = sum(nums) - target
        if diff < 0 or diff % 2 != 0 :
            return 0
        neg = diff // 2

        # 不设前置的递推值会比较麻烦
        # n = len(nums)
        # m = neg + 1
        # dp = [[0] * m for _ in range(n)]
        # dp[0][0] = 1
        # if nums[0] <= neg:
        #     dp[0][nums[0]] += 1
            
        # # 子序列问题
        # for i in range(1, n):
        #     for j in range(m):
        #         dp[i][j] = dp[i - 1][j]
        #         if nums[i] <= j:
        #             dp[i][j] += dp[i - 1][j - nums[i]]
        #     # print(dp)
        
        n = len(nums) + 1
        m = neg + 1
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        # 子序列问题
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
            # print(dp)
        return dp[-1][-1]

            



nums = [1,1,1,1,1]
target = 3

s1 = Solution()
ans = s1.findTargetSumWays(nums, target)
print(ans)