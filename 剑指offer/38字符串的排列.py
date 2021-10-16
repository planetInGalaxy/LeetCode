'''
Description: 
Author: Tjg
Date: 2021-10-13 10:28:16
LastEditTime: 2021-10-13 10:50:35
LastEditors: Please set LastEditors
'''
# 时间复杂度O（nxn!）
class Solution:
    def permutation(self, s: str) -> list[str]:
        def backtracking(index):
            if index == len(string_list):
                s = "".join(string_list)
                ans.add(s)
                return 
            for i in range(index, len(string_list)):
                string_list[i], string_list[index] = string_list[index], string_list[i]
                backtracking(index + 1)
                string_list[i], string_list[index] = string_list[index], string_list[i]
        string_list = list(s)
        ans = set()
        backtracking(0)
        ans = list(ans)
        return ans