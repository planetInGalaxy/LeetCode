'''
Description: 
Author: Tjg
Date: 2021-11-23 19:17:47
LastEditTime: 2021-11-23 19:53:09
LastEditors: Please set LastEditors
'''
# 单调栈 时间复杂度O(n)
# https://lucifer.ren/blog/2020/11/03/monotone-stack/
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        right = [n] * n
        left = [-1] * n

        monoStack = []
        for i in range(n):
            while monoStack and heights[i] < heights[monoStack[-1]]:
                peek = monoStack.pop()
                right[peek] = i
            monoStack.append(i)

        monoStack.clear()
        for i in range(n - 1, -1, -1):
            while monoStack and heights[i] < heights[monoStack[-1]]:
                peek = monoStack.pop()
                left[peek] = i
            monoStack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return ans

heights = [2,1,5,6,2,3]
s1 = Solution()
ans = s1.largestRectangleArea(heights)
print(ans)
        