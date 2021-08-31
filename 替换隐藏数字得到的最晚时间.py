'''
Description: 
Author: Tjg
Date: 2021-07-24 14:53:52
LastEditTime: 2021-07-24 15:10:11
LastEditors: Please set LastEditors
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        print(time)
        if time[0] == '?':
            if time[1] == '?' or time[1] < '4':
                time[0] = '2'
            else:
                time[0] = '1'
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'
        return "".join(time)