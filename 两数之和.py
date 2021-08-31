'''
Description: 
Author: Tjg
Date: 2021-06-01 18:36:11
LastEditTime: 2021-06-01 19:57:36
LastEditors: Please set LastEditors
'''
# 穷举
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
# 哈希
class Solution:
    def hash_code(self,num,n):
        return int((5 * abs(num) + 1) % (1e5 + 1) % n)
        
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums) * 5
        ls = [None] * n
        dict_1 = {}
        dict_2 = {}
        for i in range(len(nums)):
            code = self.hash_code(nums[i], n)
            while ls[code] is not None:
                code = (code + 1) % n
            ls[code] = nums[i]
            dict_1[i] = code
            dict_2[code] = i
        # print(dict_1,dict_2,ls)

        for i in range(len(nums)):
            code = self.hash_code(target - nums[i], n)
            # print(code)
            while ls[code] is not None:
                if ls[code] + nums[i] == target and code != dict_1[i]:
                    return [i,dict_2[code]]
                code += 1
# 官方哈希
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
        
ls =[3,3]
t = 6
s1 = Solution()
anwser = s1.twoSum(ls, t)
print(anwser)