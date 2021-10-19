'''
Description: 
Author: Tjg
Date: 2021-10-17 20:26:03
LastEditTime: 2021-10-18 09:23:04
LastEditors: Please set LastEditors
'''
# 递归 超时 p295
# 时间复杂度O(n^6) 空间复杂度O(n)
class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        def getCount(x, count):
            if x == 0:
                countList[count] += 1
                return
                # 0 ~ 5
            for i in range(6):
                getCount(x - 1, count + i)

        countList = [0] * (5 * n + 1)
        getCount(n, 0)
        sumCount = sum(countList)
        probability = [i / sumCount for i in countList]

        return probability

# 动态规划 状态压缩 次数累加
# 时间复杂度O(n^2) 空间复杂度O(n)
class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        dp = [1] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            # 前面n-1个骰子的结果，加上第n个骰子的1~6之间的结果，得到下标
            # 遍历前n-1个骰子总点数
            # （不严格是总点数，总点数是n ~ 6n， 下标是 0 ~ 5n）
            for j in range(len(dp)):
                # 因为有六种点数（1点是第0种情况 6点是第五种情况）
                for k in range(6):
                    # 前n-1个骰子的总点数加上这次掷的结果得到总点数下标
                    # 当前总点数的和应该加上前n-1个骰子总点数的和
                    tmp[j + k] += dp[j]
            # tmp和dp轮流使用
            dp = tmp
        sumCount = sum(dp)
        probability = [i / sumCount for i in dp]
        return probability

s1 = Solution()
ans = s1.dicesProbability(2)
print(ans)