'''
Description: 
Author: Tjg
Date: 2021-08-25 00:08:17
LastEditTime: 2021-08-25 00:32:57
LastEditors: Please set LastEditors
'''
# 贪心 脑筋急转弯
class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_num = values[0] + 0
        ans = 0
        for i in range(1,len(values)):
            max_num = max(max_num, values[i - 1] + i - 1)
            ans = max(ans, max_num + values[i] - i)
        return ans
