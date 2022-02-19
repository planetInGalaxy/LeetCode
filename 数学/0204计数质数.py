'''
Description:
给定整数 n ，返回所有小于非负整数 n 的质数的数量 。
Author: Tjg
Date: 2022-02-19 14:10:36
LastEditTime: 2022-02-19 14:11:44
LastEditors: Please set LastEditors
'''
# 埃氏筛法
# 时间复杂度O(nloglogn) 空间复杂度O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrimes = [1] * n
        ans = 0
        for i in range(2, n):
            if isPrimes[i] == 1:
                ans += 1
            for j in range(i * i, n, i):
                isPrimes[j] = 0
        return ans