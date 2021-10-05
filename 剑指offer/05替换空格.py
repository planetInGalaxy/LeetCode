'''
Description: 
Author: Tjg
Date: 2021-10-05 21:42:46
LastEditTime: 2021-10-05 22:01:10
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(n) p54
# 模拟原地扩增的情况（实际上不是原地）
class Solution:
    def replaceSpace(self, s: str) -> str:
        if not str:
            return None
        count = 0
        for i in s:
            if i == " ":
                count += 1
                
        s2 = [None] * (len(s) + 2 * count)
        p1 = len(s) - 1
        p2 = len(s2) - 1
        
        while p1 >= 0:
            if s[p1] == ' ':
                p1 -= 1
                s2[p2] = '0'
                p2 -= 1
                s2[p2] = '2'
                p2 -= 1
                s2[p2] = '%'
                p2 -= 1
            else:
                s2[p2] = s[p1]
                p1 -= 1
                p2 -= 1
        return "".join(s2)

# 时间复杂度O(n) 空间复杂度O(n)
# 直接构建新列表->字符串
class Solution:
    def replaceSpace(self, s: str) -> str:
        s_list = []
        for i in range(len(s)):
            if s[i]==' ':
                s_list.append('%20')
            else:
                s_list.append(s[i])
        return ''.join(s_list)