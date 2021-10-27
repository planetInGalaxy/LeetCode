'''
Description: 
Author: Tjg
Date: 2021-08-22 08:16:39
LastEditTime: 2021-08-22 08:30:41
LastEditors: Please set LastEditors
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def unique_string(self , s ):
        # write code here
        s = list(s)
        str_set = set()
        i = 0
        while i < len(s):
            if s[i] in str_set:
                s.pop(i)
            else:
                str_set.add(s[i])
                i += 1
            print(i,s[:10])
        s = "".join(s)
        return s

s1 = Solution()
s = "hellowelcometoxiaomi"
answer = s1.unique_string(s)
print(answer)