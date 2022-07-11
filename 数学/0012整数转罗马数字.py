'''
Description: 
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 
27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

Author: Tjg
Date: 2022-07-10 19:57:45
LastEditTime: 2022-07-10 19:57:46
LastEditors: Please set LastEditors
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romaUnit = [('I','V'),('X','L'),('C','D'),('M','')]
        num = str(num)
        length = len(num)
        romaNum = ""
        for i in num:
            if i <= '3':
                romaNum += romaUnit[length - 1][0] * int(i)
            elif i is '4':
                romaNum += romaUnit[length - 1][0]
                romaNum += romaUnit[length - 1][1]
            elif i <= '8':
                romaNum += romaUnit[length - 1][1] 
                romaNum += romaUnit[length - 1][0] * (int(i) - 5)                
            elif i is '9':
                romaNum += romaUnit[length - 1][0]
                romaNum += romaUnit[length][0]
            length -= 1
        return romaNum
