'''
Description: 
Author: Tjg
Date: 2021-06-29 14:53:30
LastEditTime: 2021-06-29 15:02:01
LastEditors: Please set LastEditors
'''
class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = '([{'
        right_brackets = ')]}'
        stack = list()
        for i in s:
            if i in left_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    bracket = stack.pop()
                    if left_brackets.index(bracket) != right_brackets.index(i):
                        return False
        return True if len(stack) == 0 else False

        