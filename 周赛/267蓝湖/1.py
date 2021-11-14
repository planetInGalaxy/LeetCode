'''
Description: 
Author: Tjg
Date: 2021-11-14 10:28:15
LastEditTime: 2021-11-14 10:36:46
LastEditors: Please set LastEditors
'''
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                time += tickets[i]
            else:
                if i <= k:
                    time += tickets[k]
                else:
                    time += tickets[k] - 1
        return time
        