'''
Description: 
Author: Tjg
Date: 2021-10-24 10:46:30
LastEditTime: 2021-10-24 10:56:21
LastEditors: Please set LastEditors
'''
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isValid(n):
            nums = {}
            nStr = str(n)
            for i in nStr:
                nums[i] = nums.get(i, 0) + 1
            
            for k,v in nums.items():
                if int(k) != v:
                    return False
            return True
        
        while True:
            n += 1
            if isValid(n):
                return n

n = 1000
s1 = Solution()
ans = s1.nextBeautifulNumber(n)
print(ans)