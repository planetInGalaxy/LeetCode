'''
Description: 
给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。
一个括号字符串被称为平衡的当它满足：
任何左括号 '(' 必须对应两个连续的右括号 '))' 。
左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。
你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。
请你返回让 s 平衡的最少插入次数。
Author: Tjg
Date: 2022-01-24 22:20:18
LastEditTime: 2022-01-24 22:51:41
LastEditors: Please set LastEditors
'''

# 贪心 模拟栈
# 时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def minInsertions(self, s: str) -> int:
        if s == "":
            return None
        
        ans = 0
        lefts = 0
        i = 0
        # for-range循环一定循环固定次数
        # 改变迭代变量需要用while
        while i < len(s):
            if s[i] == '(':
                lefts += 1
            else:
                if lefts > 0:
                    if i != len(s) - 1 and s[i+1] == ')':
                        lefts -= 1
                        i += 1
                    else:
                        lefts -= 1
                        ans += 1
                else:
                    if i != len(s) - 1 and s[i+1] == ')':
                        ans += 1
                        i += 1
                    else:
                        ans += 2
            i += 1
        ans += 2 * lefts
        return ans

# 优化
class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                right += 2
                # ？
                if right % 2 == 1:
                    left += 1
                    right -= 1
            if ch == ')':
                right -= 1
                if right == -1:
                    left += 1
                    right = 1
        return left + right