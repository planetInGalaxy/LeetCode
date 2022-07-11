'''
Description: 
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
Author: Tjg
Date: 2022-07-11 22:50:26
LastEditTime: 2022-07-11 23:11:46
LastEditors: Please set LastEditors
'''
# 枚举查表(打表)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ['1']
        numStr = ['1']
        for i in range(30):
            newNumStr = []
            count = 1
            for j in range(len(numStr)):
                if j == len(numStr) - 1 or numStr[j] != numStr[j + 1]:
                    newNumStr.extend([str(count), numStr[j]])
                    count = 1
                else:
                    count += 1
            numStr = newNumStr
            ans.append("".join(numStr))
        return ans[n - 1]