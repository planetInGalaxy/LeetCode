'''
Description: 
Author: Tjg
Date: 2022-01-01 21:58:51
LastEditTime: 2022-01-01 22:17:18
LastEditors: Please set LastEditors
'''
# 模拟
class Solution:
    def romanToInt(self, s: str) -> int:
        if s is None or s == "":
            return 0
        
        result = 0
        n = len(s)
        flag = True

        for i in range(n):
            if flag == False:
                flag = True
                continue
            if s[i] == 'M':
                result += 1000
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'C':
                if i != n - 1:
                    if s[i + 1] == 'M':
                        result += 900
                        flag = False
                    elif s[i + 1] == 'D':
                        result += 400
                        flag = False
                    else:
                        result += 100
                else:
                    result += 100
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'X':
                if i != n - 1:
                    if s[i + 1] == 'C':
                        result += 90
                        flag = False
                    elif s[i + 1] == 'L':
                        result += 40
                        flag = False
                    else:
                        result += 10
                else:
                    result += 10
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'I':
                if i != n - 1:
                    if s[i + 1] == 'X':
                        result += 9
                        flag = False
                    elif s[i + 1] == 'V':
                        result += 4
                        flag = False
                    else:
                        result += 1
                else:
                    result += 1
            
        return result