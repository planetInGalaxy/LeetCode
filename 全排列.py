'''
Description: 
Author: Tjg
Date: 2021-06-30 10:04:14
LastEditTime: 2021-06-30 10:33:01
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
                # print(temp)
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