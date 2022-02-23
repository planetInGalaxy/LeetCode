'''
Description: 
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，
表示其中方括号内部的 encoded_string 正好重复 k 次。
注意 k 保证为正整数。
你可以认为输入字符串总是有效的；
输入字符串中没有额外的空格，
且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，
所有的数字只表示重复的次数 k ，
例如不会出现像 3a 或 2[4] 的输入。
Author: Tjg
Date: 2022-02-23 19:53:18
LastEditTime: 2022-02-23 20:36:09
LastEditors: Please set LastEditors
'''
# 栈
# 时间复杂度O(nm) 空间复杂度O(nm)
# n为字符串长度， m为最大数字值
class Solution:
    def decodeString(self, s: str) -> str:
        if s is None or s == "":
            return None
        
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] not in "[]0123456789":
                string = []
                while i < n and s[i] not in "[]0123456789":
                    string.append(s[i])
                    i += 1
                string = "".join(string)
                # 得到字符串后及时合并
                while stack and isinstance(stack[-1], str):
                    string = stack.pop() + string
                stack.append(string)
            elif s[i] in "0123456789":
                num = []
                while s[i] in "0123456789":
                    num.append(s[i])
                    i += 1
                num = int("".join(num))
                stack.append(num)
            elif s[i] == "[":
                i += 1
            elif s[i] == "]":
                string = stack.pop()
                num = stack.pop()
                new_string = string * num
                # 得到字符串后及时合并
                while stack and isinstance(stack[-1], str):
                    new_string = stack.pop() + new_string
                stack.append(new_string)
                i += 1
            # print(s[i], stack)

        return stack[0]