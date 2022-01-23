'''
Description: 
给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。
由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。
Author: Tjg
Date: 2022-01-23 22:19:39
LastEditTime: 2022-01-23 23:31:06
LastEditors: Please set LastEditors
'''
# 数学 动态规划 前缀和
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        if arr is None or arr == []:
            return 0
        # j位置的奇数前缀和偶数前缀和的数量
        # j < i, j最小为-1
        odd, even = 0, 1
        sum = 0
        ans = 0
        for num in arr:
            # i位置的前缀和（即 arr[0]+arr[1]+…+arr[i]）
            sum += num
            if sum % 2 == 1:
                # 有even个j的前缀和为偶数，
                # 则有even个以i为结尾的和为奇数的子数组
                ans += even
                # 奇数前缀和+1
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % int(1e9+7)
        
        
