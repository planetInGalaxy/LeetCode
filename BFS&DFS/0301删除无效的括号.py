'''
Description: 
给你一个由若干括号和字母组成的字符串 s ，
删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按任意顺序返回。
Author: Tjg
Date: 2022-02-24 20:13:19
LastEditTime: 2022-02-24 20:30:39
LastEditors: Please set LastEditors
'''
# BFS
# 时间复杂度 O(n*2^n) 
# 其中 n 为字符串的长度。
# 考虑到一个字符串最多可能有 2^n个子序列，
# 每个子序列可能需要进行一次合法性检测，
# 因此时间复杂度为 O(n*2^n)
# 空间复杂度 O(n*2^n)
# 我们在进行第 i 轮迭代时，会从原始字符串中删除 i 个括号，
# 因此第 i 轮迭代产生的字符串最多有 C(n,i)个，
# 当 i = n/2 时组合数最大，此时迭代生成的字符串个数最多，
# 因此空间复杂度为 O(n*C(n, n/2)
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            if s == "":
                return True
            left = 0
            for i in s:
                # 常量池 故用is
                if i is "(":
                    left += 1
                elif i is ")":
                    left -= 1
                    if left < 0:
                        return False
            else:
                return left == 0
        
        # 答案是唯一的
        ans = []
        # 类似记忆化的思想，相同状态只计算一次
        cur_set = {s}
        while True:
            next_set = set()
            for state in cur_set:
                if isValid(state) is True:
                    ans.append(state)
                for i in range(len(state)):
                    if state[i] in "()":
                        next_set.add(state[:i] + state[i+1:])
            # 每一层每一层地遍历
            cur_set = next_set
            if ans:
                return ans