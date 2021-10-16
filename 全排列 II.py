'''
Description: 
Author: Tjg
Date: 2021-07-20 23:05:33
LastEditTime: 2021-10-13 11:01:31
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

s1 = Solution()
nums = [1,1,2]
answer = s1.permuteUnique(nums)
print(answer)