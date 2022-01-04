'''
Description: 
Author: Tjg
Date: 2022-01-01 22:22:55
LastEditTime: 2022-01-01 22:30:30
LastEditors: Please set LastEditors
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if nums is None or nums == []:
            return False
        
        hash = set()
        for i in nums:
            if i in hash:
                return True
            else:
                hash.add(i)
        return False