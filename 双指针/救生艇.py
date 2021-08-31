'''
Description: 
Author: Tjg
Date: 2021-08-26 20:07:13
LastEditTime: 2021-08-26 20:15:24
LastEditors: Please set LastEditors
'''
# 排序 双指针 贪心
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            ans += 1
        return ans