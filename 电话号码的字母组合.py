'''
Description: 
Author: Tjg
Date: 2021-01-30 16:58:04
LastEditTime: 2021-02-01 09:12:25
LastEditors: Please set LastEditors
'''
class Solution:
    def letterCombinations(self, digits):
        if not digits: return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def backtrack(conbination,nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter,nextdigit[1:])

        res = []
        backtrack('',digits)
        return res
