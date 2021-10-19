'''
Description: 
Author: Tjg
Date: 2021-10-19 17:46:59
LastEditTime: 2021-10-19 17:46:59
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')