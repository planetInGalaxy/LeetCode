'''
Description: 
Author: Tjg
Date: 2021-06-24 15:06:18
LastEditTime: 2021-08-22 09:42:57
LastEditors: Please set LastEditors
'''
# 回溯 剪枝
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(A):
            if len(A) == 2*n:
                print(A)
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A): # 栈的思想
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans

# 回溯 剪枝 
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s,open,close):
            if len(s) == 2 * n:
                ans.append("".join(s))
                # print(s)
                return
            else:
                if open < n:
                    s.append('(')
                    backtrack(s,open+1,close)
                    s.pop()
                if open > close:
                    s.append(')')
                    backtrack(s,open,close+1)
                    s.pop()
        ans = []
        backtrack([],0,0)
        return ans

# 递归
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
            # print(ans[-1])
        return ans


s1 = Solution()
ans = s1.generateParenthesis(4)
print(ans)