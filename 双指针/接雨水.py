'''
Description: 
Author: Tjg
Date: 2021-08-25 10:33:03
LastEditTime: 2021-08-25 10:46:09
LastEditors: Please set LastEditors
'''
# 双指针 
class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0
        left = 1
        right = len(height) - 2
        ans = 0
        l_max = height[0]
        r_max = height[-1]
        while left <= right:
            # 每轮选用max小的那个方向的指针，以符合min（l_max，r_max)的条件
            if l_max < r_max:
                l_max = max(l_max, height[left])
                ans += l_max - height[left]
                left += 1
            else:
                r_max = max(r_max, height[right])
                ans += r_max - height[right]
                right -= 1
        # print(ans)
        return ans
                
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s1 = Solution()
s1.trap(height)