'''
Description: 
Author: Tjg
Date: 2021-10-07 16:06:19
LastEditTime: 2021-10-07 18:06:21
LastEditors: Please set LastEditors
'''
# 时间复杂度O（n） 空间复杂度O（n） p127
# 扩展性好
class Solution:
    def isNumber(self, s: str) -> bool:
        def isIntegerNumber(s):
            if s == '':
                return False
            hasNumber = False
            for i in range(len(s)):
                if s[i] == ' ':
                    return False
                if s[i] in '+-' and i != 0:
                    return False
                if s[i].isalpha():
                    return False
                if s[i] == '.':
                    return False
                if s[i] in '0123456789':
                    hasNumber = True
            else:
                return hasNumber

        def isFloatNumber(s):
            if s == '':
                return False
            dot_flag = False
            hasNumber = False
            for i in range(len(s)):
                if s[i] == ' ':
                    return False
                if s[i] in '+-' and i != 0:
                    return False
                if s[i].isalpha():
                    return False
                if s[i] == '.':
                    if dot_flag == True:
                        return False
                    else:
                        dot_flag = True
                if s[i] in '0123456789':
                    hasNumber = True
            else:
                return hasNumber

        s = s.strip()
        if s == '':
            return False

        if 'e' in s or 'E' in s:
            if s.count('e') + s.count('E') != 1:
                return False
            s2 = s.split('e') if 'e' in s else s.split('E')

            if len(s2) <= 1:
                return False
            else:
                if (isFloatNumber(s2[0]) or isIntegerNumber(s2[0])) \
                    and isIntegerNumber(s2[1]):
                    return True
                else:
                    return False
        else:
            if isFloatNumber(s) or isIntegerNumber(s):
                return True
            else:
                return False

test = ['01','-2','-0.9','-.2','+3.','2E3','-1.e+2','e2','23E','1a','2e.2','-+1','..','1.2.3','4e+','7e69e']      
s1 = Solution()
ans = [s1.isNumber(i) for i in test]
print(ans)
