'''
Description: 
给定一个不含重复数字的数组nums，
返回其所有可能的全排列。
你可以按任意顺序返回答案。
Author: Tjg
Date: 2021-06-30 10:04:14
LastEditTime: 2022-02-03 17:25:14
LastEditors: Please set LastEditors
'''
# 回溯法 O（n x n!）
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def func():
            for i in nums:
                if i in temp:
                    continue
                temp.append(i)
                if len(temp) == len(nums):
                    answer.append(temp[:])
                    temp.pop()
                    return
                func()
                temp.pop()
        temp = []
        answer = []
        func()
        return answer

s1 = Solution()
nums = [1,2,3]
answer = s1.permute(nums)
print(answer)