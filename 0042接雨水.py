'''
Description: 
Author: Tjg
Date: 2021-11-24 08:12:26
LastEditTime: 2021-11-24 08:37:29
LastEditors: Please set LastEditors
'''
# 动态规划求两边最长柱子 再累加有效接水量 思路来源于最大矩形
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left = [-1] * n
        right = [-1] * n

        for i in range(1, n - 1):
            if left[i - 1] == -1:
                if height[i] < height[i - 1]:
                    left[i] = i - 1
            else:
                if height[i] < height[left[i - 1]]:
                    left[i] = left[i - 1]
        
        for i in range(n - 2, 0, -1):
            if right[i + 1] == -1:
                if height[i] < height[i + 1]:
                    right[i] = i + 1
            else:
                if height[i] < height[right[i + 1]]:
                    right[i] = right[i + 1]

        # print(left)
        # print(right)
        ans = 0
        for i in range(1, n - 1):
            if left[i] != -1 and right[i] != -1:
                ans += min(height[left[i]], height[right[i]]) - height[i]

        return ans

# 官方
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
s1 = Solution()
ans = s1.trap(height)
print(ans)