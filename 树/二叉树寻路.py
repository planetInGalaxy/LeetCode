'''
Description: 
Author: Tjg
Date: 2021-07-29 11:25:58
LastEditTime: 2021-07-29 12:06:29
LastEditors: 
'''

# 二叉树的基本概念 
class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        ans = []
        parent = label
        re_flag = 1
        while parent >= 1:
            ans.append(parent)
            parent //= 2
            re_flag = - re_flag
        ans.reverse()
        print(ans)

        for i in range(len(ans) - 1):
            print(i,ans[i])
            if i % 2 == 1 and re_flag == -1 or i % 2 == 0 and re_flag == 1:
                n = 2 ** i
                m = 2 ** (i + 1) - 1
                real_parent = m - (ans[i] - n)
                ans[i] = real_parent
        return ans

s1 = Solution()
label = 14
answer = s1.pathInZigZagTree(label)
print(answer)

            