'''
Description: 
Author: Tjg
Date: 2021-10-17 10:30:06
LastEditTime: 2021-10-17 10:36:47
LastEditors: Please set LastEditors
'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        strList = s.split()
        last = -1
        for i in strList:
            if i[0] in '0123456789':
                num = int(i)
                if last == -1:
                    last = num
                else:
                    if num <= last:
                        return False
                    else:
                        last = num
        return True

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
s1 = Solution()
ans = s1.areNumbersAscending(s)
print(ans)