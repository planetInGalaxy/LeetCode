'''
Description: 
给定一个可包含重复数字的序列nums，
按任意顺序返回所有不重复的全排列。
Author: Tjg
Date: 2021-07-20 23:05:33
LastEditTime: 2022-02-03 17:24:45
LastEditors: Please set LastEditors
'''
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def func():
            current_used_num = set()
            for i in nums:
                if num_count[i] < num_total_count[i] and i not in current_used_num:
                    current_used_num.add(i)
                    num_count[i] += 1
                    temp.append(i)
                    if len(temp) == len(nums):
                        answer.append(temp[:])
                        num_count[i] -= 1
                        temp.pop()
                        return
                    func()
                    num_count[i] -= 1
                    temp.pop()

        temp = []
        answer = []
        num_count = {}
        num_total_count = {}
        for i in nums:
            num_total_count[i] = num_total_count.get(i,0) + 1
            num_count[i] = 0
        func()
        return answer


# 官方 
# 时间复杂度O(n×n!)（使用 O(n)的时间复制到答案数组中）
# 对原数组排序，保证相同的数字都相邻，
# 保证每次填入的数一定是这个数所在重复数集合中
# 从左往右第一个未被填过的数字
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def func():
            nonlocal visit
            for i in range(len(nums)):
                # 这个判断条件保证了对于重复数的集合，一定是从左往右逐个填入的。
                if visit[i] is True or \
                    i != 0 and nums[i] == nums[i - 1] and \
                        not visit[i - 1]:
                    continue
                visit[i] = True
                temp.append(nums[i])
                if len(temp) == len(nums):
                    answer.append(temp[:])
                    temp.pop()
                    visit[i] = False
                    return
                func()
                temp.pop()
                visit[i] = False

        temp = []
        answer = []
        # visit保证每个temp中不会重复使用nums中相同idx的元素
        visit = [False for _ in range(len(nums))]
        nums.sort()
        func()
        return answer

s1 = Solution()
nums = [1,1,2]
answer = s1.permuteUnique(nums)
print(answer)
