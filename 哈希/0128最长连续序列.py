'''
Description: 
给定一个未排序的整数数组 nums ，找出数字连续的最长序列
（不要求序列元素在原数组中连续）的长度。
Author: Tjg
Date: 2022-01-22 18:02:19
LastEditTime: 2022-01-22 18:29:48
LastEditors: Please set LastEditors
'''
# 哈希
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums is None or nums == []:
            return 0
        
        hash = set(nums)
        computed = set()
        ans = 0
        for num in nums:
            if num not in computed:
                computed.add(num)
                count = 1

                near_num = num - 1
                while near_num in hash and near_num not in computed:
                    computed.add(near_num)
                    near_num -= 1
                    count += 1

                near_num = num + 1
                while near_num in hash and near_num not in computed:
                    computed.add(near_num)
                    near_num += 1
                    count += 1

                ans = max(ans, count)
    
        return ans


# 官方
# 左边判断即可，只向右方迭代
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak



nums = [100,4,200,1,3,2]
s1 = Solution()
ans = s1.longestConsecutive(nums)
print(ans)